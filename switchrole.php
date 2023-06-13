<?php

namespace Nottingham\RoleSwitcher;

// Only show this page to users defined in the module settings.
if ( ! in_array( USERID, $module->getRoleSwitchUsers() ) )
{
	exit;
}

$listUserRoles = $module->getRolesForUser( USERID );
$currentRole = $module->getUser()->getRights()['role_id'];

if ( isset( $_POST['set-role'] ) )
{
	if ( isset( $listUserRoles[ $_POST['set-role'] ] ) )
	{
		$module->getProject()->setRoleForUser( $listUserRoles[ $_POST['set-role'] ], USERID );
		$module->setUserDAGs( USERID, $_POST['set-role'] );
	}
	header( 'Location: https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'] );
	exit;
}

// Display the project header
require_once APP_PATH_DOCROOT . 'ProjectGeneral/header.php';


?>
<div class="projhdr">
 Switch Role
</div>
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
