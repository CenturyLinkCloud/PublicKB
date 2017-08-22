{{{
  "title": "SafeHaven 4.0.3 Release Notes",
  "date": "08-22-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 4.0.3.
- Release Date: August 21, 2017

### New Features and Enhancements

This is a patch release for [SafeHaven 4.0.2](safehaven-4.0.2-release.md), which is a patch release for [SafeHaven 4.0.1](safehaven-4.0.1-release.md).

* Add Support for Windows Server 2016
* Automatically resize storage pool when the backing storage is resized
* Fully support the migration use case
* Fully support servers with more than 10 disks
* Improve error logging in Windows server
* Added resiliency to PG resize
* Better support for Windows Dynamic Disks
* Better error handling of re-failover
* A number of minor GUI fixes such as typos, error messages, resolution problems etc

 
 ### Upgrade Path 

|Component|4.0.1->4.0.3|4.0.2->4.0.3|
|----|----|----| 
|GUI and Syntropy|Yes, no interruptions|Yes, no interruptions|
|SBD (WAN replication kernel module on SRN)|No change, therefore no need for upgrade|No change, therefore no need for upgrade|
|Windows Agent|Yes, reboot needed|Yes, reboot needed|
 

### Upgrade from 4.0.1 and 4.0.2

* **OVA and SBD module in the SRN is the same for 4.0.1, 4.0.2 and 4.0.3**

* **Upgrade Procedure** : [Upgrade Procedure for Minor Releases(Syntropy and GUI Console)](Upgrade-Procedure-for-Minor-Releases-Syntropy-and-GUI.md)
  * Note that to upgrade from 4.0.1 to 4.0.3, there is no need to upgrade to 4.0.2 first
* Note that once Syntropy is upgraded, only the Windows agent with matching version can work with new protections
  * Potentially for an already protected Windows server, it is possible to only upgrade Syntropy to 4.0.3 and keep the Windows Agent to 4.0.1 or 4.0.2
  * Upgrading the Windows Agent from 4.0.1/4.0.2 to 4.0.3 requires a reboot of the production Windows server

### Download Links

* [SHBase-4.0.1-Mar-20-2017.ova](https://download.safehaven.ctl.io/SH-4.0.1/SHBase-4.0.1-Mar-20-2017.ova): OVA to be imported to private VMware vSphere envrionment as templates for SRN/CMS appliances
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-4.0.3/safehaven-4.0.3.deb): to be used in the installer or GUI to update from SH-4.0.0
* [GUI Package](https://download.safehaven.ctl.io/SH-4.0.3/SafeHavenConsole-4.0.3.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.4.0.3_win32.jar](https://download.safehaven.ctl.io/SH-4.0.3/SafeHavenClient.4.0.3_win32.jar): to replace existing SafeHavenClient.jar inside the already downloaded 4.0.* GUI folder.
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-4.0.3/safehaven_windows_driver-4.0.3.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-4.0.3/MakeStub-4.0.3.exe)
* [Script to Turn a Ubuntu-14 VM as a Recovery Proxy for Protected Windows VM](https://download.safehaven.ctl.io/SH-4.0.1/makestub_for_windows.sh)
* [Linux Onboarding Script](./linux-onboarding-releases.md)
