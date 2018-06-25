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
https://www.ctl.io/knowledge-base/disaster-recovery/overview/most-recent-safehaven-release-updates/

 
### Documentations
 

[SafeHaven Inventory Sheet](https://download.safehaven.ctl.io/SH-5-Docs/SafeHaven-Inventory-Sheet-1.xlsm)


Please note that you can check the md5 checksum against the file named [MD5SUMS](https://download.safehaven.ctl.io/SH-5.0.1/MD5SUMS).
