{{{
  "title": "SafeHaven 4.0.2 Release Notes",
  "date": "05-03-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 4.0.2.
- Release Date: May 3, 2017

### New Features and Enhancements

This is a patch release for [SafeHaven 4.0.1](https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-4/safehaven-4.0.1-release/). 

The following three features/bug-fixes have been introduced:
1. Improving CMS performance under certain conditions by reducing file writes.
2. Allowing the deletion of a protection group in a "Failover" state.
3. Slight improvement of the Test Failover temporary space allocation policy.
   * There is a bare minimum temporary space requirement of 2GB.
   * GUI will suggest a default of 5GB temporary space.
   * Automatic deletion of the test failover instance when there is less than 1GB of free space left.
   
### Upgrade from 4.0.1 to 4.0.2

* **No changes for OVA, Driver Installer, MakeStub.exe packages**

* **Upgrade Procedure from 4.0.1 to 4.0.2** [SafeHaven-4-Upgrade Procedure for Minor Releases(Syntropy and GUI Console)](https://github.com/MahimaKumar/PublicKB/blob/master/Disaster%20Recovery/SafeHaven%204/SafeHaven-4-Upgrade%20Procedure%20for%20Minor%20Releases(Syntropy%20and%20GUI%20Console).md)


### Download Links

* [SHBase-4.0.1-Mar-20-2017.ova](https://download.safehaven.ctl.io/SH-4.0.1/SHBase-4.0.1-Mar-20-2017.ova): OVA to be imported to private VMware vSphere envrionment as templates for SRN/CMS appliances
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-4.0.2/safehaven-4.0.2.deb): to be used in the installer or GUI to update from SH-4.0.0
* [GUI Package](https://download.safehaven.ctl.io/SH-4.0.2/SafeHavenConsole-4.0.2.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.4.0.2_win32.jar](https://download.safehaven.ctl.io/SH-4.0.2/SafeHavenClient.4.0.2_win32.jar): to replace existing SafeHavenClient.jar inside the already downloaded 4.0.0 GUI folder.
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-4.0.2/safehaven_windows_driver-4.0.2.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-4.0.2/MakeStub-4.0.2.exe)
* [Script to Turn a Ubuntu-14 VM as a Recovery Proxy for Protected Windows VM](https://download.safehaven.ctl.io/SH-4.0.1/makestub_for_windows.sh)
* [Linux Onboarding Script](./linux-onboarding-releases.md)
