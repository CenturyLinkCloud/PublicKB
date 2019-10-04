{{{
"title": "Cloud Application Manager Data Center Edition Overview",
"date": "05-24-2019",
"author": "Diego Sanjuan",
"keywords": ["cam", "cloud application manager", "Data Center edition", "appliance", "overview", "platforms"],
"sticky": true,
"attachments": [],
"contentIsHTML": false
}}}


**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Supported Platforms](#supported-platforms)
* [Steps](#steps)
* [Next Steps](#next-steps)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)


### Overview


This article explains how to run Cloud Application Manager on-premise as a virtual appliance in your vCenter Data Center or OpenStack cloud. After you install and [set up Cloud Application Manager Data Center Edition](camdce-initialsetup.md) for use, you’re ready to automate deployments to any cloud and platform.

**Try the Appliance for Free**
The appliance is available as a free download.

**Download the Cloud Application Manager Virtual Appliance**
Request a download link from [support](mailto:incident@CenturyLink.com).

Experience all the same functionality as SaaS version, except for advanced features like managed services anyware or cloud optimization, and use Cloud Application Manager Data Center Edition to deploy to private clouds.


### Audience


All Cloud Application Manager Data Center Edition users who wants to deploy/install Cloud Application Manager Data Center Edition (appliance).


### Prerequisites


* You should have a Data Center or AWS account to be able to deploy appliance in your preffered platform.


### Supported Platforms


Appliance is supported when deployed on these platforms:
* [Installing Cloud Application Manager Data Center Edition in vCenter](camdce-vsphere.md)
* [Installing Cloud Application Manager Data Center Edition in Openstack](camdce-openstack.md)
* [Installing Cloud Application Manager Data Center Edition in AWS](camdce-with-aws-master-account.md)


### Next Steps


* [Setting Up Cloud Application Manager Data Center Edition](camdce-initialsetup.md)
* [Configuring Network Settings of Cloud Application Manager Data Center Edition](camdce-networking.md)
* [Upgrading Cloud Application Manager Data Center Edition](camdce-upgrading.md)
* [Cloud Application Manager Data Center Edition Migration](camdce-migration.md)


### Contacting Cloud Application Manager Support


We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at C:\ProgramData\ElasticBox\Logs\elasticbox-agent.log
