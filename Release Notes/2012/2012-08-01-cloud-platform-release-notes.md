{{{
  "title": "Cloud Platform – Release Notes: August 1, 2012",
  "date": "8-12-2012",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (6)</strong>
</p>
<hr />
<ul>
  <li><strong>Blueprints: Allow Users to specify unique values for each instance of a task in a blueprint.</strong>&nbsp;Previously, if the same software/script/task was added to a blueprint multiple times, there was no way to specify unique parameters for
    each instance. Now, users can provide specific parameters for every instance of a package. See <a href="../../Blueprints/add-multiple-instances-of-a-software-package-to-a-blueprint.md">this CenturyLink Cloud Knowledge Base article</a> for
    a detailed walkthrough.</li>
  <li><strong>Blueprints: Run package on group.&nbsp;</strong>Adds a new way to select, configure and run software/script packages against all or any of the servers in a Group. See&nbsp;<a href="../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md">this CenturyLink Cloud Knowledge Base article</a>&nbsp;for a further description of this feature.</li>
  <li><strong>Activity Log: Implement Show More.</strong>&nbsp;From the Control Portal dashboard, when the user views “Account Activity History” we now load a subset of data and allow the user to see further back in time.</li>
  <li><strong>Billing: Display Detailed information for a Group.</strong>&nbsp;CenturyLink Cloud bills are broken down by Group to help users view a more detailed cost breakdown. Now, the bills also show which servers are part of the Group that incurred charges.</li>
  <li><strong>Make it so that standard servers can go to 16GB ram in the Control Portal.&nbsp;</strong>Standard servers could only previously allocate 8 GB of RAM but now accept up to 16 GB of RAM.</li>
  <li><strong>Blueprints: add ability to clone a blueprint.</strong>&nbsp;Users can now take their blueprints and use them as a foundation for new blueprints. Note that users can only clone blueprints that were created by a user in the same account.</li>
</ul>
<p><strong><br /></strong>
</p>
<p><strong>Minor Defects Fixed (50)</strong>
</p>
<hr />
<ul>
  <li><strong>Reorder tabs on Server &amp; Groups Schedules</strong>. On “Schedules” tab for either servers or groups, “Scheduled Tasks” is now the first item shown instead of “Maintenance Window.”</li>
  <li><strong>Server: Price Calculator doesn't work for drive added by group default settings</strong>. If a user adds a storage drive to a Group’s default server settings and then creates a server in that Group, changing the amount of storage (via the slider)
    did not affect the price estimate. Now, changes to the storage amount are instantly reflected in the calculator.</li>
  <li><strong>Blueprints: Power Ops not functional.</strong> There was inconsistent behavior when using power operations (“turn on”, “turn off”) against all of the servers in a Group.</li>
  <li><strong>Web Fabric: WFs that are "Building" shouldn't be clickable. </strong>Prevent users from trying to add applications to Web Fabric environments that are still being built.</li>
  <li><strong>Server Rename Feature: several server parameters not updated when Server name is. </strong>When renaming a blueprint for Windows Server, subsequent tasks/packages were not updated with the new server name.</li>
  <li><strong>Permissions: Server Admins do not have access to Async queue details. </strong>Previously, users in the “server administrator” role couldn’t view server queue content.</li>
  <li><strong>Blueprints: Details Page doesn't auto-refresh until 'Refresh Details' button is pressed. </strong>Blueprints now reliably auto-refresh to show build process.</li>
  <li><strong>Server: Server Error when sliding memory size slider when adding a Disk. </strong>Errors were occasionally thrown when users change memory allocation, and that has been corrected.</li>
  <li><strong>Blueprints: Blueprints Queue/Async Queue - progress is not updated for blueprint execution. </strong>Ensure that blueprint execution status is accurate across all views.</li>
  <li><strong>Deleting a hardware group fails with "Value cannot be null" error. </strong>Problems encountered when deleting Groups have been fixed.</li>
  <li><strong>Packages: Unable to view a shared package when logged in as an Account Admin viewing a sub account.</strong> Fixed visibility problem when creating packages in sub accounts.</li>
  <li><strong>Add disk to Ubuntu Server fails with 'Actively Refused' connection error. </strong>Corrected problem encountered when adding disks to Ubuntu servers.</li>
  <li><strong>Monitors - Devices in remote DCs are setup incorrectly. </strong>There was an issue with creating monitors in some data centers.</li>
  <li><strong>Blueprints: Published packages need to apply correct account filtering. </strong>Did extra work to verify that private software/scripts are only available to the account holder.</li>
  <li><strong>Server: clone server - check for resource limits should use the same functionality that Create Server uses. </strong>Cloned servers now respect the group’s capacity thresholds in the same way that the “create server” process does.</li>
  <li><strong>Blueprints: Packages - Required flag is being ignored. </strong>User was previously forced to enter data in non-required fields.</li>
  <li><strong>Always Show Run As in Blueprints.</strong> For any blueprint that contains a software/script package, the system now shows a “run as” parameter that lets the user choose which account permissions drive the installation.</li>
  <li><strong>Server Permissions: Manual permissions setting doesn't stick for account admins.</strong> Fixes problem with persisting permission changes made by account administrators.</li>
  <li><strong>Blueprints: Ability to delete a blueprint / script package / software package.</strong> Users within the same account can now delete existing blueprints or uploaded software/scripts.</li>
  <li><strong>Server: Restore - Unable to restore an archived server in WA1 due to incorrect query finding datastore</strong>. Corrected archive restoration problem in WA1 data center.</li>
  <li><strong>Data Center: can't create server from Template created in Alt DC. </strong>There was a problem with creating servers from templates associated with an alternative data center.</li>
  <li><strong>API Rework. </strong>Changes were made to API methods: CreateGroup, CreateGroups, CreateServer, DeleteGroup, Group Power, Server Power.</li>
  <li><strong>Archive Settings tab in Alt DC results in 500 error. </strong>Fixed group archives so&nbsp; that they do not show settings that don’t apply.</li>
  <li><strong>Servers: Clone - users should not be able to clone a server with snapshots.</strong> Added rules to disallow cloning on servers with snapshots.</li>
  <li><strong>Blueprints: Add Blueprint during BP design includes misspelled\misaligned info columns. </strong>Cleaned up user interface within the Blueprint Designer.</li>
  <li><strong>Ubuntu 12 LTS template.</strong> Updated the Ubuntu templates.</li>
  <li><strong>Archive: 500 error loading group. </strong>Fixed error that occurred when administrators tried to load archive groups.</li>
  <li><strong>Add Disk size increments to non-even numbers if changed from the default 50 GB setting. </strong>Previously, changing disk size from the default value resulted in values that ended in “1” (“31”, “51”, “91”). Now disk size increments/decrements
    to values ending with a “0.”</li>
  <li><strong>WebFabric/ServiceChannel Error. </strong>Fixed intermittent problem discovered when provisioning Web Fabric environments.</li>
  <li><strong>Cloud Foundry tasks for Web Fabric.</strong> Update Web Fabric and other forks to latest upstream Cloud Foundry code.</li>
  <li><strong>Server: Create Server - Template list should filter out Deleted Templates from the list.</strong> Ensure that deleted templates no longer show up as valid options during the server creation process.</li>
  <li><strong>Private Shared Server Templates. </strong>Fixed private shared server templates so that they were visible for sub-accounts.</li>
  <li><strong>Blueprints: BlueprintXML TaskID and GroupIDs are not unique when same task is added multiple times in a blueprint.</strong> When associating software packages to specific servers during design of a blueprint, users had to once again associate
    software to servers during deployment of that blueprint. Now, associations made during blueprint design are persisted when starting the deployment process.</li>
  <li><strong>Server: Create Server - No Servers populate dropdown when adding a task with a server parameter. </strong>Fixed issue that occurred when adding tasks with server parameters.</li>
  <li><strong>Blueprints: Unable to view Blueprint Details. </strong>Corrected error that occurred when trying to view blueprint details from the Control Portal.</li>
  <li><strong>SendEmail boolean on CreateServer does nothing.</strong> Now we send blueprint summary emails when blueprint completes.</li>
  <li><strong>Add more info to server create change log.</strong> Show the name of the blueprint that the server was created from.</li>
  <li><strong>Queue: Error Queue page - failed requests are not appearing for Account Admins. </strong>User would expect to see failed requests when failure occurs, but only the CenturyLink Cloud Admin could see them. Corrected this issue.</li>
  <li><strong>Groups: 'Trash' Group shows as a Standard (not System) Group to non t3n admins.</strong> Some accounts were seeing the system Group that holds deleted servers and now that Group is only visible to CenturyLink Cloud administrators.</li>
  <li><strong>Server: Create - Alt DC - user should be able to select 'New Network' if no network exists in the target DC. </strong>Fixed network options for users who needed to add a network in the target data center.</li>
  <li><strong>Server: Create - Install SQL fails when added as part of Create Server operation. </strong>Corrected problem experienced when adding SQL Server software to new servers.</li>
  <li><strong>Blueprints: Error reporting. </strong>Added more error details for failed blueprints.</li>
  <li><strong>Blueprints: Scripts/Software - the Upload button is missing.</strong> Corrected problem with “upload” button not showing up on the software/scripts pages.</li>
  <li><strong>AccountService.svc CreateAccount errors during self-register activation since the last deployment.</strong> Account registration from the public CenturyLink Cloud site was causing backend error messages.</li>
  <li><strong>API: Create Server - An existing network is required to build a server, but newly created accounts have no networks. </strong>Previously, if a user created an account via the API and then tried to build a server, it would fail because no valid
    network existed yet. The system now allows empty network information where none exists.</li>
  <li><strong>Blueprints/Networking: Error creating first server when no network exists. </strong>Creating new server from the UI when no network existed yet resulted in an error.</li>
  <li><strong>Servers: Create - Tasks that have global parameters are not prompted. </strong>Blueprint execution failed when a task’s global parameters were missing, so this fix ensures that the user is prompted to enter required parameters on tasks.</li>
  <li><strong>Monitoring: Statistics Improvement. </strong>Now checks for recent ping results before trying to grab other performance statistics.</li>
  <li><strong>Blueprints: Packages - Parameters that reference an account's resources should fail validation if those resources are not available to be selected. </strong>Fixed error that occurred when user attempted to add a package when they didn’t have
    any servers created yet.</li>
  <li><strong>Blueprints: Error deploying or editing a Blueprint with multiple instances of the same blueprint included. </strong>Error occurred when adding multiple instances of the same blueprint to another blueprint.</li>
</ul>
<p></p>
