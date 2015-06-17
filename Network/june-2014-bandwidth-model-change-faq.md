{{{
  "title": "June 2014 Bandwidth Model Change FAQ",
  "date": "9-2-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
CenturyLink Cloud recently announced a change to the bandwidth billing model and a corresponding price drop. The questions and answers below describe the change and its impact.

**Q: What change are you making?**

A: CenturyLink Cloud is changing from a 95th percentile bandwidth billing model to a model based on price per GB of data transferred. Instead of paying $22 per Mbps, you will now pay $0.05 per GB of outbound data transferred.

**Q: When does this take effect?**

A: This pricing change will take effect on your July 1, 2014 invoice.

**Q: Do I have to do anything to activate this price drop?**

A: No! All customers will see this price drop automatically.

**Q: Why did you make this change?**

A: Multiple reasons. First, as part of telecommunications company CenturyLink, we can offer the most competitive bandwidth rates in the cloud industry. Second, we wanted to simplify bandwidth billing and make it easier for customers to understand their consumption.

**Q: What's the impact on the price that I was paying before?**

A: In the previous 95th percentile billing model, you paid for average consumption of inbound and outbound bandwidth over the course of the month (minus the peak 5% of usage). If you consumed 3 Mbps over the course of the month (1 Mbps inbound, and 2 Mbps outbound), that would cost you $66 dollars. Now, we are only charging for outbound bandwidth -- and given that [1Mbps equals about 320GB of data transferred](//www.google.com/#q=convert+1+Mbps+to+GB+per+month) -- so the same usage would cost just $16 ($0.05 * 320). In nearly every case, this is a noticeable price difference for CenturyLink Cloud customers.

<p><strong>Q: How does this differ from how other cloud providers bill for bandwidth?</strong>
</p>
<p><strong>A:</strong> Nearly all providers bill based on bandwidth transferred, but unlike those providers, CenturyLink Cloud has a single low rate that applies to any amount of bandwidth transferred. Most providers use a graduated rate that starts at more
  than $0.12 per GB and eventually reaches $0.05 after you transfer hundreds of terabytes of data.</p>

**Q: What network consumption do I *not* pay for?**

A: You are not charged for any data transferred in the following situations:
* Inbound Internet Bandwidth
* Between Virtual Machines in the same VLAN
* Between VLANs in a single cloud node (intra data center firewall)
* Between VLANs across cloud nodes (cross data center firewall)

**Q: What changes will I see in the CenturyLink Cloud Control Portal?**

A: The bandwidth graph on the dashboard page will now show your last 7 days of billable data transfer across all data centers. In addition, because we are constantly calculating bandwidth consumption (versus final aggregation at invoice time with the 95th percentage model), bandwidth charges are included in the current hour / month to date charges shown across the Control Portal.

**Q: Will my invoice look different now?**

A: Slightly. The invoice will now show:

**Description**|**Quantity**|**Unit Cost**|**Total**
---------------|------------|-------------|---------
Bandwidth: GB Transmitted (data center)|100|$0.05|$5.00    
