{{{
  "title": "bpimager Appliance Import Requirements for Ecosystem Partners",
  "date": "2-23-2016",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}


Allow CenturyLink customers to instantly deploy your virtual appliance within their private space on our IaaS Cloud.  

**This program is available to all registered Ecosystem partners working with an Integration Engineer**

### Getting Started

Get started by acquiring the following:

* Locate your virtual appliance source in a compatible format (see requirements below)
* Document the sizing paramerters (CPU, RAM, Storage)
* Send this information to your assigned Integration Engineer or if you don't have one contact ECOSystem@centurylink.com


### Requirements

Appliances meeting the following specifications may be compatible for instant deploy using bpimager:

* Linux-based operating system.  We have proven support for anything RPM, Deb, or Gentoo based
* All partitions on a single virtual disk with size not to exceed 1TB
* Server ready for use on boot (no first-boot console configuration can be applied)
* Partition file types one of: ReisferFS, ext*, LVM, md
* Disk formatted as vmdk, raw, or other common file type


### bpimager Deploy Process

Your virtual appliance will be cloned and some CenturyLink Cloud platform-specific modifications will be made:

* Root password will be modified to match what customer provides
* Static IP address networking and DNS will be configured based on customer specifications

