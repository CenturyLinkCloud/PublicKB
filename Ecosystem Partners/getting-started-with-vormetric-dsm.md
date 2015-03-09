{{{
"title": "Getting Started with Vormetric DSM - Partner Template",
"date": "2-24-2015",
"author": "Bob Stolzberg",
"attachments": [],
"contentIsHTML": false
}}}

![logo](http://www.vormetric.com/sites/default/files/newsletter-images/vormetric-top-main-logo-2014-0109.jpg)
###Partner Profile

Vormetric provides enterprise encryption and key management services that enable corporations to protect their data.  Vormetric addresses industry compliance mandates and government regulations globally by securing data in physical, virtual and cloud infrastructures, through Data Encryption, Key Management, Access Policies, Privileged User Control, and Security Intelligence.

http://www.Vormetric.com

#### Contact Vormetric
#####Vormetric Sales and Support:
- 24x7 Email Support - support@vormetric.com
- 24x7 Telephone Support - (877) 267-3247
- Sales and Marketing - support@vormetric.com

### Description

Vormetric has integrated their Data Security Manager (DSM) technology with the CenturyLink Cloud platform, publishing their virtual appliance as a CenturyLink Cloud Partner Template.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this encryption solution.

The Vormetric Data Security Manager is a data security appliance which enables centralizes policy control and key management for data-at-rest-encryption, privileged user access control and security intelligence across an organization.

![dsm.png](http://www.vormetric.com/sites/default/files/vormetric-data-security-manager-2014-0617.png)

For more information including whitepapers and data sheets, please view the DSM product information on Vormetric's website: http://www.vormetric.com/products/data-security-manager

### Solution Overview

The Vormetric Data Security Manager (DSM) is the brain of the Vormetric Data Security Platform. The Data Security Manager changes the data security management game by enabling an IT organization to have a consistent and repeatable method for encrypting, enforcing access policies and gaining security intelligence for all structured and unstructured data. Once the Data Security Manager is in place, new security mandates, compliance requirements and risks are quickly met through the provisioning of Vormetric Transparent Encryption, Vormetric Application Encryption, or managing keys and certificates for 3rd party devices. The result of centralizing control of such a breadth of data-at-rest security capabilities is low total cost of ownership, efficient deployment of new secure services, and an increase in control and visibility of data across your organization.

### Offer
Vormetric is making their DSM available for CenturyLink Cloud Users to deploy to their account.  In order to purchase a license or entitlement, please contact support@vormetic.com


### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable deploying the Vormetric DSM technology on CenturyLink Cloud.  Vormetric has provided a Virtual Appliance - what we call a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.  

This deployment process for Partner Templates currently requires manual interaction via the Service Task process, but will be further automated in future releases of the CenturyLink Cloud Platform.


### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Identify a Network VLAN you want the Vormetric DSM to reside on

### Postrequisite
- If you want to access your Vormetric DSM over the internet, please perform the following tasks once your Vormetric DSM has been deployed to your account:
1. Adding an external ip-address to an existing or new CenturyLink server

    ![ip.jpg](https://t3n.zendesk.com/attachments/token/kObGC9P2IjP1ate0NexwFNiXz/?name=ip.jpg)

2. Allow incoming traffic for the following ports
- TCP Ports: 22, 443, 5696, 7024, 8080, 8443, 8444, 8445, 50000
- UDP Ports: 123, 161, 7025
- ICMP: All

    ![port.jpg](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)

### Detailed Steps to Deploy Vormetric DSM
Vormetric DSM deploys in a virtual appliance model, as a CenturyLink Cloud *Partner Template*.  Follow these step by step instructions to deploy a Vormetric DSM in to your CenturyLink Cloud account:  
1. Open a service task request ticket via email to ServiceTasks@Tier3.com with the following details.  You will need to edit some of the information below.

----
>TO: ServiceTasks@Tier3.com
>
EMAIL SUBJECT:   Ecosystem Partner Template Import Request
>
CLC Support Team,
Please create a ticket to import the Ecosystem Partner Template image  referenced below to my CenturyLink Cloud Account:
- Import CenturyLink Ecosystem Partner Source Image: Vormetric DSM
- My CenturyLink Cloud Account Alias: ####
- Data Center to import image to: ###
- Server Name to import image as: ##########
- VLAN in the account to add the Server to: ########
- Additional Notes or work to be done: None
>
Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the server where this technology has been deployed.
>
Thank you very much,
>
Your_Name_Here

-----

If you are interested in seeing this type of Partner Template deployment as an automated feature in the future, please share your input with us at [features@centurylinkcloud.com](mailto:features@centurylinkcloud.com)

### Pricing
The costs associated with this deployment is $390 one-time fee in accordance with the CenturyLink Cloud Service Tasks.  There are no Vormetric license costs or additional fees bundled in.  Service Task Fees information is available here: http://www.centurylinkcloud.com/service-tasks

### Frequently Asked Questions

#### Where do I obtain my Vormetric License or entitlements?
Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a Vormetric license, or contact Vormetric directly:
-   Contact Vormetric Support via telephone: (877) 267-3247
-   Contact Vormetric via their website: http://www.Vormetric.com
-   Email Sales via support@vormetric.com

#### Who should I contact for support?
* For issues related to deploying the Centerity Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the Centerity Support Website: http://www.Vormetric.com
* For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.