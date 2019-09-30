{{{
  "title": "SafeHaven 5.1.3 Release Notes",
  "date": "10-29-2018",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Release Notes

- SafeHaven Version: 5.1.3
- Release Date: October 29, 2018

### New Features and Enhancements
This is patch release based on [SafeHaven 5.1.2](SafeHaven5.1.2-Release-Notes.md) with the following improvements:
- There are a number of improvements for the Windows Agent such as 
  - A hanging VSS provider/writer would no longer impact future non-VSS checkpoints
  - Full support for Windows storage space
  - Improved event log
- A unified job system is now working for both Generation 1 (DR to CLC) and Generate 2 (DR to AWS/Azure) protection groups (PG)
- Better timeout handling for LVM commands
- An improved method for local cache PG resize

### Upgrade Path
* Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.
* SafeHaven-5.0.1 can be upgraded to 5.1.3 using the GUI.
* SafeHaven-5.1.* can be upgraded to 5.1.3 using the GUI.

### SafeHaven Most Recent Releases
Please take a look at the link below to download the latest available release  
[Most recent Release updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md)

### Download Links
* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.1.3/safehaven-5.1.3.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.1.3/SafeHavenConsole-5.1.3.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.1.3_win64.jar](https://download.safehaven.ctl.io/SH-5.1.3/SafeHavenClient.5.1.3_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.1.3/safehaven_windows_driver-5.1.3.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.1.3/MakeStub-5.1.3.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](linux-onboarding-releases.md)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.1.3/makestub_for_windows.sh)

Please note that you can check the md5 checksum against the file named [MD5SUM-5.1.3.txt](https://download.safehaven.ctl.io/SH-5.1.3/MD5SUM-5.1.3.txt).


### Documentations
[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-Azure.xlsm)
 
