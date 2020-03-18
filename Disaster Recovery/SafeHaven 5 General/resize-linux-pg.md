{{{
  "title": "Expand Linux Protection Group",
  "date": "03-16-2020",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Outline

Suppose a Linux server protected by SafeHaven-5 has been expanded, in other words running on a larger file system,  a number of steps needs to be taken in order to sure the SafeHaven protection continue to work with the enlarged system. The high-level steps are

1. Using the SafeHaven GUI, [expand the SafeHaven protection group and protected disk](../SafeHaven 4/SafeHaven-4-Expand Protection Group Size.md):
  1.1 Ensure both SRNs contain sufficient free capacity in the correspondig storage pools
  1.2 Enlarge the protection group
  1.3 Enlarge the protected disk within the protection group

2. On the protected Linux server itself, run as root user to
  2.1 Ensure the iSCSI Disk has been expanded
  2.2 Expand the root file system partition
  2.3 Expand the root file system
  2.4 Test to confirm

The details of step 1 have been documented in [this KB](../SafeHaven 4/SafeHaven-4-Expand Protection Group Size.md) while the details of step 2 is documented below.

### Step 2: Resize the iSCSI Target from Protected Linux Server

* This step assumes step 1 is already taken.
* The following commands are to be run with root user privileges.

#### 2.1 Ensure the iSCSI Disk is Expanded

After the step 1 of resizing protection group and protected disk, the iSCSI disk LUN should change to its new size.

First, we need to find the path of the iSCSI disk presented by SafeHaven. Run `lsscsi` to find out. For example

```bash
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# lsscsi -t
[0:0:0:0]    cd/dvd  ata:                            /dev/sr0 
[2:0:0:0]    disk    spi:0                           /dev/sda 
[2:0:1:0]    disk    spi:1                           /dev/sdb 
[2:0:2:0]    disk    spi:2                           /dev/sdc 
[3:0:0:0]    disk    iqn.2016-09.io.ctl:WA1SHSJ-U18-01-PG-WA1SHSJ-U18-01-external,t,0x1  /dev/sdd 
```

In this example, the iSCSI disk path is `/dev/sdd`.

Secondly, we could run the `lsblk` command to check its disk size. It is possible that the disk size is not changed until a SCSI bus rescan. To enforce a refresh via a SCSI bus rescan, we can run

```bash
# Rescan all appliable SCSI buses.
for SCSI_SCAN in /sys/class/scsi_host/host*/scan; do
  echo "- - -" > ${SCSI_SCAN}
done
```

In this example, the size of `sdd` changes from 26GB to 30GB after the above rescan and we have

```bash
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# lsblk
NAME                   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda                      8:0    0   10G  0 disk 
`-sda1                   8:1    0  487M  0 part /boot
sdb                      8:16   0    2G  0 disk [SWAP]
sdc                      8:32   0   14G  0 disk /
sdd                      8:48   0   30G  0 disk 
|-sdd1                   8:49   0    1M  0 part 
|-sdd2                   8:50   0  487M  0 part 
`-sdd3                   8:51   0 25.5G  0 part 
  |-vg_iscsi18-swap_lv 253:0    0    2G  0 lvm  
  `-vg_iscsi18-root_lv 253:1    0 23.5G  0 lvm  /opt/datagardens/rootfs
sr0                     11:0    1 1024M  0 rom  
```

#### 2.2 Expand the root File System Partition

There are two different cases depending on the DR cloud type.

##### 2.2.1 DR Sites on VMware/CLC/vCloud: Expand Logical Volume

In this case, the iSCSI disk is partition to support Logical Volume Manager (LVM). We could check its disk partition with the `gdisk` tool as

```bash
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# gdisk -l /dev/sdd
GPT fdisk (gdisk) version 1.0.3

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.
Disk /dev/sdd: 62914560 sectors, 30.0 GiB
Model: disk_00         
Sector size (logical/physical): 512/512 bytes
Disk identifier (GUID): E4D3AF94-DE60-4E74-9420-56CA8DA39F74
Partition table holds up to 128 entries
Main partition table begins at sector 2 and ends at sector 33
First usable sector is 34, last usable sector is 54525918
Partitions will be aligned on 2048-sector b`oundaries
Total free space is 4061 sectors (2.0 MiB)

Number  Start (sector)    End (sector)  Size       Code  Name
   1            2048            4096   1024.5 KiB  EF02  grub bios boot
   2            6144         1003519   487.0 MiB   8300  boot partition
   3         1003520        54525918   25.5 GiB    8E00  PV for vg_iscsi18
```

And the `pvs` command will confirm that the `/dev/sdd3` parition is the physical volume used for the iSCSI target.

```bash
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# pvs
  PV         VG         Fmt  Attr PSize   PFree
  /dev/sdd3  vg_iscsi18 lvm2 a--  <25.52g    0 
```

We could use the `parted` command to resize the partition 3.

First time launching `parted /dev/sdd` will have a warning message, since the disk size has changed and the GPT partition table needs to be updated. Please enter `Fix` to fix it.

```bash
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# parted /dev/sdd resizepart 3 100%
Warning: Not all of the space available to /dev/sdd appears to be used, you can fix the GPT to use all of the space
(an extra 8388608 blocks) or continue with the current setting? 
parted: invalid token: 3                                                  
Fix/Ignore? Fix
```

Then we can run the `resizepart` command within the parted tool to resize the partition.  We use the `print` command to check the size before and after the resize operation to confirm.

```bash
(parted) print                                                            
Model: SCST_BIO disk_00 (scsi)
Disk /dev/sdd: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name               Flags
 1      1049kB  2098kB  1049kB               grub bios boot     bios_grub
 2      3146kB  514MB   511MB   ext4         boot partition
 3      514MB   27.9GB  27.4GB               PV for vg_iscsi18  lvm

(parted) resizepart 3 100%                                                
(parted) print                                                            
Model: SCST_BIO disk_00 (scsi)
Disk /dev/sdd: 32.2GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name               Flags
 1      1049kB  2098kB  1049kB               grub bios boot     bios_grub
 2      3146kB  514MB   511MB   ext4         boot partition
 3      514MB   32.2GB  31.7GB               PV for vg_iscsi18  lvm

```

Finally, we need to ensure the LVM is aware of the new sizes.

* first run the `pvresize /dev/sdd3` to update physical volume size

```bash
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# pvs             
  PV         VG         Fmt  Attr PSize   PFree
  /dev/sdd3  vg_iscsi18 lvm2 a--  <25.52g    0 
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# pvresize /dev/sdd3
  Physical volume "/dev/sdd3" changed
  1 physical volume(s) resized / 0 physical volume(s) not resized
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# pvs
  PV         VG         Fmt  Attr PSize   PFree
  /dev/sdd3  vg_iscsi18 lvm2 a--  <29.52g 4.00g
```
* then resize the logical volume using `lvresize`

```bash
root@WA1SHSJ-U18-01:/opt/datagardens/rootfs/mnt/fs-disk1# lvresize -l +100%FREE /dev/vg_iscsi18/root_lv 
  Size of logical volume vg_iscsi18/root_lv changed from <23.52 GiB (6021 extents) to <27.52 GiB (7045 extents).
  Logical volume vg_iscsi18/root_lv successfully resized.
```

We could confirm the new size using `lsblk`.

##### 2.2.2 DR Sites on AWS/Azure: Expand the Partition

This step is similar to the above step using LVM. The only difference is that we simply need to use `parted` to resize the 4th partition and there is no need to do anything with LVM.

```bash
root@WA1SHSJ-U16-01:/var/log# parted /dev/sdd
GNU Parted 3.2
Using /dev/sdd
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) print                                                            
Model: SCST_BIO disk_03 (scsi)
Disk /dev/sdd: 18.3GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system     Name            Flags
 1      1049kB  2098kB  1049kB                  grub bios boot  bios_grub
 2      3146kB  514MB   511MB   ext4            boot partition
 3      514MB   2661MB  2147MB  linux-swap(v1)  swap partition
 4      2661MB  18.3GB  15.6GB  ext4            root partition
```

#### 2.3 Expand the root File System

After resizing the underlying volume/partition, we still need to resize the file system on top of it. The actual command depends on the fileystem type used by the root filesystem.

* For extended file systems (ext2/3/4), we can run `resize2fs`. For example

```bash
resize2fs /dev/vg_iscsi18/root_lv
```

* For XFS, we could use `xfs_growfs`
* For ReiserFS, we could use `resize_reiserfs`


#### 2.4 Confirmation

We could mount the iSCSI root file system and use the `df` command to confirm its new size. For example:

```bash
root@WA1SHSJ-U18-01:~# mount /dev/vg_iscsi18/root_lv /opt/datagardens/rootfs/
root@WA1SHSJ-U18-01:~# df -h
Filesystem                      Size  Used Avail Use% Mounted on
udev                            460M     0  460M   0% /dev
tmpfs                            97M  820K   96M   1% /run
/dev/sdc                         14G  4.1G  9.0G  31% /
tmpfs                           481M     0  481M   0% /dev/shm
tmpfs                           5.0M     0  5.0M   0% /run/lock
tmpfs                           481M     0  481M   0% /sys/fs/cgroup
/dev/sda1                       464M  121M  316M  28% /boot
tmpfs                            97M     0   97M   0% /run/user/0
192.168.1.4:/mnt/fs-disk1      1016G  839G  127G  87% /mnt/fs-disk1
/dev/mapper/vg_iscsi18-root_lv   27G  3.9G   22G  16% /opt/datagardens/rootfs
```

In this example, the file system mounted at `/opt/datagardens/rootfs` has grown from 23GB to 27GB.

Please remember to umount the file system if it was manually mounted.
