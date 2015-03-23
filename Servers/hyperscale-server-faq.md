{{{
  "title": "Hyperscale Server FAQ",
  "date": "03-19-2015",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description
The CenturyLink Cloud now offers **Hyperscale Servers** with premium performance targeted at big data jobs and distributed systems.

**Q: What are the maximum resource limits of a Hyperscale Server?**

A: Today, Hyperscale servers can use up to 16 vCPUs, 128GB of memory, and 1 TB of SSD storage.</p>

**Q: How does a Hyperscale Server differ from a "regular" one?**

A: Hyperscale Virtual Servers differ from Standard Virtual Servers in 4 ways:

* Storage: Hyperscale storage is 100% SSD, instead of a mix of spindle/SSD. Consequently, users can expect different storage levels between Hyperscale and CenturyLink Cloud servers.
* Backups: Hyperscale servers do not include the automatic backup function found in CenturyLink Cloud Servers. This is largely because Hyperscale is designed for distributed apps that don’t typically deal with backups.
* Advanced Tasks: Snapshots, Clone, Convert to Template and Archive features are not available on Hyperscale Instances.
* Geographies: Hyperscale is only available in the SG1, NY1, IL1, CA3, GB3, UC1 & VA1 datacenters, with new locations coming online quarterly. Cloud servers, in contrast, can be deployed across 13 federated data centers

**Q: Can I interact with and manage Hyperscale Servers the same as with regular servers?**

A: Yes, except for the cases noted in the answer above.

**Q: What is the best workload for this new server class?**

A: Three workloads are suited for Hyperscale: 1) Web-scale architectures, powered by NoSQL technologies, 2) Big Data jobs running Hadoop or similar technology, 3) web applications where high performance is required.

**Q: What should I NOT run on a Hyperscale Server?**

A: Any workload where redundant storage architecture is needed; also, workloads where sever snapshots are required.

**Q: Since these servers use local storage, how do I avoid application failure if underlying hardware fails?**

A: Anti-affinity policies make it possible to spread workloads across physical hosts. When a new server is created and references an anti-affinity policy, the CenturyLink Cloud platform makes sure that all the servers in that policy are distributed.

**Q: Does Hyperscale support automatic vMotion?**

A: No, Hyperscale does not support automatic vMotion because it uses 100% local storage.

**Q: Will I see Hyperscale Servers called out separately on my invoice?**

A: Yes – Hyperscale servers will be called out as such on your monthly invoice.

**Q: Can I use the v1 SOAP or HTTP API to interact with Hyperscale Servers?**

A: For now, just for some functions. For example, metadata about each Hyperscale server can be accessed via Group API calls. You may use the v2 API, however, to interact with Hyperscale Servers programatically.
