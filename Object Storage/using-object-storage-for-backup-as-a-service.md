{{{
  "title": "Using Object Storage for Backup as a Service",
  "date": "1-7-2015",
  "author": "Chris Little",
  "attachments": []
}}}

Using Object Storage for Backup as a Service
<p>CenturyLink Cloud customers may wish to leverage our S3 compatible Object Storage for backup and recovery of file systems or applications. &nbsp;As Object Storage is consumable by any customer in a public fashion, applications or servers can be located
  within the CenturyLink Cloud or on premise. &nbsp;There are various industry backup tools that support object storage as a repository for data. &nbsp;In this knowledge base we will focus on <a href="http://www.cloudberrylab.com/" target="_blank">Cloudberry Lab</a>.
  &nbsp;The <a href="http://www.cloudberrylab.com/amazon-s3-enterprise-backup.aspx" target="_blank">Cloudberry Lab Backup Enterprise Edition</a> software provides for backup of Microsoft Windows Server File Systems, Microsoft SQL and Microsoft Exchange
  data.</p>
<h3>Supporting Information</h3>
<p>Information and details around the CenturyLink Cloud Object Storage can be found in our <a href="https://t3n.zendesk.com/forums/20789095-Object-Storage" target="_blank"><strong>Knowledge base</strong></a>. &nbsp;It is also important to note that CenturyLink
  Cloud provides no support for any 3rd party backup software tools. &nbsp;We are simply providing cloud based storage onto which backup software can store data. &nbsp;</p>
<h3>Prerequisites</h3>
<ul>
  <li>A CenturyLink Cloud Account</li>
  <li>Cloudberry Backup software is installed</li>
  <li>An object storage user and bucket for backups is created in the CenturyLink Cloud Control Portal. &nbsp;<a href="https://t3n.zendesk.com/entries/21648384-Using-Object-Storage-from-the-Control-Portal" target="_blank">See this KB</a>
  </li>
  <li>The source VM or Server has internet access</li>
</ul>
<h3>Configuring File System Backup</h3>
<p>&nbsp;1. &nbsp;Open Cloudberry Backup Enterprise Edition, select file, <strong>S3 Compatible</strong>
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/cvqc4wrmr9fq7wx/?name=02.png" alt="02.png" />
</p>
<p>2. &nbsp;Populate the S3 Compatible Account information with your CenturyLink Cloud Object Storage Access Key, Secret Key, Service Point and bucket name. <strong>&nbsp;<a href="https://t3n.zendesk.com/entries/21648384-Using-Object-Storage-from-the-Control-Portal" target="_blank">Details can be found in this KB</a></strong>.
  &nbsp;Currently, Object storage is only delivered out of Canada. &nbsp;<strong>The Service Point for Canada is ca.tier3.io</strong>
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/l14ygwoyqczxsrz/?name=03.png" alt="03.png" />
</p>
<p>3. &nbsp;Optionally, you may input cost estimate parameters as part of the storage account setup. &nbsp;By using this component the Cloudberry Lab backup software is able to estimate your costs for storage. &nbsp;<em><strong>This is merely an estimate on storage (excluding bandwidth charges) and does not necessarily reflect actual CenturyLink Cloud Object Storage fees</strong></em>.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/zmjojgg5gsxcrri/?name=04.png" alt="04.png" />
</p>
<p>4. &nbsp;Your S3 Compatible Storage Account should now be created successfully.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/mrknospqnhscwrm/?name=05.png" alt="05.png" />
</p>
<p>5. &nbsp;At the Welcome screen select <strong>Setup Backup Plan</strong>.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/x9d66p7pakhslnd/?name=07.png" alt="07.png" />
</p>
<p>6. &nbsp;Select the S3 Compatible Cloud Storage account you created in steps 1-3 as the destination for backups. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/uufla2ysxuvntqv/?name=08.png" alt="08.png" />
</p>
<p>7. &nbsp;Specify a name for the backup plan. &nbsp;We recommend a name that encompasses the server name, backup type (file, SQL etc) as a minimum. &nbsp;Additionally, it is advised that backup plan configurations are saved to the backup storage (Default).</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/nmkkb8q0vhdhaho/?name=09.png" alt="09.png" />
</p>
<p>8. &nbsp;Choose an appropriate backup model based on the features you require. &nbsp;Typical enterprise customers will want to leverage the Advanced Mode approach as it provides for Data Encryption and complex retention policies. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/pjmigw5sjzlkt1d/?name=10.png" alt="10.png" />
</p>
<p>&nbsp;9. &nbsp;Select the backup source. &nbsp;Entire Windows volumes, specific directories or UNC Shares can be added to the backup plan.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/zjjghut7wzss9q3/?name=11.png" alt="11.png" />
</p>
<p>10. &nbsp; The Advanced Filter allows administrators to include/exclude specific file types, folders and large files. &nbsp;Select the appropriate settings based on IT Department or business policies. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/jetubdi9eksjr5e/?name=12.png" alt="12.png" />
</p>
<p>11. &nbsp;In order to secure backup data and reduce cost customers can enable encryption and compression. &nbsp;It is recommended that AES 128bit or higher is implement with long, complex encryption keys. &nbsp;Additionally, file name encryption adds
  another layer of security. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/76okwjnkgyp1wgm/?name=13.png" alt="13.png" />
</p>
<p>12. &nbsp;Specify the appropriate purge options for backup files. &nbsp;Defaults can be viewed by selecting the 'options' hyperlink. &nbsp;Clients may wish to keep file system backups based on # of versions or based on data set age. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/jz76gmpbwfeiffx/?name=14.png" alt="14.png" />
</p>
<p>13. &nbsp;Choose a backup schedule that meets IT or business requirements. &nbsp;Generally, its best practice to perform a backup at least once per day during off hours. &nbsp;The Cloudberry Backup software supports recurring scheduled backups and even
  real-time backup of data. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/u5svghneoojc74l/?name=16.png" alt="16.png" />
</p>
<p>14. &nbsp;In this example we selected recurring, and set the schedule for Daily at 8 PM. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/d11ye5l3h3gcrhe/?name=17.png" alt="17.png" />
</p>
<p>15. &nbsp;Support is provided for Pre / Post commands if required.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/qhyou8jexzqffmc/?name=18.png" alt="18.png" />
</p>
<p>16. &nbsp;Notification Options provide backup administrators with alerts for success or failure for each backup plan. &nbsp;Clients can leverage the the Cloudberry backup messaging service or specify an SMTP server. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/f7cw5gorcex9vo7/?name=20.png" alt="20.png" />
</p>
<p>17. &nbsp;A summary of the backup plan is provided once configurations are complete. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/3rsdqdqsi53oxtu/?name=21.png" alt="21.png" />
</p>
<p>18. &nbsp;You have now configured a file system backup plan. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/2dn9rc2n34nfmpo/?name=22.png" alt="22.png" />
</p>
<h3>Configuring Microsoft SQL Database Backup</h3>
<p>1. &nbsp;Open Cloudberry Backup Enterprise Edition, select <strong>Backup MS SQL Server.</strong>
</p>
<p><strong><img src="https://t3n.zendesk.com/attachments/token/0cfxjsantz6iomv/?name=23.png" alt="23.png" /></strong>
</p>
<p>2. &nbsp;Select the S3 Compatible Cloud Storage account you created earlier in this KB as the destination for backups.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/lfqh80uj6mt9azs/?name=25.png" alt="25.png" />
</p>
<p>3. &nbsp;Specify a name for the backup plan. &nbsp;We recommend a name that encompasses the server name, backup type (file, SQL etc) as a minimum. &nbsp;Additionally, it is advised that backup plan configurations are saved to the backup storage (Default).</p>
<p><img src="https://t3n.zendesk.com/attachments/token/8tevcdakqzwrvsz/?name=26.png" alt="26.png" />
</p>
<p>4. &nbsp;Select the Microsoft SQL Instance you wish to backup and the appropriate authentication for your environment. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/txqjzjmmmalt0xd/?name=27.png" alt="27.png" />
</p>
<p>5. &nbsp;Select the database in the Microsoft SQL Instance you wish to backup. &nbsp;Cloudberry Backup permits backup administrator to select databases on a granular level. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/bvubhknmyspm4fv/?name=28.png" alt="28.png" />
</p>
<p>6. &nbsp;Choose the appropriate Compression and Encryption options for your environment. &nbsp;It is recommended that AES 128bit or higher encryption is implement with long, complex encryption keys.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/yvip64llazght7o/?name=29.png" alt="29.png" />
</p>
<p>7. &nbsp;Specify the appropriate purge options for backup files. &nbsp;Defaults can be viewed by selecting the 'options' hyperlink. &nbsp;Clients may wish to keep SQL backups based on # of versions or based on data set age. &nbsp;A version age methodology
  was used in this example. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/nd816zhvolfb9cs/?name=30.png" alt="30.png" />
</p>
<p>8. &nbsp;Configure a SQL Server backup schedule. &nbsp;Depending on the recovery needs of the database environment an advanced schedule may be required. &nbsp;In this example we will use the advanced schedule.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/zsdi71int0zc7wg/?name=31.png" alt="31.png" />
</p>
<p>9. &nbsp;As part of this example backup plan, we will configure a Daily Full backup at 11 PM first. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/ims4kmtlvqbi2wr/?name=32.png" alt="32.png" />
</p>
<p>10. &nbsp;Secondary to this Daily Full backup, we will configure an hourly transaction log backup to provide a 1 hour RPO for the database environment. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/xt7qrvdhb1zv75f/?name=33.png" alt="33.png" />
</p>
<p>11. &nbsp;Below is a final summary view of the Full &amp; Transaction Log backup schedules.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/k8pzeit6msdim5m/?name=34.png" alt="34.png" />
</p>
<p>12. &nbsp;Support is provided for Pre / Post commands if required.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/rh75aewwmpqjr3x/?name=35.png" alt="35.png" />
</p>
<p>13. &nbsp;Notification Options provide backup administrators with alerts for success or failure for each backup plan. &nbsp;Clients can leverage the the Cloudberry backup messaging service or specify an SMTP server.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/nggzojenjg1i8yo/?name=36.png" alt="36.png" />
</p>
<p>14. &nbsp;A summary of the backup plan is provided once configurations are complete.&nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/ych4xu9tcdmsaq8/?name=37.png" alt="37.png" />
</p>
<p>15. &nbsp;You have now configured a SQL Database backup plan.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/fuhdv2coyzbnmur/?name=38.png" alt="38.png" />
</p>
<h3>Review Backup Logs</h3>
<p>Customers should review backup logs for details on failure events. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/cidzwqnx1w4upss/?name=39.png" alt="39.png" />
</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><em><strong>Last Updated THURS, 21 NOV 2013, 18:05 PM EST</strong></em>
</p>