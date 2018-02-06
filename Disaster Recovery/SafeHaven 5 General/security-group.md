{{{
  "title": "Setup AWS VPC and VPN for SafeHaven5",
  "date": "02-05-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how create Security Group for SRN and CMS instances in AWS.
### Requirements
1. Access to AWS account.
2. VPN Connection between CLC Data Center and AWS VPC.

#### Configuration Steps
1.	Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
2.  Choose **Security Groups** in the navigation pane. 
3.  Select **Create Security Group**
4.  Specify your Security **Name tag**/**Group name** and fill the **Description** to help you identify the Security Group later.  
6.  Select the VPC that we created with the connection to production data center.
7.  Click **Yes, Create**
8.  When the wizard is done. Select the Security Group that the wizard created.
9.  Select **Inbound Rules**, click **Edit** and add the following rules and save:
| Type | Protocol | Port Range | Source | Description |
|----------|---------|--------|---------|---------|
| ALL Traffic  | All     | All   | Same security Group the wizard created |Internal Communication |
| Custom TCP Rule  | TCP (6)   | 20080-20084 | Production Subnet |Production Site Traffic |
| Custom UCP Rule  | UDP (17)   | 20080-20084 | Production Subnet |Production Site Traffic |
| All ICMP - IPv4  | ICMP (1)  | All   | Production Subnet|Production Site Traffic |
| SSH (22)  | TCP (6)   | 22 | Production Subnet |Production Site Traffic |
