{{{
  "title": "Perform Active Directory Domain Join on Windows",
  "date": "3-17-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
By leveraging [Lumen Cloud Public Blueprints](lumen-cloud-public-blueprint-packages.md) customers can automate operational tasks. In using the **Perform Active Directory Domain Join on Windows** Blueprint customers can join Microsoft Windows Servers to a domain in an automated fashion.

### Prerequisites
* A Lumen Cloud Account
* Supported Windows Operating System:
    * Windows 2008 R2 Standard 64-bit
    * Windows 2008 R2 Enterprise 64-bit
    * Windows 2008 R2 Datacenter 64-bit
    * Windows 2012 Datacenter 64-bit
    * Windows 2012 R2 Datacenter 64-bit
* A Windows 2008 or 2012 Active Directory Domain
* TCP (Firewall) Connectivity between Domain Controller(s) and Target Virtual Machine(s)
* vNIC Primary and Secondary DNS on Target Virtual Machine(s) is set to the Domain Controller(s) IP Addresses.

### EXCEPTIONS
* [Managed Managed Operating System Services Customers](http://www.ctl.io/managed-services/operating-system) should review the [Managed Operating System FAQ.](../Managed Services/managed-operating-system-frequently-asked-questions.md). In order to join Managed Servers to a dedicated customer domain, a user must deploy [Managed Active Directory](../Managed Services/getting-started-with-managed-active-directory.md) in the Lumen Cloud.
* The Perform Active Directory Domain Join on Windows Script will not perform an automated reboot of the Windows Virtual Machine. Customers are encouraged to reboot the VM at their convenience.

### Perform Active Directory Domain Join on Windows using Group Tasks
1. In the Control Portal, within the left navigation bar choose **Create** > **Server**.
   
2. Browse to the Group that houses the VM(s) you want to Join to a domain. Select Action, Execute Package.
   ![AD Join on Windows 2](../images/Perform_Active_Directory_Domain_Join_on_Windows_02.png)

3. Search for **domain** and select the **Perform Active Directory Domain Join on Windows** script.
   ![AD Join on Windows 3](../images/Perform_Active_Directory_Domain_Join_on_Windows_03.png)

4. Input the Domain information.
   * Domain User
   * Domain User Password
   * Fully Qualified Domain Name (FQDN)
   * Netbios Domain Name

   Select the VM(s) in the Group you want to join to a domain. Customers can choose an individual VM or multiple. (Quick Tip: Only supported Guest Operating Systems will be shown.)
   ![AD Join on Windows 4](../images/Perform_Active_Directory_Domain_Join_on_Windows_04.png)

### Perform Active Directory Domain Join on Windows using Blueprints
Customers who are building environments in the Lumen Cloud may wish to use Blueprints to build servers and join them to an Active Directory Domain in an automated fashion. Blueprints provide a tool for customers to build environments for multiple deployments.

To use this approach follow the [How to Build a Blueprint](how-to-build-a-blueprint.md) Knowledge Base article and the Perform Active Directory Domain Join on Windows script in conjunction with Windows Virtual Machine builds.
![AD Join on Windows 5](../images/Perform_Active_Directory_Domain_Join_on_Windows_05.png)

### Validation
Validate the Virtual Machine(s) are now joined to the Windows Domain by:

1. Login via RDP, open Server Manager.
   ![AD Join on Windows 6](../images/Perform_Active_Directory_Domain_Join_on_Windows_06.png)

2. Review the DNS field located in the Server Info area of the Cloud Portal.
   ![AD Join on Windows 7](../images/Perform_Active_Directory_Domain_Join_on_Windows_07.png)
