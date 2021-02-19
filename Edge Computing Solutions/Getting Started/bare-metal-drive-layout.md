{{{
    "title":"Bare Metal Drive Layout",
    "date":"2/21/2021",
    "author":"Keith Bierman",
    "attachments": [],
    "contentIsHTML": false, 
    "sticky": false
}}}

### Description

This article applies specifically to the Edge Bare Metal servers which are Dell C6420 hardware systems, and explains how storage is delivered in these systems.

### Details

At time of deployment, only the boot drive is formatted and configured for the installed Operating System.
The other drives are available for customer use as they see fit.

**The boot drive for Linux Operating Systems is configured as follows:**

1. /boot/efi  [1] a "fat32" partition used for booting the Operating System. In our deployments this is typically 536MiB
2. The rest of the disk is configured to use LVM [2]. This allows post deployment configuration, including adding storage from other available local disks as needed.
3. A relatively small "os-root" mounted at / to provide the initial area for the installed operating system.
4. Leaving just under 180GiB for post-deployment user configuration.

### References:

1.  https://en.wikipedia.org/wiki/EFI_system_partition
2.  https://tldp.org/HOWTO/LVM-HOWTO/
3.  DISA STIG  <http://static.open-scap.org/ssg-guides/ssg-rhel8-guide-stig.html>

[3] provides strong recommendations about specific ways to carve up, and what options should be applied to specific directories. By providing the system configured with LVM, customers can implement the requirements of this Standard.

This allows freedom to use any filesystem supported by the Operating System the customer has selected. For Linux systems that is usually some combination of ext{2,3,4}, xfs, btrfs, or even zfs. Lumen places no limitations on the customer choice of filesystem.

The precise amount of disk space in any given initial partition is subject to change.
