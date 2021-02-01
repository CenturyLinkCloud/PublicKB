{{{
  "title": "SafeHaven 5.1.4 Release Notes",
  "date": "02-12-2019",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Release Notes

- SafeHaven Version: 5.1.4
- Release Date: Februray 12, 2019

### New Features and Enhancements
This is patch release based on [SafeHaven 5.1.3](SafeHaven5.1.3-Release-Notes.md) with the following improvements:
- Upgrade of the Windows agent will no longer require rebooting the production server if there is already a kernel driver running with matching kernel version
- An upstream AWS SDK bugfix was applied to fix a rare multiple checkpoints deletion problem
- Fixed a bug where automated test failover deletion job is reported as unknown 
- Fixed a bug where the protection group fails to reconsitute in a rare condition upon network failure

### Upgrade Path
* Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.
* SafeHaven-5.0.1 can be upgraded to 5.1.4 using the GUI.
* SafeHaven-5.1.* can be upgraded to 5.1.4 using the GUI.

### SafeHaven Most Recent Releases
Please take a look at the link below to download the latest available release  
[Most recent Release updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md)

### Download Links
* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.1.4/safehaven-5.1.4.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.1.4/SafeHavenConsole-5.1.4.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.1.4_win64.jar](https://download.safehaven.ctl.io/SH-5.1.4/SafeHavenClient.5.1.4_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.1.4/safehaven_windows_driver-5.1.4.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.1.4/MakeStub-5.1.4.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](linux-onboarding-releases.md)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.1.4/makestub_for_windows.sh)

Please note that you can check the md5 checksum against the file named [MD5SUM-5.1.4.txt](https://download.safehaven.ctl.io/SH-5.1.4/MD5SUM-5.1.4.txt).


### Documentations
[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-Azure.xlsm)
 
