{{{
"title": "Hyperscale Retirement FAQ",
"date": "06-20-2018",
"author": "Matt Schwabenbauer",
"attachments": [],
"related-products" : [],
"contentIsHTML": false,
"sticky": true
}}}

### Hyperscale Server Retirement
The key to success with cloud infrastructure is to manage your deployments by using repeatable and scalable processes. In order to drive business agility while also maintaining simplicity, it is critical to streamline your infrastructure footprint on a standardized platform.

Over the past year, Lumen Cloud has worked hard to improve our standard compute service to fulfill more of our customers’ cloud hosting needs. By standardizing our storage infrastructure on all-flash platforms, customers have the ability to host distributed workloads on a common compute product while maximizing performance.

Due to the positive impact of the storage improvements across all of our cloud infrastructure, we’ve come to realize that our customers no longer need our specialized all-flash storage cloud compute service, Hyperscale. Today, we are announcing the end of availability for Hyperscale.

### FAQ

**Q**: When is Hyperscale being discontinued?

**A**: On July 10, 2018, we will remove Hyperscale links from the [Lumen Cloud control portal](https://control.ctl.io/). Existing Hyperscale servers will continue to operate until they have been migrated to our standard virtual compute infrastructure.

By August 21, 2018, all Hyperscale servers will have been migrated to our standard compute infrastructure.

**Q**: Do I have to do anything?

**A**: No, we’ll take care of it all for you. Over the next 60 days, our infrastructure engineering teams will be migrating all Hyperscale virtual machine instances to our standard compute platform.  

**Q**: Will I experience any downtime during this migration?
**A**: No. We are working hard to minimize the impact customers will experience from these migrations and plan to conduct them with zero downtime to the availability of your instances

**Q**: What will this do to the performance of my virtual machines?

**A**: The performance improvement that Hyperscale customers will experience after their instances have been migrated to standard compute can be substantial. In our testing of common storage-intensive workloads, we saw drastic improvements to I/O performance. The actual change to your storage performance may vary depending on application workloads.

**Q**: What will this do for my cost?

**A**: In addition to performance improvements, customers using Hyperscale virtual machines will also see a reduction in the total cost of their instances. The per-gigabyte price for block storage attached to standard compute instances is a 58% decrease when compared to the per-gigabyte price for block storage attached to Hyperscale compute instances. For example, the price per month of a single gigabyte of block storage for Hyperscale is $0.29, while the price per month of a single gigabyte of block storage for standard compute is only $0.12.

The price changes for regions outside of the United States may vary between each of our service locations. More information can be found at our public price catalog located [here](https://www.ctl.io/pricing/).

**Q**: What if I have a Cloud Term Commit for a dollar amount that exceeds my needs after migration to the less expensive standard cloud servers?

**A**: If you have a Cloud Term Commit agreement with us, the cost reduction of moving from Hyperscale to standard cloud servers may result in your Cloud Term Commit adjustment being higher than expected. If so, please reach out to us at help@ctl.io with a subject line of “Review Cloud Commit for Hyperscale” and we will work with you to adjust your Cloud Term Commit dollar amount appropriately.

**Q**: What if I don’t believe standard Cloud servers will meet my specific needs?

**A**: While we believe our standard compute product is a good fit for most cloud workloads, there are still some use cases that require specialized services. For customers with applications requiring the highest possible performance from their compute infrastructure, such as Big Data or Artificial Intelligence, our [Bare Metal service](https://www.ctl.io/bare-metal/) offers the power of physical servers with the flexibility of virtual machines. For customers that want to use a specialized database product and offload some of their application deployment and management tasks, our [Relational Database as a Service](https://www.ctl.io/relational-database/) is the product for you.

**Q**: What about my standard compute instances? Will they change at all?

**A**: No. For customers that are already using our standard compute platform and do not have any Hyperscale instances, no changes will need to be made. There will be no impact to standard compute workloads.

For any questions related to the end of availability of Hyperscale, please reach out to our customer care team at [help@ctl.io](mailto:help@ctl.io).
