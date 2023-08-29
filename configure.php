<?php

namespace Nottingham\RoleSwitcher;

// Only show this page to users allowed to configure the role switcher.
if ( ! $module->canConfigure() )
{
	exit;
}


if ( isset( $_POST['saveroles'] ) )
{
	$module->setProjectSetting( 'user-roles', $_POST['saveroles'] );
	exit;
}


$queryUsers = $module->query( 'SELECT ur.username, ur.role_id, ur.group_id, ui.user_firstname ' .
                              'firstname, ui.user_lastname lastname FROM redcap_user_rights ur ' .
                              'JOIN redcap_user_information ui ON ur.username = ui.username ' .
                              'WHERE project_id = ? ORDER BY ur.username',
                              [ $module->getProjectId() ] );
$listUsers = [];
while ( $infoUser = $queryUsers->fetch_assoc() )
{
	$listUsers[ $infoUser['username'] ] = $infoUser;
}

$queryRoles = $module->query( 'SELECT role_id, role_name FROM redcap_user_roles ' .
                              'WHERE project_id = ? ORDER BY role_name',
                              [ $module->getProjectId() ] );
$listRoles = [];
while ( $infoRole = $queryRoles->fetch_assoc() )
{
	$listRoles[ $infoRole['role_id'] ] = $infoRole['role_name'];
}

$userRolesData = $module->getProjectSetting( 'user-roles' );
if ( $userRolesData == '' )
{
	$userRolesData = '{}';
}
$listUserRoles = json_decode( $userRolesData, true );

$listDAGs = \REDCap::getGroupNames( false );


// Display the project header
require_once APP_PATH_DOCROOT . 'ProjectGeneral/header.php';


?>
<div class="projhdr"><i class="fas fa-user-gear"></i> User Role Assignments</div>
<table class="roleswitchertbl">
 <thead>
  <tr><th style="background:#fff;border:none" colspan="<?php
echo 3 + count( $listRoles ); ?>">&nbsp;</th></tr>
  <tr>
   <th>Username</th>
   <th>DAG<br>assignments</th>
   <th>&nbsp;</th>
<?php
foreach ( $listRoles as $roleName )
{
?>
   <th><?php echo $module->escape( $roleName ); ?></th>
<?php
}
?>
  </tr>
 </thead>
 <tbody>
<?php
foreach ( $listUsers as $infoUser )
{
	if ( isset( $listUserRoles[ $infoUser['username'] ] ) &&
	     array_reduce( $listUserRoles[ $infoUser['username'] ],
	                   function( $c, $i ) { return is_array( $i ) ? $c : false; }, true ) )
	{
		$dialogLink = 'Custom';
	}
	else
	{
		$dialogLink = 'Standard';
	}
	$dialogLink = '<a href="#" data-user="' . $module->escape( $infoUser['username'] ) .
	              '" class="roleswitcherdags">' . $dialogLink . '</a>';
?>
  <tr>
   <td>
    <b><?php echo $module->escape( $infoUser['username'] ); ?></b>
    <br>
    (<?php echo $module->escape( $infoUser['firstname'] . ' ' . $infoUser['lastname'] ); ?>)
   </td>
   <td><?php echo $dialogLink; ?></td>
   <td></td>
<?php
	foreach ( $listRoles as $roleID => $roleName )
	{
		$checked = '';
		if ( isset( $listUserRoles[ $infoUser['username'] ][ $roleID ] ) )
		{
			$checked = ' checked';
		}
?>
   <td><input type="checkbox" class="roleswitcheropt" title="<?php
		echo $module->escape( $infoUser['username'] . ' - ' . $roleName );
?>" data-user="<?php echo $module->escape( $infoUser['username'] );
?>" data-role="<?php echo $module->escape( $roleID ); ?>"<?php echo $checked; ?>></td>
<?php
	}
?>
  </tr>
<?php
}
?>
 </tbody>
</table>
<div id="dags-dialog" style="display:none">
 <p class="roleswitcherdagmsg">
  If assigning DAGs, ensure that each role has at least one DAG (or no assignment) selected.
 </p>
 <table class="roleswitchertbl">
  <thead>
   <tr>
    <th>Role</th>
    <th>[No assignment]</th>
<?php
foreach ( $listDAGs as $dagID => $dagName )
{
?>
    <th><?php echo $module->escape( $dagName ); ?></th>
<?php
}
?>
   </tr>
  </thead>
  <tbody>
  </tbody>
 </table>
</div>
<script type="text/javascript">
$('head').append('<style type="text/css">.roleswitchertbl{border-collapse:separate;' +
                 'border-spacing:0px}.roleswitchertbl th, .roleswitchertbl td{border:solid ' +
                 '#ccc;border-width:0px 1px 1px 0px;padding:4px 6px;text-align:center}' +
                 '.roleswitchertbl thead{position:sticky;top:0px;z-index:100}' +
                 '.roleswitchertbl thead th{background:#ececec;border-top-width:1px}' +
                 '.roleswitchertbl tbody tr:nth-child(2n) td{background:#f3f3f3}' +
                 '.roleswitchertbl tbody tr:nth-child(2n+1) td{background:#fff}' +
                 '.roleswitchertbl tr>:first-child{border-left-width:1px;position:sticky;' +
                 'left:0px;z-index:99}</style>')
$(function()
{
  var vListRoleIDs = JSON.parse('<?php echo json_encode( $module->escape( array_keys( $listRoles ) ) ); ?>')
  var vListRoles = JSON.parse('<?php echo json_encode( $module->escape( $listRoles ) ); ?>')
  var vListDAGs = JSON.parse('<?php echo json_encode( $module->escape( array_keys( $listDAGs ) ) ); ?>')
  var vUserRoles = $('<div></div>').html('<?php echo $module->escape( $userRolesData ); ?>').text()
  vUserRoles = JSON.parse( vUserRoles )
  $('.roleswitcheropt').click(function()
  {
    var vCheckbox = this
    var vRoleID = vCheckbox.dataset.role
    var vUsername = vCheckbox.dataset.user
    var vSet = false
    if ( vUserRoles.hasOwnProperty( vUsername ) )
    {
      if ( vUserRoles[ vUsername ].hasOwnProperty( vRoleID ) )
      {
        delete vUserRoles[ vUsername ][ vRoleID ]
        if ( $.isEmptyObject(vUserRoles[ vUsername ]) )
        {
          delete vUserRoles[ vUsername ]
          $('.roleswitcherdags[data-user="' + vUsername + '"]').text('Standard')
        }
      }
      else
      {
        vUserRoles[ vUsername ][ vRoleID ] = true
        vSet = true
      }
    }
    else
    {
      vUserRoles[ vUsername ] = {}
      vUserRoles[ vUsername ][ vRoleID ] = true
      vSet = true
    }
    vCheckbox.style.opacity = 0.4
    if ( vSet && $('.roleswitcherdags[data-user="' + vUsername + '"]').text() != 'Standard' )
    {
      $('.roleswitcherdags[data-user="' + vUsername + '"]').click()
    }
    $.post( '<?php echo $_SERVER['REQUEST_URI']; ?>',
            { saveroles : JSON.stringify( vUserRoles ) }, function()
    {
      vCheckbox.style.opacity = 1
      vCheckbox.checked = vSet
    } )
    return false
  })
  $('.roleswitcherdags').click(function()
  {
    var vUsername = this.dataset.user
    if ( ! vUserRoles.hasOwnProperty( vUsername ) )
    {
      simpleDialog( 'You must assign roles to the user before setting DAG assignments.' )
      return false
    }
    var vTblData = ''
    vListRoleIDs.forEach( function( vRoleID )
    {
      if ( ! ( vRoleID in vUserRoles[ vUsername ] ) )
      {
        return
      }
      var vRoleDAGs = vUserRoles[ vUsername ][ vRoleID ]
      vTblData += '<tr><td style="white-space:nowrap">' + vListRoles[ vRoleID ] + '</td>'
      vTblData += '<td><input type="checkbox"'
      if ( Array.isArray( vRoleDAGs ) && vRoleDAGs.includes( 'null' ) )
      {
        vTblData += ' checked'
      }
      vTblData += ' data-role="' + vRoleID + '" data-dag="null"></td>'
      vListDAGs.forEach( function( vDAGID )
      {
        vTblData += '<td><input type="checkbox"'
        if ( Array.isArray( vRoleDAGs ) && vRoleDAGs.includes( '' + vDAGID ) )
        {
          vTblData += ' checked'
        }
        vTblData += ' data-role="' + vRoleID + '" data-dag="' + vDAGID + '"></td>'
      })
      vTblData += '</tr>'
    })
    $('#dags-dialog tbody').html( vTblData )
    $('#dags-dialog').dialog(
    {
      modal : true, title : 'DAG assignments: ' + vUsername, width : '80%',
      buttons : [ { text : 'Close', click : function() { $( this ).dialog('close') } } ],
      beforeClose : function()
      {
        var vDAGsStatus = ''
        if ( $('#dags-dialog input:checked').length == 0 )
        {
          Object.keys( vUserRoles[ vUsername ] ).forEach( function( vRoleID )
          {
            vUserRoles[ vUsername ][ vRoleID ] = true
            vDAGsStatus = 'Standard'
          } )
        }
        else
        {
          var vValidConfig = true
          Object.keys( vUserRoles[ vUsername ] ).forEach( function( vRoleID )
          {
            if ( $('#dags-dialog input[data-role="' + vRoleID + '"]:checked').length == 0 )
            {
              vValidConfig = false
            }
          } )
          if ( vValidConfig )
          {
            Object.keys( vUserRoles[ vUsername ] ).forEach( function( vRoleID )
            {
              var vListRoleDAGs = []
              $('#dags-dialog input[data-role="' + vRoleID + '"]:checked').each( function()
              {
                vListRoleDAGs.push( this.dataset.dag )
              } )
              vUserRoles[ vUsername ][ vRoleID ] = vListRoleDAGs
            } )
            vDAGsStatus = 'Custom'
          }
          else
          {
            $('.roleswitcherdagmsg').css('font-weight','bold')
            setTimeout( function() { $('.roleswitcherdagmsg').css('font-weight','normal') }, 2000 )
            return false
          }
        }
        $('.roleswitcherdags[data-user="' + vUsername + '"]').text( 'Updating...' )
        $.post( '<?php echo $_SERVER['REQUEST_URI']; ?>',
                { saveroles : JSON.stringify( vUserRoles ) }, function()
                {
                  $('.roleswitcherdags[data-user="' + vUsername + '"]').text( vDAGsStatus )
                } )
      }
    } )
    return false
  })
})
</script>
<?php

// Display the project footer
require_once APP_PATH_DOCROOT . 'ProjectGeneral/footer.php';
