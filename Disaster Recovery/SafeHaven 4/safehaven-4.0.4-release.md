{{{
  "title": "SafeHaven 4.0.4 Release Notes",
  "date": "10-23-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 4.0.4.
- Release Date: October 23, 2017

### New Features and Enhancements

This is a patch release for [SafeHaven 4.0.3](safehaven-4.0.3-release.md) with only one particular new feature: at time of automatically deploying the recovery proxies using the GUI, the user now have the choice of not to create a new folder.

Reference links to previous 4.0.x series releases:
*  [SafeHaven 4.0.3](safehaven-4.0.3-release.md)
*  [SafeHaven 4.0.2](safehaven-4.0.2-release.md)
*  [SafeHaven 4.0.1](safehaven-4.0.1-release.md)



 
 ### Upgrade Path 

|Component|4.0.1->4.0.4|4.0.2->4.0.4|4.0.3->4.0.4
|----|----|----|----| 
|GUI and Syntropy|Yes, no interruptions|Yes, no interruptions|Yes, no interruptions|
|Windows Agent|Yes, reboot needed|Yes, reboot needed|No need for upgrade|
|SBD (WAN replication kernel module on SRN)|No change|No change| No change|

### Upgrade from 4.0.3

Please note that 4.0.4 only changes GUI and Syntropy on top of 4.0.3. Even though the Windows agent shows different versions for 4.0.3 and 4.0.4, there is no real difference between them. Therefore, it is perfectly OK to run Windows agent with version 4.0.3 while the GUI and Syntropy are upgraded to version 4.0.4.

### Upgrade from 4.0.1 and 4.0.2

* **OVA and SBD module in the SRN is the same for 4.0.1, 4.0.2, 4.0.3 and 4.0.4**: there is no need to upgrade them.

* **Upgrade Procedure** : [Upgrade Procedure for Minor Releases(Syntropy and GUI Console)](Upgrade-Procedure-for-Minor-Releases-Syntropy-and-GUI.md)
  * Note that to upgrade from 4.0.1 to 4.0.4, there is no need to upgrade to 4.0.2 or 4.0.3 first
  * Note that once Syntropy is upgraded, only the Windows agent with matching version can work with new protections
  * Potentially for an already protected Windows server, it is possible to only upgrade Syntropy to 4.0.4 and keep the Windows Agent to 4.0.1 or 4.0.2
  * Upgrading the Windows Agent from 4.0.1/4.0.2 to 4.0.4 requires a reboot of the production Windows server

### Download Links

#### Same As in SafeHaven-4.0.1

* [SHBase-4.0.1-Mar-20-2017.ova](https://download.safehaven.ctl.io/SH-4.0.1/SHBase-4.0.1-Mar-20-2017.ova): OVA to be imported to private VMware vSphere envrionment as templates for SRN/CMS appliances
* [Script to Turn a Ubuntu-14 VM as a Recovery Proxy for Protected Windows VM](https://download.safehaven.ctl.io/SH-4.0.1/makestub_for_windows.sh)
* [Linux Onboarding Script](./linux-onboarding-releases.md)

### New Downloads

* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-4.0.4/safehaven-4.0.4.deb): to be used in the cluster installer or GUI to update from SH-4.0.1/4.0.2/4.0.3
* [GUI Package](https://download.safehaven.ctl.io/SH-4.0.4/SafeHavenConsole-4.0.4.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.4.0.4_win32.jar](https://download.safehaven.ctl.io/SH-4.0.4/SafeHavenClient.4.0.4_win32.jar): to replace existing SafeHavenClient.jar inside the already downloaded 4.0.* GUI folder.
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-4.0.4/safehaven_windows_driver-4.0.4.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-4.0.4/MakeStub-4.0.4.exe)
  
Please note that you can check the md5 checksum against the file named [MD5SUMS](https://download.safehaven.ctl.io/SH-4.0.4/MD5SUMS).

