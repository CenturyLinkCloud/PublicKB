{{{
"title": "Getting Started with Vormetric DSM - Partner Template",
"date": "6-30-2015",
"author": "Bob Stolzberg",
"attachments": [],
"contentIsHTML": false
}}}

![logo](http://www.vormetric.com/sites/default/files/newsletter-images/vormetric-top-main-logo-2014-0109.jpg)

###Partner Profile
Vormetric provides enterprise encryption and key management services that enable corporations to protect their data.  Vormetric addresses industry compliance mandates and government regulations globally by securing data in physical, virtual and cloud infrastructures, through Data Encryption, Key Management, Access Policies, Privileged User Control, and Security Intelligence.

For more information, visit [http://www.Vormetric.com](http://www.Vormetric.com)

#### Contact Vormetric
##### Vormetric Sales and Support:
- 24x7 Email Support - [support@vormetric.com](mailto:support@vormetric.com)
- 24x7 Telephone Support - (877) 267-3247
- Sales and Marketing - [centurylink@vormetric.com](mailto:centurylink@vormetric.com)

### Description
Vormetric has integrated their Data Security Manager (DSM) technology with the CenturyLink Cloud platform, publishing their virtual appliance as a CenturyLink Cloud Partner Template.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this encryption solution.

Together, Vormetric and CenturyLink deliver data-centric security services that encrypts sensitive customer data and centralizes encryption key management and policy control for data-at-rest encryption, privileged user access control and value security intelligence to meet customer’s business and compliance requirements.

The Data-centric Security-as-a-Service (DSaaS) solution enables IT organizations to efficiently deploy data-centric security across CenturyLink Partner Templates with the Vormetric Transparent Encryption SW agents and the Vormetric Data Security Manager products.  Now, IT security managers can define what files and folders are restricted, who is allowed to view the data, when access is allowed and what operations can be performed by the individual or group.  With the Vormetric data security solution, businesses now reduce their data breach risk, guard against unauthorized data access, meet executive data privacy business requirements and satisfy security compliance regulations that govern your market.

Below is a solution diagram illustrating the Data Security Manager (DSM) deployment options available using the DSM, and also include [Vormetric Agent integrations that can be automatically deployed via CenturyLink Cloud Blueprints](getting-started-with-vormetric-encryption-agent-deployment-blueprints.md).

![DSM topology Diagram](http://www.vormetric.com/sites/default/files/vormetric-data-security-manager-2014-0617.png)

For more information including whitepapers and data sheets, please view the DSM product information on [Vormetric's website](http://www.vormetric.com/products/data-security-manager).

### Solution Overview
The Vormetric Data Security Manager (DSM) is the brain of the Vormetric Data Security Platform. The Vormetric Data Security Manager is a data security appliance which enables centralizes policy control and key management for data-at-rest-encryption, privileged user access control and security intelligence across an organization.  The Data Security Manager changes the data security management game by enabling an IT organization to have a consistent and repeatable method for encrypting, enforcing access policies and gaining security intelligence for all structured and unstructured data. Once the Data Security Manager is in place, new security mandates, compliance requirements and risks are quickly met through the provisioning of Vormetric Transparent Encryption, Vormetric Application Encryption, or managing keys and certificates for 3rd party devices. The result of centralizing control of such a breadth of data-at-rest security capabilities is low total cost of ownership, efficient deployment of new secure services, and an increase in control and visibility of data across your organization.

### Offer
Vormetric has provided a Virtual Appliance - called a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.  Although Service Tasks are ordinarily billed to the end user account, CenturyLink will provide a refund for the Service Task costs associated with deploying the Vormetric Partner Template.  Please follow the process below to request credit. In order to purchase a license or entitlement, please contact Vormetric Sales using the contact information above.

### Audience
- CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable deploying the Vormetric DSM technology on CenturyLink Cloud.  Vormetric has provided a Virtual Appliance - what we call a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.

This deployment process for Partner Templates currently requires manual interaction via the Service Task process, but will be further automated in future releases of the CenturyLink Cloud Platform.

If you are interested in seeing this type of Partner Template deployment as an automated feature in the future, please share your input with us at [features@centurylinkcloud.com](mailto:features@centurylinkcloud.com)

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Identify a Network VLAN you want the Vormetric DSM to reside on

### Postrequisite
- If you want to access your Vormetric DSM over the internet, please perform the following tasks once your Vormetric DSM has been deployed to your account:

1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal

2. If required, [allow incoming traffic for the admin port](../../Network/how-to-add-public-ip-to-virtual-machine.md) by clicking on the Servers Public IP in Control Portal.  Warning: Please make sure your firewall rules are properly configured to only allow specific source traffic.  If you do not configure source traffic rules you risk exposing your DSM to the entire internet.  Note: When accessing your DSM for the first time or for any administration, we recommend you connect to your CenturyLink Cloud environment via Client VPN.

3. Allow incoming traffic for the following ports
  - TCP Ports: 22, 443, 5696, 7024, 8080, 8443, 8444, 8445, 50000
  - UDP Ports: 123, 161, 7025
  - ICMP: All

    ![Open Firewall Port](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)

### Detailed Steps to Deploy Vormetric DSM
Vormetric DSM deploys in a virtual appliance model, as a CenturyLink Cloud *Partner Template*.  Follow these step by step instructions to deploy a Vormetric DSM in to your CenturyLink Cloud account:

* Open a service task request ticket via email to ServiceTasks@Tier3.com with the following details.  `You will need to edit some of the information below.`

----
TO: ServiceTasks@Tier3.com

EMAIL SUBJECT:   Ecosystem Partner Template Import Request

CLC Support Team,

Please create a ticket to import the Ecosystem Partner Template image  referenced below to my CenturyLink Cloud Account:
- Import CenturyLink Ecosystem Partner Source Image: Vormetric DSM
- My CenturyLink Cloud Account Alias: ####
- My CenturyLink Cloud Account PIN:  ######
- Data Center to import image to: ###
- Server Name to import image as: ##########
- VLAN in the account to add the Server to: ########
- Additional Notes or work to be done: None

Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the server where this technology has been deployed.

Thank you very much,

Your_Name_Here

-----

### Accessing and Configuring your Vormetric partner template
Follow these steps to access and configure your Vormetric partner template once you receive an email from Service Tasks confirming the partner template has been deployed to your account.

1. Connect to your DSM's IP address provided by support via SSH and login as cliadmin / Vormetric123$
2. Change your password and configure your DSM based on your requirements.  Please view the support information on [http://www.Vormetric.com](http://www.Vormetric.com) for more information.

### Pricing
There are no Vormetric license costs included.  The cost to deploy the Vormetric Partner Template will be billed as a Service Task, but CenturyLink will provide a credit for those costs.  In order to receive a credit, please follow the instructions below. More information about Service Tasks and fees is [available here](http://www.ctl.io/service-tasks).

#### Process to request credit for Service Task fee
Follow this process to request credit on your account to re-imburse any expense to deploy the Partner Template

* Please copy and paste the email below and send it to [ecosystem@ctl.io](mailto:ecosystem@ctl.io)

----

TO: Ecosystem@CTL.io

EMAIL SUBJECT:   Requesting Credit for Vormetric Partner Template Deployment

CLC Ecosystem Team,

I am requesting a credit be placed on my account to cover the fees associated with deploying the Vormetric Partner Template to my account under the Service Task deployed on MM/DD/YYYY.  My CenturyLink Cloud username or account alias the credit needs to be placed on is ######

Thank you very much, your_name_here

----

### Frequently Asked Questions

#### Where do I obtain my Vormetric License or entitlements?
Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a Vormetric license, or contact Vormetric directly:
-   Contact Vormetric Support via telephone: (877) 267-3247
-   Contact Vormetric via their website: [http://www.Vormetric.com](http://www.Vormetric.com)
-   Email Sales via [centurylinkvormetric.com](mailto:centurylink@vormetric.com)

#### Who should I contact for support?
* For issues regarding the Vormetric DSM virtual appliance, please contact Vormetric via their Support Website: [http://www.Vormetric.com](http://www.Vormetric.com)
* For issues related to cloud infrastructure (VM’s, network, etc), or is you experience a problem deploying the Blueprint, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new)

#### What is the performance impact of Vormetric encryption?
Vormetric customers typically report no perceptible impact to the end-user experience. In almost every case, the impact of encryption overhead is minimal so IT teams can continue to meet their SLAs. In a benchmark conducted with Intel, Vormetric Transparent Encryption demonstrated under 2% performance overhead at 70% system utilization.

#### How difficult is it to deploy Vormetric?
With Vormetric Transparent Encryption, securing data is easy.  Unlike other encryption offerings, this product enables security teams to implement encryption, without having to make changes to their organization’s applications, infrastructure, or business practices. Plus, Vormetric Data Security Manager offers centralized, highly efficient policy and key administration.

#### What operating systems are supported?
Vormetric solutions provide support for a broad range of operating systems, including Microsoft Windows, Linux, Solaris, IBM AIX and HP-UX.

#### What deployment models are supported?
Through the platform’s centralized policy and key management, customers can efficiently address security policies and compliance mandates across databases, files and big data nodes – whether they’re located in the cloud (or in virtual or traditional) infrastructures.
