###
1. Go to **Services**. Click on VPC.
2. Click on **Start VPC Wizard**  
3. Select **VPC with Public and Private Subnets and Hardware VPN Access**. Click **Select**.
  * Step 2 : VPC with Public and Private Subnets and Hardware VPN Access.  
    a. Enter **IPv4 CIDR block** . This is going to be a /16 IP block that will be created under the VPC.  
       **IPv6 CIDR Block** : Select the defaul option, **No IPv6 CIDR Block**.  
       Enter **VPC name**.  
       
    b. Enter **Public subnet's IPv4 CIDR**. Enter a /24 IP block to use for the public subnet. This subnet should be within the range of /16 IP clock specied in step a.  
       Select an **availability zone** for the subnet.   
       Enter the **Public subnet name**
       
    c. Enter **Private subnet's IPv4 CIDR**. Enter a /24 IP block to use for the private subnet. This subnet should be within the range of /16 IP clock specied in step a.  
       Select an **availability zone** for the subnet.   
       Enter the **Private subnet name**.
     
     d. Click **Next**.
4. Configure your VPN.  
   a. Enter **Customer Gateway IP**.   
   To find this information, login to [Centurylin Portal] (https://control.ctl.io/).   
   Click on **Network** > **Site-to-site VPN**  
   Click **+site to site vpn**  
   Select the right datacenter in front of **Control portal site**  
   Copy the **VPN Peer IPv4 address** and paste it in **Customer Gateway IP** in AWS.
   
   b. Enter **Customer Gateway name** and **VPN Connection name**.  
   
   c. Change **Routing type** to **Static**
   
   d. Go back to CLC **Site to Site VPN** page to get the **IP prefix**.
      Click on **Add Network Block**. Select the **Network** and **subnet size**. click **Add network block**.
      Copy the IP address in fron of **Tunnel Encrypted Subnets** and paste it under **IP prefix** in AWS.  
      
   e. Click **Create VPC**.  
