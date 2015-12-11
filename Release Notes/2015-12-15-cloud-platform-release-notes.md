{{{
"title": "Cloud Platform - Release Notes: December 15, 2015",
"date": "12-15-2015",
"author": "Jared Ruckle",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (2)

* __Object Storage - Now Available in US East Region [TENTATIVE] .__ CenturyLink Cloud's object storage service is now available in US East. Like the recently improved Canadian offering, object storage in US East will provide the same high availability and redundancy over the familiar S3 interface. More details are available on the [object storage product page](https://www.ctl.io/object-storage/), including pricing, and the [knowledge base](https://www.ctl.io/knowledge-base/object-storage/).

* __Orchestrate.io - Randomized Sorting.__ Now, equally scored results can show up in different orders. By adding `sort=_random` to the URL query string, the search results will now have an equal chance at being displayed first. Users can choose to randomize sort within an existing search query, i.e. randomize the results of searching for "last name Twain, first name Mark" `sort=value.last_name,value.first_name,_random`. Also, users have the option to randomize results with a predictable seed (by setting `sort=_random:somevalue`), and any subsequent calls to the same seed will result in the same random ordering.

### Early Adopter Program Updates (4)

* __NEW - Simple Backup Service Beta Launch.__ This new self-service product offers protection for your data with file-level backups hosted in secure object storage. Control every aspect of your backups - including retention period, frequency of backup, and location - with policies you create and manage. The service is now in beta and is available to select customers. To request an invitation to the beta program, [visit the product page](https://www.ctl.io/simple-backup-service/) or send an email to [help@ctl.io](mailto:help@ctl.io). Note that this service will replace [the Standard and Premium storage services in Q1 2016](https://www.ctl.io/knowledge-base/support/backup-service-changes-faq/).

![Simple Backup Service Policy](../images/2015-12-15_simplebackup.png)

* __NEW - Managed Pivotal Cloud Foundry Beta Launch.__ Many enterprises are building cloud native applications with Cloud Foundry. With this [new managed service](https://www.ctl.io/managed-services/pivotal-cloud-foundry/), the experts at CenturyLink will administer and maintain important elements of Cloud Foundry clusters running on CenturyLink Cloud. To request an invitation to the beta program, send an email to [help@ctl.io](mailto:help@ctl.io).

![Cloud Foundry AppManager](../images/2015-12-15_managedpcf.png)

* __NEW - Load Balancer as a Service Beta Launch [TENTATIVE] .__ This new shared load balancer service expands the features available to [our current production service](https://www.ctl.io/load-balancing/). New capabilities include TCP load balancing, support for load balancing on any port, and configurable health checks. The beta is available via API only. To request an invitation to the beta program, send an email to [help@ctl.io](mailto:help@ctl.io) or visit the [product page](https://www.ctl.io/load-balancing/).

* __MySQL DBaaS Notification Subscription.__ Beta users can now select to receive email notifications when CPU or Storage exceed defined thresholds. This can be done at the time of provisioning; notifications can also be added or changed from within the details page your subscription.

![MySQL Notifications](../images/2015-12-15_mysql.png)

* __Runner Beta.__ Several new capabilities are available for the agent-less automation service:

  * **Job Execution Expiration time** - Added ability for users to set an expiration time for a job. This helps users to stop any unexpected long-running executions and look at the detailed status logs to know which task was running, and for how long. Refer our latest documentation for Job Service available to beta users [Create Job - Password Protected](http://info.runner.ctl.io/job-service/#createJob) and [Update Job - Password Protected](http://info.runner.ctl.io/job-service/#updateJob) for details. The execution will move to a new state `EXPIRED` after it reaches the specified time.
  * **New default status of job execution** - When a job is executed, the default state will be `INITIALIZING` (previously, the default state was `PENDING`), since the various tasks in your playbook are being processed before they are actually executed. Further, you can stop and kill job executions that are in `PENDING` state.

### Enhancements (1)

* __Private routing of traffic between servers using public IPs provided by CenturyLink Cloud.__ Traffic between servers using public IPs provided by CenturyLink Cloud are now routed over our private MPLS network between CenturyLink Cloud Data Centers. This approach offers increased performance and reliability as well as lower cost, compared to using the public Internet.

### Announcements (1)

* __Intrusion Prevention/IPS Price Drop.__ CenturyLink is constantly reviewing the market to remain competitive with our features and pricing. Based on current research, we have lowered the price for our Intrusion Prevention/IPS product from $0.25 per VM/hr to $0.18 per vm/hr. We are continuing to add new features and review the pricing. If you would like to try IPS with a promo code, please contact [securityproduct-feedback@ctl.io](mailto:securityproduct-feedback@ctl.io) for more information.

### Ecosystem (5)

* __Mesosphere:__ Coming from Ecosystem [provisioned via blueprint on the CenturyLink platform today.](https://www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-mesosphere/)

* __Ruxit:__ Coming from Ecosystem [get started with Heirloom via single-click blueprint](https://www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-ruxit/), reducing their costly dependency on mainframe skill-sets.

* __FortyCloud:__ [FortyCloud](http://www.fortycloud.com) secures your public cloud deployment by managing security end-to-end: VPN, firewall, servers and networking. Customers can now control and monitor their multi-vendor cloud network and improve network security compliance. Try it yourself with an [easy Blueprint deployment](https://www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-fortycloud-appliance/).

* __aiScaler:__ Coming from Ecosystem [Get started with the TFS blueprint today](https://www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-aiscaler/).

* __VDIWorks:__[VDIWorks](http://www.vdiworks.com) is the leading provider of virtual desktop management solutions, providing economical, secure support for virtual desktop environments. Customers can implement large sets of desktop clients easily in the CenturyLink Cloud.  Try it yourself using [the VDIWorks blueprint solution at centurylink](https://www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-vdiworks-console/).
