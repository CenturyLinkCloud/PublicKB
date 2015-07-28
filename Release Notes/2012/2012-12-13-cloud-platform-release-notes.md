{{{
  "title": "Cloud Platform – Release Notes: December 13, 2012",
  "date": "1-22-2013",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (3)</strong>
</p>
<hr />
<ul>
  <li><strong>Self-service Firewall Policies for all customers.</strong> Administrators for a given CenturyLink Cloud account can now create and modify firewall policies for their network(s). For more information, check out Knowledge Base articles on <a href="../../Network/creating-cross-data-center-firewall-policies.md">"Connecting Data Center Networks Through Firewall Policies"</a> and <a href="../Networks/creating-bi-directional-firewall-policies.md">"Creating Bi-Directional Firewall Policies."</a>
  </li>
  <li><strong>Cross Data Center Firewall Policies.</strong>Customers can now create sophisticated firewall policies that permit traffic between CenturyLink Cloud data centers. See the Knowledge Base article <a href="../../Network/creating-cross-data-center-firewall-policies.md"
   >"Creating Cross Data Center Firewall Policies"</a> for a complete walkthrough of the feature. <strong>[NOTE: This feature may not be available to all customers until 12/21/12]</strong>
  </li>
  <li><strong>Account activity history log. </strong>Up until now, the audit history for an account was a long, scrolling list of actions performed within a single account. Now, view, filter and export the activities performed by users within an account and
    any sub-account. For more details, view the Knowledge Base article called <a href="../../Servers/searching-for-records-in-the-account-activity-history-log.md">"Searching for Records in the Account Activity History Log."</a>
  </li>
</ul>
<p></p>
<p><strong>Minor Defects Fixed or Enhancements Added (8)</strong>
</p>
<hr />
<ul>
  <li><strong><strong>Set time-to-live for a new server.</strong></strong>When building servers, users can now choose to define archival or deletion schedules for their server. To see this in action, view the Knowledge Base article&nbsp;<a href="../../Servers/creating-a-new-enterprise-cloud-server.md"
   >"Creating a New Enterprise Cloud Server"</a>.</li>
  <li><strong><strong>Ask user to pick deletion date when taking a server snapshot.&nbsp;</strong></strong>Server snapshots are a useful way to safely try server changes. However, they can grow large and are subject to deletion. Now, users can specify the
    lifespan of a snapshot (up to 10 days) when creating one. To see how this works, view the Knowledge Base article "<a href="../../Servers/creating-and-managing-server-snapshots.md">Creating and Managing Server Snapshots</a>."</li>
  <li><strong>Choice to archive or delete a server as part of Scheduled Task.&nbsp;</strong>Scheduled Tasks are used when cloud users want to perform automated actions against a single server or set of servers. Users can now archive or delete servers via
    Scheduled Tasks. Read the Knowledge Base article <a href="../../Servers/creating-a-scheduled-task.md">"Creating a Scheduled Task"</a> for a detailed walkthrough.</li>
  <li><strong>Larger server sizes available. </strong>Users can now provision individual servers with up to 16 CPUs and 128 GB of RAM.</li>
  <li><strong>Group Tasks now run against powered-off servers.&nbsp;</strong>Group Tasks are a great way to execute scripts or install software against collections of servers. Now, Group Tasks can be executed against servers that are not running. The process
    will take those servers and put them temporarily into a running state, execute the Task, and return the server to its prior state. See the Knowledge Base article <a href="../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md"
   >"Using Group Tasks to Install Software and Run Scripts on Groups"</a> for a walkthrough of Group Tasks.&nbsp;</li>
  <li><strong>Self-service disk re-size of root drive for servers running Windows Server 2008 and above.&nbsp;</strong>We recently added support for increasing disk size of non-root storage drives (see blog post <a href="http://www.tier3.com/blog/full/running-out-of-disk-space-you-can-expand-it-yourself"
   >"Running Out of Disk Space? You Can Expand It Yourself!"</a>). With this release, we also support changing the root (C:) drive of servers running Windows Server 2008 and above.</li>
  <li><strong>Email notification templates for new users within an account.&nbsp;</strong>Administrators of an account can now customize "welcome" emails for new users added to an account. This is located under the <strong>Settings</strong>&nbsp;of an <strong>Account</strong>.</li>
  <li><strong>Reorder firewall policies through both drag-and-drop and input fields.&nbsp;</strong>For long lists of firewall policy rules, users now have the option of reordering them by changing the values in input fields next to each rule.</li>
</ul>
