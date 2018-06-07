{{{
 "title": "FAQ",
 "date": "06-04-2018",
 "author": "",
 "attachments": [],
 "related-products" : [],
 "contentIsHTML": false
 }}}


**Q**: How much VMware expertise is needed to take advantage of the self-service capabilities of CenturyLink Private Cloud on VMware Cloud Foundation™?

**A**: Customers should have familiarity with the vCloud Director web client.

**Q**: What types of things can I, as the customer, manage from within vCloud Director through CenturyLink Private Cloud on VMware Cloud Foundation?

**A**: With just a minimal amount of familiarity with vCloud Director, you'll be able to scale  environments up and down, provision firewall rules, manage your virtual load balancers, copy entire environments for migration or replication, set up NAT, provision site-to-site or client-to-site VPNs, do SSL offloading, mount CD ROM drives, reboot, and much more.

**Q**: What is a Catalog from the standpoint of VMware?

**A**: A catalog is a container for vApp templates and media files in an organization. Organization administrators and catalog authors can create catalogs in an organization. Catalog contents can be shared with other users in the organization and can also be published to all organizations in the vCloud Director installation.

**Q**: What types of templates will be available?

**A**: You can start with your own templates, which you can upload in the catalog and deploy as you like. Or you can use the base images we will provide.

**Q**: Can I assign different privileges to different users?

**A**: Yes, you can assign different privileges and control access to different catalogs on a user-by-user basis.

**Q** How is migration so seamless with CenturyLink Private Cloud on VMware Cloud Foundation?

**A**: Migrations leverage vCloud Director Extender, where customers configure their VMware environment to point to their CenturyLink Private Cloud on VMware Cloud Foundation endpoint, then move workloads from the target to destination environment.

**Q**: What is vCloud Director Extender?

**A**: With vCloud Director Extender, you can migrate your virtual machines from an on-premise vCenter Server to your CenturyLink Private Cloud on VMware Cloud Foundation environment. You can migrate virtual machines both when they are powered on and powered off depending on the available downtime.

**Q**: How long does it take to get my initial environment up and running?

**A**: Like any private cloud, it will take 6-to-8 weeks to stand-up your CenturyLink Private Cloud on VMware Cloud Foundation stack. But once in place, you can deploy VMs virtually instantly.

**Q**: How is Cloud Application Manager integrated with CenturyLink Private Cloud on VMware Cloud Foundation? How does that benefit me?

**A**: Customers can easily add a CenturyLink Private Cloud on VMware Cloud Foundation Provider within Cloud Application Manager. Once that is done, customers can orchestrate the deployment and management of compute.

**Q**: Can I bring my own VMWare enterprise license(s)?

**A**: No. This is a bundled product with VMware licenses included. If you prefer to bring your own licenses, we recommend Foundation Hosting as an option.

**Q**: Do I have to manage the hypervisor in CenturyLink Private Cloud on VMware Cloud Foundation?

**A**: No. We take care of that for you.

**Q**: Why does CenturyLink Private Cloud on VMware Cloud Foundation require a minimum of four nodes?

**A**: The minimum node configuration to support VSAN is three nodes. We add a fourth node so we can offer "N-plus-2" High Availability. That means we can support two of the base 4 nodes failing and still keep the system up and running.

**Q**: Why is the maximum configuration 64 nodes per cluster?

**A**: vSAN is limited to a maximum of 64 nodes within a single cluster. However, you can have multiple clusters managed by a single vCenter. You'll just interconnect them with the switching fabric to make one happy family.
