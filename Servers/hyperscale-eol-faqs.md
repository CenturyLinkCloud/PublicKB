{{{
  "title": "Hyperscale Server Retirement FAQs",
  "date": "6-21-2018",
  "author": " ",
  "attachments": [],
  "contentIsHTML": false
}}}

**Q: Why is Hyperscale being discontinued?**

A: We recently standardized our storage infrastructure on all-flash platforms for all CenturyLink Cloud Servers, so there is no longer a need for the specialized all-flash storage cloud compute service, [Hyperscale](https://www.ctl.io/hyperscale/).

**Q: When is Hyperscale being discontinued?**

A: On August 21, 2018, we will remove Hyperscale links from the [Control navigation menu](https://control.ctl.io/), which means that no new Hyperscale server instances may be created after this date. Existing Hyperscale servers will continue to operate until they have been migrated to standard Cloud servers.

By August 21, all your Hyperscale servers will have been migrated over and appear within the Control Portal as standard cloud servers.

**Q: Do I have to do anything?**

A: No. We’ll take care of everything for you. Over the next 60 days, our infrastructure engineering teams will be migrating all Hyperscale virtual machine instances over to our improved standard compute platform.

**Q: Will I experience any downtime during this migration?**

A: No. We plan to conduct these migrations with zero downtime to the availability of your instances.

**Q: What will this do to the performance of my virtual machines?**

A: The performance improvement that Hyperscale customers will experience after their instances have been migrated to standard compute can be substantial! In our testing of common storage-intensive workloads, we saw drastic improvements to I/O performance. The actual change to your storage performance may vary depending on application workloads.

**Q: What will this do for my cost?**

A: In addition to performance improvements, customers using Hyperscale virtual machines will also see a reduction in the total cost of their instances. The per-gigabyte price for block storage attached to standard compute instances is a 58% decrease when compared to the per-gigabyte price for block storage attached to Hyperscale compute instances. For example, the price per month of a single gigabyte of block storage for Hyperscale is $0.29, while the price per month of a single gigabyte of block storage for standard compute is only $0.12.

The price changes for regions outside of the United States may vary between each of our service locations. More information can be found at our [public price catalog](https://www.ctl.io/pricing/).

**Q: What if I have a Cloud Term Commit for a dollar amount that exceeds my needs after migration to the less expensive standard cloud servers?**

A: If you have a Cloud Term Commit agreement with us, the cost reduction of moving from Hyperscale to standard cloud servers may result in your Cloud Term Commit being higher than actually warranted for your needs. If so, please reach out to us at [help@ctl.io](mailto:help@ctl.io) with the subject line of “Review Cloud Commit for Hyperscale” and we will work with you to adjust your Cloud Term Commit dollar amount appropriately.

**Q: What if I don’t believe standard Cloud servers will meet my specific needs?**

A: While we believe our standard compute product is a good fit for most cloud workloads, there are still some use cases that require specialized services. For customers with applications requiring the highest possible performance from their compute infrastructure, such as Big Data or Artificial Intelligence, our [Bare Metal service](https://www.ctl.io/bare-metal/) offers the power of physical servers with the flexibility of virtual machines. For customers who want to use a specialized database product and offload some of their application deployment and management tasks, our [Relational Database as a Service](https://www.ctl.io/relational-database/) is the product for you.

**Q: What about my standard compute instances? Will they change at all?**

A: No. For customers who are already using our standard compute platform and do not have any Hyperscale instances, no changes will need to be made. There will be no impact to standard compute workloads.

For any questions related to the end of availability of Hyperscale, please reach out to our customer care team at [help@ctl.io](mailto:help@ctl.io).
