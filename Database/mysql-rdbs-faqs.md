{{{
  "title": "FAQs: Relational DB Service",
  "date": "01-25-2016",
  "author": "Christine Parr",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}


#### Audience

This article is to support customers of Relational DB Service, CenturyLink's MySQL compatible database-as-a-service product.  Additionally, the responses in this FAQ document are specific to using the service through the Control Portal.


## FREQUENTLY ASKED QUESTIONS

<p><strong>Q: How will I connect to my MySQL instance?</strong>
</p>
<p>A: You will instantly receive your connection string information when you create your database subscription.  Use the provided connection string, port, and your selected database credentials to connect to and manage your database using your favorite MySQL Client or through Command Line Interface (CLI).</p>

<p><strong>Q: How is my data isolated from other Relational DB tenants?</strong>
</p>
<p>A: Each MySQL instance lives on its own Virtual Machine.</p>

<p><strong>Q: Can I choose to replicate my data for higher availability?</strong>
</p>
<p>A: Customers are given the option to replicate their database instance during the ordering/provisioning process.  If replication is chosen, a replica instance will be created within the same datacenter.  We use logic to ensure that the primary and replica instances do not share the same host or storage volume.  The service will then monitor both primary and replica and will auto-failover to the replica instance if the primary becomes unavailable.  Customers can also choose to perform a manual failover, if needed.  For more information on replication and failover, see our KB on [Replication and Failover](../Database/replication-and-failover.md).</p>
</p>
<p><strong>Q: Can I access my replica instance separately in order to load balance my read requests?</strong>
</p>
<p>A: No.  The replica instance is used for high availability purposes only.  A separate read replica with unique connection string is a future feature.
</p>  
<p><strong>Q: I understand that SSL Encryption options are available.  Will my data be encrypted in transit and/or at rest? </strong>
</p>
<p>A: Upon database subscription, you will be given the option to download a self-signed cert that can be consumed by your target application. When implemented, your database connection is encrypted as well as your data in transit.  Please see the KB article on [Connecting to MySQL Relational DB Over SSL](../Database/connecting-to-mysql-rdbs-over-ssl.md) for additional details.
</p>
<p><strong>Q: How will I know when my database instance is reaching maximum capacity?</strong>
</p>A: Customers have the option to sign up to receive email notification when their CPU and/or storage has reached 80% capacity.  Customers who sign up for these notifications will be notified again when capacity reaches 90%.  Upon notification, customers can easily scale their database instance size through API or UI.

<p><strong>Q: How can I grow or shrink my database instance?</strong>
</p>A: Customers can easily scale their database instance size through the UI or API.  CPU and RAM can be scaled up or down and storage can be scaled up.  Adding or removing memory or reducing CPU will require a database restart.  Growing CPU or storage will not require a restart of the database.  Please see the KB article on [Resizing a Relational DB Instance](../Database/resizing-mysql-rdbs-instance.md)
</p>
<p><strong>Q: I understand that CenturyLink is backing my data up daily.  How can I access my backups in order to restore? </strong>
</p>
<p>A: If you need to restore from an available backup, you can send a request to <a href="mailto:rdbs-help@ctl.io">rdbs-help@ctl.io</a> and we will work with you to restore your data.  Check back here soon though, because automated restores from backup are a planned feature!</p>
<p><strong>Q: Where are my backups being held? </strong>
</p>
<p>A: For disaster recovery purposes, backups are being held offsite at least 350 miles away from your primary database.  
</p>
<p><strong>Q: Will the product support the use of standard MySQL management tools including the ability to monitor and report on database tasks within the tool?  </strong>
</p>
<p>A: Yes.  Your database instance is on a dedicated VVM and there are no restrictions for any management utilities.  In fact, we expect that much of the database management will be accomplished using MySQL Command Line Interface or a MySQL client of your choice.
<p>
<p><strong>Q: Are there published APIs that I can use in my own automation? </strong>
</p>
<p>A: Yes.  We have published APIs for all actions that can be performed in the UI.  API endpoint is https://api.rdbs.ctl.io/.  For more information and to get started using our APIs, please view our [API documentation](https://api.rdbs.ctl.io/api/swagger/index.html).


**If you have questions or feedback, please submit them to our team by emailing <a href="mailto:rdbs-help@ctl.io">rdbs-help@ctl.io</a>.**
