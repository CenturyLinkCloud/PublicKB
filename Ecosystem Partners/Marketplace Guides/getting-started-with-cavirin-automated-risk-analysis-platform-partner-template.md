{{{
"title": "Getting Started with Cavirin Automated Risk Anaylysis Platform - Partner Template",
"date": "6-30-2015",
"author": "<a href='https://www.linkedin.com/in/bstolzberg'>Bob Stolzberg</a>",
"attachments": [],
"contentIsHTML": false
}}}

![logo](../../images/Ecosystem-Cavirin-ARAP_logo_full-color_200px.png)

###Partner Profile
Cavirin - Delivering Continuous Audit and Operational Compliance to the Cloud

For additional information about the company please visit [http://www.cavirin.com](http://www.cavirin.com)

#### Contact Cavirin
##### Cavirin Sales and Support:
- 24x7 Web Support - [https://support.cavirin.com](https://support.cavirin.com)
- 24x7 Email Support - [support@cavirin.com](mailto:support@cavirin.com)
- Sales Telephone Support - Please email [Tim Thompson, tthompson@cavirin.com](mailto:tthompson@cavirin.com) or via telephone: (469) 831-8357

### Description
Cavirin has integrated their technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this compliance and regulatory governance solution.

Cavirin gives you visibility across your entire IT ecosystem. It supports the broadest range of devices and vendors on the market, so nothing escapes notice. It searches out outdated and unpatched servers—the number-one culprit implicated in major IT security breaches. It checks your firewall and OS configurations against best practices and regulatory policies. But it doesn’t stop there. Cavirin also monitors your accounts—ensuring tight access control, strict password and lockout policies, and unused accounts.

Technology from Cavirin helps CenturyLink Cloud customers address the business challenge of compliance and regulatory governance for their entire IT environment by providing continuous discovery and device review.  Now available as part of the CenturyLink Cloud Blueprint Engine.

It's easy!  Think of Cavirin as your operational GRC tool in the cloud.

### Solution Overview
Cavirin is a security and compliance solution expressly designed for cloud AND data center environments-the ultimate hybrid cloud solution.  Cavirin provides a range of compliance guidelines, expressly designed to measure and monitor risk associated with these compliance guidelines (PCI, HIPAA, ISO, NIST, SOC 2, CIS, and/or DISA STIGs) that are applied to your environment.  In addition to OS-level checks, Cavirin can also evaluates application-specific CIS guidelines, such as those for Microsoft IIS, Internet Explorer, SQL Server, Firefox, Oracle, and MySQL.  Lastly, we are an extremely viable solution for File Integrity Monitoring for your hybrid cloud as well.

Cavirin is designed to assist security and compliance teams who face regulatory audits, and greatly reduces the manual effort in audit preparation, execution and maintenance in perpetuity.  A key benefit of Cavirin is that it is platform-independent, and was designed to reach and support a wide range of platforms.

### Offer
Cavirin has provided their Automated Risk Analysis Platform virtual appliance - called a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.  Although Service Tasks are ordinarily billed to the end user account, CenturyLink will provide a refund for the Service Task costs associated with deploying the Cavirin Partner Template.  Cavirin is sold on a per device basis and broken into tiers.  We also have trial licenses available upon request.  To receive pricing for your environment and/or receive a trial license please contact Cavirin sales: [Tim Thompson, tthompson@cavirin.com](mailto:tthompson@cavirin.com) or via telephone: (469) 831-8357.

### Audience
- CenturyLink Cloud Users

### Impact
After executing the steps in this Getting Started document, the users will have a functioning Cavirin Automated Risk Analysis Platform (ARAP) upon which they can start developing discovery solutions.

Customers can access the Cavirin Help Center by going to [https://support.cavirin.com](https://support.cavirin.com) to access articles and how-to videos.

This deployment process for Partner Templates currently requires manual interaction via the Service Task process, but will be further automated in future releases of the CenturyLink Cloud Platform.

If you are interested in seeing this type of Partner Template deployment as an automated feature in the future, please share your input with us at [features@centurylinkcloud.com](mailto:features@centurylinkcloud.com)

### Prerequisite
1.  Access to the CenturyLink Cloud platform as an authorized user.
2.  Identify a Network VLAN you want the Cavirin partner template to reside on
3.  A Cavirin ARAP License.  You will need to send this to CenturyLink Support at the time of deployment.
4.    The Cavirin ARAP server will utilize the following resources.  Note: larger environments may require additional processors to allow for speed of discovery.
  *    8GB RAM
  *    2 Processors
  *    100GB disk space (can be thin provisioned)
  *    line of sight network access to devices in scope
5.    The following protocols are used for discovery
  * ICMP
  * SNMP
  * SSH
  * WMI / Windows Remote Management (WinRM)
6.    To access Windows machines you will need Administrator credentials.
7.    To access Linux machines you will need root level credentials, a PEM key file can also be used for access.
8.    If you would like to access systems outside the immediate network then there must routable access to that network either through a router or vpn.
9.    Please refer to [https://support.cavirin.com](https://support.cavirin.com) to find any additional prerequisites required for your deployment

### Postrequisite
- If you want to access your Cavirin partner template over the internet, please perform the following tasks once your VM has been deployed to your account:

1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal

2. If required, [allow incoming traffic for the admin port](../../Network/how-to-add-public-ip-to-virtual-machine.md) by clicking on the Servers Public IP in Control Portal.  Warning: Please make sure your firewall rules are properly configured to only allow specific source traffic.  If you do not configure source traffic rules you risk exposing your VM to the entire internet.  Note: When accessing your VM for the first time or for any administration, we recommend you connect to your CenturyLink Cloud environment via Client VPN.

### Detailed Steps to Deploy Cavirin Automated Risk Anaylysis Platform
The Cavirin partner template deploys in a virtual appliance model, as a CenturyLink Cloud *Partner Template*.  Follow these step by step instructions to deploy a Cavirin partner template in to your CenturyLink Cloud account:

* Open a service task request ticket via email to [ServiceTasks@Tier3.com](mailto:ServiceTasks@Tier3.com) with the following details.  `You will need to edit some of the information below and attach your Cavirin license to the email!`

----
TO: ServiceTasks@Tier3.com

EMAIL SUBJECT:   Ecosystem Partner Template Import Request

CLC Support Team,

Please create a ticket to import the Ecosystem Partner Template image  referenced below to my CenturyLink Cloud Account:

- Import CenturyLink Ecosystem Partner Source Image: Cavirin OVA
- My CenturyLink Cloud Account Alias: ####
- My CenturyLink Cloud Account PIN:  ######
- Data Center to import image to: ###
- Server Name to import image as: ##########
- VLAN in the account to add the Server to: ########
- Additional Notes or work to be done: Attached to this email is my Cavirin License that you'll need during setup

Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the server where this technology has been deployed.

Thank you very much,

Your_Name_Here

-----

### Pricing
There are no Cavirin license costs included.  The cost to deploy the Cavirin Partner Template will be billed as a Service Task, but CenturyLink will provide a credit for those costs.  In order to receive a credit, please follow the instructions below. More information about Service Tasks and fees is [available here](http://www.ctl.io/service-tasks).

#### Process to request credit for Service Task fee
Follow this process to request credit on your account to re-imburse any expense to deploy the Partner Template

* Please copy and paste the email below and send it to [ecosystem@ctl.io](mailto:ecosystem@ctl.io)

----

TO: Ecosystem@CTL.io

EMAIL SUBJECT:   Requesting Credit for Cavirin Partner Template Deployment

CLC Ecosystem Team,

I am requesting a credit be placed on my account to cover the fees associated with deploying the Cavirin Partner Template to my account under the Service Task deployed on MM/DD/YYYY.  My CenturyLink Cloud username or account alias the credit needs to be placed on is ######

Thank you very much, your_name_here

----

### Accessing and Configuring your Cavirin partner template
Follow these steps to access and configure your Cavirin partner template:
1.    Using a web broweser, Go to https://server_ip_address  (This can be the private IP if you are connected via VPN, or a Public IP if you added one and opened the proper firewall rules)
2.    Log in with newly created administrator account
3.    Once logged in you start creating discovery profiles to scan your devices.
4.    Refer to [http://support.cavirin.com](http://support.cavirin.com) for additional how-to information, a user account will be required, please contact [support@cavirin.com](mailto:support@cavirin.com) to request access.

### Frequently Asked Questions

#### Where do I obtain my Cavirin License or entitlements?
Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a Cavirin license, or contact Cavirin directly: Please email [Tim Thompson, tthompson@cavirin.com](mailto:tthompson@cavirin.com) or via telephone: (469) 831-8357

#### Who should I contact for support?
* For issues regarding the Cavirin appliance, the application or functionality of it, please contact Cavirin via their 24x7 Web Support: [https://support.cavirin.com](https://support.cavirin.com), or via Email Support: [support@cavirin.com](mailto:support@cavirin.com)
* For issues related to cloud infrastructure (VM’s, network, etc), or is you experience a problem deploying the Blueprint, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new)
