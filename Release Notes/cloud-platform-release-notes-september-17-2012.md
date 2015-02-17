{{{
  "title": "Cloud Platform – Release Notes: September 17, 2012",
  "date": "9-19-2012",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (5)</strong>
</p>
<hr />
<ul>
  <li><strong>Blueprints:<em> </em>Open admin view with resume and setting completion.&nbsp;</strong>Account administrators can now resume a failed blueprint at a particular step. This functionality has been available to CenturyLink Cloud administrators and we are now
    opening it up for customers as well.&nbsp;&nbsp;</li>
  <li><strong>Web Fabric: When a user creates an app with multiple instances, show in UI.</strong>&nbsp;&nbsp;While users could use the vmc tool to see the number of instances that their Web Fabric application was running on, we have now made this information
    available in the Control Portal as well.</li>
  <li><strong>Groups: Power Operations - List of servers should include 'select all' option by clicking on the column header AND column header should be renamed</strong>.&nbsp;&nbsp;We've improved the bulk "power" tasks for a Group so that users can select
    all (or unselect all) servers that should respond to the power (on/off/pause/reset/stop/reboot) command.</li>
  <li><strong>Blueprints: Deploy Package - if selected server is powered off, power it on to execute the task, then return to original state.</strong>&nbsp;&nbsp;Previously, executing a blueprint task against a server that was powered off would result in
    an error. Now, we boot up any targeted servers, execute the task and then return the machine to whatever state it was in.</li>
  <li><strong>UI: LESS Conversion UI.</strong>&nbsp;&nbsp;We've made a number of improvements to the look and feel of the site.</li>
</ul>
<p><strong><br /></strong>
</p>
<p><strong>Minor Defects Fixed (114)</strong>
</p>
<hr />
<ul>
  <li><strong>Web Fabric: Error deleting a web fabric - requested group was not found.</strong>&nbsp;&nbsp;Occurred because of some backend changes of server type categorizations.</li>
  <li><strong>Blueprints: Packages with no prompt and sub task of a server build do not prompt for Run-As during build step.</strong>&nbsp;&nbsp;"Run As" option now shows up for all server builds, regardless of the type of packages involved.</li>
  <li><strong>Servers: Converting a server to a template does not use a blueprint. User gets redirected to the async queue.</strong>&nbsp;&nbsp;User is now taken to a blueprint (that is automatically kicked off) when converting a server to a template.</li>
  <li><strong>Web Fabric: Error loading details page for Web Fabric.</strong>&nbsp;&nbsp;Error occurs when Cloud Controller is unavailable and now we provide more details to user instead of a more generic Web Fabric error.</li>
  <li><strong>Servers: Restoring server from archive results in the user being redirected to the pending queue instead of BP Details.</strong>&nbsp;&nbsp;We now make sure that users are shown the in-progress blueprint instead of the work queue.</li>
  <li><strong>Networking: When a public IPAddress is being configured it needs to be able to handle a retry.</strong>&nbsp;We added a bit more intelligence to IP assignment to make sure that the IP address isn't already configured.</li>
  <li><strong>Blueprints: Blueprint API needs updated after internal changes.</strong>&nbsp;&nbsp;After some internal refactoring, the public SOAP API was not correctly retrieving&nbsp;blueprint parameters or enabling publication. The API now works correctly.</li>
  <li><strong>Blueprints: T3admin Errors appear for non-t3admins.</strong>&nbsp;Error messages targeting our internal support team were also being shown to account administrators. Now, those messages are hidden for account administrators.</li>
  <li><strong>Networking: Tier3 Admin - 404 error on Assign Public IP Address.</strong>&nbsp;&nbsp;Site link led to non-existent page and that link has now been corrected.</li>
  <li><strong>Account:&nbsp; Users - Details - Status does not render as expected when viewing currently logged on user's details.</strong>&nbsp;&nbsp;Cleaned up the way the user's status (active/disabled) is shown on a user's account details page.</li>
  <li><strong>Control Portal: Notes - Activity Log Details are overlapping.</strong>&nbsp;&nbsp;We've added more details to the Activity Log when a server is created, but formatting prevented users from seeing all of the messages. That has been corrected.</li>
  <li><strong>Account Management: Account - Sub Accounts - List should not include Parent account.</strong>&nbsp;&nbsp;The list of subaccounts for a given account used to also show the parent account itself, but now the list only shows actual subaccounts.</li>
  <li><strong>Server: Create Server - CPU/Memory should not get reset when selecting template.</strong>&nbsp;&nbsp;The Control Portal was resetting the CPU and Memory values to their default settings when walking through the "create server" process and selecting
    a server template.</li>
  <li><strong>Server: Server details page still has "install software" button which should be removed in lieu of Group Tasks.</strong>&nbsp;&nbsp;The new Group Tasks capability eliminates the need for the legacy "install software" action.</li>
  <li><strong>Web Fabric:&nbsp; UI - Entire tile should be clickable to the details page.</strong>&nbsp;&nbsp;We increased the clickable area of the Web Fabric application blocks.</li>
  <li><strong>Account: Create Sub Account - Remove Secondary DC dropdown option.</strong>&nbsp;&nbsp;We removed the concept of a "secondary datacenter" from the account creation pages as it often does not apply to a given account.</li>
  <li><strong>Tickets: Need to identify what roles can view tickets and only expose the link to those types of users.</strong>&nbsp;&nbsp;Only account and server administrators have the option to view open tickets.</li>
  <li><strong>UI: Put Promo Codes back into the Control Portal.</strong>&nbsp;&nbsp;Added a place for customers to add discount promotion codes to their accounts.</li>
  <li><strong>Monitoring: Overriding Monitors and Editing can cause an error.</strong>&nbsp;&nbsp;An error used to occur when overriding monitoring inheritance for an individual server and then changing multiple monitors.</li>
  <li><strong>Web Fabric: 'Error Loading Web Fabrics' error displayed if WF is powered off.</strong>&nbsp;&nbsp;The user can now see if their Web Fabric environment is offline.</li>
  <li><strong>Network/IP Address: Error adding a Note in an alternate DC.</strong>&nbsp;&nbsp;Adding network notes after switching data center contexts used to raise an exception.</li>
  <li><strong>Blueprints: Sending generic email template with server details for WF build outs, need to only send WF details.</strong>&nbsp;&nbsp;Since Web Fabric users do not typically need to (or want to) see details about the underlying PaaS infrastructure,
    "successful build" emails will now omit details about which servers were created for them.</li>
  <li><strong>Server: Clicking "add new software to library" button results in 404.</strong>&nbsp;&nbsp;At a certain stage of the workflow, a user's attempt to add software to the server would result in a re-direction to a page that didn't exist.</li>
  <li><strong>UI: change all buttons/links to lower case to be consistent throughout the Control Portal.</strong>&nbsp;&nbsp;We've made lots of UI tweaks in this release and this one impacts the appearance of buttons throughout the Control Portal.</li>
  <li><strong>Blueprints: Build - changing server alias' is not updating task label.</strong>&nbsp;&nbsp;We now make sure to use user-defined server alias throughout the blueprint wizard.</li>
  <li><strong>Notes: Description - some notes are showing markup in the text.</strong>&nbsp;&nbsp;HTML tags were visible in Note fields but now they are rendered properly.</li>
  <li><strong>Blueprints: Browse - 'Changes Needed for Approval' should be changed to 'Waiting for Approval.'</strong>&nbsp;&nbsp;Text updated on blueprints that require additional intervention.</li>
  <li><strong>Blueprint: Queue Details - IE9 - progress bar is not filled in.</strong>&nbsp;&nbsp;Updated Internet Explorer rendering problem that occurred during blueprint execution.</li>
  <li><strong>Blueprint: Queue Details - Step count area overlaps when the count wraps.</strong>&nbsp;&nbsp;Page formatting issue when a blueprint with 10+ steps was executed.</li>
  <li><strong>Blueprints: Deploy - text 'Specify the credentials this task will run as' should be hidden unless the user selects to override Credentials to run the task as.</strong>&nbsp;&nbsp;Hiding text that doesn't matter if the user doesn't decide to
    override the credentials that the blueprint task with use during execution.</li>
  <li><strong>Web Fabric: Error Creating new Web Fabric - Name is required.</strong>&nbsp;&nbsp;We cleaned up a few things to make creating and deployment Web Fabrics easier and more consistent.</li>
  <li><strong>Blueprints: Design - Add Disk task on Create Server results in error on apply.</strong>&nbsp;&nbsp;An error used to occur in select cases when adding a disk to a new server within a new or existing blueprint.</li>
  <li><strong>UI:&nbsp; Tall account images throw off upper nav alignment.</strong>&nbsp;&nbsp;User-uploaded images that exceeded a certain height would previously cause a shuffling of navigation menu items.</li>
  <li><strong>Server: Template - Error deleting Server Template.</strong>&nbsp;&nbsp;Fixed issue that occurred when attempting to delete existing server templates.</li>
  <li><strong>Scheduled Tasks: Custom schedule - Monthly modal - Screen size smaller than x900 user is unable to view confirmation buttons.</strong>&nbsp;&nbsp;Changed layout to accommodate&nbsp;smaller screens.</li>
  <li><strong>Scheduled Tasks: Custom Schedule - After custom schedule has been set, editing and then cancel results in custom repeat schedule being deleted.</strong>&nbsp;&nbsp;Corrected problem where custom schedules are preserved if put into an Edit mode
    and then cancelled.</li>
  <li><strong>Blueprints: Add Clone Blueprint Button back to BP details.</strong>&nbsp;&nbsp;Ensured that useful "clone blueprint" button was present after new UI redesign.</li>
  <li><strong>Account: Billing - Invoice page is not rendering correctly.</strong>&nbsp;&nbsp;Fixed some layout alignment issues that appeared on some invoice screens.</li>
  <li><strong>UI: Convert to Template confirmation screen radio buttons misaligned.</strong>&nbsp;&nbsp;Corrected the layout alignment on the "convert server to template" wizard.</li>
  <li><strong>UI: Radio Buttons, Checkboxes misaligned with descriptions in BP design in FF\Chrome.</strong>&nbsp;&nbsp;Cleaned up page layout that rendered funky in different browsers.</li>
  <li><strong>Server: Linux - Build fails if no secondary DNS is supplied.</strong>&nbsp;&nbsp;If the user does not provide a secondary DNS entry during server build, we now populate this value with the default secondary DNS associated with the user's account.</li>
  <li><strong>Blueprints: Converting Server to Template doesn't disable Monitoring.</strong>&nbsp;&nbsp;We now make sure to turn off monitors for templates.</li>
  <li><strong>Blueprints: Script Packages delete isn't soft deleting.</strong>&nbsp;&nbsp;Corrected problem of software packages staying around after the user deleted them.</li>
  <li><strong>Server: Convert Template to Server - Password is not required on the form but is required in the blueprint.</strong>&nbsp;&nbsp;No longer allow user to skip required steps of entering a password for the new server being generated from a template.</li>
  <li><strong>Blueprints: Fail to publish blueprint with a single global task configured to execute on a selected server.</strong>&nbsp;&nbsp;Fixed issue that occurred occasionally with single-task blueprints.</li>
  <li><strong>Blueprints: Designer - Assigning Server to a Task at Design time isn't "sticking".</strong>&nbsp;&nbsp;We noticed that applying a task to a specific server at blueprint design time (e.g. install SQL Server 2008 R2) wasn't being reflected during
    deployment. Now, those settings are retained at deployment time.</li>
  <li><strong>Blueprints: Deploy - Global tasks where a server to be built by the BP is selected shows a dropdown of servers to run on at Deploy time.</strong>&nbsp;&nbsp;[description]</li>
  <li><strong>UI: Server Activity Log headers in Firefox horked.</strong>&nbsp;&nbsp;Browser layout issue corrected.</li>
  <li><strong>Monitoring: alert settings - when unchecking the email notification box, row disappears.</strong>&nbsp;&nbsp;Fixed layout issue for monitoring alert settings.</li>
  <li><strong>Blueprints: Designer - UI Errors Deleting a Server.</strong>&nbsp;&nbsp;Fixed intermittent error that occurred when deleting servers from blueprints.</li>
  <li><strong>Servers: Details - IE9/Firefox - Recent Activity is loading in one long column.</strong>&nbsp;&nbsp;Layout issue fixed.</li>
  <li><strong>Queue (Async) Details: Step Numbers wrap when get to 2 digits.</strong>&nbsp;&nbsp;Corrected layout issue.</li>
  <li><strong>Server Permissions: Control indicates 'Permissions Saved' when they are not in certain scenarios.</strong>&nbsp;&nbsp;We now disable the "save" button on the server permissions page unless changes have actually been made.</li>
  <li><strong>Blueprints: Nested Blueprints fail if parameters are the same.</strong>&nbsp;&nbsp;Fixed issue when using nested blueprints and software/script packages. Now, the proper parameters are applied to each nested blueprint's software/script execution.</li>
  <li><strong>Servers: Quicklinks - Powered off list includes VPN server if powered off, but results in error if clicked.</strong>&nbsp;&nbsp;If a user can see the "system" group of servers and lists the servers within it, they see a details link. Otherwise,
    no links are shown.</li>
  <li><strong>Blueprints: Running a task on a server built by a BP causes the server to be shutdown after successfully completing.</strong>&nbsp;&nbsp;We have verified that new servers are always left "on" after the blueprint completes.</li>
  <li><strong>Servers: Templates - Unmap public IP when a server is converted to a template.</strong>&nbsp;&nbsp;Any public IP addresses are now released after a server is converted to a template.</li>
  <li><strong>Blueprints - Design - Removing a global task redirects to the review page with the deleted item listed.</strong>&nbsp;&nbsp;This fixes two things: first, when a blueprint designer goes from the "review" page back to the Tasks &amp; Order page
    to delete a package, they should stay on that page so that they can delete more packages if needed; second, the deleted package(s) now do now show up on the review page after being deleted.</li>
  <li><strong>Server: Deleting a template results in user redirected to the pending queue instead of blueprint details.</strong>&nbsp;&nbsp;Users now go to a page showing the in-process blueprint after deleting a template.</li>
  <li><strong>Server: When creating a server, Async queue detail page doesn't have link to blueprint detail page.</strong>&nbsp;&nbsp;Allow users to link back to the blueprint that the server is being created from.</li>
  <li><strong>Network: IP Address - Release Public IP address button does not function.</strong>&nbsp;&nbsp;Now it does.</li>
  <li><strong>Server: Details - Monitor Alerts - Hover state is not as wide as the default state.</strong>&nbsp;&nbsp;Fixed formatting of monitoring alerts on the page.</li>
  <li><strong>Alerts: UI Rollover not Working Correct on Server Details.</strong>&nbsp;&nbsp;Corrected issue of popups that wouldn't go away in a timely fashion.</li>
  <li><strong>Login: Sign in button should be lower case.</strong>&nbsp;&nbsp;We're really into lowercase letters now.</li>
  <li><strong>Blueprints: Build - Customize step - Global tasks where server has been selected should show the server name/alias for each task.</strong>&nbsp;&nbsp;Fixed issue that occurred with multiple tasks and multiple servers.</li>
  <li><strong>UI: "Create New" menu drop-down inconsistent between group over page and group detail page.</strong>&nbsp;&nbsp;Ensured that menu options are the same when viewing similar pages.</li>
  <li><strong>Server: Create Server - Add Drive - reserved drive letter warning should match the OS selected.</strong>&nbsp;&nbsp;If the user attempts to add a drive to a reserved letter (e.g. "A" on Windows) then an OS-specific message is shown to the user.</li>
  <li><strong>UI: BP Creation Description field re-sizeable via mouse in Chrome\Firefox - messes with page layout.</strong>&nbsp;&nbsp;Removed the ability to resize the description field to prevent layout wonkiness.</li>
  <li><strong>Database: Replication - Add support for 1) moving users between accounts 2) changing the parent of an existing account.</strong>&nbsp;&nbsp;We now support changing account parents and user association to a given account.</li>
  <li><strong>Monitoring: Alerts - Data includes Time but not Date.</strong>&nbsp;&nbsp;Now showing both date and time for alerts.</li>
  <li><strong>Monitoring: Display top monitor alert notifications on the dashboard. Link to full monitor alert view.</strong>&nbsp;&nbsp;Only shows the top handful of alerts on the page but the user can quickly navigate to the full set of unviewed alerts.</li>
  <li><strong>Blueprints: Designer - MultiSelect checkboxes are not rendering correctly.</strong>&nbsp;&nbsp;Formatting fixed.</li>
  <li><strong>Add "Blueprint Library" link to Blueprints subnav to be consistent with other main nav submenus.</strong>&nbsp;&nbsp;Cleaned up navigation menu and added "Blueprint Library" as a link to all the blueprints that the user is allowed to see.</li>
  <li><strong>Packages: Details - Required Arguments Preview - field and labels do not align.</strong>&nbsp;&nbsp;Formatting fixed.</li>
  <li><strong>Blueprints: Add filter for Server and Networks so that only Tier3 admins see Web Fabric Servers and Networks in dropdowns when deploying a Blueprint.</strong>&nbsp;&nbsp;Non-CenturyLink Cloud administrators can no longer see Web Fabric-type servers/networks
    when building blueprints. Users who want to create a Web Fabric instance should go directly to that portion of the Control Portal.</li>
  <li><strong>Web Fabric: Control for web fabric to display status of apps.</strong>&nbsp;&nbsp;Web Fabric dashboard now shows the states of the applications.</li>
  <li><strong>Server: Snapshot - user has no way to delete a snapshot.</strong>&nbsp;&nbsp;Now you do. The server page now shows all the snapshots for a server and provides an option to delete individual snapshots.</li>
  <li><strong>Server: Snapshot - Error reverting a snapshot multiple times without refreshing the page.</strong>&nbsp;&nbsp;User can now revert to a snapshot multiple times with no UI complication.</li>
  <li><strong>Blueprint: Queue Details - Hitting refresh before the request is queued results in a 500 error.</strong>&nbsp;&nbsp;Well, don't do that! But if you do, we now prevent race conditions from occurring.</li>
  <li><strong>Snapshots should go through Blueprints.</strong>&nbsp;&nbsp;Creating, reverting or deleting a snapshot now launches a blueprint.</li>
  <li><strong>Server: Add Public IP - redirect to the BP Queue Details page on submit.</strong>&nbsp;&nbsp;User is now directed to a blueprint instead of the work queue.</li>
  <li><strong>Layout: Add spacing between sections in right column.</strong>&nbsp;&nbsp;Formatting cleaned up.</li>
  <li><strong>Blueprints: Design - Add Server - 'run task' list is not fully visible on hover.</strong>&nbsp;&nbsp;Better handling for different screen resolutions.</li>
  <li><strong>Blueprints: Deploy - Customize - css issues label and fields are not aligned.</strong>&nbsp;&nbsp;Formatting fix.</li>
  <li><strong>Async Queue Details: formatting of page gets screwed up if message has long text.</strong>&nbsp;&nbsp;Screw ups now averted.</li>
  <li><strong>User Permissions: Domain Admin does not have rights to view Domain Names.</strong>&nbsp;&nbsp;Domain administrators now have access to all Domain pages.</li>
  <li><strong>Queue: Tier3 Admin in Tier3 account filtering off of Tier3 Account and sub accounts selected should show all DC activity.</strong>&nbsp;&nbsp;Fix to ensure that all queue items are shown for accounts and subaccounts.</li>
  <li><strong>Server/Group: Delete - Need to gracefully handle scenario where an error occurs because one or more servers are not found in host. </strong>&nbsp;&nbsp;Users can now delete servers and groups that no longer exist on an underlying virtualization
    host server.</li>
  <li><strong>UI: 'Paused' status on Group hover-over is Red instead of Orange.</strong>&nbsp;&nbsp;Rest assured, someone was fired over this.</li>
  <li><strong>Server: Details - mouse arrow should change (to a hand) on hover over the X on delete/revert snapshot.</strong>&nbsp;&nbsp;The "delete snapshot" button is now more obviously a link.</li>
  <li><strong>Move subnav items from "Dashboard" in the main nav.</strong>&nbsp;&nbsp;Shuffled the top level navigation menu a bit to keep it simple. "Activity History" is now underneath "Account."</li>
  <li><strong>Administrators need to be able to create servers in Fabric Groups and on WebFabric networks.</strong>&nbsp;&nbsp;Administrators now have more flexibility when creating Web Fabric servers.</li>
  <li><strong>Server: Details - Snapshot list - IE9 - on refresh of the page, various (deleted) snapshots are listed.</strong>&nbsp;&nbsp;Intermittent issue experienced with IE9 caching that has been fixed.</li>
  <li><strong>Clicking server link on hardware details gives a 500 for Templates.</strong>&nbsp;&nbsp;Corrected occasional problem with viewing server details page.</li>
  <li><strong>Portal: Change style of Account dropdown.</strong>&nbsp;&nbsp;Handy UI improvement of the Account dropdown list including the ability to search by account alias.</li>
  <li><strong>Queue: Add the ability to filter Completed requests back into the UI.</strong>&nbsp;&nbsp;This filter was removed before, but it's been brought back by popular demand.</li>
  <li><strong>UI: Browse button cutoff in 'Your Logo' selector in IE9\Firefox.</strong>&nbsp;&nbsp;"Browse" button for uploading a custom logo was being partial obscured.</li>
  <li><strong>Account: User Profile - Remove the DC dropdown from the User Profile page.</strong>&nbsp;&nbsp;User's profile page no longer has the option to edit their data center.</li>
  <li><strong>Queue: previous status is not removed on autorefresh.</strong>&nbsp;&nbsp;Only current status is shown now.</li>
  <li><strong>Queue: Add Auto-Refresh setting.</strong>&nbsp;&nbsp;[description]Auto-refresh occurs within the queue and is apparent to the user.</li>
  <li><strong>Domains: DNS - Zone Details - Error displayed on the page causing .css issues as well.</strong>&nbsp;&nbsp;Fixed error that occurred when viewing details of a DNS zone.</li>
  <li><strong>Server: Notes - log when a user creates or deletes a snapshot.</strong>&nbsp;&nbsp;The creation or deletion of a snapshot now results in a new note added to the log.</li>
  <li><strong>UI: Default Server Settings not honored when Creating a Server.</strong>&nbsp;&nbsp;Didn't occur when creating servers from groups, but when creating a server outside the group pages, any overridden CPU/MemoryOS settings were being ignored.</li>
  <li><strong>MonitoringManager: Error ensuring group hierarchy.</strong>&nbsp;&nbsp;Corrected problem in monitoring manager that prevented some users from loading the Monitors tab for certain server groups.</li>
  <li><strong>Blueprint: Details - When switching DC context from the BP details page, 404 error.</strong>&nbsp;&nbsp;Validated flow for users switching data center context from different pages within the Control Portal.</li>
  <li><strong>Queue: List page - timestamp should be converted to user's timezone.</strong>&nbsp;&nbsp;Converted UTC timestamps to the local user's timezone.</li>
  <li><strong>Queue: multiple issues on queue list page related to account/status filters. </strong>Fixed problems where account filters were not defaulting to the current account and some items were only showing up after an auto-refresh.</li>
  <li><strong>Servers: Group Details - IE 9 - Tiles do not have rounded corners.</strong> Formatting clean up.</li>
  <li><strong>Queue: Account filter list should be sorted by Business Name.</strong> Changed filtering to look at business name, not alias.</li>
  <li><strong>Blueprint: Error when deleting blueprint from remote DC.</strong> Fixed problem that occurred when deleting blueprints across data centers.</li>
  <li><strong>Server: Create server does not refresh template list on DC change.</strong> The list of available templates now resets when the data center changes in the "create server" flow.</li>
  <li><strong>API: Add Blueprint Validation prior to submitting requests to the blueprint engine.</strong> Improved input validation logic for API calls to the Blueprint service.</li>
  <li><strong>Server: Create Server - Add Task - hitting enter when no tasks are found causes 500 error.</strong> Fixed error that occurred when adding search text that didn't return any scripts.</li>
  <li><strong>Fabrics - Web Fabric - More than 3 apps results in wrapping.</strong> Fixed formatting of Web Fabric screen.</li>
</ul>