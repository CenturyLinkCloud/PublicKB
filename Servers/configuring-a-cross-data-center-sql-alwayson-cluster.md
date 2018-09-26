{{{
  "title": "Configuring a Cross Data Center SQL AlwaysOn Cluster",
  "date": "3-11-2014",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>SQL 2012 Enterprise Edition’s AlwaysOn Availability Groups brings high availability and disaster recovery to an entirely new level for the product- gone are the days of relying on log shipping and physical clustering! With CenturyLink Cloud’s Global Data Center
  footprint, it is easy to deploy a globally scaled and highly available database architecture in record time.</p>
<p>SQL AlwaysOn Database Availability Groups require an Active Directory environment, as well as SQL 2012 Enterprise Edition- both are can easily be automated through the CenturyLink Cloud “Create Server” wizard or use of our Blueprint Library. This article assumes
  an existing AD Forest, and as such we simply add the “Join Domain” and “Install SQL” tasks on the final page of the “Create Server” walk-through:</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/zvm1xjzopu5ba52/?name=SQLAlwaysOn1.JPG" alt="SQLAlwaysOn1.JPG" />
  </a>
</p>
<p>Create the desired amount of servers, in the appropriate groups and&nbsp;desired data centers- in this&nbsp;example, we are using&nbsp;four servers across&nbsp;CenturyLink Cloud’s two&nbsp;Canadian data centers- Toronto and Vancouver. Our servers will need to communicate
  with each other, while all CenturyLink Cloud data centers are equipped with 10G interconnects, we will still need to allow communication between networks and vlans.</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/idv8oqdnpiikpir/?name=SQLAlwaysOn2FW.JPG" alt="SQLAlwaysOn2FW.JPG" />
  </a>
</p>
<p>In the Control Portal, navigate to the “Firewall” section uunder the “Network” tab. Click “Add Policy” and choose the appropriate vlan by clicking “Set Local Address”</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/7hgqwoq0egfmlpl/?name=SQLAlwaysOn2FW2.JPG" alt="SQLAlwaysOn2FW2.JPG" />
  </a>
</p>
<p>In this example, we will enable communication across the entire subnet range (CIDR /24). Cross data center firewall policies allow communication across all ports, so if your security policies require restricting access to a certain group of hosts, choose
  your network segment carefully. Likewise, if you require only certain ports to be open, they must be secured on the host OS layer (though intra-data center policies allow for the specification of ports or a port range).</p>

<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/feqgcmpomihd1yh/?name=SQLAlwaysOn2FW3.JPG" alt="SQLAlwaysOn2FW3.JPG" />
  </a>
</p>
<p>We repeat the same&nbsp;process&nbsp;for the remote address segment, and save the firewall policy.</p>
<p>Once the servers have been created, we will need to install the <strong>Failover Clustering </strong>Role. This is done via the <strong>Add Roles</strong> function of <strong>Server Manager</strong>:</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/avdhocyhtusvtxk/?name=FailoverCluster1.JPG" alt="FailoverCluster1.JPG" />
  </a></p>
<p>This action can also be batch-applied across an entire group via the “Execute Script” groups command. Open up the <strong>Failover Cluster Manager</strong>, select “Validate Cluster” and add all of your SQL server hostnames:</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/anxigxpmphwiwtf/?name=FailoverValidation1.JPG" alt="FailoverValidation1.JPG" />
  </a>
</p>
<p>Click “Run All Tests”. It is expected for some tests to fail or pass with warnings. View the report and troubleshoot any issues that may prevent the cluster formation. After validation,&nbsp;proceed to create the cluster and&nbsp;virtual IP addresses.
  Once the cluster is created, you should see all nodes present and online:</p>

<p>&nbsp;
  <a><img src="https://t3n.zendesk.com/attachments/token/0xkuqiyrow8jyn9/?name=SQLAlwaysOnClusterNodes.JPG" alt="SQLAlwaysOnClusterNodes.JPG" />
  </a>
</p>

<p>We will then configure the quorum settings. Right click the cluster name, go to “More Actions” and select “Configure Cluster Quorum Settings”.</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/wwi6qxauy3opxga/?name=SQLAlwaysOnQuorum.jpg" alt="SQLAlwaysOnQuorum.jpg" />
  </a>
</p>
<p>Select “Node and File Share&nbsp;Majority” as we will be utilizing a file share rather than shared disk. Click “Next” and&nbsp;enter the path to the&nbsp;share&nbsp;to be used for the witness server.&nbsp;This share must reside on a different server than
  the cluster nodes- in this instance,&nbsp;a share on the Domain Controller was previously created.</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/6cxhtsalqv0zmnt/?name=SQLAlwaysOnQuorumWitness.jpg" alt="SQLAlwaysOnQuorumWitness.jpg" />
  </a>
</p>
<p>Click <strong>Next</strong> twice and then <strong>Finish</strong> to complete the cluster quorum configuration. Finally, we ready to build our SQL AlwaysOn Availability Group!</p>
<p>First, enable the AlwaysOn Group feature in SQL- this step will need to be done on all participating servers. Open <strong>SQL Configuration Manager&nbsp;</strong>(Start Menu-&gt;SQL 2012-&gt;Configuration Tools)&nbsp;and with SQL Server Services highlighted,
  double click on the <strong>SQLServer (MSSQLSERVER)</strong>
</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/euqotd8xwhh8bbw/?name=SqlService.JPG" alt="SqlService.JPG" />
  </a></p>
<p>Select the “AlwaysOn High Availability” tab and check the <strong>Enable</strong> box, and hit <strong>OK.</strong> The SQL Service will need to be restarted, which you can do by right clicking and selecting restart in the <strong>Configuration Manager.</strong>
</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/oaogckgsmtx81p7/?name=SQLEnable.JPG" alt="SQLEnable.JPG" />
  </a>
</p>
<p>Next, open <strong>SQL Server Management Studio. </strong>Connect to the local SQL Server instance. In <strong>Object Explorer</strong>, expand the <strong>AlwaysOn High Availability</strong> folder. Right-click on the <strong>Availability Groups</strong>  folder and select the <strong>New Availability Group Wizard…</strong> option. This will launch the <strong>New Availability Group Wizard.</strong>
</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/p9wgvxhjf3ooknv/?name=SQLNewAG.jpg" alt="SQLNewAG.jpg" />
  </a>
</p>
<p>Click through the introduction page and enter the desired name for the Availability Group in the <strong>Availability Group Name </strong>field. Click Next. You will then be presented with a list of local databases and their eligibility for Availability
  Group Membership. The database will need to be consistent, in Full Recovery Mode- so take a backup before starting this process, if the database is not already backed up nightly.</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/ksdzn5rgxufpqob/?name=SQLAPrereq.JPG" alt="SQLAPrereq.JPG" />
  </a>
</p>
<p>In the <strong>Specify Replicas</strong> page, under the Replicas tab, click the <strong>Add Replicas</strong> button and connect to the other SQL Server instances that you joined as nodes in your Windows Server Failover Cluster. It is suggested to leave
  Automatic Failover, Synchronous Commit checked. You can choose whether or not you need a <strong>Readable Secondary</strong> database- A readable secondary replica allows read-only access to all its secondary databases. However, readable secondary databases
  are not set to read-only. They are dynamic. If you get a network or named pipes error- make sure that named pipes/IP connections are enabled in SQL and that Windows Firewall is configured to allow traffic through, or turned off entirely. Named Pipes/IP
  are configured under <strong>SQL Configuration Manager</strong> in the appropriate instance name (default MSSQLSERVER)</p>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/0uqazicr8g8dxfd/?name=SQLNamedPipes.JPG" alt="SQLNamedPipes.JPG" />
  </a>
</p>

<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/abwcduheeerv6rz/?name=SQLReplicas.JPG" alt="SQLReplicas.JPG" />
  </a>
</p>
<p>It is recommended that all local servers are synchronous commits, and all offsite replicas are asynchronous commits- automatic failover is recommended locally but may not be appropriate given the applications relying on the SQL Cluster. The fourth node
  is a readable secondary, and will be used for lagged backups and read-only operations, it cannot accept writes or be used in production.</p>
<p>Select <strong>Full</strong> for the initial data synchronization and specify a share accessible to all cluster nodes. After you pass the validation, click <strong>Finish.</strong>
</p>
<p>You have just created a SQL AlwaysOn Cluster!</p>
