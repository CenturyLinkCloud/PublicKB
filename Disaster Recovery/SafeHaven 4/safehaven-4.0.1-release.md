{{{
  "title": "SafeHaven 4.0.1 Release Notes",
  "date": "03-20-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 4.0.1
- Release Date: March 20, 2017

#### 1.New Features and Enhancements

* Introduced Linux VMs as recovery proxy servers for protected Windows servers
* Added support to 64bit Windows Server 2008 R1 with the conditions
  * Manual LRA installation only
  * Only support 64bit version
  * Requires Powershell v2
* Enhanced hard quota managing policy for Local Cache protection groups
* New Windows tool to report on amount of IOs for a given period
* Improved support for MANUAL site
* Improved E-Mail Reporting and Management
* Enhanced WAN data replication performance
* Added support for NAT (does not work with the hairpin problem)

#### 2. Support Matrix

##### 2.1 OS

* Windows (64bit only): Windows2008R1, Windows2008R2, Win2012R1, Win2012R2
* Linux (32bit and 64bit): RHEL (CentOS)-5/6/7, Ubuntu-12/14/16, openSUSE-11/13


##### 2.2 Data Center Types

* VMware vSphere
* CLC
* MANUAL

##### 2.3 Data Protection Types

* Local Replica
* Local Cache

##### 2.4 Limits of standard deployments ( SRN on 2 CPUs, 4GB RAM)

|Maximum of Item|Limit|Comments|
|---|---|---|
|Number of Sites per CMS|64|
|Number of SRNs per CMS|64|
|Number of Disks attached to SRN as storage pools|12|CLC default limit of disks per VM is 15|
|Number of Protected Disks (in protected VMs) per SRN|20|
|Number of Disks per Protected Windows Guest|16|Maximum number of disks (including iSCSI LUNs) per Windows server is 32
|Total Storage per Windows Guest|9TB|CLC default limit is 4TB|
|Total Storage per Linux Guest|9TB|CLC default limit is 4TB|
|Total Storage per SRN|32TB|CLC default limit is 4TB|
|Number of Protection Group per SRN|10|16 is the absolute limit|
|Number of Protected VMs per SRN|10|
|Number of PGs per CMS|320|
|Number of Protected VMs per CMS|320|
|Capacity per Disk|9TB|CLC default limit is 1TB|
|Capacity per PG|9TB|GUI limits numbers to 9999GB|
|VMs per PG|5|
|Minimum number of CPU per protected Windows VM|2|single core might work but might have problems in some cases|

Currently, CLC limits a VM to 15 disks, a total of 4TB capacity and a maximum of 1TB per disk capacity.
  * With special requests to the customer request team, they can typically accommodate up to 12TB per VM with maximum individual disk capacity limited to 4TB.
  * The CLC default limits might change in the near future.


##### 2.6 Known Limitations

* We do not support Windows VMs using E1000E NIC.
* Linux VM onboarding: we do not support the protected guest running on a different subnet from the SRN iSCSI IP.


##### 2.7 Password Limitations


* CMS root password: no constraints
* SRN root password: ```'``` (single quote) and ```^``` are legitimate Linux characters but not supported by SH-4.0. GUI will warn about it. Not supporting: ```# and $```
* SafeHaven user password: no constraints
* Windows Ansible password: not supporting ```"``` (double quote)
* Email SSMTP password (#227): not supporting  ```# : =``` and ``` ``` (space)
* vSphere password (#420):  password cannot have space at the beginning or the end
* CLC password: no constraints


### Download Links

* [SHBase-4.0.1-Mar-20-2017.ova](https://download.safehaven.ctl.io/SH-4.0.1/SHBase-4.0.1-Mar-20-2017.ova): OVA to be imported to private VMware vSphere envrionment as templates for SRN/CMS appliances
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-4.0.1/safehaven-4.0.1.deb): to be used in the installer or GUI to update from SH-4.0.0
* [GUI Package](https://download.safehaven.ctl.io/SH-4.0.1/SafeHavenConsole-4.0.1.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.4.0.1_win32.jar](https://download.safehaven.ctl.io/SH-4.0.1/SafeHavenClient.4.0.1_win32.jar): to replace existing SafeHavenClient.jar inside the already downloaded 4.0.0 GUI folder.
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-4.0.1/safehaven_windows_driver-4.0.1.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-4.0.1/MakeStub-4.0.1.exe)
* [Script to Turn a Ubuntu-14 VM as a Recovery Proxy for Protected Windows VM](https://download.safehaven.ctl.io/SH-4.0.1/makestub_for_windows.sh)
* [Linux Onboarding Script](linux-onboarding-releases.md)
