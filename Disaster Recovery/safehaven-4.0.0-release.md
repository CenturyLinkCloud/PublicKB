{{{
  "title": "SafeHaven 4.0.0 Release Notes",
  "date": "12-28-2016",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 4.0.0
- Release Date: October 7, 2016

#### 1.New Features

* Improved performance: Local cache disk alignment issue solved
* Allow reduction of SBD COW page size: solves the checkpoint inflation problem
* Better automation:  Ansible based LRA installation and Makestub is no longer experimental
* Better hard quota management: a lot more LRA-SRN communication and control
* Enhanced user experience: auto stub deployment and configuration in PG creation
* More reliable: fixed a number of SBD bugs
* Better package management and version control: debian package
* Removed a lot of password constrains
* Improved GUI



#### 2. Support Matrix

##### 2.1 OS

* Windows: Windows2008R2, Win2012R1, Win2012R2
* Linux: RHEL (CentOS)-5/6/7, Ubuntu-12/14, openSUSE-11/13


##### 2.2 Data Center Types

* VMware vSphere
* CLC
* MANUAL 
 
##### 2.3 Data Protection Types

* Local Repica
* Local Cache

##### 2.4 Limits of standard deployments ( SRN on 2 CPUs, 4GB RAM)

|Maximum of Item|Limit|Comments|
|---|---|---|
|Number of Sites per CMS|8|
|Number of SRNs per CMS|64|
|Number of Disks attached to SRN as storage pools|12|CLC default limit of disks per VM is 15|
|Number of Protected Disks (in protected VMs) per SRN|20|
|Number of Disks per Protected Windows Guest|8|
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

* We do not support Windows VMs using E1000E NIC
* Linux VM onboarding: we do not support the protected guest running on a different subnet from the SRN iSCSI IP. 


##### 2.7 Password Limitations

 
* CMS root password: no constrains
* SRN root password: ```'``` (single quote) and ```^``` are legitimate Linux characters but not supported by SH-4.0. GUI will warn about it. 
* SafeHaven user password: no constrains
* Windows Ansible password: not supporting ```"``` (double quote)
* Email SSMTP password (#227): not supporting  ```# : =``` and ``` ``` (space)
* vSphere password (#420):  password cannot have space at the beginning or the end.
* CLC password: no constrains


### Download Links

* [Relese Notes as a PDF File](https://download.safehaven.ctl.io/SH-4.0.0/SafeHaven+4++Release+notes.pdf)
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-4.0.0/safehaven-4.0.0.deb): to be used in the installer
* [GUI Package](https://download.safehaven.ctl.io/SH-4.0.0/SafeHavenConsole-4.0.0.zip): zip file containing the JRE, runs on any Windows platform
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-4.0.0/safehaven_windows_driver-4.0.0.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-4.0.0/MakeStub-4.0.0.exe)
* [Script to Turn a Ubuntu-14 VM as a Recovery Proxy for Protected Windows VM](https://download.safehaven.ctl.io/SH-4.0.0/makestub_for_windows.sh)
* [Linux Onboarding Script](https://download.safehaven.ctl.io/SH-4.0.0/sh-linuxonboarding-1.2.0.tar.gz)
