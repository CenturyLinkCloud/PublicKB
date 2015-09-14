{{{
  "title": "Using Cloud Services without Console Access",
  "date": "09-15-2015",
  "author": "Jared Ruckle",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Audience

IT Operations

### CenturyLink Cloud does not offer console access to cloud servers. So now what?

Some IT pros may be accustomed to managing environments with this capability. Here are a few ideas and strategies to help system administrators build and maintain environments without it.
 
* **Follow proper change management for VM modifications as well as for the applications inside them.** Use [snapshots when a roll-back of VM “state” is desired](../Servers/creating-and-managing-server-snapshots.md). NOTE: this only works for VMs with less than 1 TB of storage.

* **Virtual machines, by definition, are not indestructible.** Accordingly, build services and applications such that they can be easily deployed (and re-deployed) on new VMs. From there, admins can then place the new VM back into a service rotation. [Blueprints](../Blueprints/how-to-build-a-blueprint.md) are a great way to load software onto a single VM, or a group of them.

* **Treat VMs as "parts" that simply can be replaced outside of the end user purview.** Users should never even know that VMs are getting swapped in and out. [Load balancers](../Network/load-balancing-comparison-matrix.md), [database clustering](../Servers/configuring-high-availability-on-microsoft-sql-server-databases.md), and cloud-native application architectures (running on [AppFog](../AppFog/getting-started-with-appfog.md)) are services and approaches to consider.

* **For mission critical services, always have a QA environment available for testing.** Here, developers can validate changes against a code base without touching production servers. Use automated tools that can re-build a QA environment quickly when OS-level corruption occurs in test VMs.  CenturyLink Cloud offers [Blueprints](../Blueprints/blueprints-best-practices.md), [SDKs](https://www.ctl.io/developers/sdks-tools), and [APIs](../Servers/using-the-api-to-create-and-then-manage-a-server.md) to help quickly re-build infrastructure environments. Our cloud services also support configuration management tools like [Chef](../Ecosystem Partners/Marketplace Guides/getting-started-with-chef-server-blueprint.md) and [Puppet](..../Ecosystem Partners/Marketplace Guides/getting-started-with-puppet-agent.md), which can also be used to quickly build out new environments.

* **Operate “above the operating system”.** CenturyLink Cloud offers several services that manage the OS for administrators – AppFog, [PivotalCF](../Ecosystem Partners/Marketplace Guides/getting-started-with-pivotal-cloud-foundry.md), and [Orchestrate](https://orchestrate.io/) are just a few. In all of these scenarios, the service is available for consumption according to an SLA, and OS-level issues are not the user’s concern.
