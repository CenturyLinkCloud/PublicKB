{{{
  "title": "Getting started with Cloudsoft AMP",
  "date": "04/05/2016",
  "author": "Cloudsoft",
  "attachments": [],
  "contentIsHTML": false
}}}

![Cloudsoft logo](../../images/cloudsoft/cloudsoft-logo.jpg)

### Technology Profile

Cloudsoft Application Management Platform (AMP) is software which streamlines the development and operation of applications. AMP orchestrates services, platforms and infrastructures to ensure they directly meet the needs of applications, dynamically and in real time. This results in more reliable operations, productive development and greater agility for IT to respond to their business needs.

### Description

AMP is built on the open-source project [Apache Brooklyn](http://www.cloudsoftcorp.com/community/), with Cloudsoft's commercial support and additional enterprise features.

For more information, please visit http://www.cloudsoftcorp.com/product/.

### Audience

CenturyLink Cloud Users

### Impact

After reading this article, the user will be able to install and use Cloudsoft AMP in the CenturyLink Cloud platform.

### Prerequisites

- Access to the CenturyLink Cloud platform as an authorized user.

- Setup of [Cross Data Center Policies](../../Network/creating-cross-data-center-firewall-policies.md) for all Datacenters AMP will be managing. 

### Postrequisite

If you are deploying from "CenturyLink BluePrints Library" all the prerequisites are configured. There is no need to perform any tasks.


### Deploying the "Ubuntu 14 with AMP Pro 310" Blueprint

#### Steps to Deploy Blueprint

1. **Locate the Ubuntu 14 with AMP Pro 310 Blueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for "AMP" in the keyword search on the right side of the page and filter for "Ubuntu 14 64-bit" Operating System
  3. Locate the 'Ubuntu 14 with AMP Pro 310 Blueprint

2. **Choose and Deploy the Blueprint.**
  Click the ""Ubuntu 14 with AMP Pro 310" Blueprint.

3. **Deploy Ubuntu 14 with AMP Pro 310 Blueprint section**
  1. Specify password
  2. Confirm password
  3. Optionally update Network, Primary and Secondary DNS, Server Type and Server Level.
<img src="../../images/cloudsoft/amp310-customise-1.png">

  4. **Specify the Server Name(s) section**
<img src="../../images/cloudsoft/amp310-customise-server-name.png">

  5. **AMP Pro Install Script on AMPPRO section**
    1. Specify AMP Pro username (default: admin)
    2. Specify AMP Pro Password
    3. Specify CenturyLink Cloud account
    4. Specify CenturyLink Cloud password
    5. Select one or multiple CenturyLink Cloud datacenters
<img src="../../images/cloudsoft/amp310-customise-install-script.png">

4. **Review and Confirm the Blueprint**
  1. Click "next: step 2"
  2. Verify your configuration details.

5. **Deploy the Blueprint**
  1. Once verified, click on the 'deploy blueprint' button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.


### Access your AMP server

After your Blueprint deploys successfully, please follow these instructions to access your server:

1. Click on the link that brings you to the VM that hosts AMP and grab the public IP address of that VM.
<img src="../../images/cloudsoft/amp310-deployment.png"> 
2. Browse to http://publicIpAddress:8080 and use the credentials specified at "AMP Pro Install Script on AMPPRO" section.
3. Start deploying AMP blueprints to the CenturyLink Cloud Datacenters specified above.

### Pricing

The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.

### About Cloudsoft

CenturyLink Cloud works with [Cloudsoft](http://www.cloudsoftcorp.com/) to provide agility and reliability throughout the application lifecycle.

### Frequently Asked Questions

#### Who should I contact for support?

* For issues related to deploying the Cloudsoft Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Cloudsoft Support website](http://support.cloudsoftcorp.com)
* For issues related to cloud infrastructure (VMs, network, etc), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
