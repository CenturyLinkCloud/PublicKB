{{{
  "title": "Moving Servers Between Groups",
  "date": "8-5-2014",
  "author": "Bryan Friedman",
  "attachments": []
}}}

<h3>Description</h3>
<p>CenturyLink Cloud servers are logically organized into groups within each data center. When you create a server, you define which group to put that new server in. If for any reason, you need to put that server into a different group, the following steps
  will show you how to&nbsp;move a server into another group any time after it has been created.</p>
<h3>Steps</h3>
<ol>
  <li>From the Servers page, click on the server you wish to move.
    <br /><img src="https://t3n.zendesk.com/attachments/token/fldpjbB0p6uTmh1Zy6lgYSQ2R/?name=select-server-to-move.png" alt="select-server-to-move.png" />
    <br />
  </li>
  <li>On the Server Details page, click "settings" to view the Server Settings page.
    <br /><img src="https://t3n.zendesk.com/attachments/token/ryNRf6lFyFAj1TTPqeSoZwQAU/?name=server-settings-move.png" alt="server-settings-move.png" />
    <br />
  </li>
  <li>On the Server Settings page, click on the "member of" field to change the parent group.
    <br /><img src="https://t3n.zendesk.com/attachments/token/cdQ7rpYTdisGPHcHH3GbDYHdY/?name=server-settings-member-of.png" alt="server-settings-member-of.png" />
    <br />
  </li>
  <li>Now, from the list of groups, select which group you would like to move the server into and then click "save".
    <br /><img src="https://t3n.zendesk.com/attachments/token/pUOv7hYG71JobeRn24Zt2CRlR/?name=server-settings-select-group.png" alt="server-settings-select-group.png" />
    <br /><em>Note: You can only move servers to groups within the same data center that the server is in. Also, you cannot move servers into the Archive or Templates groups, as these are special groups used for archiving and templates. For more information, read about <a href="https://t3n.zendesk.com/entries/23112825-Understanding-VM-Deployment-Options-and-Power-States#archive" target="_blank">archiving</a>&nbsp;and <a href="https://t3n.zendesk.com/entries/22353625-How-To-Create-Customer-Specific-OS-Templates" target="_blank">custom templates</a>.</em>
  </li>
  <li>The page should refresh after a few seconds and show the server is now in the group you selected.
    <br /><img src="https://t3n.zendesk.com/attachments/token/1tanzf8XDCeqk7rLrNT5hhZzI/?name=server-moved.png" alt="server-moved.png" />
    <br />
  </li>
</ol>
<p>Finally, please note that although through the control UI you can only move one server at a time, you can use the API to move multiple servers programmatically, if desired. Also,&nbsp;you can rename a group from the group's Group Settings page.</p>