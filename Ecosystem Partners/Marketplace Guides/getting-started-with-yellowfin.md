{{{
  "title": "Yellowfin 7.2 for CenturyLink",
  "date": "12-30-2015",
  "author": "Cadell Falconer",
  "attachments": [],
  "contentIsHTML": false
}}}

![Yellowfin Business Intelligence](../../images/YF_LOGO.png)

### Technology Profile
Yellowfin is a 100% web-based platform ideal for Business Intelligence and analytics in the cloud. Just launch your free trial version of Yellowfin directly from the CenturyLink marketplace and get started in minutes with your free trial that enables 3 users to create and share unlimited reports and dashboards for 12 months. Then upgrade at anytime to seamlessly scale throughout your enterprise.

### Description
Yellowfin is a 100% web-based platform ideal for Business Intelligence and analytics in the cloud. Just launch your free trial version of Yellowfin directly from the CenturyLink marketplace and get started in minutes with your free trial that enables 3 users to create and share unlimited reports and dashboards for 12 months. Then upgrade at anytime to seamlessly scale throughout your enterprise.

For more information, please visit http://www.yellowfinbi.com/.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be able to spin up Yellowfin 7.1 on CenturyLink.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.
* Organizational/Company email address.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
* [Add a Public IP](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal.
* [Allow incoming traffic](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through the Control Portal and configuring appropriately.
  * The default ports to access the application are: `80`, `443`.
* Visit your Public IP address in a web browser.
* Click the "Register to Receive your login details" link and follow the prompts.

### Deploying the Yellowfin 7.2 Template

### How to Deploy the Partner Image
1. Create an email to ServiceTasks@ctl.io.

2. Copy and paste the information below into the body of the email.

3. Edit the information as needed and send.

   ```
  TO: ServiceTasks@ctl.io

  EMAIL SUBJECT:   Ecosystem Partner Template Import Request

  CLC Support Team,

  Please create a ticket to import the Ecosystem Partner Template image referenced below to my CenturyLink Cloud Account:

  - Import CenturyLink Ecosystem Partner Source Image: Yellowfin 7.2 20160701 (from account YFBI)
  - My CenturyLink Cloud Account Alias: ####
  - My CenturyLink Cloud Account PIN:  ######
  - Data Center to import image to: ###
  - Server Name to import image as: ##########
  - VLAN in the account to add the Server to: ########
  - Additional Notes or work to be done: ########

  Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the server where this technology has been deployed.

  Thank you very much,

	   Your_Name_Here
	   ``` 	
Your account alias and PIN are available from your account info page and your user profile page respectively.

### Access your Yellowfin 7.2 server
After your Blueprint deploys successfully, please follow these instructions to access your server.
* [Add a Public IP](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal
* [Allow incoming traffic](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through the Control Portal and configuring appropriately.
   * The default ports to access the application are: `80`, `443`.
* Visit your Public IP address in a web browser.
* Click the "Register to Receive your login details" link and follow the prompts.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. There are no Yellowfin 7.1 for CenturyLink license costs or additional fees bundled in.

### About Yellowfin
CenturyLink Cloud works with [Yellowfin](http://www.yellowfinbi.com/) to provide Yellowfin 7.2, a business Intelligence software package.

### Frequently Asked Questions

#### Who should I contact for support?
* [Yellowfin Forum](http://www.yellowfinbi.com/YFForum.i4).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
