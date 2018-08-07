{{{
  "title": "SafeHaven 5.1.1 Release Notes",
  "date": "08-07-2018",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Release Notes

- SafeHaven Version: 5.1.1
- Release Date: August 7, 2018

### New Features and Enhancements
This is patch release based on [SafeHaven 5.1.0](SafeHaven5.1.0-Release-Notes.md) with the following improvements:
- Use managed storage for Microsoft Azure, to be consistent with Azure and CenturyLink directions
- Introduce the Azure Statistics tab in the GUI
- Allow the automatically LRA installation using a non-Administrator username
- Fixed power operation bug in failback
- Fixed a bug where changes to email configuration is not effective until the CMS manager service is restarted 


### Upgrade Path
* Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.
* SafeHaven-5.0.1 can be upgraded to 5.1.1 using the GUI.
* SafeHaven-5.1.0 can be upgraded to 5.1.1 using the GUI.

### SafeHaven Most Recent Releases
Please take a look at the link below to download the latest available release  
[Most recent Release updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md)

### Download Links
* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.1.1/safehaven-5.1.1.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.1.1/SafeHavenConsole-5.1.1.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.1.1_win64.jar](https://download.safehaven.ctl.io/SH-5.1.1/SafeHavenClient.5.1.1_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.1.1/safehaven_windows_driver-5.1.1.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.1.1/MakeStub-5.1.1.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](https://download.safehaven.ctl.io/SH-5.1.1/safehaven_linux_onboarding_scripts-5.1.1.tar.gz)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.1.1/makestub_for_windows.sh)

Please note that you can check the md5 checksum against the file named [MD5SUM-5.1.1.txt](https://download.safehaven.ctl.io/SH-5.1.1/MD5SUM-5.1.1.txt).


### Documentations
[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-Azure.xlsm)
 
