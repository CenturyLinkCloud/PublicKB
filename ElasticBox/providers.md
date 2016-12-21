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
| [Century Link Cloud](https://elasticbox.com/documentation/deploying-and-managing-instances/using-centurylink/) | | ✓ | ✓ | ✓ |
| [Amazon Web Services](https://elasticbox.com/documentation/deploying-and-managing-instances/using-your-aws-account/) | ✓ | ✓ | ✓ | ✓ |
| [Google Cloud](https://elasticbox.com/documentation/deploying-and-managing-instances/using-your-google-cloud-account/) | ✓ | ✓ | ✓ | ✓ |
| [Microsoft Azure](https://elasticbox.com/documentation/deploying-and-managing-instances/using-azure/) | ✓ | ✓ | ✓ | ✓ |
| [VMware vCenter](https://elasticbox.com/documentation/deploying-and-managing-instances/using-the-vsphere-private-datacenter/) |  | ✓ | ✓ | ✓ |
| [vCloud Air and vCloud Director](https://elasticbox.com/documentation/deploying-and-managing-instances/vcloudair-director/) |  |  | ✓ | ✓ |
| [OpenStack Cloud](https://elasticbox.com/documentation/deploying-and-managing-instances/using-the-openstack-cloud/) |  | ✓ | ✓ | ✓ |
| [CloudStack](https://elasticbox.com/documentation/deploying-and-managing-instances/using-cloudstack/) |  | ✓ | ✓ | ✓ |
| [Rackspace Cloud](https://elasticbox.com/documentation/deploying-and-managing-instances/using-rackspacecloud/) |  |  | ✓ | ✓ |
| [SoftLayer](https://elasticbox.com/documentation/deploying-and-managing-instances/using-softlayer/) |  |  | ✓ | ✓ |
| [AWS GovCloud](https://elasticbox.com/documentation/deploying-and-managing-instances/using-awsgovcloud/) |  |  | ✓ <br> Available upon request | ✓ <br> Available upon request |

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](https://www.ctl.io/elasticbox/). Please review the [troubleshooting tips](https://elasticbox.com/documentation/troubleshooting/troubleshooting-tips/), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
