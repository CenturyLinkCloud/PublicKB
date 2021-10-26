{{{
  "title": "Moving Servers Between Groups",
  "date": "10-26-2021",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>Lumen Cloud servers are logically organized into groups within each data center. When you create a server, you define which group to put that new server in. If for any reason, you need to put that server into a different group, the following steps
  will show you how to&nbsp;move a server into another group any time after it has been created.</p>
<h3>Steps</h3>
<ol>
  <li><p>From the Servers page, click on the server you wish to move.</p>
  
  </li>
  <li><p>On the Server Details page, click "settings" to view the Server Settings page.</p>
  </li>
  <li><p>On the Server Settings page, click on the "member of" field to change the parent group.</p>
  </li>
  <li><p>Now, from the list of groups, select which group you would like to move the server into and then click "save."</p>
    <p><em><b>Note</b>: You can only move servers to groups within the same data center that the server is in. Also, you cannot move servers into the Archive or Templates groups, as these are special groups used for archiving and templates.</em>
  </li>
  <li><p>The page should refresh after a few seconds to show that the server is now in the group you selected.</p>
  </li>
  <li>Finally, please note that although through the control UI you can only move one server at a time, you can use the API to move multiple servers programmatically, if desired. Also,&nbsp;you can rename a group from the group's Group Settings page.</li>
</ol>
