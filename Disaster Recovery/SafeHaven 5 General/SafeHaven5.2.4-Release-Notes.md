{{{
  "title": "SafeHaven 5.2.4 Release Notes",
  "date": "03-13-2020",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Release Notes

- SafeHaven Version: 5.2.4
- Release Date: March 13, 2019

### New Features and Enhancements

This is patch release based on [SafeHaven 5.2.3](SafeHaven5.2.3-Release-Notes.md) with the following improvements:

- Improve on the Windows checkpoint status report
- Added features needed by the [CAM DR product](../../Cloud Application Manager/DR Readiness/Enable DR.md)

### Upgrade Path

* Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.
* SafeHaven-5.0.1 and SafeHaven-5.1.* can be upgraded to 5.2.4 using the GUI but the SRN kernel and base package needs manual upgrade
  * Note that even though it is possible to just upgrade the debian package using the GUI without updating the kernel and base package, it is highly recommended to update the kernel and base package to benefit from the bug fix and also avoid complications on technical support
  * It is recommended that customers obtain help from the SafeHaven support team to perform the kernel and base package upgrade. Please create tickets via help@ctl.io
  * Only **expert** users may follow this [Upgrade procedure for SafeHaven 5.2](SH-5.1-Upgrade-5.2.md) on their own
* SafeHaven-5.2.* can be upgraded to 5.2.4 using the GUI.  

### SafeHaven Most Recent Releases

Please take a look at the link below to download the latest available release  
[Most recent Release updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md)

### Download Links

* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.2.4/safehaven-5.2.4.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.2.4/SafeHavenConsole-5.2.4.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.2.4_win64.jar](https://download.safehaven.ctl.io/SH-5.2.4/SafeHavenClient.5.2.4_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.2.4/safehaven_windows_driver-5.2.4.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.2.4/MakeStub-5.2.4.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](linux-onboarding-releases.md)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.2.4/makestub_for_windows.sh)

Please note that you can check the md5 checksum against the file named [MD5SUM-5.2.4.txt](https://download.safehaven.ctl.io/SH-5.2.4/MD5SUM-5.2.4.txt).

### Documentations

[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-Azure.xlsm)
