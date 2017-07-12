{{{
  "title": "Boot from Primary Data Storage for a Linux Protection Group",
  "date": "06-28-2017",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview

This article explains how to boot from a Production VM from primary data storage after it has been configured to boot from iSCSI disks for failback. This is the last step for failback 

**NOTE**: To follow this step the user MUST have already completed Failback Phase 1 and Phase 2 covered in "Failback a Linux Protection Group" KB Article

### Requirements

1. The protection group has already been Failed Back from the DR site back to its production site. The Production site is the active site now.
2. The Production server should be configured with makestub.sh to boot from the disk of the production SRN.
3. The Production Server should be successfully booted from the production SRN's disks.

### Assumptions

This article assumes that the user has already performed Failback Phase 1 and Phase 2, and the Production VM has been configured with makestub.sh and is booting from the iSCSI disks. Now the user wants to copy data from the iSCSI disks to the production VM's local disk and then boot the VM from the Primary Storage.

For the purpose of this article, we have used Ubuntu 14 as a production server in CenturyLink's CA2(Toronto) production datacenter. The recovery site being used is CenturyLink's WA1(Washington) recovery datacenter.

### Boot from local storage
Right click on the Linux protection group, and click ** Boot from Primary Data Storage**
![Linux](../../images/SH4.0/LinuxFailover/LF33.png)

Select the Linux Protection group then click ** Next**
![Linux](../../images/SH4.0/LinuxFailover/LF34.png)

Login to the production server, and go to "Safehaven _linux_onboarding" directory
![Linux](../../images/SH4.0/LinuxFailover/LF35.png)

Run **./rsync2local.sh**. Use -d to run with default parameters.
This script will copy the data from the SRN's disks to the production VM's local disks.
![Linux](../../images/SH4.0/LinuxFailover/LF36.png)

Type ** YES** when the script asks ** Are you sure you want to continue?**
![Linux](../../images/SH4.0/LinuxFailover/LF37.png)

The script will now copy all the files from the SRN's disks to the production VM's local disks. This may take some time.
Once the copy is complete, the script will automatically reboot the VM if it was run with -d option.
![Linux](../../images/SH4.0/LinuxFailover/LF38.png)

Go back to SafeHaven Console, check both **Manual setup needed** and ** Manual Reboot needed** boxes, then click ** Next**
![Linux](../../images/SH4.0/LinuxFailover/LF39.png)
Wait till ** Register boot from Primary Data Storage** is completed, click **Finish** to leave the wizard.
![Linux](../../images/SH4.0/LinuxFailover/LF40.png)

This concludes the Failback of a Linux Protection Group. The production VM and the Protection group should be in the same state that they were before failover.
