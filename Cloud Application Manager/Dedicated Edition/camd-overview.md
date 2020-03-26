{{{
"title": "Cloud Application Manager Dedicated Edition Overview",
"date": "03-25-2020",
"author": "Diego Sanjuan and Guillermo Sanchez",
"keywords": ["cam", "cloud application manager", "Data Center edition", "appliance", "overview", "platforms", "dedicated", "cam-d"],
"sticky": true,
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Supported Platforms](#supported-platforms)
* [Installing Cloud Application Manager Dedicated Edition](#installing-cloud-application-manager-dedicated-edition)
* [Next Steps](#next-steps)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article explains how to run Cloud Application Manager platform on-premise as a virtual appliance in your CenturyLink Private Cloud on VMware Cloud Foundation (CPC on VCF), VMWare data center or OpenStack cloud. After you install and [set up Cloud Application Manager Dedicated Edition](camd-initialsetup.md) for use, you’re ready to automate deployments to any cloud and platform.

**Download the Cloud Application Manager Virtual Appliance**
Request a download link from [support](mailto:incident@CenturyLink.com).

Experience all the same functionality as the SaaS version, including managed services anywhere, except for some advanced features like cloud optimization. Use Cloud Application Manager Dedicated Edition to deploy either on private or public clouds.

### Audience

All Cloud Application Manager Dedicated Edition users who wants to deploy/install Cloud Application Manager Dedicated Edition (appliance).

### Prerequisites

* You should have a Data Center or AWS account to be able to deploy appliance in your preffered platform.

### Supported Platforms

Cloud Application Manager Dedicated edition is supported when deployed on these platforms:

* CenturyLink Private Cloud on VMware Cloud Foundation (CPC on VCF)
* VMware vSphere vCenter or Cloud Foundation data centers
* OpenStack
* AWS

### Installing Cloud Application Manager Dedicated Edition

For specific considerations on each platform, please refer to the corresponding link:

* [Installing Cloud Application Manager Dedicated Edition in vCenter](camd-vsphere.md)
* [Installing Cloud Application Manager Dedicated Edition in Openstack](camd-openstack.md)
* [Installing Cloud Application Manager Dedicated Edition in AWS](camd-with-aws-master-account.md)

### Next Steps

* [Setting Up Cloud Application Manager Dedicated Edition](camd-initialsetup.md)
* [Configuring Network Settings of Cloud Application Manager Dedicated Edition](camd-networking.md)
* [Upgrading Cloud Application Manager Dedicated Edition](camd-upgrading.md)
* [Cloud Application Manager Dedicated Edition Migration](camd-migration.md)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at C:\ProgramData\ElasticBox\Logs\elasticbox-agent.log
