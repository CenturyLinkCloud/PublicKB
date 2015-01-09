{{{
  "title": "Group Level Patch Management",
  "date": "3-18-2013",
  "author": "Shantu Roy",
  "attachments": []
}}}

<p>Description:</p>
<p>The following article describes on how to use blueprint and automated tasks to manage patches on a server. &nbsp;The process will detail the steps to create a snapshot, deploy a script, and then delete the snapshot.</p>
<p>1. Locate the Server Group that you plan to run patches on.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/eauo1nqk49ubdkl/?name=Screenshot_3_18_13_4_42_PM.png" alt="Screenshot_3_18_13_4_42_PM.png" />
</p>
<p>2. Schedule a maintenance window. &nbsp;This will disable all the monitoring for the group at the start time and re-enable the monitoring on schedule3. </p>
<p><img src="https://t3n.zendesk.com/attachments/token/lzy1uee0ueop3dp/?name=Screenshot_3_18_13_11_52_AM-2.png" alt="Screenshot_3_18_13_11_52_AM-2.png" />
</p>
<p>3. Take a snapshot</p>
<p><img src="https://t3n.zendesk.com/attachments/token/qrzk7qxvu54q2cj/?name=Screenshot_3_18_13_11_58_AM.png" alt="Screenshot_3_18_13_11_58_AM.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/jrsoqggbz1ygte0/?name=Screenshot_3_18_13_12_00_PM-2.png" alt="Screenshot_3_18_13_12_00_PM-2.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/rexy9zg7yybxt4i/?name=Screenshot_3_18_13_4_17_PM.png" alt="Screenshot_3_18_13_4_17_PM.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/zuc7qhmwzlakpiu/?name=Screenshot_3_18_13_4_18_PM.png" alt="Screenshot_3_18_13_4_18_PM.png" />
</p>
<p>4. Execute update script&nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/ta1skwa1wcyehp4/?name=Screenshot_3_18_13_4_20_PM.png" alt="Screenshot_3_18_13_4_20_PM.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/2bkv5icsa5qp7lo/?name=Screenshot_3_18_13_4_22_PM.png" alt="Screenshot_3_18_13_4_22_PM.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/04gd3qdgpd2csu6/?name=Screenshot_3_18_13_4_23_PM.png" alt="Screenshot_3_18_13_4_23_PM.png" />
</p>
<p>5. Login and verify that the updates worked</p>
<p>Before Update:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/rtdydcb58nhigur/?name=Screenshot_3_18_13_4_25_PM.png" alt="Screenshot_3_18_13_4_25_PM.png" />
</p>
<p>After Update:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/o2c1rstuijyxoks/?name=Screenshot_3_18_13_4_33_PM.png" alt="Screenshot_3_18_13_4_33_PM.png" />
</p>
<p>6. Delete the snapshot</p>
<p><img src="https://t3n.zendesk.com/attachments/token/ifettfsulltjv9t/?name=Screenshot_3_18_13_4_35_PM.png" alt="Screenshot_3_18_13_4_35_PM.png" />
</p>