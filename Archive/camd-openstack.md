{{{
"title": "Installing Cloud Application Manager Dedicated Edition in OpenStack",
"date": "05-24-2019",
"author": "Diego Sanjuan",
"keywords": ["cam", "cloud application manager", "Data Center edition", "appliance", "deploy", "openstack", "install"],
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [OpenStack Requirements](#openstack-requirements)
* [Video](#video)
* [Steps](#steps)
* [Next Steps](#next-steps)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article explains Cloud Application Manager Dedicated Edition can run as a virtual appliance in your OpenStack private cloud. Here are the requirements, high-level steps, and a video that shows how to install the appliance.

### Audience

All Cloud Application Manager Dedicated Edition users who would like to deploy Cloud Application Manager Dedicated Edition (appliance) using Openstack.

### Prerequisites

* You should have a Data Center with Openstack to be able to deploy appliance using it.

### OpenStack Requirements

Cloud Application Manager requires the following OpenStack services:

* Identity Service (Keystone)
* Compute (Nova)
* Image (Glance)
* Networking (Nova-net or Neutron). This is optional.
* Block storage (Cinder). Optional, unless you want to add volume storage to the Cloud Application Manager appliance VM.

### Video

Follow the video for detailed help.
<iframe src="//player.vimeo.com/video/121204949" width="561" height="316" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen=""></iframe>

### Steps

* Create a flavor with these attributes:
  * 2 VCPUs
  * 2048 MB RAM
  * 100 GB root disk

* Create an image of the appliance. Under Image Location, paste the appliance image download link you got from  [support](mailto:incident@CenturyLink.com). The appliance image is in QCOW2 compressed format.
* Launch an instance of Cloud Application Manager from the appliance image and flavor.

### Next Steps

* [Configure networking](camd-networking.md)
* [Set up the appliance for use](camd-initialsetup.md)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at C:\ProgramData\ElasticBox\Logs\elasticbox-agent.log
