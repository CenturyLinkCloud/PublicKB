{{{
  "title": "Using Managed Backup Client",
  "date": "08-18-2017",
  "author": "John Gerger",
  "attachments": [],
  "contentIsHTML": true
}}}

**Managed Backup went End of Sale 6/25/19, all existing subscriptions will still continue to function**

**You will not be able to add Managed Backup to new servers, but it can be removed from existing servers**

<h2>Overview</h2>
<p>While Control Portal allows for turning Managed Backup on and off for a given server, getting details about the status of recent backups or changing the target of the backups using an exclusions list are not yet supported through this interface. This functionality is provided, however, by the Netbackup Client installed on the server itself. After gaining access to the server remotely through either RDP on Windows or SSH on Linux, you can use the following instructions to review status or set paths for exclusion. For help using the Netbackup Client for exclusions or viewing status, you may also contact the CenturyLink Client Service Center at 1-888-638-6771.</p>
<h2>Using Netbackup Client</h2>
<h3>Reviewing Backup Status</h3>
<p>Netbackup Client can be used to obtain the status of recent backups on both Windows and Linux machines.</p>
<h4><strong>Windows</strong></h4>
<p>Windows offers both a GUI client as well as information on the command line.</p>
<ol>
<li>To use the GUI, launch the <em>Netbackup Client Job Tracker</em> via the Start Menu. Make sure to use "Run as Administrator" as it will be required to launch this app. This interface will show the most recent backup and status, as well as the start and end time. Clicking the "Previous" or "Next" buttons will show other completed backups.<br /><img src="https://t3n.zendesk.com/attachments/token/1WEtQoIoZTFnzOiElbyNppMCO/?name=job-tracker-2.png" alt="job-tracker-2.png" width="436" height="333" /><br /></li>
<li>For the command line tool, you can run the bpclimagelist command as follows <code>C:\Program Files\VERITAS\NetBackup\bin\bpclimagelist.exe -client &lthostname&gt</code> . This will display a list of the successful backups that have occurred for the past 14 days, which correlates with the 2 weeks of retention on the backups. If any dates are missing, this is an indicator of a backup that did not occur or failed. (In these cases, notification has been sent to the Operations Support Team at the time of failure to remedy the failed backup.)<br /><img src="https://t3n.zendesk.com/attachments/token/Z7Ij7nhSki6gamgajWTTi5Pb6/?name=windows-cmd-line.png" alt="windows-cmd-line.png" width="619" height="500" /></li>
</ol>
<p><strong>Linux</strong></p>
<p>Linux provides the bpclimagelist command that can be ran as follows <code>/usr/openv/netbackup/bin/bpclimagelist -client <hostname> -b</code>&nbsp;. This will display&nbsp;a list of the successful backups that have occurred for the past 14 days, which correlates with the 2 weeks of retention on the backups. If any dates are missing, this is an indicator of a backup that did not occur or failed. (In these cases, notification has been sent to the Operations Support Team at the time of failure to remedy the failed backup.)<br /><img src="https://t3n.zendesk.com/attachments/token/n70hTP5bAs32Eg2jaAKs20sss/?name=linux-cmd-line.png" alt="linux-cmd-line.png" width="644" height="352" /></p>
<h3>Setting Exclusion Rules</h3>
<p>NetBackup provides for the ability to exclude or filter data from a backup job while it is running. A backup job is created with a defined include list for the policy and in the case CenturyLink Cloud Managed Backup, includes the entire volume for all disks by default. By creating an exclude list, it is possible to remove entries from the backup job which would normally be covered by the running job.&nbsp;It is recommended to utilize small, simple exclude lists where possible as they will add additional processing overhead.</p>
<p>The primary cases for defining an exclude list are when you would like to:</p>
<ul>
<li>Exclude data which would cause the backup to exit with a partial success code (e.g. locked temp file)</li>
<li>Prevent backup of junk data which has limited utility for system recovery (e.g. live database files which should be backed up with an agent, or using a script to export data to another directory)</li>
<li>Prevent backup of data which does not require frequent backup (e.g. Archive directory)</li>
<li>Lower the total usage resulting in lower billing</li>
</ul>
<p>The exclude list can be modified for both Windows and Linux machines.</p>
<h4>Windows</h4>
<div>Custom excludes can be set up using the NetBackup Client in Windows.</div>
<ol>
<li>Open the Netbackup client&nbsp;via the Start Menu (<em>Netbackup 7.x Start &gt; Symantec Netbackup &gt;Backup, Archive and Restore</em>).</li>
<li>Navigate to <em>File &gt; Netbackup Client Properties&nbsp;</em>then to the&nbsp;<em>Exclude List</em> tab.&nbsp;<br /><img src="https://t3n.zendesk.com/attachments/token/3qSqcuGdr7T7f6SEgAQ34NX8M/?name=netbackup-exclude-windows.png" alt="netbackup-exclude-windows.png" width="407" height="273" /><img src="https://t3n.zendesk.com/attachments/token/UVHfLzuQY4ilGNMkDKnLCi97G/?name=netbackup-exclude-list-windows.png" alt="netbackup-exclude-list-windows.png" width="304" height="273" /><br /></li>
<li>Enter a file or path name including the asterisk (*) as a wildcard and click the "Add" button to add it to the list.</li>
</ol>
<h4>Linux</h4>
<p>Custom excludes are configured in Linux by adding a line to the <code>/usr/openv/netbackup/exclude_list file.</code></p>
<ol>
<li>Open the <code>/usr/openv/netbackup/exclude_list</code> using <code>vi</code> (or your favorite Linux text editor).</li>
<li>Add the directories to be excluded.<br /><br />e.g. You might add the below paths to exclude_list:<br />
<pre>/data02/apphome/crmprd/purging/<br />/data02/apphome/crmprd/appjobs/filter/Neolane*<br />/data02/apphome/crmprd/ temp</pre>
</li>
<li>Save the file and quite (<code>:wq!</code> in <code>vi</code>).</li>
</ol>
