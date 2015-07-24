{{{
  "title": "Getting Started with Alert Logic Threat Manager - Partner Template",
  "date": "4-10-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![Alert Logic Logo](http://www.ingaa.org/File.aspx?id=21717)
###Partner Profile
Alert Logic, the leader in security and compliance solutions for the cloud, provides Security-as-a-Service for on-premises, cloud, and hybrid infrastructures, delivering deep security insight and continuous protection for customers at a lower cost than traditional security solutions. Fully managed by a team of experts, the Alert Logic Security-as-a-Service solution provides network, system and web application protection immediately, wherever your IT infrastructure resides. Alert Logic partners with the leading cloud platforms and hosting providers to protect over 3,000 organizations worldwide. Built for cloud scale, our patented platform stores petabytes of data, analyses over 450 million events and identifies over 60,000 security incidents each month, which are managed by our 24x7 Security Operations Center. Alert Logic, founded in 2002, is headquartered in Houston, Texas, with offices in Seattle, Cardiff and London.

http://www.AlertLogic.com

#### Contact Alert Logic
#####Alert Logic Sales and Support:
- Email Support - support@alertlogic.com
- Telephone Support - +1.877.484.8383
- Sales and Marketing - support@alertlogic.com

### Description
Alert Logic has integrated their Threat Manager technology with the CenturyLink Cloud platform, publishing their virtual appliance as a CenturyLink Cloud Partner Template.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this security solution.

Alert Logic Security-as-a-Service delivery deploys easily in any IT environment - cloud, hosted and/or on-premises infrastructure.  It includes comprehensive security protection, with 52,000+ IDS signature database and new signatures updated weekly, as well as unlimited internal and external vulnerability scanning and meets key requirements in PCI DSS, HIPAA, Sarbanes-Oxley and other compliance regulations.

Threat Manager from Alert Logic helps CenturyLink Cloud customers address the business challenge of compreheisive security and compliance by implementing industry recognized, leading security solutions.

### Solution Overview
Alert Logic Threat Manager with ActiveWatch services provides 24×7 threat detection monitored by experts in Alert Logic’s Security Operations Center (SOC) for your entire IT environment. Driven by global threat data and research, Threat Manager detects suspicious activity and scans your network to identify vulnerabilities before an intrusion occurs.

For more information, view the product information on AlertLogic's website: https://www.alertlogic.com/products-services/threat-manager/

### Offer
Alert Logic is making their Threat Manager available for CenturyLink Cloud Users to deploy to their account.  In order to purchase a license or entitlement, please contact sales@alertlogic.com

### Audience
CenturyLink Cloud Users

### Impact
Alert Logic has provided a Virtual Appliance - called a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.  After reading this article, the user should feel comfortable deploying the Alert Logic Threat Manager technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Identify a Network VLAN you want the Alert Logic Threat Manager to reside on

### Postrequisite
- If you want to access your Alert Logic Threat Manager over the internet, please perform the following tasks once your Alert Logic Threat Manager has been deployed to your account:

1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control

2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for ports 80 and 443 to access the Alert Logic Web Console by clicking on the Servers Public IP through Control Portal

### Detailed Steps to Deploy Alert Logic Threat Manager Partner Template
Follow these step by step instructions to deploy a Alert Logic Threat Manager in to your CenturyLink Cloud account:

- Open a service task request ticket via email to ServiceTasks@Tier3.com with the following details.  You will need to edit some of the information below.

----
TO: ServiceTasks@Tier3.com

EMAIL SUBJECT:   Custom Image Import Request for Ecosystem Partner Template

CLC Support Team,
Please create a ticket to complete the following Service Task:

Please import the Ecosystem Partner Template image file referenced below to my CenturyLink Cloud Account:
- Import CenturyLink Ecosystem Partner Source Image: Alert Logic Threat Manager
- My CenturyLink Cloud Account Alias: ####
- Data Center to import image to: ###
- Server Name to import image as: ##########
- VLAN in the account to add the Server to: ########

Additional Information to add Partner Template to Network:
- Please reference the Alert Logic documentation and follow the steps below; http://docs.alertlogic.com/#docs/install_and_configure/alert_logic_threat_manager/install_alert_logic_tm_in_a_private_cloud/installvafortmprivate.htm

1. Boot the server up and at the command prompt:
2. Login as:  setup / 7739521
3. On the Alert Logic config screen, select 4.
4. Confirm the IP address
5. On the Alert Logic config screen, select 1.
6. On the Network Configuration Screen, enter the appropriate address, gateway, and netmask.
7. On the Alert Logic config screen, select 2.
8. When asked to restart networking, select Yes.
9. On the Alert Logic config screen, select 4.
10. Confirm the IP address.
11. On the Alert Logic config screen, select 5.
12. On the Ping an IP address screen, enter the IP address you want to ping.
13. Confirm the data output.
14. On the Alert Logic config screen, select 6.
15. Navigate to http://<YOURVIRTUALAPPLIANCEIPADDRESS> in your web browser to confirm it is on the network.

Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the Threat Manager VM.

Thank you very much, Your_Name_Here

-----

### Accessing and Configuring your Alert Logic Threat Manager
Follow these steps to access your Alert Logic Threat Manager:

- Refer to the email from Service Tasks with the IP address, and then navigate to http://<YOURTHREATMANAGERIPADDRESS> via a web browser from a server on the same VLAN. Alternatively, if you want to connect via internet, you'll need to add a Public IP and then connect via web browser.
- Enter your appliance hostname and unique registration key into the Appliance Name and Registration Key fields
- Click Claim appliance
- For additional information on how to configure your Alert Logic Threat Manager, please visit the support website at http:///www.AlertLogic.com

### Pricing
There are no Alert Logic license costs or additional fees bundled in. The cost to deploy the Alert Logic Threat Manager Partner Template will be billed as a Service Task. More information about Service Tasks and fees are available here: http://www.ctl.io/service-tasks

### Frequently Asked Questions
Frequently Asked Questions:
- #### Where do I obtain my Alert Logic License or entitlements?
- Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a Alert Logic license, or contact Alert Logic directly:
-   Contact Alert Logic Support via telephone: +1.877.484.8383
-   Contact Alert Logic via their website: http://www.AlertLogic.com
-   Email Sales via support@alertlogic.com

- #### Who should I contact for support?
* For issues related to Licensing, Accessing or Configuring the deployed software, please visit the Alert Logic Support Website: http://www.AlertLogic.com
* For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.
