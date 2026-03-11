<?php

namespace Nottingham\RoleSwitcher;

// Only show this page to users defined in the module settings.
if ( ! in_array( USERID, $module->getRoleSwitchUsers() ) )
{
	exit;
}

$listUserRoles = $module->getRolesForUser( USERID );
$currentRole = $module->getUser()->getRights()['role_id'];
$isAdmin = $module->getUser()->isSuperUser();
$isDeactivated = false;
$proto = ( $_SERVER['HTTP_HOST'] == '127.0.0.1' ? 'http://' : 'https://' );
if ( ! $isAdmin )
{
	$listDeactivatedAdmins =
		json_decode( $module->getSystemSetting('deactivated-admins') ?? '[]', true );
	if ( in_array( USERID, $listDeactivatedAdmins ) )
	{
		$isAdmin = true;
		$isDeactivated = true;
	}
}

if ( $isAdmin && isset( $_POST['toggle-admin'] ) )
{
	if ( $isDeactivated )
	{
		$module->query( 'UPDATE redcap_user_information SET super_user = 1 WHERE username = ?',
		                [ USERID ] );
		$listDeactivatedAdmins = array_diff( $listDeactivatedAdmins, [ USERID ] );
	}
	else
	{
		$module->query( 'UPDATE redcap_user_information SET super_user = 0 WHERE username = ?',
		                [ USERID ] );
		$listDeactivatedAdmins[] = USERID;
	}
	$module->setSystemSetting( 'deactivated-admins', json_encode( $listDeactivatedAdmins ) );
	header( 'Location: ' . $proto . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'] );
	exit;
}
if ( isset( $_POST['set-role'] ) )
{
	if ( isset( $listUserRoles[ $_POST['set-role'] ] ) )
	{
		$module->getProject()->setRoleForUser( $listUserRoles[ $_POST['set-role'] ], USERID );
		$module->setUserDAGs( USERID, $_POST['set-role'] );
	}
	header( 'Location: ' . $proto . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'] );
	exit;
}

// Display the project header
require_once APP_PATH_DOCROOT . 'ProjectGeneral/header.php';


?>
<div class="projhdr">
 Switch Role
</div>
<?php

if ( $isAdmin )
{
?>
<div class="yellow" style="max-width:900px">
 <img src="<?php echo APP_PATH_WEBROOT; ?>/Resources/images/exclamation_orange.png">
 <b>You are a REDCap Administrator, with access to all data.</b>&nbsp;
 <form method="post" style="display:inline;font-size:0.85em">
  <input type="hidden" name="toggle-admin" value="1">
  <input type="submit" value="<?php echo $isDeactivated ? 'R' : 'D'; ?>eactivate access">
 </form>
<?php
	if ( ! $isDeactivated )
	{
?>
 <br>You must deactivate your administrator access for roles to take effect properly.
<?php
	}
?>
</div>
<?php
}

?>
<p>&nbsp;</p>
<p>Please choose a role:</p>
<div class="roleswitcher">
<?php
foreach ( $listUserRoles as $roleID => $roleName )
{
	$attrDis = '';
	if ( $roleID == $currentRole )
	{
		$attrDis = ' disabled';
	}
?>
 <form method="post">
  <p>
   <input type="hidden" name="set-role" value="<?php echo $module->escape( $roleID ); ?>">
   <input type="submit" value="<?php echo $module->escape( $roleName ); ?>"<?php echo $attrDis; ?>>
  </p>
 </form>
<?php
}
?>
</div>
<script type="text/javascript">
 $('head').append('<style type="text/css">.roleswitcher input{min-width:275px;height:45px}</style>')
</script>
<?php

// Display the project footer
require_once APP_PATH_DOCROOT . 'ProjectGeneral/footer.php';
