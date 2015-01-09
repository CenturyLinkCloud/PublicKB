{{{
  "title": "Deploy Microsoft SQL Server using Blueprint",
  "date": "12-5-2014",
  "author": "Chris Little",
  "attachments": []
}}}

Deploy Microsoft SQL Server using CenturyLink Cloud Blueprint
<p>CenturyLink Cloud customers can procure and deploy Microsoft SQL Server licensing within the Control Portal. &nbsp;Microsoft SQL Server is licensed via the Microsoft SPLA program. &nbsp;By using the CenturyLink Cloud public blueprint customers have multiple
  ways to consume and install this business critical database software.</p>
<h3>Prerequisites</h3>
<ul>
  <li>A CenturyLink Cloud Account</li>
  <li>Supported Guest Operating Systems are deployed and in a running state. &nbsp;</li>
  <ul>
    <li>Windows 2008 R2 Standard 64-bit</li>
    <li>Windows 2008 R2 Enterprise 64-bit</li>
    <li>Windows 2008 R2 Datacenter 64-bit</li>
    <li>Windows 2012 Datacenter 64-bit</li>
    <li>Windows 2012 R2 Data Center 64-bit&nbsp;</li>
  </ul>
  <li>~15 GB Free Storage on C:\&nbsp;</li>
  <li>The Supported SQL Server Editions via blueprint are as follows</li>
  <ul>
    <li>SQL Server 2008 R2 Web Edition</li>
    <li>SQL Server 2008 R2 Standard Edition</li>
    <li>SQL Server 2008 R2 Enterprise Edition</li>
    <li>SQL Server 2012 Web Edition</li>
    <li>SQL Server 2012 Standard Edition</li>
    <li>SQL Server 2012 Enterprise Edition</li>
  </ul>
</ul>
<h3>Exceptions</h3>
<p><em>This KB does not apply to <a href="http://www.centurylinkcloud.com/managed-services/ms-sql" target="_blank">Managed Microsoft SQL</a> Customers</em>
</p>
<h3>General Notes</h3>
<p>The following are quick tips/notes based on past experiences with customers leveraging this blueprint</p>
<ul>
  <li>It is not possible at the current time to install SQL to a drive other than C:\ via blueprint. &nbsp;Customers can modify the SQL database, tempdb, log locations post install to other volumes using SQL tools</li>
  <li>The fee's for Microsoft SQL server will be applied automatically to the customers invoice when using the public blueprint. &nbsp;These fee's are documented in a customers agreement. &nbsp;If you are unsure what these fee's are please contact your account
    manager.</li>
  <li>Licensing fee's are adjusted based on number of vCPU allocated to a virtual machine. &nbsp;By using tools like Autoscale, customers billing will be modified as vCPU configurations change. &nbsp;</li>
</ul>
<h3>Installing Microsoft SQL Server using Group Tasks</h3>
<p>&nbsp;1. &nbsp;Navigate to the Servers Menu in Control</p>
<p><img src="https://t3n.zendesk.com/attachments/token/pjhHtoYDchNKcfLrBS5ybxJc5/?name=01.png" alt="01.png" />
</p>
<p>2. &nbsp;Browse to the Group that houses the VM(s) you want to deploy SQL. &nbsp;Select Action, Execute Package.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/14BBzI5AuRZ7UVBqOpbxktLAT/?name=02.png" alt="02.png" />
</p>
<p>3. &nbsp;Search for '<strong>SQL</strong>' and select the <strong>Install SQL Server on Windows</strong> blueprint.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/YaBFo9h4cW4ICQaAkNV2hRnOi/?name=03.png" alt="03.png" />
</p>
<p>4. &nbsp;Input the appropriate parameters based on the SQL server requirements for your application.&nbsp;Select the VM(s) in the Group you want to deploy SQL. Customers can choose an individual VM or multiple. &nbsp;(Quick Tip: Only supported Guest Operating
  Systems will be shown)&nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/M113cuQ4hcwotHyyXMsv25dYQ/?name=04.png" alt="04.png" />
</p>
<h3>Installing Microsoft SQL Server using Blueprints Library</h3>
<p>1. &nbsp;Navigate to the Blueprint Library in Control.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/cpf5xBLeMTVrbKlsjeNzkniVf/?name=02.png" alt="02.png" />
</p>
<p>2. &nbsp;Search for '<strong>SQL</strong>' and select '<strong>Install SQL Server on Existing Server</strong>.'</p>
<p><img src="https://t3n.zendesk.com/attachments/token/beQGk9fLn72Lt5AhSWjhT4rwL/?name=02.png" alt="02.png" /><img src="https://t3n.zendesk.com/attachments/token/J5bzq5tspgYWOZ1U26pr68QOn/?name=03.png" alt="03.png" />
</p>
<p>3. &nbsp;Select Deploy blueprint.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/KOVvpyFsjYQRozwUYGqSWD5qj/?name=04.png" alt="04.png" />
</p>
<p>4. &nbsp;Input the appropriate parameters based on the SQL server requirements for your application and select the Virtual Machine you wish to execute the install against.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/hIyEiUPJRx0uJoYboE16mCc4O/?name=05.png" alt="05.png" />
</p>
<p>5. &nbsp;Confirm the virtual machine(s), features and select Deploy Blueprint</p>
<p><img src="https://t3n.zendesk.com/attachments/token/skfISBior0Hg7nwnsYrqMEjOj/?name=06.png" alt="06.png" />
</p>
<p>&nbsp;</p>