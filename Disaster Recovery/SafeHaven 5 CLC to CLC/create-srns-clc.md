{{{
  "title": "Create SRNs in Lumen Cloud",
  "date": "12-27-2017",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to deploy both production site and recovery site SafeHaven Replication Node(SRN)s in Lumen Cloud.
SRN resides in both production and DR datacenters and work in pairs. A single SafeHaven Cluster can have upto 64 SRN's registered. This article explains how to deploy SRN in Lumen Cloud Production Datacenter and Recovery Datacenter.

### Requirements
1. Login access to the Lumen Cloud Portal at https://control.ctl.io.
2. Internet access on the Production and Recovery SRNs in Lumen Cloud once it is deployed.

### Assumptions
This article assumes that the user has login access to the Lumen Cloud Portal.

### Deploy the SafeHaven Repliation Node(SRN) in Lumen Cloud
1. Login to Lumen Cloud portal with your ceredentials - https://control.ctl.io/
2. Change the subaccount if needed by clicking on top of the screen.
3. Click on the Datacenter that is required to be the Production Datacenter.
4. Create a Group(Optional):  
  a. Click on **create** button on the right to expand it.  
  b. Click **Group**.  
  c. Enter the group **name**  
  d. Click **Create Server Group**.  
5. Create an SRN:  
  a. Click **Create** button on the right to expand it.  
  b. Click **Server**.  
  c. Make sure that correct **Datacenter** and **Group** is selected.    
     Select **Server Type** : **Standard**  
     Select **Operating System** : **Ubuntu 16|64-bit**  
     Enter **Server Name**. Just 6 characters are allowed.  
     Enter **admin/root password**
     Give the server **2 CPUs** and **4 GB Memory**.  
     **Note**: No need to add any additional storage at this point.  
     Select a **Network**. This is the network where the Recovery Servers will be deployed.
     Click **Create Server**. 
     
 6. You can monitor the VM create job. It can take a few minutes. An email notification will be sent to the registered email account upon successful deployment.
 7. Repeat step 1-6 in Recovery Datacenter to create DR-SRN
 
 Both PROD-SRN and DR-SRN are now deployed. 
