{{{
  "title": "Getting Started with Alert Logic Web Security Manager - Partner Template",
  "date": "4-10-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![Alert Logic Logo](http://www.ingaa.org/File.aspx?id=21717)
###Partner Profile
Alert Logic, the leader in security and compliance solutions for the cloud, provides Security-as-a-Service for on-premises, cloud, and hybrid infrastructures, delivering deep security insight and continuous protection for customers at a lower cost than traditional security solutions. Fully managed by a team of experts, the Alert Logic Security-as-a-Service solution provides network, system and web application protection immediately, wherever your IT infrastructure resides. Alert Logic partners with the leading cloud platforms and hosting providers to protect over 3,000 organizations worldwide. Built for cloud scale, our patented platform stores petabytes of data, analyses over 450 million events and identifies over 60,000 security incidents each month, which are managed by our 24x7 Security Operations Center. Alert Logic, founded in 2002, is headquartered in Houston, Texas, with offices in Seattle, Cardiff and London.

http://www.AlertLogic.com

#### Contact AlertLogic
#####Alert Logic Sales and Support:
- Email Support - support@alertlogic.com
- Telephone Support - +1.877.484.8383
- Sales and Marketing - support@alertlogic.com

### Description
Alert Logic has integrated their Web Security Manager technology with the CenturyLink Cloud platform, publishing their virtual appliance as a CenturyLink Cloud Partner Template.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this security solution.

Alert Logic Security-as-a-Service delivery deploys easily in any IT environment - cloud, hosted and/or on-premises infrastructure.  It includes comprehensive security protection, with 52,000+ IDS signature database and new signatures updated weekly, as well as unlimited internal and external vulnerability scanning and meets key requirements in PCI DSS, HIPAA, Sarbanes-Oxley and other compliance regulations.

Alert Logic Web Security Manager helps CenturyLink Cloud customers address the business challengex of compreheisive security, network optimization and website availability by including the following product modules that provide acceleration, scalability and proactive protection of web systems:
* Load Balancer - Enabling scalability and acceleration of even complex SSL-enabled stateful web applications.
* Web Accelerator and Cache - Reducing traffic cost, improving response time and off-loading web servers.
* Web Application Firewall - Proactive protection of web servers and web applications by employing a positive security model providing defenses against all OWASP top ten vulnerabilities.

### Solution Overview
The best way to protect web applications is with a Web Application Firewall, or WAF. WAFs interrogate web traffic in context with how web applications work and identify everything bad, even traffic coming from a known, good source. So why doesn’t everyone have a WAF? Because monitoring, managing and tuning a WAF so it only identifies that bad traffic is hard. That is, until Alert Logic Web Security Manager.

Web Security Manager is a Web Application Firewall that is implemented in the network as a filtering gateway which validates all requests to the web systems. Web Security Manager defends against all OWASP Top Ten vulnerabilities, supports XML web services and provides full PCI DSS Section 6.6 requirements compliance. Additionally, Web Security Manager includes ActiveWatch Services that provide monitoring, tuning and incident response 24×7.

Web Security Manager includes a hardened OS and installs on most standard hardware.  The Web Security Manager software appliance installer turns a piece of general purpose application server hardware into a dedicated application acceleration and security gateway within minutes - with minimal interaction.

The Web Security Manager software appliance combines the flexibility and scalability advantages of software with the security advantages and administrative simplicity from dedicated hardware appliances.

Automated application profiling, adaptive learning, positive and negative filtering and support for XML based web services allow for out of the box protection against attacks from malicious hackers and worms.

As your websites are learned Web Security Manager gradually turns towards a positive, white-list based, policy providing protection against attacks targeting undisclosed vulnerabilities in standard software and custom built applications.

For more information, view the product information on Alert Logic's website: https://www.alertlogic.com/products-services/web-security-manager/

### Offer
Alert Logic is making their Web Security Manager available for CenturyLink Cloud Users to deploy to their account.  In order to purchase a license or entitlement, please contact sales@alertlogic.com

### Audience
CenturyLink Cloud Users

### Impact
Alert Logic has provided a Virtual Appliance - called a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.  After reading this article, the user should feel comfortable deploying the Alert Logic Web Security Manager technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Identify a Network VLAN you want the Alert Logic Web Security Manager to reside on

### Detailed Steps to Deploy Alert Logic Web Security Manager Partner Template
Follow these step by step instructions to deploy a Alert Logic Web Security Manager in to your CenturyLink Cloud account:

- Open a service task request ticket via email to ServiceTasks@Tier3.com with the following details.  You will need to edit some of the information below.

----
TO: ServiceTasks@Tier3.com

EMAIL SUBJECT:   Custom Image Import Request for Ecosystem Partner Template

CLC Support Team,
Please create a ticket to complete the following Service Task:

Please import the Ecosystem Partner Template image file referenced below to my CenturyLink Cloud Account:
- Import CenturyLink Ecosystem Partner Source Image: Alert Logic Web Security Manager
- My CenturyLink Cloud Account Alias: ####
- Data Center to import image to: ###
- Server Name to import image as: ##########
- VLAN in the account to add the Server to: ########

Additional Information to add Partner Template to Network:

- Boot the server up and at the command prompt:
- Login as:  operator / changeme
- Configure the network interface with the following commands:
-   show interfaces
-   show interface eth0
-   set interface eth0 ip [xxx.xxx.xxx.xxx] netmask [xxx.xxx.xxx.xxx]
- Confirm the IP address
-   set gateway [xxx.xxx.xxx.xxx]
-   show gateway
-   system ping 8.8.8.8
- Add a Public IP to the server through Control
- Configure the Public IP firewall rules to allow incoming traffic for TCP ports 80, 443 and 4849

Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the Web Security Manager VM.

Thank you very much, [Your_Name_Here]

-----

### Acessing and Configuring your Alert Logic Web Security Manager
Follow these steps to access your Alert Logic Web Security Manager:

Contact Alert Logic at +1.877.484.8383

### Pricing
The cost associated with this deployment is $195/hr for the CenturyLink Cloud Service Tasks.  There are no Alert Logic license costs or additional fees bundled in.  Service Task Fees are available here: http://www.ctl.io/service-tasks#Pricing

### Frequently Asked Questions
Frequently Asked Questions:
- #### Where do I obtain my Alert Logic License or entitlements?
- Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a Alert Logic license, or contact Alert Logic directly:
-   Contact Alert Logic Support via telephone: +1.877.484.8383
-   Contact Alert Logic via their website: http://www.alertlogic.com
-   Email Sales via sales@alertlogic.com


- #### Who should I contact for support?
* For issues related to Licensing, Accessing or Configuring the deployed software, please visit the Alert Logic Support Website: http://www.AlertLogic.com
* For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.
