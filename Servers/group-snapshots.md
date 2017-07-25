{{{
  "title": "Group Snapshots",
  "date": "5-22-2013",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>There are a myriad of uses for Virtual Machine snapshots, common use cases include&nbsp;pre/post-patching roll back and protection, or&nbsp;reverting&nbsp;machine changes&nbsp;to a preserved state in a demo environment. This article will illustrate two
  means of utilizing snapshots on a group of servers.</p>
<p>CenturyLink Cloud’s “Groups” are a powerful feature which enable the management of large groups of virtual machine, including executing scripts, controlling power state, and of course- taking and reverting snapshots.</p>
<p>To manually take a snapshot of a group, select the snapshot icon from the root of the desired group:</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/jvxwaaoc2nubpyc/?name=sn1.PNG" alt="sn1.PNG" />
</p>
<p>You will be shown a list of the servers, and can select the machines that you desire to be snapped:</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/dsu1inegz3gxsrb/?name=sn2.PNG" alt="sn2.PNG" />
</p>
<p>Simply selecting “OK” will begin the snapshot process.</p>
<p>There are cases wherein a customer will benefit from taking or reverting snapshots of a group on a regular basis, such as prior to scheduled patching. CenturyLink Cloud’s scheduling agent makes it easy to manage this task- simply select the “Schedules” tab of the
  desired group:</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/xyp6gbvtjfmabtm/?name=sn3.PNG" alt="sn3.PNG" />
</p>
<p>Click the “+ Schedule Task” button to begin adding a new task. Select the appropriate action and desired time (i.e. Create or Delete Snapshot). Click save, and a snapshot of your group will be taken at the desired time.</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/pjk0gvin9hbc0ka/?name=sn4.png" alt="sn4.png" />
</p>





