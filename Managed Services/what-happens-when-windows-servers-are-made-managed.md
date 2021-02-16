{{{
  "title": "What Happens When Windows Servers Are Made Managed",
  "date": "08-05-2015",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This document provides an overview of steps taken when Windows servers are prepared to be managed by Lumen.

### Audience

Users employed by companies that have agreed to terms with [Lumen Sales](http://www.centurylink.com/) for the Lumen Cloud product.

### Prerequisites
* An understanding of the process for [making newly created servers managed](../Managed Services/created-a-managed-server-now-what.md) or for [converting pre-existing servers to managed](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md)

* Some idea of the benefits included with [managed servers](../Managed Services/managed-operating-system-frequently-asked-questions.md)

* Grasp of Windows Server fundamentals

### Important Information

It is required that a Windows server reboot during the make managed process. If the server already exists and is being [converted](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md) then the server should be placed in maintenance mode prior to running the blueprint and removed from maintenance mode once an email verifying completion has been received.

The following is not meant to be a complete description of everything that happens when a VM is prepared for management, but to give users a better idea of configuration changes that might be necessary to manage their servers.

Many of the following items are mandatory. Some default items have options for change. If you would like to alter default options, please contact the Lumen Client Service Center at 1-888-638-6771 to submit your request for review.

* A client is downloaded onto the VM. This client allows for installation of management tools, configuration, and remote support.
* If a [dedicated domain exists](../Managed Services/getting-started-with-managed-active-directory.md) for the customer, the server will be joined to it. Otherwise, the server will join a shared domain.
* Our monitoring agent is installed and configured. Heartbeat monitoring of the agent commences.
* Our approved virus scanning agent is downloaded and configured. It will be updated weekly.
* 10 GB D: drive is added. If D: drive already exists, the next available, unused drive will be added.
* A pre-defined Windows Update Group Policy Object is linked to each customer OU. Miscrosoft-approved patches will be applied  [If the server already exists ](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md) there is an exception. No updates will be applied to Customer Provided Images (CPI). [requests can be made](../Managed Services/created-a-managed-server-now-what.md) to approve or un-approve particular patches. The server is rebooted as required.
* Basic OS standardization is performed, including setting time zone
* Hibernation disabled
* Boot config timeout set to five seconds
*	Data Execution Prevention (DEP) disabled
* Operational event log is created
* Password requirements are set: complexity is enabled; eight-character minimum length; lockout takes place after 3 invalid logon attempts and has a thirty minute duration; and password expirations are set at forty-two days.
* Games are restricted from the installation
* A scripting engine is set
* RDP is enabled
* A variety of user rights are assigned or left undefined
* Audit settings are defined
* Security policies are defined
* IPV6 is disabled

* Registry modification includes, but is not limited to:
  * "SYN flooding attack protection" TCP feature that detects symptoms of denial-of-service attacks (also known as SYN flooding), and it responds by reducing the time the server spends on connection requests that it cannot acknowledge.
  * Prevent anonymous log on access to all resources, with the exception of resources the anonymous user may have explicitly been given access to
  * Restricts access to clients logged on to the system account without username and password authentication.
  * Disables server support for internet printing
  * Disables Client Printer Auto-Mapping to Terminal Session
  * Adds Command Prompt to folder view
  * Updates Default installation source directory to use c:\ vice d:\
  * Removes "open" value from RAS (prevents Event Logging)
  * Enables use of Recovery Console without a password
  * Set application event log size
  * Set system event log size
  * Set security event log size
  * Sets application event log retention size
  * Sets system event log retention size
  * Sets system event log retention size


* The following are disabled:
  * Alerter Service
  * ClipBook Service
  * FAX Service
  * Messenger Service
  * Miscrosoft NetMeeting service
  * File Replication service
  * UPS service
  * CPQ Web service service
  * CPQ Nic Teaming service
  * Windows Firewall Profiles
  * NLA For RDP
  * Certain NIC features
  * Scheduled tasks



* The following software is either installed or configured and required for management and should not be altered without consulting with Lumen
  * Our approved, managed antivirus
  * Opsware agent
  * ActivePerl
  * Sysinternals Bgnfo
  * SIA
  * OpenSSH
  * Server Manager module for PowerShell - installed
  * DotNet (approved version) - installed
  * Disk Cleanup Tool - installed



* The following directories are required for management and should not be altered without consulting with Lumen
  * D:\svvstools
  * C:\XFER
