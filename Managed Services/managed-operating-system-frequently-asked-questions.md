{{{
  "title": "Managed Operating System - Frequently Asked Questions",
  "date": "4-22-2015",
  "author": "Jacob Kenner",
  "attachments": [],
  "contentIsHTML": false
}}}

Here are a few frequently asked questions for our managed OS service.

**What is included in the Managed OS service?**

CenturyLink’s Managed OS service helps you spend less time on the IT tasks that don’t contribute immediately to your daily goals. To this end, here are the tasks performed on your behalf with our managed OS service:

* Vendor Management – CenturyLink maintains ownership and management responsibility for your OS, freeing you from managing OS-level functions, SPLAs and license keys.
* Access Management – We take responsibility for user policies, administration and password management enforcement.
* Configuration Management – We confirm the initial install and basic functionality using an OS image built on vendor-recommended best-practices &amp; years of industry experience.
* Change Management – We provide access to OS-level change data performed by CenturyLink staff, along with robust ITIL-based internal changed control.
* Patch/Update Management – With support available for all critical and vendor-recommended patches, we ensure only OS vendor-recommended patches are installed.
* Security – We secure the OS with industry-standard anti-virus protection, regular virus and malware signature updates, and additional OS-level hardening to mitigate risk.

**How do I create a Managed VM?**

For starters, you need to identify a data center that supports managed operating systems. In the [data centers](//www.ctl.io/data-centers/) page, find the filter in the Cloud category called Public Cloud Managed OS.

From the Control Portal menu, select “Create Server.”  Then, select the data center, group membership, and other VM properties.  Select the data center that supports managed services and then click the “managed server” element to “Yes.” The operating system drop-down menu will automatically show available options. Choose your version, and then proceed with the remainder of the server creation process.

After creating a managed VM, the VM will be 'Under Construction' while background processes are completed. You will not have access to the server during that time; you will receive a notification via email once the operation has completed. Please allow up to a 30 minutes. If there are any issues beyond that time, contact us via email <a href="mailto:request@centurylink.com">request@centurylink.com</a> or by phone at the following numbers. In the US: 888.638.6771; UK: +44.118.322.6100; Singapore: +65.6305.8099. Please do not email the CenturyLink Cloud NOC or raise the issue via chat - faster responses to inquiries will come from the email address and support numbers above.


**What if I don’t see an option for Managed OS in the CenturyLink Cloud Control Panel?**

There could be a few causes:

* Be sure you are creating the server in a data center that supports managed services.
* It is possible your company has not yet executed a Master Services Agreement (MSA) with CenturyLink Technology Solutions. To obtain a MSA – or if you believe you should already have one in place – please contact a CenturyLink Sales Representative toll free at:

    * United States: 1-855-287-2541
    * Canada: 1-877-387-3764
    * Europe, Middle East &amp; Africa: +44 (0) 207 400 5600
    * Japan: +81 3 5214 0180
    * Hong Kong: +852 3079 4461
    * Singapore: +65 6591 8824

**Is there anything that I cannot do in the Control Portal with a managed VM?**

A managed virtual machine cannot be cloned, archived, or converted to a template. Also, the "time to live" option is not available when creating a new managed server. At this time, you cannot create a managed server within a Cloud Blueprint.

**How do I log into my server?**

To access your managed VM, you will need your Local Account server name and password, unless you have created a Managed Active Directory Domain or are using a CenturyLink Shared Active Directory Domain.

The Local Account user name is the full server name, and the password credential is available in your CenturyLink Cloud Control Portal using the “<em>click to authenticate</em>” link on the server overview page. **Please note that the user name and password for your Server is not the same user name and password for the Cloud Control Portal.**

Once you have obtained your password, you may access Windows environments using Remote Desktop and RHEL environments using SSH. For more detailed information about accessing your server for the first time, please see the articles for [Windows Server](managed-windows-server-connecting-to-your-server-with-remote-desktop.md) or [RHEL](managed-red-hat-connecting-to-your-server-with-ssh.md).

**What should I do if I have trouble connecting via Remote Desktop?**

If you have difficulty connecting via RDP, be sure you are connecting from an IP that has TCP Port 3389 allowed on the <em>inbound</em> firewall. If you have a firewall at your location, you will need to have TCP port 3389 opened for *outbound* traffic. The firewall rule-set can be reviewed with your primary CenturyLink order contact or Consulting Engineer. Note that you should NEVER manage your remote servers through public IP address, and ONLY access servers through a secure tunnel like client VPN or site to site VPN!

If you connect and find that the system disconnects you immediately, you should ensure you are using the latest Remote Desktop client and that your client machine is fully patched. For additional support, please contact the Client Service Center at 1-888-638-6771 and choose menu option 2.

**How can I have my VM patched?**

An important component of OS administration and management is keeping the system up-to-date. This includes keeping the system current with all patches to help prevent security compromises or operational reliability issues. CenturyLink will, from time to time, schedule the installation of system patches as deemed appropriate by our Solution Engineers. We will schedule the installation with you in advance. This will allow both parties to prepare for the patching, as well as provide ample time for discussion regarding the potential impact the patch may have on specific applications within your environment.

In addition, you can request patching for your VM by contacting the Client Service Center at 1-888-638-6771 and choosing menu option 2.

**How can I transfer files to my server using Remote Desktop?**

Files can be transferred by simply drag and drop in Windows Explorer from your remote desktop session.

* Configuring Remote Desktop for files transfer:
* Run Remote Desktop Connection (Start Menu/All Programs/Accessories).
* Enter the IP Address of the server.
* Click Options, then select Local Resources tab.
* Under Local devices and resources, click on More…
* Click on the “+”next to Drives, then select the local drive on your client which you would like to copy files from.
* Click Ok when done.
* Click Connect to initiate the connection.
* After connection is established, in your remote desktop session, open Windows Explorer (Start Menu/All Programs/Accessories)
* Local drive will show as Driver Letter on Hostname format, e.g. C on MyPC, process to copy files to or from your local drive

**Who do I contact if I have trouble with my Managed VM?**

The CenturyLink Technology Solutions Client Service Center is available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771, or send email to request@centurylink.com for Managed OS issues. If there is an incident, email can be sent to incident@centurylink.com.

**How can I remove Managed Services from a VM?**

Currently, the only way to remove Managed Services from a VM once it has been deployed is to delete the VM and to create a new server that is unmanaged. This process should be followed for managed operating systems as well as for managed applications.

**How can I tell my *managed* VMs from my <em>unmanaged</em> VMs in the CenturyLink Cloud Control portal?**

Managed VMs will be noted with an asterisk (*) in front of the server name. For example, *ILMHPELCTA04*. This notation is intended to make it easier to locate managed VMs from within a list of all Cloud VMs you have created.

**My VM shows under construction in Control, but shows that the build has completed successfully?**

On Managed VMs, there are additional tasks that is being processed in the background in order to fully integrate into the Managed system, once this is complete Control will reflect it as active and manageable.

**Can I join Managed Servers to my own domain?**

Yes, customers may elect to join a Managed Server to their own domain instead of the CenturyLink Shared Active Directory Domain.  In order to join Managed Servers to a <em>dedicated</em> customer domain a user must deploy [Managed Active Directory](getting-started-with-managed-active-directory.md) in the CenturyLink Cloud.

**Can *un-managed* Servers be converted to *Managed* (or vice versa)?**

Servers **can** be converted from unmanaged to managed by executing the "Managed RHEL for CPI" (for Red Hat servers) or "Managed WIN for CPI" (for Windows servers) Blueprints in the library. Customers **cannot** go from a managed server to an unmanaged server.

**What Anti-Virus is provided for Windows Servers and how often is it updated?**

McAfee is leveraged on Managed Windows Servers and is updated daily.
