
{{{
  "title": "SafeHaven 5.0.0 Release Notes",
  "date": "12-29-2017",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Release Notes

- SafeHaven Version: 5.0.0
- Release Date: December 29, 2017

### New Features and Enhancements
#### New Use Case: Use of Amazon Web Services (AWS) as a Disaster Recovery Site

One of the major feature's of this release is the capability to protect production servers on **multiple hypervisors** and failover to **AWS**. Examples of validated hypervisors are:
* VMware: including VMware based cloud platforms such as CenturyLink Cloud, CenturyLink Private Cloud on VMware Cloud Foundation (vCloud Director), etc.
* Hyper-V Generation 1
* Xen(AWS)
* KVM
* Physical servers: all the available baremetal servers provided by CLC have been validated

**NOTE**: Please refer to [SafeHaven-5.0-Use-Case-and-Support-Matrix](SafeHaven-5.0-Use-Case-and-Support-Matrix.md) for more information on all the use cases and support matrix.

#### Microsoft Virtual Shadow Copy (VSS) Enabled Checkpoints
Another major feature is the introduction of Microsoft Virtual Shadow Copy (VSS) enabled checkpoint for single Windows server protection groups.

**NOTE**:This feature is available for both recovery into AWS as well as CenturyLink Cloud (CLC).

#### Built-in network isolation capability via GUI
Introduced built-in network isolation capability via GUI for recovery servers running on the same subnet as the recovery SRN.

**NOTE**:This feature is ONLY available for Windows Production VMs when the recovery site is CenturyLink Cloud (CLC).

### Upgrade Path
This is the first major release in the SafeHaven-5 product line and there is no upgrade path from any previous SafeHaven versions. Even the appliances (CMS/SRN) used in previous versions cannot be reused in SafeHaven-5 since it uses Ubuntu-16.04 as the base OS for the first time (in comparision, SafeHaven-4 uses Ubuntu-14.04 as the base OS).

**NOTE**: Upgrade from SafeHaven-4 to SafeHaven-5 will be a fresh new installation.

### SafeHaven Most Recent Releases
Please take a look at the link below to download the latest available release
https://www.ctl.io/knowledge-base/disaster-recovery/overview/most-recent-safehaven-release-updates/

### Download Links
* [SafeHavenAppliance-5.0.0.ova](https://download.safehaven.ctl.io/SH-5.0.0/SafeHavenAppliance-5.0.0.ova): OVA to be imported to private VMware vSphere or vCloud Director envrionment as templates for SRN/CMS appliances
* [Ubuntu-16.vhdx](https://download.safehaven.ctl.io/SH-5.0.0/Ubuntu-16.vhdx): Hyper-V image for SRN/CMS appliances in a private Hyper-V envrionment
* [Debian Package for CMS/SRN](https://download.safehaven.ctl.io/SH-5.0.0/safehaven-5.0.0.deb): to be used in the cluster installer
* [GUI Package](https://download.safehaven.ctl.io/SH-5.0.0/SafeHavenConsole-5.0.0.zip): zip file containing the JRE, runs on any Windows platform
  * [SafeHavenClient.5.0.0_win32.jar](https://download.safehaven.ctl.io/SH-5.0.0/SafeHavenClient.5.0.0_win32.jar): the Java application that requires an existing 32bit JRE-8 to run on a Windows OS
* Windows Downloads:
  * [Driver Installer](https://download.safehaven.ctl.io/SH-5.0.0/safehaven_windows_driver-5.0.0.exe)
  * [MakeStub.exe](https://download.safehaven.ctl.io/SH-5.0.0/MakeStub-5.0.0.exe)
* [Linux SafeHaven Onboarding Scripts Downloads](https://download.safehaven.ctl.io/SH-5.0.0/safehaven_linux_onboarding_scripts-5.0.0.tar.gz)

Please note that you can check the md5 checksum against the file named [MD5SUMS](https://download.safehaven.ctl.io/SH-5.0.0/MD5SUMS).

### Documentations

[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-1.xlsm)
