{{{
  "title": "Resizing a Relational Database Instance",
  "date": "10-22-2017",
  "author": "Brian Waganer",
  "keywords": ["clc", "cloud", "database", "db", "dbaas", "mysql", "rdbs", "portal"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Audience
This article is to support customers of Relational Database service (RDBS), Lumen's database-as-a-service product. These instructions are specific to resizing a subscription through the Control Portal.

### Overview
Lumen's Relational Database service is a database-as-a-service that provides instant access to a database instance with SSL support, daily backups, basic monitoring, logs, metrics, and a replication option. Users can configure the amount of CPU, memory, and storage based on their database needs. They can choose to replicate their instance in a data center for a more highly available solution. As the customer's capacity needs grow, they can easily scale their CPU, RAM, and/or storage with the click of a button.

### Prerequisites
* access to the Lumen Cloud platform as an authorized user
* an existing RDBS instance

### Resizing an Existing Relational Database Instance
1. Browse to Lumen Cloud’s RDBS dashboard through the [Control Portal][1] or directly at [rdbs.ctl.io][2].

2. Under the tab "Databases", identify and select the database subscription you would like to resize. This takes you to a details screen specific to that subscription.

3. From the details screen, click the "resources" button. This brings up a new section of the screen with slide bars that allows you to select the new size of your instance.
    ![ReSizeDB][3]

4.  Make your new selections and click "save". You should then see the status change to "Configuring".
    - The dashboard will warn that the database will be restarted upon making any changes. However, this is not the case; only the following resize requests result in a database restart.  
    \- Increasing Memory  
    \- Decreasing Memory  
    \- Decreasing CPU
    - Storage can be scaled up, but cannot be scaled down through the API or UI.
    - New applicable hourly charges apply after successful resize.

**Note:** All changes to the RDBS instance will be locked until the change operations have completed.

**If you have questions or feedback, please submit them to our team by emailing [rdbs-help@ctl.io][4].**

[1]: https://control.ctl.io
[2]: https://rdbs.ctl.io
[3]: ../images/rdbs/rdbs-resize-db.png
[4]: mailto:rdbs-help@ctl.io
