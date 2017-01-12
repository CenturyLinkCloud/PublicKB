{{{
"title": "ElasticBox Editions",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### ElasticBox Editions

ElasticBox comes in two flavors, the Developer Edition, which is free and the Enterprise Edition. While the free Developer Edition is good to try out ElasticBox and a lot of the features, you get advanced functionality with the Enterprise Edition. To learn about Developer Edition limits and how it differs from the Enterprise Edition, see editions.

**Why Get Enterprise Edition?**

With the Enterprise Edition, you get an organization of unlimited users with differing access levels to build, deploy, and manage applications collaboratively. You also get administrative level reporting and monitoring capabilities.

Specifically, the Enterprise Edition exclusively offers several cool features.

* Use ElasticBox as a SaaS platform or as a virtual appliance in your private cloud.
* In addition to public clouds, deploy in private clouds like [vSphere](./using-the-vmware-vcenter-private-datacenter.md), [OpenStack](./using-the-openstack-cloud.md), and [CloudStack](./using-cloudstack.md).
* Get [sharing and collaboration features](./workspaces-and-collaboration.md) to let users share providers, boxes, and instances with each other as they work on applications in shared workspaces.
* [Administer ElasticBox](./admin-overview.md) to complement your IT application management workflows. Manage all users and assets centrally, and monitor and report on resource usage.
* Manage deployments org-wide through [tagging](./resource-tags.md), [webhooks](./webhooks.md) that integrate with custom IPAM or CMDB solutions, or [admin boxes](./admin-boxes.md) that let you make sure deployments consistently comply with company policies.

**Upgrade to Enterprise Edition**
In order to benefit from all the powerful features in ElasticBox, we recommend upgrading to the Enterprise Edition. For more information, [contact sales](mailto:support@elasticbox.com).

If you’re running the Developer Edition as an [appliance](./appliance-overview.md), you can directly upgrade from the product following these steps:

**Steps**

* Sign in to ElasticBox by browsing to the appliance virtual machine IP address in vCenter.
* In your workspace, from the top right corner menu drop-down, select **Upgrade to Enterprise**.
* In the form, click contact sales.

This sends an email to our sales team who will contact you to create an ElasticBox organization based on your email domain and convert your account to the Enterprise Edition.

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
