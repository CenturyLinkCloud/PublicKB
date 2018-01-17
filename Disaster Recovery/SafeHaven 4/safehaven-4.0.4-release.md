{{{
  "title": "SafeHaven 4.0.4 Release Notes",
  "date": "12-18-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 4.0.4.
- Release Date: October 23, 2017

### New Features and Enhancements

This is a patch release for [SafeHaven 4.0.3](safehaven-4.0.3-release.md) with only **ONE** particular new feature: 

* at the time of automatically deploying the CLC recovery proxy servers using the SafeHaven GUI, the user now has a choice to NOT create  a new CLC folder. This will make it easier for the users to manage their DR infrastructure.

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

* Please note that **4.0.4 only changes GUI and Syntropy on top of 4.0.3**. 

* Even though the Windows agent shows different versions for 4.0.3 and 4.0.4, there is no real difference between them. Therefore, **it is perfectly OK to run 4.0.3 Windows agent while the GUI and Syntropy are upgraded to version 4.0.4.**

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
* [Linux Onboarding Script](linux-onboarding-releases.md)

#### New Downloads

* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-4.0.4/safehaven-4.0.4.deb): to be used in the cluster installer or GUI to update from SH-4.0.1/4.0.2/4.0.3
* [GUI Package](https://download.safehaven.ctl.io/SH-4.0.4/SafeHavenConsole-4.0.4.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.4.0.4_win32.jar](https://download.safehaven.ctl.io/SH-4.0.4/SafeHavenClient.4.0.4_win32.jar): to replace existing SafeHavenClient.jar inside the already downloaded 4.0.* GUI folder.
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-4.0.4/safehaven_windows_driver-4.0.4.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-4.0.4/MakeStub-4.0.4.exe)
  
Please note that you can check the md5 checksum against the file named [MD5SUMS](https://download.safehaven.ctl.io/SH-4.0.4/MD5SUMS).

#### safehaven_windows_driver-4.0.4-hotfix1.exe

Please note this hotfix release is only needed if you are having problem running the Manager.exe installed from the official 4.0.4 release above. 

For Windows Server 2008 R2 with the installation of an optional Microsoft hotfix  [KB2647409](https://support.microsoft.com/kb/2647409), the `Manager.exe` installed by the official 4.0.4 SafeHaven Windows driver would fail to proceed due to the failure to confirm the existence of a depedent Microsoft hotfix [KB2550978](https://support.microsoft.com/kb/2550978). This is because [KB2647409](https://support.microsoft.com/kb/2647409) already includes the fix needed for [KB2550978](https://support.microsoft.com/kb/2550978 ) so that [KB2647409](https://support.microsoft.com/kb/2647409) blocks the installation of [KB2550978](https://support.microsoft.com/kb/2550978)  (but not vice versa, ie, installing [KB2647409](https://support.microsoft.com/kb/2647409) after installing [KB2550978](https://support.microsoft.com/kb/2550978) is perfectly fine). The SafeHaven-4.0.4-hotfix1 provides a fix that would skip the check for [KB2550978](https://support.microsoft.com/kb/2550978) if [KB2647409](https://support.microsoft.com/kb/2647409) is already in place. 

* New download link for [safehaven_windows_driver-4.0.4-hotfix1.exe](https://download.safehaven.ctl.io/SH-4.0.4/safehaven_windows_driver-4.0.4-hotfix1.exe)
* If the 4.0.4 driver is already installed, in order to avoid an unecessary reboot, one can choose the "Customized Installation" instead of the default "Express Installation" and under the "Expert Installation" section, only select the "Install SafeHaven Manager" option. This way, only the `manager.exe` is replaced and no reboot is needed.
