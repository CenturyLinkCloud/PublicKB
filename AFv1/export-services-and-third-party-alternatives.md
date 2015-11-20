{{{
  "title": "Migrating a Service",
  "date": "10-5-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.


### Export Services
The export utility in AppFog v1 is subject to timeout for databases larger than approximately 100M. Please verify your data before deleting any services. For databases near 100M or that experience export errors please login to open a [Support Ticket](https://support.appfog.com/tickets/new) or email support@appfog.com and we will provide a dump of your database.

1. Export using the tunnel:
  * [Tunneling](service-database-content-management-tunneling.md) on AppFog v1.
  * From the command line:
<pre>af tunnel</pre>
  * Select the service to export.
  * When prompted choose to download a dumpfile, or if not available select "1. none" to use a third party tool to connect to the open tunnel using the credentials it provides.
<pre>Starting tunnel to mysql-b0085 on port 10000.
1: none
2: mysql
3: mysqldump
</pre>
2. Export a MySQL database using the `export-service` command:
  * Use `export-service` to generate a dump URI.
  * Download the file from the URL.
  * Give the file the ZIP file extension.
  * Decompress the ZIP and navigate to the content folder in your current directory.
  * Decompress the SQL file from the Gunzip (GZ) file.
  * An example is below:
<pre>af export-service \<service_name\>
mkdir \<service_name\>
cd \<service_name\>
wget -c -O \<service_name\>.zip \<URL_provided_by_export-service_command\>
unzip \<service_name\>.zip
cd content
gunzip *.gz
</pre>
3. Export a MySQL database using phpMyAdmin:
  * Deploy a [phpMyAdmin on AppFog](phpmyadmin-on-appfog.md) jumpstart app.
  * Use the phpMyAdmin export utility.
  * For large databases that still experience timeouts you can export the database in chunks, selecting single or multiple tables at a time.

### AppFog v2 Services
At this time [Orchestrate](https://orchestrate.io/) and [MySQL](https://www.ctl.io/dbaas/) are the first-party service offerings of AppFog v2.

#### Orchestrate
* [Getting Started With Orchestrate](https://orchestrate.io/docs)

#### MySQL on CenturyLink Cloud
* [Using CenturyLink MySQL with AppFog](../AppFog/using-ctl-mysql-with-appfog-apps.md)
* [Database](../Database/) Knowledge Base page.

#### AppFog v2 Third Party Service Alternatives

##### MySQL
* [ClearDB](https://www.cleardb.com/)

##### Mongo
* [Compose (MongoDB)](https://www.compose.io/)
* [MongoLab](https://mongolab.com/)

##### PostgreSQL
* [ElephantSQL](http://www.elephantsql.com/)
* [Compose](https://www.compose.io/)

##### Redis
* [redislabs](https://redislabs.com/)
* [openredis](https://openredis.com/)

##### RabbitMQ
* [CloudAMQP](https://www.cloudamqp.com/)
