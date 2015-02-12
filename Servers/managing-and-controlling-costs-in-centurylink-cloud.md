{{{
  "title": "Managing and Controlling Costs in CenturyLink Cloud",
  "date": "10-9-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Overview</h3>
<p>CenturyLink Cloud provides several tools to enable customers to maximize the benefits of cloud computing, this article will outline some of the controls available to minimize cost. These tools are: pausing, archiving, scheduled tasks and autoscale.</p>
<h3>Audience</h3>
<ul>
  <li>CenturyLink Cloud Customers</li>
</ul>
<h3>Reference Material</h3>
<ul>
  <li><a href="https://t3n.zendesk.com/entries/23112825-Understanding-VM-Deployment-Options-and-Power-States" target="_blank">Understanding VM Deployment Options &amp; Power States</a>
  </li>
  <li><a href="https://t3n.zendesk.com/entries/22586501-Creating-a-Scheduled-Task" target="_blank">Creating a Scheduled Task</a>
  </li>
  <li><a href="https://t3n.zendesk.com/entries/22032834-Creating-and-Applying-Autoscale-Policies" target="_blank">Creating &amp; Applying Autoscale Policies</a>
  </li>
</ul>
<h3>Pausing</h3>
<p>Pausing is the act of suspending a virtual machine; virtual machines in a paused state are not billed for compute (RAM,CPU) usage- only storage consumption and licensing costs. Individual machines or entire groups can easily be paused through our Control
  Portal. To do so, simply select the appropriate group and use the "pause" button located on the black control bar.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/NOekI2cJUYt9Vcd0LTNM2r1rN/?name=01.png" alt="01.png" />
</p>
<p>Once you have selected the pause button, a selection box will appear which will allow you to choose one or all of the servers to be paused. Simple select the servers you wish to pause and select the "pause" button.</p>
<h3>Archiving</h3>
<p>Pausing servers is an effective way to temporarily reduce server costs; however, certain servers may no longer be needed in production but are needed either for reference or are planned for production usage at a later date. These servers can be "Archived"
  which suspends the virtual machine, and moves the server to a significantly cheaper storage tier. In the archive state, a customer pays only for the archival storage consumed by the machine, at a reduced rate- no compute or licensing costs are levied.
  Despite being archived, it is still an easily-executed and timely task to bring servers out of an archival state and back into production. To archive a server, simply select the "Archive" option from the actions menu. Note that selecting "Archive" on
  a group will archive the entire group of servers, though there will be a prompt to ensure this is the desired action before execution.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/CjioM32aH4TK4KF5Q9ehMylHc/?name=02.png" alt="02.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/NRSEyK887JktL5pC9VnTHgERf/?name=03.png" alt="03.png" />
</p>
<h3>Scheduled Tasks</h3>
<p>Both tasks, pausing and archiving, can be scheduled on an individual or group level. To do so, simply select the "Schedules" tab located on the Settings page on either a group or individual VM. You will then be able to setup the scheduled task (pause,
  power on, reboot, shutdown, archive, delete, create snapshot, delete snapshot), the desired time for the operation, and the expiration date. You can also set schedules to&nbsp;propagate&nbsp;through child groups in a hierarchical fashion to control,
  for example, and entire development stack. Scheduling pausing of servers is a great way to reduce resource utilization during off-hours for non-critical servers, simply pause your servers at night or over the weekend, and schedule them to power on at
  the start of the work week.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/VC0c72fd49Bq7D8aFrWlHnmpD/?name=04.png" alt="04.png" />
</p>
<h3>Autoscale</h3>
<p>The CenturyLink Cloud platform supports both vertical Autoscale of CPU capacity for servers as well as horizontal Autoscale of servers. This makes it possible to scale servers up and down (vertical) or out and in (horizontal) based on utilization, ensuring
  optimal deployment of resources for cloud environments under a variety of conditions. </p>
<p>For vertical Autoscale, servers that exceed a user-defined CPU utilization threshold will instantly scale up, and servers that go below a user-defined CPU utilization threshold will scale down (and reboot) during a user-defined window. In the case of
  horizontal Autoscale, groups of servers that exceed a user-defined CPU/RAM utilization threshold will scale out by powering on one or more additional servers in the group, and groups of servers that go below a user-defined CPU/RAM utilization threshold
  will scale in by powering off one or more servers in the group.</p>
<p>Autoscale makes it possible for a server or group of servers to self-regulate and deliver only the capacity it needs at any given time. This offers users two benefits: cost savings, and a reduction in administrative overhead.</p>
<p>Instead of requiring system administrators to closely monitor and scale servers based on changes in utilization, you can create policies that add and remove capacity automatically. This ensures that you don't have unnecessary CPUs allocated or additional
  servers powered on unless you need them.</p>