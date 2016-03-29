﻿
{{{
  "title": "Deploying SMS PASSCODE on CenturyLink Cloud",
  "date": "12-30-2015",
  "author": "Max Ranzau",
  "attachments": [],
  "contentIsHTML": false
}}}

![SMSPasscode Logo](../../images/smspasscode_logo.png)

### Technology Profile

SMS PASSCODE – “Experience the New Generation in User Authentication”
- Website: www.smspasscode.com
- Customer Support: support@smspasscode.freshdesk.com
- Phone: 888 440 8456

SMS PASSCODE has integrated their technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this multi-factor authentication solution.
SMS PASSCODE® is a technology leader in adaptive multi-factor authentication using SMS, voice call, or secure e-mail. The solution offers a highly secure challenge- and session-specific login process tightly integrated into leading authentication systems such as Citrix, Cisco, Microsoft, VMware and many other VPN systems. The platform is designed as scalable and fault tolerant from the ground up and offers a much lower TCO compared with alternatives.

Technology from SMS PASSCODE helps CenturyLink Cloud customers address the business challenge of securing remote access by implementing multi-factor authentication - now available as part of the CenturyLink Cloud Blueprint Engine.

For more information, please visit https://www.smspasscode.com

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using SMS PASSCODE on CenturyLink Cloud.

After executing the steps in this Getting Started document, the users will have a functioning SMS PASSCODE Authentication Server upon which they can start securing access for their Citrix, VPN-connections, Windows Login, Remote Desktop and some cloud services etc..

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Windows Server

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80, 443 <this is incorrect, correct to required ports>

### Deploying the SMSPasscode partner Template
### How to Deploy the Partner Image
  1. Create an email to ServiceTasks@ctl.io
  2. Copy and paste the information below into the body of the email
	3. Edit the information as needed and send

```
  TO: ServiceTasks@ctl.io

  EMAIL SUBJECT:   Ecosystem Partner Template Import Request

  CLC Support Team,

  Please create a ticket to import the Ecosystem Partner Template image referenced below to my CenturyLink Cloud Account:

  - Import CenturyLink Ecosystem Partner Source Image: SMS Passcode Base Server Template (from account SMSP)
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


#### Steps to Complete Installation
Once the Template is copied and server is created, complete the following steps to complete the SMS Passcode installation:

  1. Log into the new server, using administrator + password used when server was instantiated.

  2. Close/minimize the server manager, which will be open per default.

  3. From the start menu, launch the SMS PASSCODE configuration tool and browse to the Network tab, change the shared secret (password) to something customer unique (min 15 chars).

The Configuration Tool  <this doesn't seem to make sense>

The shared secret on the Network tab <this doesn't seem to make sense>


  4. On the configuration tool Database tab, change the hostname to the hostname of the new instance (if in doubt, open command prompt, type hostname).

    - Note that if you hit the test button on the database test now, the test will fail, this is okay as the cause is fixed in the next steps.

  5. Launch the web admin interface (http://localhost:2000) and:

  6. Navigate to Hosts > Authentication Hosts > Edit > insert new current hostname here as well.

  7. Navigate to Hosts > Transmitter Hosts > Edit, insert new current hostname here too. You can now re-run the config tool and verify the database test works at this point.

  8. Navigate to Settings > License and paste in the new license number (long hex string) as received from SMS Passcode corp. The console will (depending on issued license) prompt for the following information:
     - "The license key contains one or more new CAL types. You may grant these new CAL types manually, e.g. by mantaining the license grants on your User Group Policies. Or alternatively, you may select the CAL types below, that you would like to grant to all users immediately. Select the CAL types to grant to all users immediately"

  9. Check all options that apply (this will typically be: MFA standard)

From here, there are two additional steps to complete provisioning of a new CenturyLink SMS Passcode setup:

  10.  Configure one or more of the following:
    - Web service dispatchers
    - E-mail dispatchers
    - Hardware SMS Gateways to be able to send out text messsages/voice number calls to mobile devices or e-mails.
    - For setting up a Web Dispatcher with Nexmo, refer to the attached installation guide. <What guide? need a link>

  11.  Install the necessary authentication clients on other servers. These are all documented in detail in the SMS Passcode administrative guide, <need link>

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  SMS PASSCODE Multifactor Authentication is priced on a per user per month basis for the number of users you will be protecting with SMS PASSCODE.  Pricing is $3.50 per user per month regardless of what that user is protecting (including Citrix, VPN, Remote Desktop, Windows Login, etc.) <is it a good idea to put pricing here? what if it changes?>
After deploying this template, the user can secure entitlements to the technology by sending a request via e-mail to: dad@smspasscode.com.

### About SMS PASSCODE
CenturyLink Cloud works with [SMS PASSCODE](https://www.smspasscode.com) to provide a high level of secure access with Multifactor Authentication including session based One Time Passcode delivery via e-mail, text or voice call with the unique ability to differentiate access or code delivery based on geography.

### Frequently Asked Questions

#### Where do I get my License?
* Submit and request by e-mail to dad@smspasscode.com to request a license.

#### Who should I contact for support?

* For issues related to deploying the SMS PASSCODE Template on CenturyLink Cloud, please contact support@smspasscode.com
* For issues related to cloud infrastructure, please open a ticket using the CenturyLink Cloud Support Process.please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
