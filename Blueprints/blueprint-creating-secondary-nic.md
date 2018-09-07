{{{
  "title": "Adding a Secondary NIC to Servers as Part of a Blueprint",
  "date": "2-17-2016",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

### Challenge
Standard and virtual servers are deployed with a single network interface card (NIC) on a single network VLAN.

Customers can assign any number of IP addresses and aliases to the NIC but they are all on the same network VLAN.  Applications that require layer-2 access to multiple VLANs require secondary NICs.

### Solution
Build a Blueprint and use the script [Utilities - Add secondary NIC on Linux](https://control.ctl.io/Blueprints/Packages/Details?uuid=706865e5-7afb-4cdb-ac35-b200f917758c&classification=Script&type=AccountLibrary) to add additional secondary NICs to your cloud server.

### Usage Notes
* This package cannot currently be executed using the Servers -> Group -> Execute Package framework.
* Script is compatible with all supported Linux distributions.
* Each secondary NIC must be on a different VLAN. There is no pre-execution policy in place that prevents someone from selecting the same VLAN multiple times so make sure to document usage in any follow-up Blueprint deploy guide.
* This package may be included multiple times in your Blueprint to add a total of up to four NICs on any cloud server.
