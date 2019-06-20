{{{
  "title": "SafeHaven 5.2.0 Release Notes",
  "date": "06-13-2019",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Release Notes

- SafeHaven Version: 5.2.0
- Release Date: June 13, 2019

### New Features and Enhancements
This is new minor released based on [SafeHaven 5.2.0](SafeHaven5.2.0-Release-Notes.md) with the following improvements:
- New SafeHaven Replication Node (SRN) Linux kernel module for WAN replication (SBD) that fixes a rare data corruption case
- New SRN base package that 
  - uses an updated version of the Ansible library for automated driver installation or makestub
  - improves the sbd log rotation
- Bug fix where a local replica protection group data replication does not resume automatically upon network interruption  

### Upgrade Path
* Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.
* SafeHaven-5.0.1 and SafeHaven-5.1.* can be upgraded to 5.2.0 using the GUI but the SRN kernel and base package needs manual upgrade
  * Note that even though it is possible to just upgrade the debian package using the GUI without updating the kernel and base package, it is highly recommended to update the kernel and base package to benefit from the bug fix and also avoid complications on technical support
  * It is recommended that customers obtain help from the SafeHaven support team to perform the kernel and base package upgrade. Please create tickets via help@ctl.io

### SafeHaven Most Recent Releases
Please take a look at the link below to download the latest available release  
[Most recent Release updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md)

### Download Links
* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.2.0/safehaven-5.2.0.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.2.0/SafeHavenConsole-5.2.0.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.2.0_win64.jar](https://download.safehaven.ctl.io/SH-5.2.0/SafeHavenClient.5.2.0_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.2.0/safehaven_windows_driver-5.2.0.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.2.0/MakeStub-5.2.0.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](linux-onboarding-releases.md)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.2.0/makestub_for_windows.sh)

Please note that you can check the md5 checksum against the file named [MD5SUM-5.2.0.txt](https://download.safehaven.ctl.io/SH-5.2.0/MD5SUM-5.2.0.txt).


### Documentations
[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-Azure.xlsm)
 
