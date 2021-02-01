{{{
  "title": "What Happens When RedHat Servers Are Made Managed",
  "date": "07-29-2015",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This document provides an overview of steps taken when RHEL servers are prepared to be managed by Lumen.

### Audience

Users employed by companies that have agreed to terms with [Lumen Sales](http://www.centurylink.com/) for the Lumen Cloud product.

### Prerequisites
* An understanding of the process for [making newly created servers managed](../Managed Services/created-a-managed-server-now-what.md) or for [converting pre-existing servers to managed](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md)

* Some idea of the benefits included with [managed servers](../Managed Services/managed-operating-system-frequently-asked-questions.md)

* Grasp of Red Hat Enterprise Linux fundamentals

### Important Information

The following is not meant to be a complete description of everything that happens when a VM is prepared for management, but to give users a better idea of configuration changes that might be necessary to manage their servers.

Many of the following items are mandatory. Some default items have options for change. If you would like to alter default options, please contact the Lumen Client Service Center at 1-888-638-6771 to submit your request for review.

Some of the items below only occur when the server is new. If the server already exists before it is [converted to managed](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md)it is considered a Customer Provided Image (CPI). Because each CPI server is different and there is no guarantee that some of the steps below would not harm CPI servers, some of the steps -  indicated by "Not for CPI" statements - will not apply.

* A client is downloaded onto the VM. This client allows for installation of management tools, configuration, and remote support.
* By default, a Managed RHEL server will be a part of a sub domain specific to the data center in which the server resides. It will point to our infrastructure DNS servers for name resolution. For any needs beyond simple name resolution met by the above configuration, please contact us.
* Our monitoring agent is installed and configured. Heartbeat monitoring of the agent commences.
* 10 GB data01 is added
* Bash is configured (Not for CPI)
* The Managed Server is disconnected from the standard [RedHat Update Infrastructure](../Servers/redhat-machines-report-they-are-not-registered-to-rhn-when-running-yum.md) and registered with RedHat Network.
* Operationally expected patches are installed.
* Basic OS standardization is performed, including setting the locale and clock. (Not for CPI)
* The majority of network services in the RHEL build are disabled. A newly provisioned system will only have the following network services running: Secure Shell, SNMP agent, and NTP Protocol. By default, our Managed RHEL servers will synchronize NTP against managed infrastructure NTP servers, which are polling multiple internet stratum 1 time sources. It is also configured, by default, to deny querying from other servers or clients. (Not for CPI)
* A restrictive umask is set for boot processes. (Not for CPI)
* Core dumps are disabled to increase performance, reduce storage demands, and prevent collection of sensitive data on the server. (Not for CPI)
* IPV6 is disabled (Not for CPI)
* Unnecesarry crontab entries are disabled (Not for CPI)
* SUID/SGID on non-essential binaries is removed (Not for CPI)
* Accounts with restrictive permissions are created at build to allow operational access.
* Postfix is configured by default to be a null client. Local delivery is disabled, and Postfix is not started. Should the server need mail services, please provide an example of the type of mail traffic that will be generated from the system so that it can be configured appropriately for the system's needs. (Not for CPI)
* Log rotation is set at 4 weeks worth of logs (Not for CPI)
* Password requirements and expirations are set. Password aging (90 days), increased password complexity, and eight character minimum length are set. (Not for CPI)
* AIDE is configured to perform a baseline and that is all. The customer is able to configure AIDE themselves. (Not for CPI)
* PAM is configured (Not for CPI)
