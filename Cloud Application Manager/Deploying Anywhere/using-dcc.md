{{{
"title": "Using CenturyLink DCC",
"date": "12-17-2019",
"author": "Guillermo Sánchez",
"attachments": [],
"keywords": ["cam", "cloud application manager", "dcc", "dedicated cloud compute", "provider"],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Creating a CenturyLink DCC provider](#creating-a-centurylink-dcc-provider)
* [Editing Policy Boxes on CenturyLink DCC](#editing-policy-boxes-on-centurylink-dcc)
* [Deploying Instances from Deployment Policies](#deploying-instances-from-deployment-policies)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article is meant to assist users of Cloud Application Manager to learn how to use a CenturyLink DCC (Dedicated Cloud Compute) provider.

### Audience

All Cloud Application Manager users who want to integrate with an existing CenturyLink DCC environment.

### Prerequisites

* You must have a Cloud Application Manager Account
* Your user credentials for the CenturyLink DCC environment.

### Creating a CenturyLink DCC provider

Select CenturyLink DCC from the Provider list and enter a username and password to logon to the CenturyLink DCC Portal.

> The user must have "customer purchase permission" and an associated billing account in CenturyLink DCC to operate in the Cloud Application Manager.
>
> If this is not the case, open a ticket [here](https://savvisstation.savvis.com) to get it fixed.

![New CenturyLink DCC provider](../../images/cloud-application-manager/deploying-anywhere/dcc/centurylink-dcc-add-provider-credentials.png)

Once the provider information is saved, Cloud Application Manager starts synchronizing the Provider account. After the synchronization is complete, Cloud Application Manager creates default Deployment Policies with the different deployment options available.

![CenturyLink DCC sample policy boxes](../../images/cloud-application-manager/deploying-anywhere/dcc/centurylink-dcc-example-policy-boxes.png)

The user account used when creating the Provider is linked to a Company, Billing Site, Clusters, Domains, etc.

When the synchronization process finishes, the list of Linux and Windows Templates available to deploy on each cluster is available on the provider's "Configuration" tab.

![CenturyLink DCC Configuration tab OS Catalog list](../../images/cloud-application-manager/deploying-anywhere/dcc/centurylink-dcc-template-list.png)

### Editing Policy Boxes on CenturyLink DCC

In addition to the services list, Cloud Application Manager creates sample Policy Boxes for Linux and Windows. These can be customized anytime.

![Edit DCC policy box](../../images/cloud-application-manager/deploying-anywhere/dcc/centurylink-dcc-policy-box-edit.png)

To do this, access the details by selecting "Code", then "Edit", where the following options are available:

#### Order

![Order section of deployment policy](../../images/cloud-application-manager/deployment-policy/centurylink-dcc-order.png)

| Option | Description |
|--------|-------------|
| Company | Select the company of your DDC provider. |
| Billing Site | Select the billing site of your DDC provider. |
| Datacenter | Clusters are grouped in [Datacenters](../../General/CenturyLinkCloud/centurylink-cloud-data-center-locations.md). To select a Cluster, Cloud Application Manager needs to know the Datacenter the Cluster belongs to. |
| Cluster | Select the cluster where you want to deploy. |
| Domain | Select the domain where you want to deploy. |

#### Resource

![Resourse section of deployment policy](../../images/cloud-application-manager/deployment-policy/centurylink-dcc-resource.png)

| Option | Description |
|--------|-------------|
| Machine configuration | Select the profile of the machine. |
| OS | Select from a list of CenturyLink DCC Linux or Windows images. |
| Language | Select the languaje of instance. |
| Instances | Cloud Application Manager can deploy several servers at once, with the restriction that all the operations run on all the instances (start, stop, delete, and script boxes installation). |
| VCPU | Select the number of CPUs. |
| VRAM | Select the amount of memory assigned to the Virtual Machine. |
| Storage | Select the disk group to use. |

#### Network

![Network section of deployment policy](../../images/cloud-application-manager/deployment-policy/centurylink-dcc-network.png)

| Option | Description |
|--------|-------------|
| Network | The net segment where the VM is configured. Please note that the IP address is set automatically. The user must select a segment with available IP addresses. |

#### Proxy

![Proxy section of deployment policy](../../images/cloud-application-manager/deployment-policy/centurylink-dcc-proxy.png)

| Option | Description |
|--------|-------------|
| Host | The hostname or domain of the proxy that the agent will use to connect back to Cloud Application Manager, once it has been installed in the deployed instance. |
| Port | The port of the proxy that the agent will use to connect back to Cloud Application Manager, once it has been installed in the deployed instance. |

### Deploying Instances from Deployment Policies

Virtual machines get deployed on clusters. If Cloud Application Manager doesn't have enough information to deploy a cluster, the cluster will not be available as a deployment option for the Policy Boxes. In that case, Cloud Application Manager displays an alert in the provider activity logs as follows.

![CenturyLink DCC provider activity log with cluster alert](../../images/cloud-application-manager/centurylink-cluster-error-alert.png)

Once the Box deploys, Cloud Application Manager shows the traces of what is happening with the provider. At the end of the process it displays a script that has to be executed manually on the newly created Virtual Machine to complete the ALM agent installation.

![centurylink-dcc-deployment-traces.png](../../images/cloud-application-manager/deploying-anywhere/dcc/centurylink-dcc-deployment-traces.png)

Credentials for the Virtual Machine are sent via email which contains the necessary privileges to install the Cloud Application Manager agent using the script shown above.

> To run this script, the user needs access to the new Virtual Machines. This task, as in the creation of the account, needs to be done by CenturyLink DCC.

Once this is done, the deployment process is complete.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a error registering an instance, share the instance to a workspace that your organization and Cloud Application Manager support group can access and attach the logs.

* Linux: SSH into the instance and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at \ProgramData\ElasticBox\Logs\elasticbox-agent.log
