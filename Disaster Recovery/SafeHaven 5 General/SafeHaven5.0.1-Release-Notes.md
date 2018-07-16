{{{
  "title": "SafeHaven 5.0.1 Release Notes",
  "date": "03-27-2018",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 5.0.1
- Release Date: March 27, 2018

### New Features and Enhancements
This is a patch release for [SafeHaven 5.0.0](SafeHaven5.0.0-Release-Notes.md) with the following improvements:
- Ensured the proper vSphere library is installed in the [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova)
- An improved internal messaging implementation between SafeHaven nodes to meet even more demanding scalability and security requirements. 
- Simplified communication  among SafeHaven nodes by not using UDP ports, making it easier to setup.
- Added disk resize funtionality for AWS PGs.
- Now supports the SRNs with Windows local cache PG(s) to be gracefully rebooted. To reboot SRNs protecting Linux Protection Groups please contact Safehaven team via help@ctl.io


### Upgrade Path
**NOTE**: Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.

### SafeHaven Most Recent Releases
Please take a look at the link below to download the latest available release   
[Most recent Release updates](../Overview/Most-Recent-SafeHaven-Release-Updates.md)


### Download Links
* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.0.1/safehaven-5.0.1.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenConsole-5.0.1.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.0.1_win64.jar](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenClient.5.0.1_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.0.1/safehaven_windows_driver-5.0.1.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.0.1/MakeStub-5.0.1.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](https://download.safehaven.ctl.io/SH-5.0.1/safehaven_linux_onboarding_scripts-5.0.1.tar.gz)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.0.1/makestub_for_windows.sh)
 
Please note that you can check the md5 checksum against the file named [MD5SUMS](https://download.safehaven.ctl.io/SH-5.0.1/MD5SUMS).

#### SH-5.0.1-hotfix1
This hotfix only addresses one problem: improve the email report format as well as report on latest instead of oldest checkpoints.

Download links:
* [safehaven-5.0.1-hotfix1.deb](https://download.safehaven.ctl.io/SH-5.0.1/safehaven-5.0.1-hotfix1.deb): Debian package to be used in the cluster installer or GUI code update dialog.
* [SafeHavenConsole-5.0.1-hotfix1.zip](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenConsole-5.0.1-hotfix1.zip): zip file containing the JRE, runs on any Windows platform. No real change rather than matching the version of the debian package.
  * [SafeHavenClient.5.0.1-hotfix1_win64.jar](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenClient.5.0.1-hotfix1_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS. For quick upgrading, can be used to replace the existing SafeHavenClient.jar
 
### Documentations
 

[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-1.xlsm)


Please note that you can check the md5 checksum against the file named [MD5SUMS](https://download.safehaven.ctl.io/SH-5.0.1/MD5SUMS).
