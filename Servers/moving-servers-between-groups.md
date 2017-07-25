{{{
  "title": "Moving Servers Between Groups",
  "date": "8-5-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>CenturyLink Cloud servers are logically organized into groups within each data center. When you create a server, you define which group to put that new server in. If for any reason, you need to put that server into a different group, the following steps
  will show you how to&nbsp;move a server into another group any time after it has been created.</p>
<h3>Steps</h3>
<ol>
  <li><p>From the Servers page, click on the server you wish to move.</p>
  <p><img src="https://t3n.zendesk.com/attachments/token/fldpjbB0p6uTmh1Zy6lgYSQ2R/?name=select-server-to-move.png" alt="select-server-to-move.png" /></p>
  </li>
  <li><p>On the Server Details page, click "settings" to view the Server Settings page.</p>
    <p><img src="https://t3n.zendesk.com/attachments/token/ryNRf6lFyFAj1TTPqeSoZwQAU/?name=server-settings-move.png" alt="server-settings-move.png" /></p>
  </li>
  <li><p>On the Server Settings page, click on the "member of" field to change the parent group.</p>
  <p><img src="https://t3n.zendesk.com/attachments/token/cdQ7rpYTdisGPHcHH3GbDYHdY/?name=server-settings-member-of.png" alt="server-settings-member-of.png" /></p>
  </li>
  <li><p>Now, from the list of groups, select which group you would like to move the server into and then click "save".</p>
    <p><img src="https://t3n.zendesk.com/attachments/token/pUOv7hYG71JobeRn24Zt2CRlR/?name=server-settings-select-group.png" alt="server-settings-select-group.png" /></p>
    <p><em>Note: You can only move servers to groups within the same data center that the server is in. Also, you cannot move servers into the Archive or Templates groups, as these are special groups used for archiving and templates. For more information, read about <a href="https://t3n.zendesk.com/entries/23112825-Understanding-VM-Deployment-Options-and-Power-States#archive">archiving</a>&nbsp;and <a href="https://t3n.zendesk.com/entries/22353625-How-To-Create-Customer-Specific-OS-Templates">custom templates</a>.</em></p>
  </li>
  <li><p>The page should refresh after a few seconds and show the server is now in the group you selected.</p>
    <p><img src="https://t3n.zendesk.com/attachments/token/1tanzf8XDCeqk7rLrNT5hhZzI/?name=server-moved.png" alt="server-moved.png" /></p>
  </li>
  <li>Finally, please note that although through the control UI you can only move one server at a time, you can use the API to move multiple servers programmatically, if desired. Also,&nbsp;you can rename a group from the group's Group Settings page.</li>
</ol>
