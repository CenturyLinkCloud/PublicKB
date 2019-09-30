{{{
  "title": "Managed OS - Operating System Patching & Update Processes",
  "date": "01-04-2018",
  "author": "Modified by Gavin Lai",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

CenturyLink provides reactive and self-service patching to servers with both standard and managed customer operating systems. For managed servers, patches and updates are available upon request to ensure no patches are applied without customer knowledge and consent, effectively reducing risks to application and data integrity. Data and/or reports are available you in different ways, depending on the solution used.


### Group Policies

If you extend your domain into CenturyLink Cloud as a managed domain then we will need to work with you to establish group policies to point your windows domain members to use our managed WSUS servers. Please contact the CenturyLink Client Service Center at 1-888-638-6771 and choose menu option 2. If you buy [managed Active Direcory](../Managed Services/getting-started-with-managed-active-directory.md) and it is provided by CenturyLink and not an extension of your domain, then we provide the group policy in our automation calls to provision the active directory.

### Self-Service Patching

It is recommended that clients planning to update managed devices work with the Client Service Center to schedule a maintenance activity for Standard, Managed Patching because it is included with managed servers.

### Standard, Managed Patching

Whether the process for scheduling patching maintenance actions is initiated by customers or CenturyLink, keeping the system up-to-date is an important component of OS administration and management. This includes discussion of potential impact on specific applications, communication strategies, health checks, suppression of monitoring alerts, and fallback planning.

#### Customer Requesitioned Patching

As part of our managed cloud service, CenturyLink will work with your designated contact to install patches in agreed-upon maintenance windows.  Please contact the CenturyLink Client Service Center at 1-888-638-6771 and choose menu option 1 to submit your request for a maintenance activity.

Since CenturyLink is often not responsible for the customer’s entire application tier, CenturyLink cannot be responsible for any adverse effects from patches that are installed at the request of the customer.

#### CenturyLink Requesitioned Patching

This includes keeping the system current with all patches to help prevent security compromises or operational reliability issues. CenturyLink will, from time to time, schedule the installation of system patches as deemed appropriate by our Solution Engineers. We will schedule the installation with you in advance. This will allow both parties to prepare for the patching, as well as provide ample time for discussion.


### Advanced Patching

Customized Patch Policies (environment & server specific) are not included with CenturyLink Cloud Managed OS. Please contact your CenturyLink sales representative to set up a special engagement.

### OS Updates

On a monthly basis, CenturyLink Cloud product engineers review all vendor-recommended patches made available by operating system software vendors. A subset of these patches and updates are identified by the OS vendor as **Critical** or **Important** to installed operating systems. The most recent version of our OS is given these updates and is then re-certified by CenturyLink before it is made available to be implemented with new server builds.

### Managed Server Updates

As a part of making a server managed, more updates may automatically be applied to the server. Please review the articles regarding [RedHat](../Managed Services/what-happens-when-RedHat-servers-are-made-managed.md) and [Windows](../Managed Services/what-happens-when-windows-servers-are-made-managed.md) to gain a general understanding of when these updates may be applied.

### Service Packs and Sub Releases

All service packs are evaluated and tested thoroughly on the standard CenturyLink Cloud Server configurations. Integration of the service pack into the CenturyLink standard operating system build only occurs once testing has proven its stability and performance benefits. All applicable servers will be automatically configured with this new base build after it has completed certification.

CenturyLink intends to keep in production current level N-2 to the extent that the underlying vendor is still providing patching and support. When underlying vendor support ceases to exist, CenturyLink  will be liable for best effort service and patching up to the last available support structure. Existing production servers, if requested by the customer, will be upgraded during maintenance windows that will be coordinated with the customer.

### Anti-Virus Protection

Standard CenturyLink practice shall be that anti-virus software is provided automatically with each managed Microsoft Windows OS. CenturyLink uses third-party anti-virus software in conjunction with centralized management tools to maintain anti-virus software updates, policy control and regular signature file updates per the policies defined at the AV vendor’s central management server. Anti-virus technology provides reasonable protection against malware, including viruses, spyware and trojans, but such technology cannot guarantee the prevention of such malware. Should disruption or changes occur due to malware, CenturyLink will use commercially reasonable efforts to promptly remedy the situation after being notified of the problem, but CenturyLink will not be responsible for any damages due to worms, phishing attacks, rootkits, trojan horses or other such malware, including infection of end-user devices or lost or corrupted data/messages.

### SavvisStation Portal Functionality

Some clients who use other CenturyLink products are likely familiar with SavvisStation Portal as a source for requesting and tracking maintenance activities for patching requests. However, SavvisStation portal is not integrated with CenturyLink Cloud. Clients should not expect to see data for CenturyLink Cloud products in SavvisStation portal.
