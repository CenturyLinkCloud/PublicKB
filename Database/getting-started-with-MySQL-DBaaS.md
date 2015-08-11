{{{
  "title": "Getting Started with MySQL DBaaS",
  "date": "08-14-2015",
  "author": "Christine Parr",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

#### IMPORTANT NOTE

CenturyLink Cloud’s MySQL-compatible Database-as-a-Service product is currently in a Limited Beta with specific customers by invitation only and is not intended for production usage.
During the Limited Beta there is no production Service Level Agreement.

#### Audience

Currently, this article is to support customers in the Limited Beta program.  Additionally, these instructions are specific to provisioning service directly through the DBaas user interface.  

## Overview

Our MySQL Database-as-a-Service limited beta provides instant access to a single MySQL-compatible database instance with SSL support, daily backups held locally for 7 days and basic monitoring.  The free beta is limited to a 1vCPU/1GB database instance with up to 100 MB storage and support for 100 concurrent connections in IL1 datacenter.

#### Prerequisites

- Access to the CenturyLink Cloud Platform as an authorized user.
- Acceptance into the DBaaS Limited Beta Program

## Configuring a New MySQL-compatible DBaaS Subscription

1.	Browse to CenturyLink Cloud’s DBaaS Beta User Interface.

2.  Input your CenturyLink Cloud username and password and click the login button. ![Login](../images/dbaas-login-beta.png)

3.  Click on the Create Database tab.

4.	Select datacenter from the drop-down menu, choose a plan, select your username and password for the database and enter a name for the database.  Click “Create Database”.  ![CreateDB](../images/dbaas-createdb-beta.png)

5.  When created, you will be returned your database information including connection string and can choose to download your certificate at that time. ![ListDB](../images/dbaas-dblist-beta.png)

6.  You can view a list of all your database subscriptions with connection string info on the "Database Instances" tab.  You can also download your certificate from this list at any time.

7.  Use the provided connection string information to administer your MySQL instance using standard command line interface from your favorite MySQL client.

8.  If you have questions or feedback, please submit them to our team using the feedback button. ![Feedback](../images/dbaas-feedback-beta.png)
