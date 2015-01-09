{{{
  "title": "Understanding VM Deployment Options and Power States",
  "date": "1-5-2015",
  "author": "Chris Little",
  "attachments": []
}}}

Understanding VM Deployment Options and Power States
<h3>Templates</h3>
<ul>
  <li>Definition: &nbsp;A Virtual Machine template provides a standardized group of hardware and software settings that can be used repeatedly to create new virtual machines configured with those settings.</li>
  <li>How To: <a href="https://t3n.zendesk.com/entries/22353625-How-To-Create-Customer-Specific-OS-Templates" target="_blank">https://t3n.zendesk.com/entries/22353625-How-To-Create-Customer-Specific-OS-Templates</a>
  </li>
  <li>Costs: Customer specific template storage is billed on a per GB basis as Standard Storage. &nbsp;Out of the box Virtual Machine templates in the Tier 3 platform do not incur a storage fee. &nbsp;</li>
  <li>Sample Use Case: &nbsp;ISV would like to build a virtual machine base template that includes the OS, software packages and security customization to improve speed of delivery to their client base. &nbsp;</li>
</ul>
<h3>Clones</h3>
<ul>
  <li>
    <p>Definition: &nbsp;Cloning creates an independent, duplicate copy of an existing virtual machine which is nearly identical to the “source” virtual machine. The cloned machine retains the same hardware, operating system, application and configuration
      items as the original virtual machine; however, certain items, such as the server’s security identifier, are changed during the process. For some further information around cloning, please see <a href="https://t3n.zendesk.com/entries/22622950-Cloning-Best-Practices"
      target="_blank">https://t3n.zendesk.com/entries/22622950-Cloning-Best-Practices</a>
    </p>
  </li>
  <li>
    <p>How To: <a href="https://t3n.zendesk.com/entries/22775929-How-To-Clone-a-Virtual-Machine-OS-Instance" target="_blank">https://t3n.zendesk.com/entries/22775929-How-To-Clone-a-Virtual-Machine-OS-Instance</a>
    </p>
  </li>
  <li>
    <p>Costs: &nbsp;As a &nbsp;virtual machine clone is a completely separate copy of a VM, it is billed per hour based on the resources assigned. &nbsp;</p>
  </li>
  <li>Sample Use Case: &nbsp;IT department needs to reproduce and find a resolution to a software bug that is affecting their customers. &nbsp;In order to avoid changes and downtime to the production environment , a clone of the problem virtual machine is
    created allowing for further troubleshooting without customer impact. &nbsp;</li>
</ul>
<h3>Snapshots</h3>
<ul>
  <li>
    <p>Definition: A snapshot preserves the state and data of a virtual machine at a specific point in time. &nbsp;The state includes the virtual machine’s power state (for example, powered-on, powered-off, suspended). &nbsp;The data includes all of the
      files that make up the virtual machine. This includes disks, memory, and other devices, such as virtual network interface cards.</p>
  </li>
  <li>
    <p>How To: <a href="https://t3n.zendesk.com/entries/21381762-Creating-and-Managing-Server-Snapshots" target="_blank">https://t3n.zendesk.com/entries/21381762-Creating-and-Managing-Server-Snapshots</a>
    </p>
  </li>
  <li>
    <p>Costs: &nbsp;Snapshots are included as part of the Tier 3 platform. &nbsp;Snapshots can be automatically created or deleted using the built in scheduler.</p>
  </li>
  <li>Sample Use Case: &nbsp;IT Department is preparing for the monthly patch release cycle for their Windows servers. &nbsp;For rapid fallback group level snapshots are created against the production environment prior to application of patches. &nbsp;</li>
</ul>
<h3>Pause&nbsp;</h3>
<ul>
  <li>
    <p>Definition: Pausing a virtual machine suspends the operating system. &nbsp;A virtual machines pause or power state can be changed in a rapid fashion.</p>
  </li>
  <li>
    <p>How To: &nbsp;The Pause function is available at both the group or individual virtual machine details pane. &nbsp;Customers can leverage the built in scheduler to perform automated changes to power states against individual or groups of virtual machines.
      &nbsp;</p>
  </li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/LaIWCmiv5gXqZKsLTKbtAJD3U/?name=01.png" alt="01.png" />
</p>
<ul>
  <li>
    <p>Costs: In the pause state, a customer pays for storage consumed by the virtual machine and licensing costs. Compute and memory costs are not levied. &nbsp;For further details see&nbsp;<a href="https://t3n.zendesk.com/entries/23227276-Managing-and-Controlling-Costs-in-the-Tier-3-Cloud"
      target="_blank">Managing and Controlling Costs in the Tier 3 Cloud</a>.</p>
  </li>
  <li>Sample Use Case: &nbsp;A customer maintains a development and staging environment for their production workloads. &nbsp;This environment is only used during business hours 8 AM to 8 PM EST. &nbsp;The IT department, in order to save costs, creates a
    scheduled pause and power on event during off hours. &nbsp;This automated task eliminates CPU &amp; RAM fee's between the 8 PM and 8 AM EST time window for these environments.</li>
  <li><strong>NOTE: &nbsp;Customers who use the Power Off or Stop OS function receive the same cost benefits detailed above</strong>
  </li>
</ul>
<p>
  <a name="archive"></a>
</p>
<h3>Archive</h3>
<ul>
  <li>
    <p>Definition: Archiving a virtual machine suspends the operating system and migrates the instance to a significantly cheaper storage tier. Bringing a virtual server out of an archive state can take a few hours.</p>
  </li>
  <li>
    <p>How to: &nbsp;The Archive function is available in the individual virtual machine details pane. &nbsp; Customers can leverage the built in scheduler to automate migrate of virtual machine in or out of archive.</p>
  </li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/CEst2oMljyDImt4Pa4JtIQQTD/?name=02.png" alt="02.png" />
</p>
<ul>
  <li>
    <p>Costs: In the archive state, a customer pays only for the archival storage consumed by the virtual machine (at a reduced rate). Compute, memory and licensing costs are not levied. &nbsp;For further details see&nbsp;<a href="https://t3n.zendesk.com/entries/57443680-Managing-and-Controlling-Costs-in-CenturyLink-Cloud"
      target="_blank">Managing and Controlling Costs in the Tier 3 Cloud</a>.</p>
  </li>
  <li>Sample Use Case: &nbsp;The business department has a reporting server that pulls data on a monthly basis from a 3rd party and generates reports for business analysis. &nbsp;This virtual machine is only required for 2 days per month and otherwise is
    unused. &nbsp;To save costs, the IT department schedules the server to be placed in archive and brought out of archived for operation during just these 2 days of the month. &nbsp;</li>
  <li>Note: Archived servers are not backed up daily. Rather, a single copy of it is stored. To restore a VM in which you have archived, simply unarchive it.&nbsp;</li>
</ul>
<p><strong>Last updated: &nbsp;TUES 11/12/2013 10:27 EST</strong>
</p>