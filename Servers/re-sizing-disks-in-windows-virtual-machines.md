{{{
  "title": "Re-sizing Disks in Windows Virtual Machines",
  "date": "12-24-2014",
  "author": "Aaron Lemoine",
  "attachments": [],
  "contentIsHTML": false
}}}

<h3>Description (goal/purpose)</h3>
<p>When a disk is provisioned to your server in control, occasionally you will get this warning "Manual intervention required". This indicates that manual intervention is required to complete the process of expanding your disk.</p>

<p><strong>Audience</strong>
</p>
<ul>
  <li>Lumen Cloud Users</li>
</ul>

<h3>Prerequisites</h3>
<ul>
  <li>Access to Lumen Control Portal: https://control.ctl.io</li>
  <li>Access to the server that being re-sized</li>
  <li>No server snapshots in place.</li>
</ul>
<h3>Detailed Steps</h3>
<p><strong>Windows Server 2008 / 2012</strong></p>

1. Log into the server
2. Launch server manager, and expand Storage
3. Right click Disk Management, and click Rescan Disks.
4. In the details pane, right-click the volume that you want, and then click&nbsp;<strong>Extend Volume</strong>.
5. Follow the instructions in the Extend Volume Wizard to extend the partition.


</ol>
