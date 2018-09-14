{{{
  "title": "SafeHaven 4.0.3 Release Notes",
  "date": "08-24-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 4.0.3.
- Release Date: August 25, 2017

### New Features and Enhancements

This is a patch release for [SafeHaven 4.0.2](safehaven-4.0.2-release.md), which is a patch release for [SafeHaven 4.0.1](safehaven-4.0.1-release.md).

* Add Support for Windows Server 2016.
* Automatically resize storage pool when the backing storage is resized.
* Fully support the migration use case.
* Fully support servers with more than 10 disks.
* Improve error logging in Windows server.
* Added resiliency to PG resize.
* Better support for Windows Dynamic Disks.
* Better error handling of re-failover.
* A number of minor GUI fixes such as typos, error messages, resolution problems, etc.

 
 ### Upgrade Path 

|Component|4.0.1->4.0.3|4.0.2->4.0.3|
|----|----|----| 
|GUI and Syntropy|Yes, no interruptions|Yes, no interruptions|
|Windows Agent|Yes, reboot needed|Yes, reboot needed|
|SBD (WAN replication kernel module on SRN)|No change|No change| 

### Upgrade from 4.0.1 and 4.0.2

* **OVA and SBD modules in the SRN is the same for 4.0.1, 4.0.2, and 4.0.3**. There is no need to upgrade them.

* **Upgrade Procedure** : [Upgrade Procedure for Minor Releases (Syntropy and GUI Console)](Upgrade-Procedure-for-Minor-Releases-Syntropy-and-GUI.md)
  * To upgrade from 4.0.1 to 4.0.3, there is no need to upgrade to 4.0.2 first.
* Once Syntropy is upgraded, only the Windows agent with the matching version works with new protections.
  * Potentially, for an already protected Windows server, it is possible to upgrade only Syntropy to 4.0.3 and keep the Windows Agent on 4.0.1 or 4.0.2.
  * Upgrading the Windows Agent from 4.0.1/4.0.2 to 4.0.3 requires a reboot of the production Windows server.

### Download Links

#### Same As in SafeHaven 4.0.2

* [SHBase-4.0.1-Mar-20-2017.ova](https://download.safehaven.ctl.io/SH-4.0.1/SHBase-4.0.1-Mar-20-2017.ova): OVA to be imported to private VMware vSphere envrionment as templates for SRN/CMS appliances
* [Script to Turn a Ubuntu-14 VM as a Recovery Proxy for Protected Windows VM](https://download.safehaven.ctl.io/SH-4.0.1/makestub_for_windows.sh)
* [Linux Onboarding Script](linux-onboarding-releases.md)

### New Downloads

* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-4.0.3/safehaven-4.0.3.deb): to be used in the cluster installer or GUI to update from SH-4.0.1/4.0.2
* [GUI Package](https://download.safehaven.ctl.io/SH-4.0.3/SafeHavenConsole-4.0.3.zip): zip file containing the JRE. This runs on any Windows platform.
  * [SafeHavenClient.4.0.3_win32.jar](https://download.safehaven.ctl.io/SH-4.0.3/SafeHavenClient.4.0.3_win32.jar): to replace the existing SafeHavenClient.jar inside the already downloaded 4.0. GUI folder.
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-4.0.3/safehaven_windows_driver-4.0.3.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-4.0.3/MakeStub-4.0.3.exe)
  
Please note that you can check the md5 checksum against the file named [MD5SUMS](https://download.safehaven.ctl.io/SH-4.0.3/MD5SUMS).

