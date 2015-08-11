{{{
  "title": "Getting Started with Managed MySQL Replication",
  "date": "01-23-2015",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>We offer two options of MySQL Replication: Master/Master and Master/Slave.</p>
<p>This will allow for a much higher level of fault tolerance and redundancy for your MySQL databases.&nbsp; Replication enables data from one MySQL database server (the Master) to be replicated to another MySQL database servers (the Slave).&nbsp; In the case of Master/Master both nodes will replicate their databases to each other so each acts as a Master for themselves and a Slave for the other Node and the reverse.</p>
<h3>Prerequisites (for both Master/Master and Master/Slave)</h3>
<p>1. Build two Managed RedHat Linux 6 servers, or two Managed RedHat Linux 7 servers</p>
<p>2. Run CLC Managed Oracle MySQL Enterprise Blueprint on both hosts (<a style="background-color: initial;" href="https://t3n.zendesk.com/entries/45109574-Getting-Started-with-Managed-MySQL">https://t3n.zendesk.com/entries/45109574-Getting-Started-with-Managed-MySQL</a>)</p>
<h3>Running the MySQL Master/Master Blueprint</h3>
<p>1. Search for the <strong style="background-color: initial;">CLC Managed MySQL Master Master Replication</strong> Blueprint in the Blueprint library.&nbsp; Then, click the Blueprint and then click the deploy blueprint button</p>
<p><img src="https://t3n.zendesk.com/attachments/token/in7xbmGdaHMfvdoUTHtT9QBWp/?name=My_SQL_1.png" alt="My_SQL_1.png" /></p>
<p>2. Fill out the appropriate details for the Blueprint</p>
<ul>
<li>Password for MASTER server MySQL account (1<sup style="background-color: initial;">st</sup>&nbsp;Master, in the example below 101). <B>NOTE: This should be the password used when MySQL was configured and can be found at /root/.mysqlclc</b></li>
<li>Slave Server Host Name - This is the 1st Slave Server (In the example below 102 is the slave) or the name of the 2<sup style="background-color: initial;">nd</sup>&nbsp;Master</li>
<li>Password for SLAVE server MySQL account (in the example below 102) <b>NOTE: This should be the password used when MySQL was configured and can be found at /root/.mysqlclc</b></li>
<li>Install Managed MySQL Master Master Replication - Execute on Server - Choose the 1st Master (in the example below 101)</li>
<li>Install Managed MySQL Master Master Replication - Execute on Server - Choose the 1st Master (in the example below 101)</li>
<li>Register Managed MySQL Replication - Execute on Server - Choose the 1st Master (in the example below 101)</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/oF5VNChLkBV3k33rcsXf55KbU/?name=My_SQL_2.png" alt="My_SQL_2.png" width="709" height="763" /></p>
<p>&nbsp;</p>
<p>3. Verify your entries and Deploy the Blueprint<br />4. You will receive an email that your Blueprint has been installed when the Blueprint is complete</p>
<h3>Running the MySQL Master/Slave Blueprint</h3>
<p>1. Search for the <strong style="background-color: initial;">CLC Managed MySQL Master Slave Replication</strong> Blueprint in the Blueprint library.&nbsp; Then, click the Blueprint and then click the deploy blueprint button</p>
<p><img src="https://t3n.zendesk.com/attachments/token/Lk7xVPdlIx1pqML0bpxK1cTBl/?name=My_SQL_4.png" alt="My_SQL_4.png" /></p>
<p><br />2. Fill out the appropriate details for the Blueprint</p>
<ul>
<li>Password for MASTER host MySQL account (in the example below 103)</li>
<li>Slave Server Host Name - This is the Slave Server</li>
<li>Password for SLAVE host MySQL account (in the example below 104)</li>
<li>Install Managed MySQL Master Slave Replication - Execute on Server - Choose the Master (in the example below 103)</li>
<li>Register Managed MySQL Replication - Execute on Server - Choose the Master (in the example below 103)</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/8BM2HmVVSItrqafKjSCiOdBGF/?name=My_SQL_5.png" alt="My_SQL_5.png" width="707" height="744" /></p>
<ul>
<li>Verify your entries and Deploy the Blueprint</li>
<li>You will receive an email that your Blueprint has been installed when the Blueprint is complete</li>
</ul>
<h3>FREQUENTLY ASKED QUESTIONS</h3>
<p><strong>Q: How is the CenturyLink Cloud for Managed Oracle MySQL Replication priced?</strong></p>
<p>A: CenturyLink Cloud Managed Oracle MySQL Replication is priced per install, billed hourly depending on the version of Replication you are using.&nbsp; The hourly rate encompasses all servers in the replicated environment, but is in addition to the hourly rate charged for MySQL licensing and management.</p>
<p><strong>Q: What Versions of Oracle MySQL Replication are supported?</strong></p>
<p>A: CenturyLink Cloud Supports&nbsp;MySQL v5.5, MySQL 5.6.</p>
<p><strong>Q: What operating systems are supported for Managed Oracle MySQL Replication?</strong></p>
<p>A: Managed Red Hat 6 and Managed Red Hat 7.
</p>
<p><strong>Q: Can *un-managed* MySQL Replication Services be converted to *Managed* (or vice versa)?</strong>
</p>
<p>A: This capability is not available at this time.</p>
