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
  <li>CenturyLink Cloud Users</li>
</ul>

<h3>Prerequisites</h3>
<ul>
  <li>Access to CenturyLink Control Portal: https://control.tier3.com</li>
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

<p><strong>Windows Server 2003</strong></p>

<p>If you are attempting to grow an Windows 2003 system partition (generally "C:\"), the partition will not be automatically re-sized to reflect the newly added space. You can verify this by examining the disk under "<strong>Disk Management</strong>"
  (diskmgmt.msc).</p>
<p>To grow the partition: Download<a href="https://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;ved=0CDMQFjAA&amp;url=http%3A%2F%2Fwww.dell.com%2Fsupport%2Fdrivers%2Fus%2Fen%2F19%2Fdriverdetails%3Fdriverid%3DR64398&amp;ei=dt0SUZ3cL8fZqQH9qIHQDw&amp;usg=AFQjCNEcFKhyIUlHmBdX2mjxyl3rA1mvPQ&amp;bvm=bv.41934586,d.aWM"
 >&nbsp;ExtPart.exe from Dell</a>&nbsp;(many other free partition management software packages can be used, if preferred). ExtPart runs on &nbsp; &nbsp; &nbsp;both 32 and 64bit machines.</p>
<ol>
  <li>Open up a command prompt and navigate to the extpart folder.</li>
  <li>Type "<strong>extpart.exe</strong>"</li>
  <li>Enter the volume to be extended (in most cases, C:)</li>
  <li>Enter the amount you would like to expand the disk by (this will generally be the amount you specified in Control), and hit enter. As a reminder, Diskpart is expecting the input in MB, for example, 4GB would be 4096 MB.&nbsp;</li>
</ol>
