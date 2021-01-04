{{{
  "title": "Manual Intervention Required when Adding a Disk to a Linux Machine",
  "date": "06-Nov-2019",
  "author": "Derek Jansen",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description (Goal/Purpose)
Lumen Cloud supports the ability to add additional disks to Linux machines, and the operation can be monitored in the deployment queue of the control portal. The job can fail for various reasons, resulting in the error "manual intervention required". These are the manual steps required to detect and mount the new disk.

### Impact
The new disk will be detected, formatted, and mounted.

### Prerequisites
- basic Linux knowledge
- root access to the machine in question
- understanding of the format and options for FSTab in Linux

### Detailed Steps
1. Log in to the machine as Root.

2. List all current devices on the machine. In most cases, the newly added disk isn't yet detected and won't show up here.

    ```
    fdisk -l
    ```

3. Identify the host bus name. This can vary, depending on the type of controller used on any particular system, so try the command under the appropriate scenario below.
    - Scenario 1: The server is using the LSI parallel controller. This is usually the case when the server was built from one of our Linux templates.

        ```
        host_bus_name=$(grep mptspi /sys/class/scsi_host/host?/proc_name | grep -o 'host[^/]')
        ```

    - Scenario 2: Another SCSI controller type is in use (e.g. the VMware para-virtual controller would be named "vmw_pvscsi").

        ```
        host_bus_name=$(grep scsi /sys/class/scsi_host/host?/proc_name | grep -o 'host[^/]')
        ```

4. Re-scan the host bus.

    ```
    echo "- - -" /sys/class/scsi_host/$host_bus_name/scan
    ```

5. List the current devices again, and make note of the new device's name (e.g. "/dev/sdd").

    ```
    fdisk -l
    ```

6. While advanced users may use any partition styles they like, only single-partition disks are fully compatible with platform automation and reporting. In the example command below, an EXT4 single-partition file system will be formatted directly on the disk (replace "NAME" with the new device name you just found).

    ```
    mkfs -t ext4 NAME
    ```

7. Make a new directory where you want the the disk to be mounted (e.g. "/data"). In the command below, replace "PATH" with the absolute path to the desired directory.

    ```
    mkdir PATH
    ```

8. The platform mounts new disks by UUID. Run the following command, and take note of the UUID for the new drive.

    ```
    blkid
    ```

9. Edit the FSTab. Add the UUID, mount point, and necessary options as per the normal FSTab format (e.g. "<device> <mount_point> <file_system_type> <options> <dump> <FSCK_order>").

    ```
    vi /etc/fstab
    ```

10. Mount the disk using the new entry in the FSTab.

    ```
    mount -a
    ```

11. Confirm everything looks correct by checking the free space on the disks.

    ```
    df -h
    ```
