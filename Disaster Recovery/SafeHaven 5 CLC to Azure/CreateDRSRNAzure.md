{{{
  "title": "Create DR SRN in Azure",
  "date": "06-13-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a SRN (SafeHaven Replication Node) in Azure DR Datacenter.

### Requirements
1. User must have an Azure account and permissions to deploy a server in the DR subnet.
2. Internet access on DR-SRN in Azure once it is deployed.

### Assumptions
1. It is assumed here that the user has an Azure account, a VNet created which has accessibility to CenturyLink Cloud Production Datacenter and a Resource Group that will contain all the resources related to SafeHaven.
2. Typically CMS and DR-SRN reside in the same subnet so we will simply re-use the Network Security Group we created in the previous step [Create CMS in Azure](CreateCMSAzure.md)
3. It is assumed the user has a storage account created.

### Create an Azure instance
1. Go to the Azure portal https://portal.azure.com 
2. Go to **Virtual Machines** service on the **Favorites** list or search for the service at top of the page next to the arrow glass.
3. Click on  the plus sign **Add**.
4. Click on **Ubuntu Server**, and then click on **Ubuntu Server 16.04 LTS**. Finally click on the Create button.
5. On the **Basics** blade provide the following information:   
    a. Enter a  **Name** for the Virtual Machine  
    b.  Select **HDD** for the VM disk type  
    c.  Click on **Password** for Authentication type and provide both a **Username** and **Password** for it.  The username cannot be root, the password for root is generated automatically by Azure.  
    d.  Select a **Subscription** and a **Resource Group**.   
    e.  Select the **Location** for the DR-SRN. This location must match the location of the Vnet where the Instance will reside on.    
    f.  Click on the OK button.  
6. On the **Size** blade search for F4 and then select the F4 Standard type instance. 4 vCPUs, 8 GB of RAM and 16 data disks. Click on the Select button.
7. On the **Settings** blade provide the following information:  
   a. Click on No for Use unmanaged disks, select a **Storage account** for the destination of the DR-SRN unmanaged disks. Azure will filter out automatically the storage accounts that do not match the location selected previously for the Virtual Machine in step 5.  
   b. Click on **Virtual Network** under Network and select the VNet. Azure will filter out automatically the virtual networks that do not match the location selected previously for the Virtual Machine in step 5.  
   c. Select a **Subnet** and a **Public IP address** for the DR-SRN, by default Azure will create a new IP address. DR-SRN requires access to the Internet therefore a public IP address is needed.  
   d. Click on Advanced under **Network Security Group**, this will open the option to select a Network Security Group, by default Azure will create one that has all traffic open to Instances deployed on the same VNet and any Point to Point VPNs on it. Use the Network security group created during the CMS deployment.  
   e. Select a **Diagnostics storage account**, it can be the same storage account selected in step 7. By default Azure enables the Boot diagnostics on the Virtual Machine.  
8. Leave all the other values to default and click on the OK button.
9. On the **Summary** blade review the settings and click on the OK button.
10. Once the Virtual Machine is created go to **Virtual Machines** service and find the Instance, select it and then click on **Networking**, write down either the Public IP or Private IP information depending if you will be accessing the server through the Internet or via VPN from CenturyLink.
11. SSH to the DR-SRN Instance using the credentials created in step 5.  
    1. Once logged in elevate to root access and modify the password  
    
        ```bash
        sudo -s
        passwd root
        ```
    
    2. Enable SSH root login by editing `/etc/ssh/sshd_config` with this line  

        ```
        PermitRootLogin yes
        ```  

    3. and if the key based authentication was used to created the user instead of password in the Azure portal, we need to also change
        ```
        PasswordAuthentication yes
        ```
    4. Restart the SSH service  
        ```
        systemctl restart sshd
        ```  
    5. If ssh as root gets a message like `Please login as the user "seki" rather than the user "root".`, please run `rm /root/.ssh/authorized_keys` and try again.
    6. Confirm "ssh as root works using password" works


