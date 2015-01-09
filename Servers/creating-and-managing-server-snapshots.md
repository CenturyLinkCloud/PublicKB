{{{
  "title": "Creating and Managing Server Snapshots",
  "date": "10-10-2014",
  "author": "James Morris",
  "attachments": []
}}}

<blockquote>
  <p><strong>WARNING: </strong>Using snapshots with a very high rate of change can cause significant performance degradation when the snapshot is removed. &nbsp;Your server may <strong>lose connectivity</strong> or become&nbsp;<strong>unavailable</strong>&nbsp;for
    several minutes or longer during the removal process.</p>
  <p><strong>CRITICAL NOTE: &nbsp;</strong>Snapshots are not supported on Standard Virtual Servers with &gt; 1 TB of &nbsp;Storage Allocated. &nbsp;Hyperscale Servers cannot leverage the Snapshot feature.</p>
</blockquote>
<p><strong>Description:</strong>
</p>
<p>Snapshots are a feature of our platform that allow a machine to be quickly reverted back to a set point in time.&nbsp; This can be very useful for things such as short term testing of updates or configuration changes however due to the way that snapshots
  operate they should not be kept active for&nbsp;extended periods of time .&nbsp; <strong>A snapshot is not a backup of a machine and should not be used as such! </strong>&nbsp;Snapshots do not contain a duplicate copy of the machines data rather they
  operate more like a change log that starts from the point in time the snapshot is initiated. Due to the nature of their operation snapshots are in a constant state of growth from the time they are created and the larger a snapshot becomes the longer
  delete or revert operations of the snapshot will take. If left active for an extended period of time snapshots also have the potential to completely fill the storage the machine is housed on causing many additional problems. &nbsp;&nbsp;In order to
  avoid these performance issues snapshots should not be kept active longer than 10 days.&nbsp; <strong>Any snapshot active longer than 10 days WILL be removed without notice as part of our maintenance process.</strong>
</p>
<p>&nbsp;</p>
<h3><strong>Create a snapshot of an existing server</strong></h3>
<ul>
  <li>Navigate to the <strong>Action,&nbsp;Snapshot&nbsp;</strong>button on the <em><strong>server</strong> </em>details page.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/ZJx3GGo5j1JeXm4D5n8MDOG19/?name=01.png" alt="01.png" />
</p>
<ul>
  <li>Choose the snapshot lifespan. &nbsp;Snapshots created by users must be deleted within 10 days.&nbsp;</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/6bOKYYtwxXG67w5HJyFO74b58/?name=04.png" alt="04.png" />
</p>
<ul>
  <li>After the "create snapshot" completes, the user can see their snapshot on the server details page. A server can only have a single snapshot at a time. The snapshot entry shows the date the snapshot was taken.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/rcbnc8XqY0MG20Jb1rbKMMw2t/?name=05.png" alt="05.png" />
  </li>
</ul>
<h3><strong>Create a snapshot of a group of servers</strong></h3>
<ul>
  <li>Navigate to the <strong>Action, Snapshot</strong> button on the <em><strong>group</strong> </em>details page.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/KDZEl7r90Mu3sqfsj60dquYnI/?name=02.png" alt="02.png" />
</p>
<ul>
  <li>Select the Servers in the group you wish to snapshot as well as the snapshot lifespan. &nbsp;Snapshots created by users must be deleted within 10 days.&nbsp;</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/AIjiHWMUKlR9hVFgzka2mQvHQ/?name=03.png" alt="03.png" />
</p>
<div></div>
<div></div>
<h3><strong>Restore a server snapshot</strong></h3>
<ul>
  <li>Users can use snapshots to restore a VM to its previous state by simply clicking on the snapshot name in the server details. After restoring a server to a snapshot, the snapshot itself is reset and retained.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/Si850ucLK2mH6O0mL7H5CefNa/?name=06.png" alt="06.png" />
  </li>
</ul>
<h3><strong>Delete the server snapshot</strong></h3>
<ul>
  <li>To delete a snapshot, the user can simply select the red X next to the snapshot name in the servers detail page.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/RtT0EwpLVGxQEPvgE0qARvArg/?name=05.png" alt="05.png" />
  </li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/c9qennb1fKOlVxunq9yi2BaAO/?name=07.png" alt="07.png" />
</p>
<p><strong>Summary:</strong>
</p>
<p>The basic points to remember about snapshots:</p>
<ul>
  <li>Not a viable form of backup (in fact not a form of backup at all)</li>
  <li>Useful for <strong>short term</strong> rollback of changes only</li>
  <li>Performance issues result from old snapshots</li>
  <li>Should not be kept longer than 10 days</li>
  <li>
    <p>The platform uses the following VMware Options flags in the Snapshot</p>
  </li>
</ul>
<p>Memory: true; a dump of the internal state of the virtual machine is included in the snapshot.&nbsp;</p>
<p>Quiesce: true; VMware Tools is used to quiesce the file system in the virtual machine. Quiescing a file system is a process of bringing the on-disk data of a physical or virtual computer into a state suitable for backups. This process might include such
  operations as flushing dirty buffers from the operating system's in-memory cache to disk, or other higher-level application-specific tasks</p>
<div>
  <p>A more technical overview of &nbsp;VMware snapshots can be found at :<a href="http://kb.vmware.com/kb/1015180">http://kb.vmware.com/kb/1015180</a>
  </p>
</div>