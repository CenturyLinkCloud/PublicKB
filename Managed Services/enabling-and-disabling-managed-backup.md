{{{
  "title": "Enabling and Disabling Managed Backup",
  "date": "01-30-2015",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false
}}}

<h2>Description</h2>
<p>The Managed Backup service can be configured on new or existing managed servers. For more information on what Managed Backup provides, review the [Managed Backup FAQ](../Managed Services/managed-backup-frequently-asked-questions.md). The steps below walk through how to configure Managed Backup in both scenarios.</p>
<h2>Steps</h2>
<h3>New Server</h3>
<ol>
<li>Follow the [basic steps for creating a new server](../Servers/creating-a-new-enterprise-cloud-server.md).</li>
<li>From the Create Server page, make sure to select a data center that supports both Managed Services and Managed Backup (an updated list is <a href="http://www.ctl.io/managed-services">available here</a></li>
<li>Click the Managed Server toggle to turn it on and then the option for Managed Backup will appear. Click this toggle as well to enable Managed Backup on the new server.<br /><br /><img src="https://t3n.zendesk.com/attachments/token/fPeVUSXJkB6p88aZh4unx4wvL/?name=create-managed-backup.jpg" alt="create-managed-backup.jpg" width="437" height="488" /><br /></li>
<li>The list of operating systems will now be limited to only ones that are supported by both Managed Server and Managed Backup. Select the one you'd like to use for this server, [complete the remaining requested fields](../Servers/creating-a-new-enterprise-cloud-server.md) and click the "create server" button.</li>
<li>Your server will now be provisioned with Managed Backup (and Managed OS) enabled.</li>
</ol>
<h3>Existing Server</h3>
<ol>
<li>Navigate to the Server Details page for the server you'd like to enable or disable Managed Backup on. Make sure the server is in one of the data centers that supports both Managed Services and Managed Backup (an updated list is <a href="http://www.ctl.io/managed-services">available here</a>).</li>
<li>On the right side under the Server Info section, find the button for enabling or disabling Managed Backup.<br /><img src="https://t3n.zendesk.com/attachments/token/1zd6mxWo6HUOXNFNoEvowWgZC/?name=server-details-backup.jpg" alt="server-details-backup.jpg" width="459" height="412" /><br /></li>
<li>Clicking this button will slide down the Managed Backup configuration area where you may toggle Managed Backup on or off.<br /><img src="https://t3n.zendesk.com/attachments/token/xrwvpNsH2k5JR01NPBZsj4Qxy/?name=server-details-backup-on-off.jpg" alt="server-details-backup-on-off.jpg" width="458" height="411" /><br /></li>
<li>After setting the toggle, click "apply" and a Blueprint will run to configure the server as indicated.</li>
</ol>

<h2>Troubleshooting</h2>
<h3>Error on New Server Creation - VA1</h3>

<p>
As of Sept 10th, 2016, any customer that tries to create a new VM with Managed Backup enabled in the VA1 datacenter, on a network that was created after Sept 10th, 2016, will receive an error that looks like this.
</p>

<br />
<img src="https://www.ctl.io/knowledge-base/images/managed%20backup%20-%20manual%20ticket%20error%20example.png" alt="managed%20backup%20-%20manual%20ticket%20error%20example.png" />
<br />

 on before you can create a server with managed backup.

<p> Upon receiving this error, you will need to wait while we manually enable managed backup for the network you have chosen to create the new server. Updates on our progress will come via our ticketing system and this is a one time change that is needed for any new network that is created after Sept 10, 2016. Once this work is complete, you can go ahead and create servers on this network with managed backup enabled. Alternatively, you can go ahead and create a server on this network without managed backup. Then, after we are complete with this work, you can go ahead and add managed backup to this server.
</p>

<h3>Managed Backup isn't enabled in VA1, but should be. </h3>
<p>
Even though managed backup is a service that is available in VA1, under certain conditions our user interface will not allow you to create new servers with managed backup. As of Sept 10th, 2016, on any CenturyLink Cloud account that has no networks in VA1, the 'add managed backup' button will be disabled on the create server webpage. To resolve this, you will need to first create a network manually in VA1. Once you do that, you will need to follow the process above listed in section 'Error on New Server Creation - VA1'.
</p>
