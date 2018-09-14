{{{
  "title": "Create DR SRN in AWS",
  "date": "12-27-2017",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a SRN (SafeHaven Replication Node) in AWS DR Datacenter.

### Requirements
1. User must have an AWS account and permissions to deploy a server in the DR subnet.
2. Internet access on DR-SRN in AWS once it is deployed.

### Assumptions
1. It is assumed here that the user has an AWS account and a VPC created which has accessibility to CenturyLink Cloud Production Datacenter.
2. Typically CMS and DR-SRN reside in the same subnet so we will simply re-use the Security Group we created in the previous step [Create CMS in AWS](Create CMS in AWS.md)

### Create an AWS instance
1. Go to **Services** > **EC2**
2. Click on **Launch Instance**.
3. Select **Community AMIs**, and search for **SafeHaven**. Select **SafeHaven-5 Base OS**.
4. Select **m4.large** resource type, and click on **Next:Configure Instance Details**.
5. Select a subnet on your VPC which has reachability to CLC Production datacenter. Rest of the options can be left as default.
6. Proceed with default 30GB storage and Make sure that Volume type is **General Purpose SSD(GP2)**.
7. Click **Next: Add Tags**.
8. Click **Next: Configure Security Group**. Click on **Select existing Security Group**. Select the pre-existing security group that was created during [Create CMS in AWS](Create CMS in AWS.md) setup.
9. Click on **Review and Launch**.
10. Click on **Launch**.
11. Select **Proceed without a key pair**.
12. Click on **Launch Instances**.
13. Once the Instance is created, user can name the instance as CMS and add tags if required.

**NOTE:** The default root password for the SRN will be provided upon SafeHaven License Request. **It is STRONGLY recommended to change the default root password for security purposes.**

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/YH-XudTKrlQ" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</p>  

**Next Step** is to [Create SafeHaven Cluster and Login to SafeHaven Console](Create SafeHaven Cluster and Login to SafeHaven Console.md)
