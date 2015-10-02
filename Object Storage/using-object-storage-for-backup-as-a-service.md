{{{
  "title": "Using Object Storage for Backup as a Service",
  "date": "4-20-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
CenturyLink Cloud customers may wish to leverage our S3 compatible Object Storage for backup and recovery of file systems or applications. As Object Storage is consumable by any customer in a public fashion, applications or servers can be located within the CenturyLink Cloud or on premise. There are various industry backup tools that support object storage as a repository for data. In this knowledge base we will focus on [Cloudberry Lab](http://www.cloudberrylab.com).

[Cloudberry Backup Enterprise Edition](http://www.cloudberrylab.com/enterprise-cloud-backup-software.aspx) permits backup of Microsoft Windows Server File Systems, Microsoft SQL and Microsoft Exchange data.

### Supporting Information
* Information and details around the CenturyLink Cloud Object Storage services can be found in our [Knowledge Base.](//www.ctl.io/knowledge-base/object-storage)
* It is also important to note that CenturyLink Cloud provides no support for any 3rd party backup software tools. We are simply providing cloud based storage onto which backup software can store data.

### Prerequisites
* A CenturyLink Cloud Account
* Cloudberry Backup software licenses and installation
* [An object storage user and bucket for backups is created in the CenturyLink Cloud Control Portal.](../Object Storage/using-object-storage-from-the-control-portal.md)
* The source VM or Server has internet access

### Configuring File System Backup
1. Open Cloudberry Backup Enterprise Edition, select file, **S3 Compatible**

    ![Select S3 compatible](../images/using-object-storage-for-backup-as-a-service-01.png)

2. Populate the S3 Compatible Account information with your CenturyLink Cloud [Object Storage Access Key, Secret Key, Service Point and bucket name.](../Object Storage/using-object-storage-from-the-control-portal.md)
    * The Service Point for Canada is **ca.tier3.io**

    ![S3 Compatible Account input](../images/using-object-storage-for-backup-as-a-service-02.png)

3. Optionally, you may input cost estimate parameters as part of the storage account setup. By using this component the Cloudberry Lab backup software is able to estimate your costs for storage. **This is merely an estimate on storage (excluding bandwidth charges) and does not necessarily reflect actual CenturyLink Cloud Object Storage fees.**

    ![S3 Compatible Costs](../images/using-object-storage-for-backup-as-a-service-03.png)

4. Your S3 Compatible Storage Account should now be created successfully.

    ![Cloud Storage Account List](../images/using-object-storage-for-backup-as-a-service-04.png)

5. At the Welcome screen select **Setup Backup Plan.**

    ![select setup backup plan](../images/using-object-storage-for-backup-as-a-service-05.png)

6. Select the S3 Compatible Cloud Storage account you created in steps 1-3 as the destination for backups.

    ![select cloud storage account](../images/using-object-storage-for-backup-as-a-service-06.png)

7. Specify a name for the backup plan. We recommend a name that encompasses the server name, backup type (file, SQL etc) as a minimum. Additionally, it is advised that backup plan configurations are saved to the backup storage (Default).

    ![backup plan name](../images/using-object-storage-for-backup-as-a-service-07.png)

8. Choose an appropriate backup model based on the features you require. Typical enterprise customers will want to leverage the Advanced Mode approach as it provides for Data Encryption and complex retention policies.

    ![select backup mode](../images/using-object-storage-for-backup-as-a-service-08.png)

9. Select the backup source. Entire Windows volumes, specific directories or UNC Shares can be added to the backup plan.

    ![backup source](../images/using-object-storage-for-backup-as-a-service-09.png)

10. The Advanced Filter allows administrators to include or exclude specific file types, folders and large files. Select the appropriate settings based on IT Department or business policies.

    ![include or exclude](../images/using-object-storage-for-backup-as-a-service-10.png)

11. In order to secure backup data and reduce cost customers can enable encryption and compression. It is recommended that AES 128bit or higher is implement with long, complex encryption keys. Additionally, file name encryption adds another layer of security.

    ![compression and encryption options](../images/using-object-storage-for-backup-as-a-service-11.png)

12. Specify the appropriate purge options for backup files. Defaults can be viewed by selecting the 'options' hyperlink. Clients may wish to keep file system backups based on number of versions or based on data set age.

    ![purge options](../images/using-object-storage-for-backup-as-a-service-12.png)

13. Choose a backup schedule that meets IT or business requirements. Generally, its best practice to perform a backup at least once per day during off hours. The Cloudberry Backup software supports recurring scheduled backups and even real-time backup of data.

    ![schedule](../images/using-object-storage-for-backup-as-a-service-13.png)

14. In this example we selected recurring, and set the schedule for Daily at 8 PM.

    ![schedule recurring options](../images/using-object-storage-for-backup-as-a-service-14.png)

15. Support is provided for Pre / Post commands if required.

    ![Pre-Post Actions](../images/using-object-storage-for-backup-as-a-service-15.png)

16. Notification Options provide backup administrators with alerts for success or failure for each backup plan. Clients can leverage the the Cloudberry backup messaging service or specify an SMTP server.

    ![notifications](../images/using-object-storage-for-backup-as-a-service-16.png)

17. A summary of the backup plan is provided once configurations are complete.

    ![summary](../images/using-object-storage-for-backup-as-a-service-17.png)

18. You have now configured a file system backup plan.

    ![plan completed successfully](../images/using-object-storage-for-backup-as-a-service-18.png)

### Configuring Microsoft SQL Database Backup
1. Open Cloudberry Backup Enterprise Edition, select **Backup MS SQL Server.**

    ![backup ms sql](../images/using-object-storage-for-backup-as-a-service-19.png)

2. Select the S3 Compatible Cloud Storage account you created earlier in this KB as the destination for backups.

    ![select cloud account](../images/using-object-storage-for-backup-as-a-service-20.png)

3. Specify a name for the backup plan. We recommend a name that encompasses the server name, backup type (file, SQL etc) as a minimum. Additionally, it is advised that backup plan configurations are saved to the backup storage (Default).

    ![sql plan name](../images/using-object-storage-for-backup-as-a-service-21.png)

4. Select the Microsoft SQL Instance you wish to backup and the appropriate authentication for your environment.

    ![select sql instance](../images/using-object-storage-for-backup-as-a-service-22.png)

5. Select the database in the Microsoft SQL Instance you wish to backup. Cloudberry Backup permits backup administrator to select databases on a granular level.

    ![select databases](../images/using-object-storage-for-backup-as-a-service-23.png)

6. Choose the appropriate Compression and Encryption options for your environment. It is recommended that AES 128bit or higher encryption is implement with long, complex encryption keys.

    ![compression and encryption options](../images/using-object-storage-for-backup-as-a-service-24.png)

7. Specify the appropriate purge options for backup files. Defaults can be viewed by selecting the 'options' hyperlink. Clients may wish to keep SQL backups based on number of versions or based on data set age. A version age methodology was used in this example.

    ![purge options](../images/using-object-storage-for-backup-as-a-service-25.png)

8. Configure a SQL Server backup schedule. Depending on the recovery needs of the database environment an advanced schedule may be required. In this example we will use the advanced schedule.

    ![schedule](../images/using-object-storage-for-backup-as-a-service-26.png)

9. As part of this example backup plan, we will configure a Daily Full backup at 11 PM first.

    ![advanced recurring schedule daily](../images/using-object-storage-for-backup-as-a-service-27.png)

10. Secondary to this Daily Full backup, we will configure an hourly transaction log backup to provide a 1 hour RPO for the database environment.

    ![advanced recurring schedule hourly](../images/using-object-storage-for-backup-as-a-service-28.png)

11. Below is a final summary view of the Full and Transaction Log backup schedules.

    ![advanced recurring schedule final](../images/using-object-storage-for-backup-as-a-service-29.png)

12. Support is provided for Pre / Post commands if required.

    ![pre and post actions](../images/using-object-storage-for-backup-as-a-service-30.png)

13. Notification Options provide backup administrators with alerts for success or failure for each backup plan. Clients can leverage the the Cloudberry backup messaging service or specify an SMTP server.

    ![notifications](../images/using-object-storage-for-backup-as-a-service-31.png)

14. A summary of the backup plan is provided once configurations are complete.

    ![summary sql job](../images/using-object-storage-for-backup-as-a-service-32.png)

15. You have now configured a SQL Database backup plan.

    ![job setup completed](../images/using-object-storage-for-backup-as-a-service-33.png)

### Review Backup Logs
Customers should review backup logs for details on failure events.

![cloudberry logs](../images/using-object-storage-for-backup-as-a-service-34.png)
