{{{
  "title": "Create Site-to-site VPN between CLC and AWS",
  "date": "03-06-2018",
  "author": "Gavin Lai",
  "attachments": [
  {
    "file_name": "Sample CloudFormation template to create VPC with VPN connectivity",
    "url": "../attachments/vpn-vpc-cloudforamtion.zip",
    "type": "application/zip"
  }
  ],
  "contentIsHTML": false,
  "sticky": true
}}}

### Table of contents

* [Overview](#overview)
* [Create a Site to Site VPN in Lumen Cloud](#create-a-site-to-site-vpn-in-lumen-cloud)
* [Create VPC](#create-vpc)
* [Using CloudFormation Template](#using-cloudformation-template)
* [VPN setup with an existing VPC](#vpn-setup-with-an-existing-vpc)
* [VPN Configuration on CLC](#vpn-configuration-on-clc)
  * [Phase 1](#phase-1)
  * [Phase 2](#phase-2)
* [Verify AWS Route Tables ](#verify-aws-route-tables)
* [Custom Configurations](#custom-configurations)
* [Support](#support)

###  Overview
This guide will walk through the different scenarios of connecting to an AWS environment using Site to Site VPN, including connecting to new VPC, existing VPC through console and using a basic CloudFormation template.

### Create a Site to Site VPN in Lumen Cloud

1. Before creating the VPN, a network diagram below would help to identify the VLANs in Lumen cloud and the subnets in AWS to communicate over the site to site VPN.  

   ![aws-clc](../../images/awsvpn/clc-aws.png)

2. First is to obtain the public IP address of the Lumen Cloud VPN gateway, this can be obtained from Lumen Cloud portal under Network -> Site to Site VPN.  Detail is for the Lumen Cloud Site to Site VPN setup is available [here](../Lumen Cloud/creating-a-self-service-ipsec-site-to-site-vpn-tunnel.md).

   ![aws-vpn](../../images/awsvpn/clc-s2s.png)

3. The Lumen Cloud end point IP address will be displayed once the desired data center is chosen (see below):

   ![aws-vpn](../../images/awsvpn/clc-vpn-endpoint.png)

4. Once the IP address is collected, the next step will be creating the VPN connection for AWS.  Depending on the situation, one of the following steps will be required in order to establish the VPN connection:

  * For a new AWS environment, a new VPC will be required
  * An existing AWS enironment with VPC, a Virtual Private Gateway is needed

A quick view on the configuration on the AWS side:
### Create VPC

1. In the AWS console, go to **Services**. Click on VPC and select the appropriate AWS region.

2. Click on **Start VPC Wizard**

3. Select either **VPC with Private Subnets and Hardware VPN Access** or **VPC with Public and Private Subnets and Hardware VPN Access**. Click **Select**.     
   * Enter **IPv4 CIDR block** . This is going to be a /16 IP block that will be created under the VPC.   
     **IPv6 CIDR Block** : Select the defaul option, **No IPv6 CIDR Block**.  
     Enter **VPC name**.  

   * (if required) Enter **Public subnet's IPv4 CIDR**. Enter a /24 IP block to use for the public subnet. This subnet should be within the range of /16 IP clock specied in step a.  
     Select an **availability zone** for the subnet.
     Enter the **Public subnet name**

   * Enter **Private subnet's IPv4 CIDR**. Enter a /24 IP block to use for the private subnet. This subnet should be within the range        of /16 IP clock specied in step a.  
     Select an **availability zone** for the subnet.   
     Enter the **Private subnet name**.

   * Click **Next**.

4. Configure your VPN.  
   * Enter **Customer Gateway IP** using the public IP of the Lumen VPN gateway obtained from first step.   

   * Enter **Customer Gateway name** and **VPN Connection name**.  

   * Change **Routing type** to **Static**

   * Enter the IP address of the Lumen Cloud VLAN(s) that needs to be communicated over the VLAN and paste it under **IP prefix** of Static Routes in AWS.  

   * Click **Create VPC**. This will initiate the VPC.

   * Click **ok**  
     Select the newly created VPC.
     click **VPN Connections**.  
     At the bottom left of the screen. Under tunnel details you can see the 2 tunnels created. The status will be down because CLC side of the tunnel has not been configured yet

5. Once the VPN is created, go to the **VPN Connections** page under **VPC** of AWS portal, click on **Download Configuration**.  Pick either "Generic" or "pfSense" from the drop down menu, as both are text file configuration.  

   ![clc-vpn-download](../../images/awsvpn/aws-vpn-download.png)

Please take note of the following parameters for the Lumen Cloud side VPN configuration:  
```
  Your VPN Connection ID 		  : vpn-xxxxxxxx
  Your Virtual Private Gateway ID  : vgw-xxxxxxxx
  Your Customer Gateway ID		  : cgw-xxxxxxxx
  Remote Gateway: xxx.xxx.xxx.xxx
  Description: Amazon-IKE-vpn-xxxxxxxx-0
  Pre-Shared Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  Phase 1
  Encryption algorithm : aes128
  Hash algorithm :  sha1
  DH key group :  2
  Lifetime : 28800 seconds
  NAT Traversal : Auto
  Deed Peer Detection : Enable DPD
  Phase 2
  Protocol : ESP
  Encryption algorigthms :aes128
  Hash algorithms : sha1
  PFS key group :   2
  Lifetime : 3600 seconds
```  
### Using CloudFormation Template
An Alternative way to create a VPC with VPN connection is using CloudFormation template, a sample is attached to this knowledge article.  CloudFormation templates can be deployed from AWS portal or Cloud Application Manager.  For detail on using AWS portal to deploy a CloudFormation template, please refer to this [article](//docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html).  When using [Cloud Application Manager](//www.ctl.io/cloud-application-manager/) for CloudFormation templates, please make sure to have the appropriated permissions in the AWS IAM policy, more detail can be found [here](../../Cloud Application Manager/Deploying Anywhere/using-your-aws-account.md).  The process can be found in this [knowledge article](../../Cloud Application Manager/Automating Deployments/template-box.md).

### VPN setup with an existing VPC

1. Under VPC, Virtual Private Gateways, create a VPG for the VPC if one does not exist

   ![aws-vpg](../../images/awsvpn/aws-vpg.png)

2. Once it is created, create a VPN connection under VPC on AWS portal

   ![aws-vpn](../../images/awsvpn/aws-vpn.png)  

3. Provide  
  *	Name Tag  
  *	Virtual Private Gateway that the VPN is connecting  
  *	Customer Gateway (New for Lumen Cloud)  
  *	IP can be found in Create VPN page on Lumen Cloud (1 per data center)  
  *	BGP ASN (leave as default)  
  *	Routing option: Static  
  *	Enter Lumen Cloud Network(s) that needs to communicate with AWS environment  
  *	Tunnel Options: default  
4. Using the AWS VPN configuration file, with the information from the file, complete the VPN setup in Lumen Cloud Site to Site VPN setup

### VPN Configuration on CLC
1. From Lumen Cloud portal under Network -> Site to Site VPN.  Detail is for the Lumen Cloud Site to Site VPN setup is available here. Pick the VPN endpoint that is configured as part of the AWS VPN configuration and add the Lumen Cloud VLAN(s) as part of the VPN setup for **VPN Peer IPv4 Address**.
   ![aws-vpn](../../images/awsvpn/clc-vpn-endpoint.png)

2. Enter **Site Name** (this can be the AWS VPN Connection ID) and **Device Name** (can be anything or using the AWS VPN ID).  

   **VPN Peer IPv4 Address** is the Remote Gateway from the configuration file.  

3. **Tunnel Encrypted Subnets** : Click **Add network block**. This is the private subnet from the AWS VPC.

4. Click **next: phase 1**   

Using the VPN configuration file downloaded to complete the next two step

#### Phase 1

* **Protocol Mode** - Main
* **Encryption Algorithm** - AES-128 (can be AES-128, AES-192, AES-256 or 3DES)
* **Hashing Algorithm** - SHA1(96) (can be SHA1, SHA2 or MD5)
* **Pre-Shared Key** - Shared Key from the AWS VPN configuration
* **Diffie-Hellman Group** - Group 2
* **Lifetime Value** - 8 hours
* **DPD State** - ON
* NAT-T State - OFF

#### Phase 2  
* **IPEC Protocol** ESP  
* **Encryption Algorithm**: AES-128   
* **Hashing Algorithm**: SHA1  
* **PFS Enabled**: ON, Group 2  
* **Lifetime Value**: 1 hour  

Click **Finish**.  
Once the Lumen VPN is created, check on the AWS portal and click on **VPN connections**. The tunnel should now be **UP**.  


### Verify AWS Route Tables
1. Once VPN setup is completed, verify the VPC Route Tables is correct, either the default route or the Lumen subnets should be routed through the Virtual Private Network
   ![aws-routing](../../images/awsvpn/aws-routing.png)
2. Ensure Network ACL and Security Group are configured to allow traffic from the CLC network  
   ![acl](../../images/awsvpn/acl.png)  
   ![aws-securitygroup](../../images/awsvpn/aws-securitygroup.png)  
3. Initiate “ping” or SSH from a CLC server to a server in the AWS network to validate the connectivity

### Custom configurations
Customers who require custom configuration can leverage our [service task](//www.ctl.io/service-tasks/#vpn-tunnels-deployment). Examples include:
* Redundant VPN Tunnels
* AES256 IPSEC Encryption

### Support

* For issues related to cloud infrastructure (VM's, network, etc), or if you experience a problem deploying any Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](//t3n.zendesk.com/tickets/new).
