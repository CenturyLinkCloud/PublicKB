{{{
 "title": "DCC Foundation FAQs",
 "date": "06-29-2017",
 "author": "",
 "attachments": [],
 "related-products" : [],
 "contentIsHTML": false
 }}}


**Q**: How much VMware expertise is needed to take advantage of the self-service capabilities of DCC Foundation?

**A**: Customers should have familiarity with the vCloud Director web client.

**Q**: What types of things can I, as the customer, manage from within vCloud Director on DCC Foundation?

**A**: With just a minimal amount of familiarity with vCloud Director, you'll be able to scale  environments up and down, provision firewall rules, manage your virtual load balancers, copy entire environments for migration or replication, set up NAT, provision site-to-site or client-to-site VPNs, do SSL offloading, mount CD ROM drives, reboot, and much more.

**Q**: What is a "catalog," from the standpoint of VMware?

**A**: A catalog is a container for vApp templates and media files in an organization. Organization administrators and catalog authors can create catalogs in an organization. Catalog contents can be shared with other users in the organization and can also be published to all organizations in the vCloud Director installation.

**Q**: What types of templates will be available?

**A**: You can start with your own templates, which you can upload in the catalog and deploy as you like. Or you can use a base vanilla image we will provide.

**Q**: Can I assign different privileges to different users?

**A**: Yes, you can assign different privileges and control access to different catalogs on a user-by-user basis.

**Q**: What is vCloud Availability?

**A**: vCloud Availability for vCloud Director makes it easy for service providers to run a disaster-recovery-as-a-service (DRaaS) offering that is natively compatible with the end customer’s vSphere environment.

**Q**: How long does it take to get my initial DCC Foundation environment up and running?

**A**: Like any private cloud, it will take 6-to-8 weeks to stand-up your DCC Foundation stack. But once in place, you can deploy VMs virtually instantly.

**Q**: Is vCAV (vCloud Availability) free to use?

**A**: Yes, it's free to us for migration and replication. But it can also be used for disaster recovery. For that, there is a licensing fee that is paid to VMware, but it is less than you would pay for SRM.

**Q** How is migration so seamless with DCC Foundation?

**A**: Migrations will leverage vCloud Availability, where customers configure their VMware environment to point to their DCC Foundation endpoint, then move workloads from the target to destination environment.

**Q**: How is Cloud Application Manager integrated with DCC Foundation? How does that benefit me?

**A**: Customers can easily add a DCC Foundation Provider within Cloud Application Manager. Once that is done, customers can orchestrate the deployment and management of compute.

**Q**: Can I bring my own VMWare enterprise license(s)?

**A**: No. This is a bundled product with VMware licenses included. If you prefer to bring your own licenses, we recommend Foundation Hosting as an option.

**Q**: Do I have to manage the hypervisor in DCC Foundation?

**A**: No. We take care of that for you.

**Q**: Why does DCC Foundation require a minimum of four nodes?

**A**: The minimum node configuration to support VSAN is three nodes. We add a fourth node so we can offer "N-plus-2" High Availability. That means we can support two of the base 4 nodes failing and still keep the system up and running.

**Q**: Why is the maximum configuration for DCC Foundation 32 nodes per cluster?

**A**: vSAN is limited to a maximum of 32 nodes within a single cluster. However, you can have multiple clusters managed by a single vCenter. You'll just interconnect them with the switching fabric to make one happy family.
