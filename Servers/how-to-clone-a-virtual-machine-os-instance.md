{{{
  "title": "How To: Clone a Virtual Machine OS Instance",
  "date": "7-28-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Overview</h3>
<p>A clone is a copy of an existing virtual machine. &nbsp;When the cloning operation is complete, the clone is a separate virtual machine. &nbsp;The resulting clone is an independent copy of a virtual machine and shares nothing with the source virtual machine
  after the cloning operation. Ongoing operation of a clone is entirely separate from the source virtual machine.</p>
<h3>Important Notices</h3>
<p>Customers using the clone function for Windows Servers should carefully review the <a href="http://technet.microsoft.com/en-us/library/hh824835.aspx" target="_blank">Microsoft Sysprep for Server Roles technet article</a>. &nbsp;Sysprep is a component
  of creating a clone and as such certain OS Roles are not supported in the clone process. </p>
<p>The source server is shutdown to ensure that there are no pending operations/information held in memory, and the server contents are copied to the destination virtual machine</p>
<h3>Steps</h3>
<ol>
  <li>Navigate to the Virtual Machine you wish to clone. From the "action" menu, select the "clone" option.</li>
</ol>
<p><img src="https://t3n.zendesk.com/attachments/token/mU4R9Fwije2bZcA2xymt02Tru/?name=clone-server-menu.png" alt="clone-server-menu.png" />
  <br />
  <br />
</p>
<p>2. &nbsp;The Clone Server form is used to input critical data points (server name, administrator password, network VLAN, storage type) for the resulting virtual machine clone. </p>
<p><img src="https://t3n.zendesk.com/attachments/token/qUc3FEo8lyKjAK9sIHmIDkWw5/?name=clone-server-create-screen.png" alt="clone-server-create-screen.png" />
</p>
<p>3. &nbsp;Customers can monitor the Queue for status of the Clone process or wait for email notification.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/9lRiBdqZZx6byx1A8Sk3TwNUI/?name=clone-queue.png" alt="clone-queue.png" />
</p>
<p><strong>Last updated: &nbsp;Mon 7/28/2014 17:57 PST</strong>
</p>