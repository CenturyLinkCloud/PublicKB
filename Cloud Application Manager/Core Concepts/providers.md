{{{
"title": "Providers",
"date": "06-16-2017",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Providers

A provider is a public or private cloud account you register in Cloud Application Manager. Cloud Application Manager interfaces with the provider account’s API to provision and orchestrate deployments automatically. Before you can deploy workloads from Cloud Application Manager, you need to register a provider first. Cloud Application Manager integrates with many popular clouds. Here’s a full list of clouds Cloud Application Manager supports and their availability by Edition:

| Clouds | Enterprise <br> (Saas) | Enterprise <br> (Appliance) |
|-----|:-----:|:-----:|
| [CenturyLink Cloud](../Deploying Anywhere/using-centurylink-cloud.md) | ✓ | ✓ |
| [CenturyLink DCC](../Deploying Anywhere/using-dcc.md) | ✓ | ✓ |
| [CenturyLink DCC Foundation](../../Dedicated Cloud Compute/DCC Foundation/dcc-foundation-in-cloud-application-manager.md) | ✓ | ✓ |
| [Amazon Web Services](../Deploying Anywhere/using-your-aws-account.md) | ✓ | ✓ |
| [Google Cloud](../Deploying Anywhere/using-google-cloud.md) | ✓ | ✓ |
| [Microsoft Azure](../Deploying Anywhere/using-azure.md) | ✓ | ✓ |
| [VMware vCenter](../Deploying Anywhere/using-the-vmware-vcenter-private-datacenter.md) | ✓ | ✓ |
| [vCloud Air and vCloud Director](../Deploying Anywhere/orchestrating-vcloud-air-vcloud-director-deployments.md) | ✓ | ✓ |
| [OpenStack Cloud](../Deploying Anywhere/using-openstack-cloud.md) | ✓ | ✓ |
| [CloudStack](../Deploying Anywhere/using-cloudstack.md) | ✓ | ✓ |
| [Rackspace Cloud](../Deploying Anywhere/using-rackspace-cloud.md) | ✓ | ✓ |
| [SoftLayer](../Deploying Anywhere/using-softlayer.md) | ✓ | ✓ |
| [AWS GovCloud](../Deploying Anywhere/using-aws-govcloud.md) | ✓ <br> Available upon request | ✓ <br> Available upon request |

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:cloudsupport@centurylink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
