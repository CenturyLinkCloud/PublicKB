{{{
  "title": "Hyperscale Server FAQ",
  "date": "9-15-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3><strong>Description</strong></h3>
<p>The CenturyLink Cloud now offers&nbsp;<strong>Hyperscale Servers</strong> with premium performance targeted at big data jobs and distributed systems.</p>

<p><strong>Q: What are the maximum resource limits of a Hyperscale Server?</strong>
</p>
<p>A: Today, Hyperscale servers can use up to 16 vCPUs, 128GB of memory, and 1 TB of SSD storage.</p>

<p><strong>Q: How does a Hyperscale Server differ from a "regular" one?</strong>
</p>
<p>A: Five ways:</p>
<ul>
  <li><em>Storage.</em>&nbsp; Hyperscale storage is 100% SSD, instead of a mix of spindle/SSD.&nbsp; Consequently, users can expect different storage levels between Hyperscale and CenturyLink Cloud servers.</li>
  <li><em>Backups.</em> Hyperscale servers do not include the automatic backup function found in CenturyLink Cloud Servers.&nbsp; This is largely because Hyperscale is designed for distributed apps that don’t typically deal with backups.</li>
  <li><em>Advanced Tasks. &nbsp;</em>Snapshots, Clone, Convert to Template and Archive features are not available on Hyperscale Instances</li>
  <li><em>Geographies.</em>&nbsp; Hyperscale is only available in the NY1, IL1, CA3, GB3, UC1 &amp; VA1 datacenters, with new locations coming online quarterly.&nbsp; Cloud servers, in contrast, can be deployed across 12 federated data centers.&nbsp;</li>
  <li><em>API parity is unavailable for Hyperscale at launch. </em>Full API compatibility will be in place in coming releases.</li>
</ul>

<p><strong>Q: Can I interact with and manage Hyperscale Servers the same as with regular servers?</strong>
</p>
<p>A: Yes, except for the cases noted in the answer above.</p>

<p><strong>Q: What is the best workload for this new server class?</strong>
</p>
<p>A: Three workloads are suited for Hyperscale: 1) Web-scale architectures, powered by NoSQL technologies, 2) Big Data jobs running Hadoop or similar technology, 3) web applications where high performance is required.</p>

<p><strong>Q: What should I NOT run on a Hyperscale Server?</strong>
</p>
<p>A: Any workload where redundant storage architecture is needed; also, workloads where sever snapshots are required.</p>

<p><strong>Q: Since these servers use local storage, how do I avoid application failure if underlying hardware fails?</strong>
</p>
<p>A: Anti-affinity policies make it possible to spread workloads across physical hosts. When a new server is created and references an anti-affinity policy, the CenturyLink Cloud platform makes sure that all the servers in that policy are distributed. &nbsp;</p>

<p><strong>Q: Will I see Hyperscale Servers called out separately on my invoice?</strong>
</p>
<p>A: Yes – Hyperscale servers will be called out as such on your monthly invoice.</p>

<p><strong>Q: Can I use the v1 SOAP or HTTP API to interact with Hyperscale Servers?</strong>
</p>
<p>A: For now, just for some functions, for example, metadata about each Hyperscale server can be accessed via Group API calls.&nbsp; Full API parity will be achieved in the coming months.</p>