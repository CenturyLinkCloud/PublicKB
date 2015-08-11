{{{
  "title": "Getting Started with Cohesive Networks VNS3 - Partner Template",
  "date": "3-26-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![Cohesive Networks logo](https://cohesive.net/wp-content/uploads/2015/01/cohesive-networks-logo.gif)

###Partner Profile
Cohesive Networks is a cloud-native network and security company. Over 1,000 customer use our VNS3 network routing and security products to connect, integrate and secure their critical applications in any cloud. VNS3 is a family of award-winning software-only appliances available in public, private and hybrid clouds.

Cohesive is a member of the Open Data Center Alliance (ODCA), a member of the Amazon Partner Network, an Amazon Marketplace Seller, Microsoft Azure certified, a Google Cloud Platform Authorized Technology Partner, certified HP Helion Ready, an IBM Business Partner and member of the CenturyLink Cloud Marketplace Program.

https://www.cohesive.net

#### Contact Cohesive Networks
#####Cohesive Networks Sales and Support:
- Sales and licensing - sales@cohesive.net
- Email Support - support@cohesive.net
- Web Support - http://support.cohesive.net
- Telephone Support available with enhnaced technical support. Visit https://cohesive.net/support/support-plans for details and pricing.

### Description
Cohesive Networks has integrated their technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this network security and access solution.

VNS3 lets you manage your cloud deployment with your data center resources as if running locally. A VNS3 network can be distributed across multiple public and private clouds to create one logical group of federated resource. VNS3 doesn't require new knowledge or training to implement, so you can integrate with existing network equipment.

Technology from Cohesive Networks helps CenturyLink Cloud customers address the business challenge of secure connectivity by implementing numerous core network/security solutions in to one appliance.

Easily connect to your existing datacenter edges using industry standard IPsec and SSL VPN - now available as part of the CenturyLink Cloud Blueprint Engine.

### Solution Overview
VNS3 is a networking and security virtual appliance that lets you extend networks into public, private and hybrid clouds. The core network functions of switch, router, firewall, VPN gateway for SSL and IPsec VPNs and protocol redistributor can all be configured through an API or the web based user interface.

The Cohesive Networks VNS3 solution also provides a Docker subsystem that can run container based network application services such as proxy, reverse proxy, SSL/TLS termination, load balancing, content cache, network intrusion detection (NIDS) and web application firewall (WAF).

### Offer
Cohesive Networks has provided a Virtual Appliance - called a Partner Template - that can be deployed to your CenturyLink Cloud account via a Service Task.  Although Service Tasks are ordinarily billed to the end user account, CenturyLink will provide a refund for the Service Task costs associated with deploying the Cohesive Partner Template.  Please follow the process below to request credit. In order to purchase a license or entitlement, please contact Cohesive Networks Sales using the contact information above.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable deploying the Cohesive Networks VNS3 virtual appliance technology on CenturyLink Cloud.

After executing the steps in this Getting Started document, the users will have a functioning VNS3 network/security appliance upon which they can start developing secure connectivity solutions.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Create a Network VLAN you want the Cohesive Networks VNS3 virtual appliance to reside on.  Creating a new VLAN follows best practices so users can secure the private VIPs with firewalls. Important:  Once you create a new VLAN, or if you use an existing VLAN, through the Control Portal navigate to Networks and then click on the specific VLAN you want to use.  Note down a free IP address, the network mask and the gateway address from the VLAN as these will be used when deploying the VNS3 manager appliance.
- Configure a Client VPN so that you can securely connect to the VNS3 virtual appliance for configuration.  When accessing your CohesiveFT VNS3 virtual appliance for the first time, we recommend you connect to your CenturyLink Cloud environment via secure Client VPN.    For more information on configuring your Client VPN, please see the "how to configure client vpn" knowledge base article.
- Ensure you have the proper firewall rule settings to allow VPN communication to the VLAN the VNS3 virtual appliance resides on.  For more information, see the "Creating cross data center firewall policies" knowledge base article.

### Postrequisite
- If you want to access your Cohesive Networks VNS3 virtual appliance from the internet, please perform the following tasks once your VNS3 virtual appliance has been deployed to your account and has been configured:

1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal

2. If required, [allow incoming traffic for the admin port](../../Network/how-to-add-public-ip-to-virtual-machine.md) by clicking on the Servers Public IP in Control Portal.  Warning: Please make sure your VNS3 appliance firewall rules are properly configured to only allow specific source traffic.  If you do not configure source traffic rules you risk exposing your VNS3 appliance admin port to the entire internet.  Note: When accessing your CohesiveFT VNS3 virtual appliance for the first time or for any administration, we recommend you connect to your CenturyLink Cloud environment via Client VPN.
![Admin Port Firewall Ports](https://cohesive.net/wp-content/uploads/2015/03/CohesiveNetworks_CL_port8000.png)

### Detailed Steps to Deploy Cohesive Networks VNS3 Partner Template
Follow these step by step instructions to deploy a VNS3 virtual appliance in to your CenturyLink Cloud account:

- Open a service task request ticket via email to ServiceTasks@Tier3.com with the following details.  You will need to edit some of the information below.

----
TO: ServiceTasks@Tier3.com

EMAIL SUBJECT:   Custom Image Import Request for Ecosystem Partner Template

CLC Support Team,
Please open a Service Task to implement a Cohesive Networks Partner Template in accordance with this CenturyLink Policy (https://t3n.zendesk.com/hc/en-us/articles/204538645) and the following requirements below.

Please import the Ecosystem Partner Template image file referenced below to my CenturyLink Cloud Account:
- Import CenturyLink Ecosystem Partner Source Image: “Cohesive Networks VNS3 virtual appliance”
- My CenturyLink Cloud Account Alias: ####
- Data Center to import image to: ###
- (Optional) Group to import Server to: #####
- Server Name to import image as: ##########
- VLAN in the account to add the Server to: ########

Additional Information to add Partner Template to Network:

- Interface=eth0
- VLAN_free_IP=#.#.#.#
- VLAN_net_mask=#.#.#.#
- VLAN_gateway=#.#.#.#
- DNS_servers=#.#.#.#


Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed.

Thank you very much, Your_Name_Here

-----

### Accessing and Configuring your Cohesive Networks VNS3 virtual appliance
Once the Service Task team deploys your Cohesive Networks VNS3 virtual appliance, you will get an email notification with details on your new devices.  Follow these instructions to access and configure your VNS3 virtual appliance:

1. Connect to your CenturyLink Cloud environment via Client VPN by starting or initiating your VPN client.
2. Log in to the VNS3 Web UI at `https://<VNS3 PRIVATE IP>:8000`   The Default username is vnscubed and default password is vnscubed
3. Reset your passwords and log in again
4. From the left hand menu, select Upload License. Paste the encrypted VNS3 license received from Cohesive in the first field. Then click Submit.
5. Either select a preconfigured subnet, or click the Custom Radio button to specify a custom subnet range. Once you complete this step, the VNS3 manager instance will reboot itself and will come up with your specified topology enabled and running.
6. Generate a keyset by clicking Generate New under Overlay in the left column. Click Generate keys link. Key generator will be started in the background, and you can refresh screen to observe progress.

- For a downloadable PDF version of the detailed configuration guide, visit: https://cohesive.net/dnld/Cohesive-Networks_VNS3-3.5-Configuration.pdf

- For support on how to configure your Cohesive Networks VNS3 virtual appliance, please visit the Cohesive support website at https://cohesive.net/support/support-contacts/

### Pricing
There are no Cohesive Networks VNS3 license costs included.  The cost to deploy the Cohesive Networks VNS3 Partner Template will be billed as a Service Task, but CenturyLink will provide a credit for those costs.  In order to receive a credit, please follow the instructions below. More information about Service Tasks and fees are available here: http://www.ctl.io/service-tasks

#### Process to request credit for Service Task fee
Follow this process to request credit on your account to re-imburse any expense to deploy the Partner Template

1. Please copy and paste the email below and send it to [ecosystem@ctl.io](mailto:ecosystem@ctl.io)

----

TO: Ecosystem@CTL.io

EMAIL SUBJECT:   Requesting Credit for Cohesive Partner Template Deployment

CLC Ecosystem Team,

I am requesting a credit be placed on my account to cover the fees associated with deploying the CovesiveFT Partner Template to my account under the Service Task deployed on MM/DD/YYYY.  My CenturyLink Cloud username or account alias the credit needs to be placed on is ######

Thank you very much, your_name_here

----

### Frequently Asked Questions

#### Where do I obtain my Cohesive Networks VNS3 License or entitlements?
- Contact Cohesive Networks directly to receive your license: sales@cohesive.net
- Cohesive will send you an email with license and configuration and aministration guides.
- Existing CenturyLink Enterprise Customers can contact their Account Representative for additional help obtaining a Cohesive license.

#### Who should I contact for support?
- For issues regarding the VNS3 virtual appliance, please contact Cohesive Networks Support:
- Email Support - sales@cohesive.net
- Web Support - http://support.cohesive.net
- Telephone Support available with enhnaced technical support. Visit https://cohesive.net/support/support-plans for details and pricing.
- For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.
