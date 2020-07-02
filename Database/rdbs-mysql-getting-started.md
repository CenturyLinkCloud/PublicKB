{{{
  "title": "Getting Started with MySQL Relational DB Service",
  "date": "10-22-2017",
  "author": "Brian Waganer",
  "keywords": ["clc", "cloud", "database", "db", "dbaas", "configuration", "mysql", "portal"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Audience
This article is to support customers of Relational DB Service, CenturyLink's database-as-a-service product.  These instructions are specific to getting started provisioning and using a MySQL-compatible instance directly through the Control Portal.

### Overview
CenturyLink's Relational DB Service is a database-as-a-service product that provides instant access to a MySQL-compatible database instance with SSL support, daily backups, restore functionality, logs, OS monitoring, notifications, and a replication option with auto-failover. Users can configure the amount of CPU, Memory, and Storage based on their database needs. Customers with High Available needs can choose to replicate their instance in-datacenter to meet their HA solution. As the customer's capacity needs grow, they can easily scale their CPU, RAM, and/or Storage with the click of a button.
For users who would like some sizing guidance, below are a few common configurations:

**Micro**|**Small**|**Medium**|**Large**|**X-Large**
-----------|-----------|--------------|------------ |------------
CPUs: 1       |CPUs: 1      |CPUs: 2       |CPUs: 4         |CPUs: 8
Memory: 1 GB  |Memory: 2 GB |Memory: 6 GB  |Memory: 16 GB   |Memory: 32 GB
Storage: 1 GB |Storage: 2 GB|Storage: 64 GB|Storage: 256 GB |Storage: 512 GB

### Prerequisites
* Access to the CenturyLink Cloud Platform as an authorized user

### Configuring a New MySQL-Compatible Relational DB Subscription
1. Browse to CenturyLink Cloud’s Relational DB UI through the Control Portal by clicking on Create->Relational DB, or Services->RelationalDB, or directly at [rdbs.ctl.io](https://rdbs.ctl.io).

   ![Navigate](../images/rdbs/rdbs-navigate-to-create-page.png)
   ![Navigate](../images/rdbs/rdbs-navigate-to-summary-page.png)

2. Click the '+Database' button from the "Database Instances" screen to provision a new database instance.

   ![Navigate](../images/rdbs/rdbs-navigate-to-create-db-page.png)

3. Select a the engine, edition, location, network, enter an instance name (dns-friendly) for the database, and enter your DB password.  Please make sure not to lose this password.  We do not store it.

   ![CreateDB](../images/rdbs/rdbs-create-mysql-db-section.png)

4. Set the Resources for your database.
   * Select amount of CPU, Memory, and Storage to provision.

   ![MySQLResources](../images/rdbs/rdbs-create-mysql-resources-section.png)

5. Setup the Options section
   * If you would like your DB/Instance to be Replicated, move the slider. If selected, a replica of the primary database is created. Failover occurs when you manually push the fail-over button. Notice how estimated charges change when you choose Replication.
   * If you would like to be notified when your CPU or Storage reaches 80% and 90% of capacity, move the slider to choose to "enable notifications".  This will then prompt you for an email address to be used for the notifications.
   * If you would like to define the time of day your backup is run, move the slider to choose "customize backup schedule" and select the time of day in UTC you would like backups to run. If no customization is made, backups will run at 0:00 UTC.
   * If you would like to change your backup retention period
   * If you would like to assign a Configuration Profile, just select it.

   ![MySQLOptions](../images/rdbs/rdbs-create-mysql-options-section.png)

6. Click “Create Database”. Your database information will be returned, including connection string.

   ![DetailsPage](../images/rdbs/rdbs-db-details-page-overview-mysql.png)

7. You can view a list of all your database subscriptions with the datacenter and connection string information on the "Database Instances" tab.  Here you will see both MSSQL and MySQL instances if you are also a MySQL Relational DB customer.

   ![ListDB](../images/rdbs/rdbs-dblist2.png)

8. Click on any instance name to view subscription details. From there you can:
   * Breadcrumbs
     * Databases (Takes you back to the Summary Page)
   * Action Bar
     * Failover (If your Db is replicated)
     * Restart your VM
     * Backup your Instance/DB
     * Restore a Backup to your Instance
     * Delete your instance
   * Resource Box on the left side
     * Change Resources (CPU, RAM, Disk
     * Change your alert notification settings
   * Info Section
     * Download an SSL Certificate
     * Use the connection string information provided to connect from your favorite Database client.
   * Detail Tab Bar

   ![DetailsPage](../images/rdbs/rdbs-db-details-page-overview-mysql.png)

     * The Details Tab Bar (Backups)
        * Change your Backup Policy
        * Delete backups (Hover over backup to delete)
        ![DetailsPageBackups](../images/rdbs/rdbs-db-details-page-backups.png)

     * Configuration (Currently not on msSQL)
        * Allows you to connect a DB to a Configuration Parameter Profile

     * Logs (Displays log files in near real-time)
        * Instance (Pick the server you want to look at)
        * Filename (list of the log files you can look at)
        ![DetailsPageLogs](../images/rdbs/rdbs-db-details-page-logs.png)

     * Metrics (Shows OS level metrics)
        * Host (Pick which server you want to look at)
        * Type (CPU, Memory, Storage)
        * Graph Time Range (1 hour, 1 day, 31 days)
        * If you don't want to see a metric click on it in the Ledgen
        ![DetailsPageMetrics](../images/rdbs/rdbs-db-details-page-metrics2.png)


If you have questions or feedback, please submit them to our team by emailing <a href="mailto:rdbs-help@ctl.io">rdbs-help@ctl.io</a>.
