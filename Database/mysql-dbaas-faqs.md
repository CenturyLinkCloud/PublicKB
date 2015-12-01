{{{
  "title": "FAQs: MySQL DBaaS",
  "date": "11-23-2015",
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

Currently, this article is to support customers in the Limited Beta program.  Additionally, the responses in this FAQ document are specific to using the service through our DBaaS user interface.


## FREQUENTLY ASKED QUESTIONS

<p><strong>Q: How will I connect to my MySQL instance?</strong>
</p>
<p>A: You will instantly receive your connection string information when you create your database subscription.  Use the provided connection string and your selected credentials to connect to and manage your database using your favorite MySQL Client.</p>

<p><strong>Q: How is my data isolated from other Database-as-a-Service tenants?</strong>
</p>
<p>A: Each MySQL instance lives on its own Virtual Machine.</p>

<p><strong>Q: Can I choose to replicate my data for higher availability?</strong>
</p>
<p>A: As of November 30th, 2015, beta users will be given the option to replicate their database instance.  If replication is chosen, a replica instance will be created within the same datacenter.  We use logic to ensure that the primary and replica instances do not share the same host.
</p>
<p><strong>Q: I understand that SSL Encryption options are available.  Will my data be encrypted in transit and/or at rest? </strong>
</p>
<p>A: Upon database subscription, you will be given the option to download a self-signed cert that can be consumed by your target application. When implemented, your database connection is encrypted as well as your data in transit.  Please see the KB article on [Connecting to MySQL DBaas Over SSL](../Database/connecting-to-mysql-dbaas-over-ssl.md) for additional details.</p>
</p>
<p><strong>Q: I understand that CenturyLink is backing my data up daily.  How can I access my backups in order to restore? </strong>
</p>
<p>A: If you need to restore from an available backup, you can send a request to <a href="mailto:dbaas-support@ctl.io">dbaas-support@ctl.io</a> and we will work with you to restore your data.</p>
