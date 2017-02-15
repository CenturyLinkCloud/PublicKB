{{{
"title": "Installing the Virtual Appliance in OpenStack",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Installing the Virtual Appliance in OpenStack
ElasticBox can run as a virtual appliance in your OpenStack private cloud in Grizzly or Havana. Here are the requirements, high-level steps, and a video that shows how to install the appliance.

**In this article:**
* OpenStack Requirements
* Installing the Appliance in OpenStack
* Next Steps

### OpenStack Requirements
ElasticBox requires the following OpenStack services:
* Identity Service (Keystone)
* Compute (Nova)
* Image (Glance)
* Networking (Nova-net or Neutron). This is optional.
* Block storage (Cinder). Optional, unless you want to add volume storage to the ElasticBox appliance VM.

### Installing the Appliance in OpenStack
Follow the video for detailed help.
<iframe src="//player.vimeo.com/video/121204949" width="561" height="316" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen=""></iframe>

**Steps**
1. Create a flavor with these attributes:
   * 2 VCPUs
   * 2048 MB RAM
   * 100 GB root disk

2. Create an image of the appliance. Under Image Location, paste the appliance image download link you got from  [support](mailto:support@elasticbox.com). The appliance image is in QCOW2 compressed format.
3. Launch an instance of ElasticBox from the appliance image and flavor.

### Next Steps
* [Configure networking](./appliance-networking.md)
* [Set up the appliance for use](./appliance-initialsetup.md)

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
