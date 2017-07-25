{{{
  "title": "Dedicated Cloud Compute Storage and Failover",
  "date": "05-11-2017",
  "author": "",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Storage for Dedicated Cloud Compute Instances

No storage for the Dedicated Cloud Compute Instances is available via the Utility/Unified Storage service unless the customer purchases such storage separately to provide storage for Dedicated Cloud Compute Instances. Information on the Utility/Unified Storage service is contained within the Utility or Unified Storage Services sections of the Service Guide.

### Dedicated Cloud Compute Instance Failover Service

For customers that purchase more than one Dedicated Cloud Compute Node in a failover group, should a hardware failover occur with a Dedicated Cloud Compute Node, the Dedicated Cloud Compute Instances will automatically be restarted and distributed across the other available nodes within the failover group. Failover groups can be configured with up to 16 Dedicated Cloud Compute Nodes. Instances on a node can only fail over to other nodes within the defined failover group. Once the failed node is restored and confirmed as stable by CenturyLink Operations, instances may be redistributed across the nodes. The instance redistribution is automated via the Dedicated Cloud Compute Dynamic Instance Balancing capability. The speed of the failover is a function of available resources on the remaining nodes within the failover group.
