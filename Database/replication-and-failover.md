{{{
  "title": "Replication and Failover",
  "date": "01-25-2016",
  "author": "Christine Parr",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}


#### Audience

This article is to support customers of Relational DB Service, CenturyLink's MySQL compatible database-as-a-service product.  Additionally, these instructions are specific to using the replication features through Control Portal.

## Overview

CenturyLink's Relational DB Service is a MySQL-compatible database-as-a-service that provides instant access to a database instance with SSL support, daily backups held for 7 days, basic monitoring and a replication option.  Users can configure the amount of CPU, Memory and Storage based on their database needs and can choose to replicate their instance in datacenter for a more highly available solution.  As customers' capacity needs grown, they can easily scale their CPU, RAM and/or Storage through the click of a button.  

#### Prerequisites

- Access to the CenturyLink Cloud Platform as an authorized user


## Provisioning an Instance with Replication

1. Browse to CenturyLink Cloud’s Relational DB UI through the Control Portal or directly at [rdbs.ctl.io](https://rdbs.ctl.io).

2.	Click on "Create Database".  From here, select your subscription details (database name, username, password, cpu, memory and storage).  If you want your instance to be replicated, simply, flip the Replication toggle to yes and click on Create Database.
<p>![CreateReplicatedDB](../images/rdbs-createdb-replicated.png)

3. The resulting provisioning will create a primary database instance as well as a replica database instance and will return you a single connection string.  When a failover occurs, your application will continue to access your database instance using the same connection string.

## Manual & Automatic Failover
1.  Automatic Failover - Your instance will automatically failover to the replica when we detect that your primary instance is unavailable for longer than 6 seconds or 3 consecutive failed health checks.  Failback will occur after one minute of successful health checks of the primary.

2. A customer can determine if their database instance is currently running on the primary or replica by selecting the database subscription in question from the "Database Instances" screen.  When you click on the subscription in question, it will take you to a details page with a line for Active Instance.  This line will indicate either 'Primary' or 'Replica'.

3.  Manual Failover - To perform a manual failover, navigate to the same location in the UI as described in step 2, above, and click on the "failover" button in the top left corner.  This will trigger failover, and the
active instance will now show as being on the replica.
<p>![Failover](../images/rdbs-failover.png)

4.  If you have questions or feedback, please submit them to our team by emailing <a href="mailto:rdbs-help@ctl.io">rdbs-help@ctl.io</a>.
