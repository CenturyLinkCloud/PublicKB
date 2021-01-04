{{{
  "title": "Create CMS in Azure",
  "date": "06-13-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to create a CMS (Central Management Server) in Azure DR Datacenter.

### Requirements
1. User must have an Azure account and permissions to deploy a server in the DR subnet.
2. Internet access on CMS in Azure once it is deployed.

### Assumptions
1. It is assumed here that the user has an Azure account, a VNet created which has accessibility to Lumen Cloud Production Datacenter and a Resource Group that will contain all the resources related to SafeHaven.
2. It is assumed the user has a storage account created.

### Create an Azure instance
1. Go to the Azure portal https://portal.azure.com 
2. Go to **Virtual Machines** service on the **Favorites** list or search for the service at top of the page next to the arrow glass.
3. Click on  the plus sign **Add**.
4. On the **Basics** tab provide the following information: 
    * Select a **Subscription** and a **Resource Group**. 
    * Enter a  **Name** for the Virtual Machine 
    * Select the **Region** for the CMS. This location must match the region of the VNet where the Instance will reside on. 
    * Leave the **Availability options** on the default value.
    * Select Ubuntu Server 16.04 LTS on the **Image** field.
    * For **Size** click on the **Change size** link. Search for B1ms on the search box and then select the B1ms Standard type instance, 1 vCPU, 2 GB of RAM and 2 data disks. Click on the Select button. 
    * Click on **Password** for Authentication type and provide both a **Username** and **Password** for it.  The username cannot be root, the password for root is generated automatically by Azure.
    * Leave the **INBOUND PORT RULES** section unchanged.     
    * Click on the **Next: Disk >** button.
5. On the **Disks** tab provide the following information:
   * Select Standard HDD for **OS disk type**.
   * Leave the rest of the options unchanged and click on the **Next: Networking >** button.
6. On the **Networking** tab provide the following information:
   * Click on **Virtual Network** under Network and select the VNet. Azure will filter out automatically the virtual networks that do not match the location selected previously for the Virtual Machine on step 4.
   * Select a **Subnet** 
   * Leave **Public IP** value as default, Azure will create a new IP address. CMS requires access to the Internet therefore a public IP address is needed.
   * Select Basic for **Network Security Group**, by default Azure will create one that has all traffic open to Instances deployed on the same VNet and any Point to Point VPNs on it. Use the automatically created Network security group.
   * For **Public inbound ports** leave the default None option selected.
   * Click on the **Next: Management >** button.
7. On the **Management** tab provide the following information:
   * Select a **Diagnostics storage account**. By default Azure enables the Boot diagnostics on the Virtual Machine.
   * Leave all the other values to default and click on the **Next: Guest config** button.
8. Click on the **Next: Tags >** button and then **Next: Review + create >**.
9. Finally review the settings selected and click on **Create**.
10. Once the Virtual Machine is created go to **Virtual Machines** service and find the Instance, select it and then click on **Networking**, write down either the Public IP or Private IP information depending if you will be accessing the server through the Internet or via VPN from Lumen.
11. SSH to the CMS Instance using the credentials created on step 5.
    * Once logged in elevate to root access and modify the password
        ```bash
        sudo -s
        passwd root
        ```
    * Enable SSH root login vi editing /etc/ssh/sshd_config with this line
        ```
        PermitRootLogin yes
        ```
    * Restart the SSH service
        ```
        systemctl restart sshd
        ```

