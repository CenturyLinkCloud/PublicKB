{{{
  "title": "Getting Started with A10 vThunder Appliance - Partner Template",
  "date": "3-18-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](http://www.a10networks.com/images/logo_s.png)
###Partner Profile
A10 Networks - An industry leader in data security and cloud security solutions.

http://www.A10Networks.com

#### Contact A10
#####A10 Sales and Support:
- Email Support - support@a10networks.com
- Web Support - http://www.a10networks.com/support/
- Telephone Support - For US Support please call(888) 822-7210.  For  international support please call (408) 325-8676
- US Sales and Marketing - For US Sales please contact pwidman@a10networks.com or call (770) 289-7245
- International Sales and Marketing - For International Sales please contact sales@a10networks.com or call (408)-325-8616

### Description

A10 has pioneered a new generation of application networking technologies. Our solutions enable enterprises, service providers, Web giants and government organizations to accelerate, secure and optimize the performance of their data center applications and networks. Our Advanced Core Operating System (ACOS®) platform is designed to deliver substantially greater performance and security relative to prior generation application networking products. Our software-based ACOS architecture provides the flexibility that enables us to expand our business with additional products to solve a growing array of networking and security challenges across cloud computing and mobility. A10 Networks has a portfolio of application-layer networking products that assure user-to-application connectivity is available, accelerated and secure.

http://www.a10networks.com

### Solution Overview
A10 has integrated their vThunder virtual appliance with the CenturyLink Cloud to provide users with maximum flexibility. vThunder virtual appliances are available for both application delivery controller (ADC) and carrier grade networking (CGN) product lines. With vThunder virtual appliances you gain a flexible and easy-to-deploy appliance featuring advanced services for any enterprises, web giant or service provider, on demand.

The vThunder ADC provides advanced L4-7 ADC services (including security) and server load balancing (SLB). The vThunder CGN provides IPv4 scaling with carrier grade NAT (CGNAT) and IPv6 migration capabilities.

For more information, view the product information on A10's website: http://www.a10networks.com/products/vThunder.php

### Offer
A10 is making their vThunder Appliance available for CenturyLink Cloud Users to deploy to their account.  In order to purchase a license or entitlement, please contact A10 Sales using the contact information above.

### Audience
CenturyLink Cloud Users

### Impact
A10 has provided a Virtual Appliance - called a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.  After reading this article, the user should feel comfortable deploying the A10 vThunder Appliance technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Create a Network VLAN you want the A10 vThunder Appliance to reside on.  Creating a new VLAN follows best practices so users can secure the private VIPs with firewalls.

### Postrequisite
- If you want to access your A10 vThunder Appliance over the internet, please perform the following tasks once your A10 vThunder Appliance has been deployed to your account:

1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal

2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal

### Detailed Steps to Deploy A10 vThunder Appliance Partner Template
Follow these step by step instructions to deploy a A10 vThunder Appliance in to your CenturyLink Cloud account:

- Open a service task request ticket via email to ServiceTasks@Tier3.com with the following details.  You will need to edit some of the information below.

----
TO: ServiceTasks@Tier3.com

EMAIL SUBJECT:   Custom Image Import Request for Ecosystem Partner Template

CLC Support Team,
Please create a ticket to complete the following Service Task:

Please import the Ecosystem Partner Template image file referenced below to my CenturyLink Cloud Account:
- Import CenturyLink Ecosystem Partner Source Image: “vThunder-2.7.2-P4-single-interface-v2.ova”
- My CenturyLink Cloud Account Alias: ####
- Data Center to import image to: ###
- Server Name to import image as: ##########
- VLAN in the account to add the Server to: ########
- Number of VIP's you'd like reserved in the network for load balancing.  (The support team can reserve more later via a ticket.  CLC Support team will reserve 10 VIPs unless stated otherwise.)

Additional Information to add Partner Template to Network:
- Please reference the A10 documentation and follow the steps below;
- During the initial install, the first interface will be used for both management and data. Please request "black hole" VLANs for interfaces 2 and 3 for the system to work correctly. This requirement will be removed in the future as vThunder is tailored for CenturyLink's Cloud.
- Boot the server up and at the command prompt:
- Login as:  admin / 10
- Enter privileged mode by running: "enable" (Just hit enter when prompted for a password)
- Enter ethernet 1 configuration area by running: "interface ethernet 1"
- Assign an IP to ethernet 1 by running: "ip address <ip> <mask>"
- Exit ethernet 1 configuration area by running: "exit"
- Add a default route by running:    "ip route 0.0.0.0 /0 <gateway>"
- Change the admin password by running: "admin admin password <password>"
(Yes, there's 2 "admin", the first is the "admin" command, the 2nd is to configure the user admin)
- Set the hostname by running: "hostname <hostname>"
- Save the configuration by running: "write memory"

- Navigate to http://<YOURVIRTUALAPPLIANCEIPADDRESS> in your web browser to confirm it is on the network

Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the vThunder Appliance VM.

Thank you very much, Your_Name_Here

-----

### Accessing and Configuring your A10 vThunder Appliance
Once the Service Task team deploy's your A10 vThunder Appliance, you will get a notification with details on your new devices.  This list will include:
- The server name of the vThunder Appliance: IL1BOSTA10LB01 for example
- The Management IP of the A10 vThunders(s):  In this example the IP is 10.100.97.100
- The RNAT IP of the A10 vThunder:  In this example the RNAT IP is 10.100.97.101
- Username & Password to perform administration of your new appliances
- The list of VIP's reserved for the A10 vThunder:  In this example the reserved pool is 10.100.97.103-113

- Refer to the email from Service Tasks with the IP address, and then navigate to http://<YOURTHREATMANAGERIPADDRESS> via a web browser from a server on the same VLAN. Alternatively, if you want to connect via internet, you'll need to add a Public IP and then connect via web browser.
- Enter your appliance hostname and unique registration key into the Appliance Name and Registration Key fields
- Click Register Appliance button
- For additional information on how to configure your A10 vThunder Appliance, please visit the support website at http:///www.A10Networks.com/support/

### Pricing
There are no A10 license costs or additional fees bundled in.  The cost to deploy the A10 vThunder Partner Template will be billed as a Service Task.  More information about Service Tasks and fees are available here: http://www.ctl.io/service-tasks

### Frequently Asked Questions
Frequently Asked Questions:
- #### Where do I obtain my A10 License or entitlements?
- You can contact A10 directly using the information below.  Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a A10 license.
-   US Sales and Marketing - For US Sales please contact pwidman@a10networks.com or call (770) 289-7245
-   International Sales and Marketing - For International Sales please contact sales@a10networks.com or call (408)-325-8616

- #### Who should I contact for support?
- For issues regarding the vThunder appliance, please contact A10 Networks Support:
-   Web http://www.a10networks.com/support/
-   Email support@a10networks.com
-   Telephone: (888) 822-7210 or or international (408) 325-8676
- For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.
