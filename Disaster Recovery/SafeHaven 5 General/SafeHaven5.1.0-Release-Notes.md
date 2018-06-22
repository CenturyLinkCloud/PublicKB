{{{
  "title": "SafeHaven 5.1.0 Release Notes",
  "date": "06-22-2018",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Release Notes

- SafeHaven Version: 5.1.0
- Release Date: June 22, 2018

### New Features and Enhancements
This is a feature release based on [SafeHaven 5.0.1](SafeHaven5.0.1-Release-Notes.md) with the following new features:
- Add support to use Microsoft Azure as disaster recovery data center. Please refer to the [SafeHaven KBs](../) for more detailed documentation on the "DR to Azure" use case.
- Introduce a new job system 

It also comes with a number of bug fixes such as
- removing the network isolation checkbox in GUI for Linux PG since there is no such capability
- providing a way to enter new license key in GUI after the old license is expired
- fixing the bug where an AWS PG does not automatically resume sync after a temporary network outage
- and more...


### Upgrade Path
* Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.
* It is possible to upgrade from SafeHaven-5.0.1 to version 5.1.0 using the GUI. 

### Download Links
* [SafeHavenAppliance-5.0.1.ova](https://download.safehaven.ctl.io/SH-5.0.1/SafeHavenAppliance-5.0.1.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.1.0/safehaven-5.1.0.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.1.0/SafeHavenConsole-5.1.0.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.1.0_win64.jar](https://download.safehaven.ctl.io/SH-5.1.0/SafeHavenClient.5.1.0_win64.jar): the Java application that requires an existing 64bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.1.0/safehaven_windows_driver-5.1.0.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.1.0/MakeStub-5.1.0.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](https://download.safehaven.ctl.io/SH-5.1.0/safehaven_linux_onboarding_scripts-5.1.0.tar.gz)
* [script to turn a Ubuntu-14 machine into a recovery proxy for Windows servers](https://download.safehaven.ctl.io/SH-5.1.0/makestub_for_windows.sh)
 
Please note that you can check the md5 checksum against the file named [MD5SUM-5.1.0.txt](https://download.safehaven.ctl.io/SH-5.1.0/MD5SUM-5.1.0.txt).
