{{{
  "title": "Cloud Platform – Release Notes: July 28, 2014",
  "date": "10-13-2014",
  "author": "Bryan Friedman",
  "attachments": []
}}}

<p><strong>New Features (5)</strong>
</p>
<hr />
<ul>
  <li><strong>Horizontal Autoscale.</strong>&nbsp;CenturyLink Cloud now supports Horizontal Autoscale, allowing for groups of servers that meet a user-defined CPU and/or RAM utilization threshold to be scaled out/in by powering on/off one or more additional
    servers in the group. (The existing Autoscale functionality allowing for scaling number of CPUs up or down on a server is still available as Vertical Autoscale.)
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/yQNnG88xba6VngVV1XTOeKWjg/?name=create-h-autoscale.png" alt="create-h-autoscale.png" />
    <br />
  </li>
  <li><strong><strong>Completed Redesign of Server UI.&nbsp;</strong></strong>The new version of the Server UI has been completed and now incorporates all remaining features from the previous UI including viewing partitions, disk management, scheduled task
    management, and actions for converting to template, archiving, cloning and toggling maintenance mode.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/Ojsbts6ExfgaIUgbV7FqYdTiT/?name=partition-disk-new-ui.png" alt="partition-disk-new-ui.png" />
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/BYSN2lwOov3n4pHMHd9ohJG4L/?name=scheduled-tasks.png" alt="scheduled-tasks.png" />
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/xXmFulEevjZht4v2VZb4szVOs/?name=maint-mode.png" alt="maint-mode.png" />
    <br />
    <br />
  </li>
  <li><strong>Data Center Updates.&nbsp;</strong>The CenturyLink Cloud opened another data center in Toronto, Canada (CA3). This new location is now live for all users and offers all the standard CenturyLink Cloud capabilities including support for Hyperscale
    Servers. There is further data center expansion planned for later this year as well.&nbsp;
    <br /><img src="https://t3n.zendesk.com/attachments/token/dY44pCFVakFBS4tueAboQeoFr/?name=dc-list-ca3-nogb2.png" alt="dc-list-ca3-nogb2.png" />
  </li>
  <li><strong>Managed Services. </strong>Combining&nbsp;CenturyLink’s expertise in both the cloud and managed services spaces, users (CenturyLink-managed customers only) will now see a "managed server" option&nbsp;when creating a server, allowing them to
    enable managed services with just one click, the ease of a cloud utility, and pay-by-the hour billing. Currently, the available managed services are Microsoft Windows Server (2008 and 2012), Red Hat Enterprise Linux 6.5, Active Directory, Apache HTTP
    Server, Microsoft IIS, MS SQL, MySQL, and Tomcat, with more rolling out in the coming months.&nbsp;The configuration, monitoring, and ongoing administration as well as the provisioning of each of these services is also automated via our Blueprints
    orchestration engine. Managed services are available in Sterling and Santa Clara data centers only at this time, with additional sites online in the coming months. Read more about managed services on our <a href="http://www.ctl.io/managed-services"
   >web site</a> and in our <a href="https://t3n.zendesk.com/categories/20074004-Managed-Services">Knowledge Base</a>.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/5bBJQEkZAT4zzRmRIs8bEfEBv/?name=create-managed-server.png" alt="create-managed-server.png" />
    <br />
    <br />
  </li>
  <li><strong>Improved Cloning. </strong>Some improvements were made behind the scenes to the server cloning process. Along with the updated UI shown above, the underlying cloning process is now faster and&nbsp;more resilient.
    <br />
    <br />
  </li>
</ul>
<p><strong>Minor Enhancements (4)</strong>
</p>
<hr />
<ul>
  <li><strong>Consolidated "Policies" Menu.&nbsp;</strong>The management of Alerts, Autoscale, and Hyperscale Anti-Affinity has been consolidated into one area called "Policies" which is accessible from the Servers menu.
    <br /><img src="https://t3n.zendesk.com/attachments/token/Z9ytuI0EaGo1ilZsosG8TfG58/?name=policies-menu.png" alt="policies-menu.png" />
    <br /><img src="https://t3n.zendesk.com/attachments/token/N7vOSxqen80b3zPpiMizm4LaG/?name=policies.png" alt="policies.png" />
  </li>
  <li><strong>Group/Server Permissions removed.&nbsp;</strong>Over the past 8 months, the CenturyLink Cloud team has been rebuilding the underlying platform API and the new, robust permissions model is incompatible with the legacy server and group resource-level
    permission model. With the completion of the new Server API v2 this month, the Server and Group permissions have been retired. Look out for new role-based access controls in the Control Portal later this year.
    <br />
  </li>
  <li><strong>Maintenance Window removed. </strong>The&nbsp;Maintenance Window section under Scheduled Tasks has been removed, however we still encourage users to put servers or groups of servers into maintenance mode before applying patches or software updates.
    This will ensure that all monitoring&nbsp;of the server or group of servers is turned off for the maintenance tasks to be performed. Webhooks are still enabled and will be triggered when a server is put into or taken out of maintenance mode.</li>
  <li><strong>60GB Sizing for Windows Servers.&nbsp;</strong>The disk size for servers provisioned with Windows 2008 or 2012 Server templates have been set to a consistent size and have been increased to 60GB. This was due to customers running into
    build failures caused by the drives not having sufficient space to run a number of blueprints.</li>
  <li><strong>New CoreOS Blueprint.&nbsp;</strong>Blueprints have been created for deploying CoreOS servers. Follow the <a href="https://t3n.zendesk.com/entries/47064274-Building-CoreOS-Server-Cluster-on-the-CenturyLink-Cloud">KB article on building CoreOS servers on CenturyLink Cloud</a>&nbsp;to
    see how they are used.</li>
</ul>