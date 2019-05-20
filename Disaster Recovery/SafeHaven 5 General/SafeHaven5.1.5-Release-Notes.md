{{{
  "title": "SafeHaven 5.1.5 Release Notes",
  "date": "05-02-2019",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Release Notes

- SafeHaven Version: 5.1.5
- Release Date: May 2, 2019

### New Features and Enhancements
This is patch release based on [SafeHaven 5.1.4](SafeHaven5.1.4-Release-Notes.md) with the following improvements:
- Support for HTTP proxy for environments that do not have direct outgoing access to Internet
- Support for Azure PG Resize
- Support for better recovery upon temporary network disruptions

### Upgrade Path
* Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.
* SafeHaven-5.0.1 can be upgraded to 5.1.5 using the GUI.
* SafeHaven-5.1.* can be upgraded to 5.1.5 using the GUI.

### SafeHaven Most Recent Releases
Please take a look at the link below to download the latest available release  
[Most recent Release updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md)

### Download Links
* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.1.5/safehaven-5.1.5.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.1.5/SafeHavenConsole-5.1.5.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.1.5_win64.jar](https://download.safehaven.ctl.io/SH-5.1.5/SafeHavenClient.5.1.5_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.1.5/safehaven_windows_driver-5.1.5.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.1.5/MakeStub-5.1.5.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](linux-onboarding-releases.md)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.1.5/makestub_for_windows.sh)

Please note that you can check the md5 checksum against the file named [MD5SUM-5.1.5.txt](https://download.safehaven.ctl.io/SH-5.1.5/MD5SUM-5.1.5.txt).


### Documentations
[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-Azure.xlsm)
 
