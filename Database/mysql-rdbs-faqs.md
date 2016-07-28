{{{
  "title": "FAQs: Relational DB Service",
  "date": "02-28-2016",
  "author": "Christine Parr",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Audience
This article is to support customers of Relational DB Service, CenturyLink's MySQL compatible database-as-a-service product. These responses in this FAQ document are specific to using the service through the Control Portal.

### FREQUENTLY ASKED QUESTIONS
**Q:** How will I connect to my MySQL instance?
**A:** You will instantly receive your connection string information when you create your database subscription. Use the provided connection string, port, and your selected database credentials to connect to and manage your database using your favorite MySQL Client or through Command Line Interface (CLI).

**Q:** How is my data isolated from other Relational DB tenants?
**A:** Each MySQL instance lives on its own Virtual Machine.

**Q:** Are there published APIs that I can use in my own automation?
**A:** Yes. We have published APIs for all actions that can be performed in the UI. API endpoint is https://api.rdbs.ctl.io/. For more information and to get started using our APIs, you can view our [API documentation](https://www.ctl.io/api-docs/v2/#relational-database-rdbs).

**Q:** Can I choose to replicate my data for higher availability?
**A:** Customers are given the option to replicate their database instance during the ordering/provisioning process. If replication is chosen, a replica instance will be created within the same datacenter. We use logic to ensure that the primary and replica instances do not share the same host or storage volume. The service will then monitor both primary and replica and will auto-failover to the replica instance if the primary becomes unavailable. Customers can also choose to perform a manual failover, if needed. For more information on replication and failover, see our KB on [Replication and Failover](../Database/replication-and-failover.md).

**Q:** Is the replication synchronous or asynchronous?
**A:** Replication is asynchronous across a local 10G network, resulting in real time replication assuming normal networking conditions.

**Q:** Can I access my replica instance separately in order to load balance my read requests?
**A:** No. The replica instance is used for high availability purposes only. A separate read replica with unique connection string is a future feature.

**Q:** I understand that SSL Encryption options are available. Will my data be encrypted in transit and/or at rest?
**A:** Upon database subscription, you will be given the option to download a self-signed cert that can be consumed by your target application. When implemented, your database connection is encrypted as well as your data in transit. Please see the KB article on [Connecting to MySQL Relational DB Over SSL](../Database/connecting-to-mysql-rdbs-over-ssl.md) for additional details.

**Q:** How will I know when my database instance is reaching maximum capacity?
**A:** Customers have the option to sign up to receive email notification when their CPU and/or storage has reached 80% capacity. Customers who sign up for these notifications will be notified again when capacity reaches 90%. Upon notification, customers can easily scale their database instance size through API or UI.

**Q:** How can I grow or shrink my database instance?
**A:** Customers can easily scale their database instance size through the UI or API. CPU and RAM can be scaled up or down and storage can be scaled up only. Adding or removing memory or reducing CPU will require a database restart. Growing CPU or storage will not require a restart of the database. Please see the KB article on [Resizing a Relational DB Instance](../Database/resizing-mysql-rdbs-instance.md)

**Q:** I understand that CenturyLink is backing my data up daily. How can I access my backups in order to restore?
**A:** If you need to restore from an available backup, you can leverage the Restore Backup API or perform the restore in the Control Portal. For more information on performing database restores in Control, please see the KB on [Backups and Restores](../Database/backups-and-restores.md).
**Q:** Are my backups encrypted?
**A:** Yes. All backups are encrypted at rest.

**Q:** How long are my backups being held?
**A:** At the time of Relational DB subscription creation, the user will define backup retention policy. Customers can select a retention policy as short as 1 day or as long as 35 days. Customers can also change the backup retention policy post-provisioning through the Subscription details page of the UI or through API.

**Q:** Where are my backups being held?
**A:** For disaster recovery purposes, backups are being held offsite at least 350 miles away from your primary database. Backups are also held in the same country as the associated Relational DB instance to maintain data sovereignty.

**Q:** Will the product support the use of standard MySQL management tools including the ability to monitor and report on database tasks within the tool?  
**A:** Yes. Your database instance is on a dedicated VM and there are no restrictions for any management utilities. In fact, we expect that much of the database management will be accomplished using MySQL Command Line Interface or a MySQL client of your choice.

**If you have questions or feedback, please submit them to our team by emailing <a href="mailto:rdbs-help@ctl.io">rdbs-help@ctl.io</a>.**
