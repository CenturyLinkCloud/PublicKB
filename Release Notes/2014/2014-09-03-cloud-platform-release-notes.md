{{{
  "title": "Cloud Platform – Release Notes: September 3, 2014",
  "date": "10-13-2014",
  "author": "Bryan Friedman",
  "attachments": []
}}}

<p><strong>New Features (3)</strong>
</p>
<div>
  <hr />
</div>
<ul>
  <li><strong>Groups UI Redesign.&nbsp;</strong>The new Groups UI has been restyled to offer usability enhancements and more new features including a 'create' page, a 'settings' page, and maintenance mode toggling.</li>
  <ul>
    <li><strong>Create Group. </strong>Create a new group right from within the new UI. Define the name, description, parent group, any custom field values, and then return to the primary Groups view to easily perform popular activities and seamlessly navigate
      between the compute resources in an account. You can even associate a horizontal autoscale policy at group creation time!
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/O61nX80sKqEZgYo7OkSoZuu3j/?name=create-group.png" alt="create-group.png" /><strong><br /><br /></strong>
    </li>
    <li><strong>Group Settings.</strong>&nbsp;Viewing and editing Group settings and defaults can now be done directly from the new Groups UI without bouncing back and forth between the old and new interfaces. Make common changes (like renaming, changing
      the description, and setting server defaults) from the new Group Settings page.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/D2DnP5Pzako1m5RRgKf0hjlT3/?name=group-settings.png" alt="group-settings.png" />
      <br />
      <br />
    </li>
    <li><strong>Group Maintenance Mode.&nbsp;</strong>Toggle maintenance mode on or off for multiple servers within a Group. With one click, you'll see a complete list of servers within the Group, as well as the the current maintenance mode state for each
      one. Check a server to turn on maintenance mode, or uncheck it to turn it off.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/AMPISKpnMupnzJSe3h41Ufzeq/?name=maint-mode-groups.png" alt="maint-mode-groups.png" />
    </li>
  </ul>
  <li><strong>1 TB Hyperscale.&nbsp;</strong><a href="http://www.ctl.io/hyperscale/">Hyperscale</a> instances now support up to <em>one terabyte</em> (1,024 GB) of total storage. This offers more than six times the previously
    available capacity for web-scale and distributed architectures like&nbsp;NoSQL workloads, distributed systems, and other big data jobs.</li>
</ul>
<ul>
  <li><strong>Create Server with Custom Fields. </strong>Users who have custom fields defined to store additional metadata about servers can now save time by populating these values at server creation time. No more waiting for the server to finish provisioning
    in order to update this metadata.</li>
</ul>
<p></p>
<p><strong>Minor Enhancements (6)</strong>
</p>
<div>
  <hr />
</div>
<ul>
  <li><strong>Ubuntu 14 support.&nbsp;</strong>CenturyLink Cloud now supports&nbsp;Ubuntu 14 as an OS template for servers. Customers can now create and deploy 64-bit Ubuntu 14 virtual instances to all data centers. Among other things, this latest version
    of Ubuntu has native support for Docker. Check out&nbsp;<a href="https://insights.ubuntu.com/2014/04/17/whats-new-in-ubuntu-server-14-04-lts/">what else is new in version 14</a>&nbsp;and read the <a href="https://wiki.ubuntu.com/TrustyTahr/ReleaseNotes"
   >Ubuntu 14 Release Notes</a> for more information.
    <br /><img src="https://t3n.zendesk.com/attachments/token/VEu6qTztoK4IPTjZUY2aBPfTN/?name=ubuntu-14.png" alt="ubuntu-14.png" />&nbsp;</li>
  <li><strong>Group Power Operations UI update.&nbsp;</strong>When applying power operations on servers in a group, users no longer have to contend with a modal dialog box. Right from the server details page, users now see a list of servers slide down right
    there for easy access to select which ones to power on, off, or reset.
    <br /><img src="https://t3n.zendesk.com/attachments/token/6b8f3Kt9hDAABJs4l7dChhuYP/?name=group-power-ops.gif" alt="group-power-ops.gif" />
    <br />
    <br />
  </li>
  <li><strong>Updated Account Hierarchy/Billing Page (for some accounts). </strong>For selected customers, this update displays consumption details for cloud services while billing details will continue to come directly from CenturyLink. This update also
    exposes access to the full suite of <a href="https://t3n.zendesk.com/categories/20074004-Managed-Services">managed services</a> available on CenturyLink Cloud.
    <br /><img src="https://t3n.zendesk.com/attachments/token/aYFFxeop7WfTGaEVZe7PpzD95/?name=usage-history.png" alt="usage-history.png" /><img src="https://t3n.zendesk.com/attachments/token/y5FsSU18ywzCmlovCQN77vwql/?name=usage-details.png" alt="usage-details.png"
    />
  </li>
</ul>
<ul>
  <li><strong>Docker and Panamax Blueprints.&nbsp;</strong>Following the <a href="https://t3n.zendesk.com/entries/47893914-Cloud-Platform-Release-Notes-July-28-2014">release of the CoreOS&nbsp;blueprints</a> last month, additional blueprints
    have been created for installing&nbsp;<a href="http://www.centurylinklabs.com/">CenturyLink Labs</a>' Docker management utility,&nbsp;<a href="http://www.panamax.io/">Panamax</a>, as well as one for installing Docker on Linux servers. Check out all
    the ways you can now&nbsp;<a href="http://www.ctl.io/blog/full/deploying-docker-containers-on-centurylink-cloud">Deploy Containers on CenturyLink Cloud</a>!</li>
  <li><strong>Better Back Office support. </strong>We've done some housekeeping on our side to improve logging and more efficiently manage certain common requests. With these tools, we can now better support our customers who may run into blueprint failures
    or are in&nbsp;need of&nbsp;<a href="http://www.ctl.io/products/support/service-tasks">Service Tasks</a>.&nbsp;</li>
  <li><strong>Data Center Updates.&nbsp;</strong>The CenturyLink Cloud successfully migrated all users from the Croyden (GB2) data center to our data center in Portsmouth (GB1). There is also data center expansion planned in Great Britain in the coming weeks.&nbsp;
    <br
    /><img src="https://t3n.zendesk.com/attachments/token/dY44pCFVakFBS4tueAboQeoFr/?name=dc-list-ca3-nogb2.png" alt="dc-list-ca3-nogb2.png" />
  </li>
</ul>