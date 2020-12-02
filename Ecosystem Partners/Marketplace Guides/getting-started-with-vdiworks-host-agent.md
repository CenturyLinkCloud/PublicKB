{{{
  "title": "Getting Started With VDIworks VDP Host Agent",
  "date": "08-10-2015",
  "author": "VDIworks",
  "attachments": [],
  "contentIsHTML": false
}}}

![VDIworks logo](../../images/VDIworkls_color_logo_smallerl.png)

### Technology Profile
VDP is an end to end VDI management system. Combining connection brokering, VM management, health, alerting, inventory, physical management, and remote protocols.

### Description
This Lumen Blueprint provides a click-through solution to install and configure the VDIworks VDP Host Agent on the Windows Server platform.

For more information, please visit [http://www.vdiworks.com/](http://www.vdiworks.com).
To get in contact with sales representative please email [sales@vdiworks.com](mailto:sales@vdiworks.com).

### Audience
Lumen Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Blueprint technology on Lumen Cloud.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.

### Postrequisite
* If you want to access your application over the internet, please perform the following tasks after you receive an email notifying you that the Blueprint completed successfully.

* If you need to connect to your server via the Internet, [Add a Public IP](../../Network/Lumen Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal.

* [Allow incoming traffic](../../Network/Lumen Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through the Control Portal and configuring appropriately.
   * Ports needed for Public Access: RDP `3389`, TCP&UDP `8004`, `6502`.

* Alternatively, you can use the Lumen Cloud VPN that is available through the Control Portal.  

### Deploying VDIworks VDP Host Agent
VDP Host Agent is available as a Blueprint for deployment on a new server.

#### Steps to deploy VDIworks Host Agent
1. Locate and Select the VDIworks VDP Host Agent Blueprint and Deploy.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for 'VDIworks VDP' in the keyword search on the right side of the page.
   * Locate the 'VDIworks VDP HostAgent 351' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the 'Install VDIworks VDP Host Agent' Blueprint.

3. Configure the Blueprint.
   Complete the information below:

   * Enter a Password for the Server and repeat to confirm.
   * Select a Group for your server, e.g., Default Group.
   * Select a Network.
   * Select a Primary DNS, e.g., Manually Specify.
   * Select a Secondary DNS, e.g., Manually Specify.
   * Select a Server Type, e.g., Standard.
   * Select a Service Level.
   * Create a Server Name.
   * Create a VNC Password.

4. Review Blueprint and Deploy.

### Access VDIworks VDP Host Agent
 After your Blueprint Deploys successfully, please follow these instructions to access your server.

1. Watch email for notification of deployment completion.  

2. Log in to your server.

3. Start the VDIworks VDP Console and login using your Server Account.

### Pricing
For pricing information please contact us through [http://www.vdiworks.com/contact-vdiworks/](http://www.vdiworks.com/contact-vdiworks/)
To get in contact with sales representative please email [sales@vdiworks.com](mailto:sales@vdiworks.com)

### About VDIWorks
Headquartered in Austin, Texas and founded in 2007, VDIworks is a leading provider of Virtual Desktop enablement and management software. Our solution is built on 10 years of pioneering work in the fields of centralized computing and virtualization. Our innovation has been recognized with 6 awarded and over 12 pending patents thus far. We offer the ultimate flexibility and preserves customer choice by giving customers the ability to deploy the right solution for the right user type, utilize any back-end hardware, end-point user access device or virtualization technology for desktop virtualization.

One of the industry's most reputable benchmarks of segment leadership, Computer Reseller News (CRN) has included VDIworks in their Top 100 Virtualization Vendors for several consecutive years and again most recently in the top 50 in 2013.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the VDIworks Blueprint on Lumen Cloud, licensing or accessing the deployed software, please visit the [VDIworks website](http://www.vdiworks.com/) or email [support@vdiworks.com](mailto:support@vdiworks.com).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).
