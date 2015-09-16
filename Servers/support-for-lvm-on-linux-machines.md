{{{
  "title": "Support for LVM on Linux machines",
  "date": "8-25-2014",
  "author": "James Morris",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>All of CenturyLink's Linux templates use a partitionless configuration for the root drive and, by default, all additional drives added through the Control Portal.&nbsp;Though it does not apply for physical servers, this partitionless concept has some
  advantages over traditional partitioning and LVM in a virtualized environment like the one CenturyLink Cloud offers.&nbsp;This configuration allows for the best possible performance in addition to the ability for Control to perform seamless expansion
  of these drives (and any mounted volume) without requiring the server to reboot.</p>
<p>Customers who are looking to use LVM (or any other tool) to partition additional drives will not be able to do so from Control. While&nbsp;it is still recommended to use this standard method of&nbsp;<a href="https://t3n.zendesk.com/entries/23317598-Adding-Disks-to-Linux-Virtual-Machines"
 >adding disks using Control</a>, customers may choose to manually configure <em>additional</em> partitions using LVM while directly logged in on the server. However,&nbsp;the primary (root) partition as deployed from the standard Linux
  templates will&nbsp;always have this partitionless configuration and should be kept this way and left alone&nbsp;to ensure the best server performance and greatest compatibility with the Control Portal.</p>
<p>Users who require a custom image with LVM being used on the primary drive will need to <a href="http://www.ctl.io/products/support/service-tasks#quick-start">enter a request to the professional services team to perform a custom template import</a>&nbsp;(for
  a fee).&nbsp;Using this method means that not all&nbsp;Control site features will be supported, specifically the automatic expansion of the file system when expanding disks.</p>
<p>As a final note, it is considered best practice to avoid using LVM and stick with the partitionless configuration provided by CenturyLink Cloud. It is also heavily discouraged to undo the partitionless setup in favor of traditional partitioning as it
  may render the server unusable if done incorrectly. Despite what many Linux users may be used to in other configurations, the partitionless setup will provide the best performance and compatibility in the CenturyLink Cloud.</p>
<p><strong>Last updated: &nbsp;Thu 8/25/2014 13:32 PST</strong>
</p>