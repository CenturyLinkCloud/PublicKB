{{{

  "title": "Deploy CMS in Lumen Cloud",
  "date": "04-30-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a CMS (Central Management Server) in lumen cloud to use in a SafeHaven 5 Environment. A CMS( Center Management Server) is basically a management server that is used to access the Safehaven Cluster. It provides a user interface through a java application. For SafeHaven 5, an Ubuntu-16 VM template is used to deploy the CMS machine.

### Requirements
1. Login access to the Lumen Cloud Portal at https://control.ctl.io.
2. Permissions to deploy a VM in the account.

### Assumptions
This article assumes that the user has login access to the Lumen Cloud Portal. Login to the **Lumen Control Portal**  https://control.ctl.io with your credentials.



### Deploy the CMS Node in Lumen Cloud
1. Login to Lumen Cloud portal with your ceredentials - https://control.ctl.io/
2. Change the subaccount if needed by clicking on top of the screen.
3. Click on the Datacenter that is required to be the DR Datacenter.
4. Create a Group(Optional):  
  a. Click on **create** button on the right to expand it.  
  b. Click **Group**.  
  c. Enter the group **name**  
  d. Click **Create Server Group**.  
5. Create a new VM:  
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
 
 
 The CMS VM is now deployed.    
