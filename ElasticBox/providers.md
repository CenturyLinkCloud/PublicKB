{{{
"title": "Providers",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Providers

A provider is a public or private cloud account you register in ElasticBox. ElasticBox interfaces with the provider account’s API to provision and orchestrate deployments automatically. Before you can deploy workloads from ElasticBox, you need to register a provider first. ElasticBox integrates with many popular clouds. Here’s a full list of clouds ElasticBox supports and their availability by Edition:

| Clouds | Developer <br> (SaaS) Free | Developer <br> (Appliance) Free | Enterprise <br> (Saas) | Enterprise <br> (Appliance) |
|-----|:-----:|:-----:|:-----:|:-----:|
| [Century Link Cloud](../ElasticBox/using-centurylink-cloud.md) | | ✓ | ✓ | ✓ |
| [Amazon Web Services](../ElasticBox/using-your-aws-account.md) | ✓ | ✓ | ✓ | ✓ |
| [Google Cloud](../ElasticBox/using-google-cloud.md) | ✓ | ✓ | ✓ | ✓ |
| [Microsoft Azure](../ElasticBox/using-azure.md) | ✓ | ✓ | ✓ | ✓ |
| [VMware vCenter](../ElasticBox/using-the-vmware-vcenter-private-datacenter.md) |  | ✓ | ✓ | ✓ |
| [vCloud Air and vCloud Director](../ElasticBox/orchestrating-vcloud-air-vcloud-director-deployments.md) |  |  | ✓ | ✓ |
| [OpenStack Cloud](../ElasticBox/using-openstack-cloud.md) |  | ✓ | ✓ | ✓ |
| [CloudStack](../ElasticBox/using-cloudstack.md) |  | ✓ | ✓ | ✓ |
| [Rackspace Cloud](../ElasticBox/using-rackspace-cloud.md) |  |  | ✓ | ✓ |
| [SoftLayer](../ElasticBox/using-softlayer.md) |  |  | ✓ | ✓ |
| [AWS GovCloud](../ElasticBox/using-aws-govcloud.md) |  |  | ✓ <br> Available upon request | ✓ <br> Available upon request |

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](../ElasticBox/troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
