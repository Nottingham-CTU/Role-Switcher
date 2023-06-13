<?php

namespace Nottingham\RoleSwitcher;

class RoleSwitcher extends \ExternalModules\AbstractExternalModule
{
	// Always show module links.
	function redcap_module_link_check_display( $project_id, $link )
	{
		if ( ( $link['icon'] == 'fas fa-user-tag' &&
		       in_array( USERID, $this->getRoleSwitchUsers() ) ) ||
		     ( $link['icon'] == 'fas fa-user-gear' && $this->canConfigure() ) )
		{
			return $link;
		}
		return null;
	}

	// Always hide module configure button.
	function redcap_module_configure_button_display()
	{
		return $this->getProjectId() === null ? true : null;
	}

	// If the REDCap UI Tweaker module is enabled, instruct the external modules simplified view to
	// exclude the role assignments.
	function redcap_every_page_before_render( $project_id )
	{
		if ( !$project_id || ! $this->isModuleEnabled('redcap_ui_tweaker') )
		{
			return;
		}
		$moduleDirPrefix = preg_replace( '/_v[^_]*$/', '', $this->getModuleDirectoryName() );
		$UITweaker = \ExternalModules\ExternalModules::getModuleInstance('redcap_ui_tweaker');
		if ( method_exists( $UITweaker, 'areExtModFuncExpected' ) &&
		     $UITweaker->areExtModFuncExpected() )
		{
			$UITweaker->addExtModFunc( $moduleDirPrefix, function( $data ) { return false; } );
		}
	}

	// Check if the user can access the role switcher configuration.
	function canConfigure()
	{
		// Administrators can always access configuration.
		$isSuperUser = $this->getUser()->isSuperUser();
		$userRights = $this->getUser()->getRights();
		if ( $isSuperUser )
		{
			return true;
		}

		// If no user rights, prohibit access to configuration.
		if ( $userRights === null )
		{
			return false;
		}

		// If module specific rights are enabled, use this to determine whether access is allowed.
		if ( $this->getSystemSetting( 'config-require-user-permission' ) == 'true' )
		{
			return is_array( $userRights['external_module_config'] ) &&
			       in_array( 'role_switcher', $userRights['external_module_config'] );
		}

		// Otherwise allow access based on user rights permission.
		return ( $userRights['user_rights'] == '1' );
	}

	// Get the users that can switch role.
	function getRoleSwitchUsers()
	{
		$listUsers = [];
		$listUserRoles = $this->getProjectSetting( 'user-roles' );
		$listUserRoles = ( $listUserRoles == '' ? [] : json_decode( $listUserRoles, true ) );
		foreach ( $listUserRoles as $username => $itemUserRoles )
		{
			if ( count( $itemUserRoles ) > 1 )
			{
				$listUsers[] = $username;
			}
		}
		return $listUsers;
	}

	// For a given user, return the roles they can switch to.
	function getRolesForUser( $username )
	{
		$listUsers = [];
		$listUserRoles = $this->getProjectSetting( 'user-roles' );
		$listUserRoles = ( $listUserRoles == '' ? [] : json_decode( $listUserRoles, true ) );
		if ( ! isset( $listUserRoles[ $username ] ) )
		{
			return [];
		}
		$listRoleIDs = array_keys( $listUserRoles[ $username ] );
		$queryRoleNames = $this->query( 'SELECT role_id, role_name FROM redcap_user_roles ' .
		                               'WHERE project_id = ?', [ $this->getProjectId() ] );
		$listRoleNames = [];
		while ( $infoRoleName = $queryRoleNames->fetch_assoc() )
		{
			$listRoleNames[ $infoRoleName['role_id'] ] = $infoRoleName['role_name'];
		}
		$listRoles = [];
		foreach ( $listRoleIDs as $roleID )
		{
			if ( isset( $listRoleNames[ $roleID ] ) )
			{
				$listRoles[ $roleID ] = $listRoleNames[ $roleID ];
			}
		}
		return $listRoles;
	}

	// Set the user's DAGs following a role change.
	function setUserDAGs( $username, $roleID )
	{
		$listUsers = [];
		$listUserRoles = $this->getProjectSetting( 'user-roles' );
		$listUserRoles = ( $listUserRoles == '' ? [] : json_decode( $listUserRoles, true ) );
		if ( ! isset( $listUserRoles[ $username ] ) ||
		     ! isset( $listUserRoles[ $username ][ $roleID ] ) ||
		     $listUserRoles[ $username ][ $roleID ] === true )
		{
			return;
		}
		$projectID = $this->getProjectId();
		$this->query( 'DELETE FROM redcap_data_access_groups_users WHERE project_id = ? AND ' .
		              'username = ?', [ $projectID, $username ] );
		foreach ( $listUserRoles[ $username ][ $roleID ] as $dagID )
		{
			$dagID = ( $dagID == 'null' ) ? null : intval( $dagID );
			$this->query( 'INSERT INTO redcap_data_access_groups_users (project_id, group_id, ' .
			              'username) VALUES (?, ?, ?)', [ $projectID, $dagID, $username ] );
		}
		$userDAG = $this->query( 'SELECT group_id g FROM redcap_user_rights WHERE project_id = ? ' .
		                         'AND username = ?', [ $projectID, $username ] )->fetch_assoc();
		$userDAG = ( $userDAG === null || $userDAG['g'] === null ) ? 'null' : $userDAG['g'];
		if ( ! in_array( $userDAG, $listUserRoles[ $username ][ $roleID ] ) )
		{
			$dagID = reset( $listUserRoles[ $username ][ $roleID ] );
			$dagID = ( $dagID == 'null' ) ? null : intval( $dagID );
			$this->query( 'UPDATE redcap_user_rights SET group_id = ? WHERE project_id = ? AND ' .
			              'username = ?', [ $dagID, $projectID, $username ] );
		}
	}

}
