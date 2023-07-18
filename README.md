# Role-Switcher
REDCap External Module: Allow users to switch themselves between roles.

## Accessing the Role Switcher
When the module has been enabled in a project, there are two links which may be displayed under the
external modules heading in the project menu.
* Switch role<br>
  This link will appear for any user assigned to multiple roles with the role switcher. It will take
  them to a page that has a button for each of their roles and they can click the buttons to switch
  between the roles.
* User role assignments<br>
  This link will appear for any user with the User Rights privilege (or the module specific
  privilege if enabled). It links to a page with a table of users and roles and allows the
  assignment and un-assignment of users to roles.

## Configuring role assignment rights
By default, users with the User Rights privilege can edit user role assignments. If the system
setting **Module configuration permissions in projects** is changed to **Require module-specific
user privilege**, then this privilege will control access to user role assignments instead.

## Setting user role assignments
To change the role assignments for a user, go to the *User role assignments* page and tick or untick
the roles next to the user as required.

## Setting custom per-role DAG assignments
If the DAG assignments are left as standard, the user will always be assigned to the same DAGs
regardless of which role they have selected. Clicking the link under *DAG assignments* will open the
option to select the DAGs the user should be assigned to when they change to each role. Each role
can have any combination of DAGs (including *no assignment*) but each role must have at least one
DAG (or *no assignment*) selected. If every role has no DAGs selected, the DAG assignments will
revert to standard.