{{{
  "title": "Getting Started with Elastic COBOL by Heirloom Computing",
  "date": "09-28-2015",
  "author": "Heirloom Computing",
  "attachments": [],
  "contentIsHTML": false
}}}

![Heirloom Computing Logo](http://heirloomcomputing.com/wp-content/themes/heirloomcomputing/img/logo.png)



### Technology Profile

Heirloom Computing accurately transforms enterprise applications into Java while preserving business logic, thereby reducing cost and providing integration with modern systems. Through patented advanced language transformation and open architecture, Heirloom software complies and translates COBOL to Java in one-step, eliminating complexity and risk without vendor lock-in. The industry-leading development and deployment technology is compatible with internal systems, private, public or hybrid clouds, and Heirloom’s platform-as-a-service. Java programmers are empowered to own, manage and maintain mainframe applications, which reduce the dependency on mainframe skill-sets. Companies can now quickly and safely transforms their enterprise applications with ease and confidence.

### Description

With Elastic COBOL your mainframe applications (including CICS and JCL) execute as Java applications deployed to the Java application server of your choice, on-premise or in the cloud. Applications can continue to be developed in COBOL or in Java or both, enabling the transformation to Java to occur at a pace that is optimal for your business.

For more information, please visit [Heirloom Computing](http://www.heirloomcomputing.com)

### Audience
CenturyLink Cloud Users

Developers wishing to migrate their CICS/COBOL applications to Java

### Impact
After reading this article, the user should be able to start a server running Elastic COBOL Developer, connect to that server using Remote Desktop and begin using the Eclipse based Development environment to convert COBOL code into Java code.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- An Elastic COBOL Developer license from Heirloom Computing. See [Heirloom Computing](http://heirloomcomputing.com) for details.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network over the public internet, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:

  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for the remote desktop port by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default port to access the application through Microsoft Remote Desktop is: 3389

Alternatively, you may add a VPN connection to your installation, and omit adding the public IP address.  This will allow access with the machine being exposed to the external internet.  See: [Adding a VPN connection](../../Network/how-to-configure-client-vpn.md)

### Deploying the Elastic COBOL Developer for Windows Blueprint

#### Steps to Deploy Blueprint
1. **Locate the Elastic COBOL Developer for Windows Blueprint**

  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library
  2. Search for "Elastic" in the keyword search on the right side of the page
  3. Locate the "Elastic COBOL Developer for Windows" Blueprint

2. **Choose and Deploy the Blueprint.**
  1. Click the "Elastic COBOL Developer for Windows" Blueprint.

3. **Customize the Blueprint**
  1. **Provide standard Blueprint details**
      1. Enter an Administrator password
      2. Provide group and network details
      3. Select server type and service level.  A standard server will suffice
      3. Customize the server name as required

  2. **Provide Heirloom License details**
      1. Enter the email address in your Heirloom Computing license file
      2. Enter the subscription id in your Heirloom Computing license file


4. **Review and Confirm the Blueprint**
  1. Click "next: step 2"
  2. Verify your configuration details.

5. **Deploy the Blueprint**
  1. Once verified, click on the "deploy blueprint" button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will start the blueprint deploy process and load a deployment queue page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.


### Access your Elastic COBOL Developer server
After your Blueprint deploys successfully, please follow these instructions to access your server:

  1. Use a remote desktop client to connect to your server
  2. Log in using the Administrator account and the password you provided when customizing the Blueprint
  3. Once you are on the Remote Desktop, use the Elastic COBOL icon on the desktop to start Elastic COBOL Developer

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no license costs or additional fees bundled in. You will need a valid Elastic COBOL Developer license from Heirloom Computing.

### About Heirloom Computing
[Heirloom Computing](http://heirloomcomputing.com) provides patented compiler technology to automatically transform mainframe applications into highly-maintainable Java source-code, with 100% accuracy, while guaranteeing the preservation of existing business logic.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Heirloom Computing Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Heirloom Computing Support website](http://heirloomcomputing.zendesk.com)
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
