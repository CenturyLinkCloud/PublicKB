
{{{
  "title": "Create CMS in AWS",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a CMS (Central Management Server) in AWS DR Datacenter.

### Requirements
1. User must have an AWS account and permissions to deploy a server in the DR subnet.
2. Internet access on CMS in AWS once is is deployed.

### Assumptions
It is assumed here that the user has an AWS account and a VPC created which has accessibility to Lumen Cloud Production Datacenter.

### Create a Security Group
1. Click on **Security Groups** from the navigation tree, then click on **Create Security Group** button on the right.
2. Name the security group and select the default VPN, click on **Add Rule** button.  
   a. Add **Custom TCP Rule**, Port Range 20080-20084, Source Restricted  
   b. Add **Custom UDP Rule**, Port Range 20080-20084, Source Restricted  
   c. Add **All ICMP Rule IPv4**, Source Restricted  
   d. Add **SSH**, Port Range 22, Source Restricted  
3. Click on **Create**.

### Create CMS in AWS
1. Go to **Services** > **EC2**.
2. Click on **Launch Instance**.
3. Select **Community AMIs**, and search for **SafeHaven**. Select **SafeHaven-5 Base OS**.
4. Select **t2.small** resource type, and click **Configure Instance Details**.
5. Select a subnet on your VPC which has reachability to CLC Production datacenter. Rest of the options can be left as default. Click **Next: Add Storage**.
6. Proceed with default 30GB storage.
7. Click **Next: Add Tags**.
8. Click **Next: Configure Security Group**. Click on **Select existing Security Group**. Select the security group that was created for the setup.
9. Click on **Review and Launch**.
10. Click on **Launch**.
11. Select **Proceed without a key pair**, and click on the checkbox **"I acknowledge that I will not ..."**.
12. Click on **Launch Instances**.
13. Once the Instance is created, user can name the instance as CMS and add tags if required.

**NOTE:** The default root password for the CMS will be provided upon SafeHaven License Request. **It is STRONGLY recommended to change the default root password for security purposes.**

**Next Step** is to [Create DR SRN in AWS](Create DR SRN in AWS.md)
