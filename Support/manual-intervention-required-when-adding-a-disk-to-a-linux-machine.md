{{{
  "title": "Manual intervention required when adding a disk to a Linux machine",
  "date": "11-12-2014",
  "author": "James Morris",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description (goal/purpose)</h3>
<p>CenturyLink Cloud supports the ability to add additional disks to Linux machines. This automated task can fail for various reasons requiring manual intervention on the customer machine in order to complete. These are the manual steps required to detect
  and mount a new disk.</p>

<h3>Audience</h3>
<ul>
  <li>NOC Engineers,&nbsp;Customers</li>
</ul>
<h3>Impact</h3>
<p>New drive will be detected, formatted, and mounted</p>
<h3>Prerequisites</h3>
<ul>
  <li>Must have root access to the machine in question</li>
  <li>Must have basic Linux knowledge</li>
  <li>Must understand the format and options for fstab in Linux</li>
</ul>
<h3>Detailed Steps</h3>
<ol>
  <li>After the disk addition has failed with the message "manual intervention required" log on as root to the machine.</li>
  <li>On the machine run:
    <br />
    <br /><em><strong>fdisk -l</strong></em>
    <br />
    <br />This will show all current drives/ partitions on the machine. In most cases the newly added drive will not show up here as it has not yet been detected.
    <br />
    <br />
  </li>
  <li>To get the OS to detect the new drive we must rescan the SCSI bus, in order to do this we must first Identify the host bus number. This can very depending on the type of controller used on any particular system. Run the following command:
    <br />
    <br />All our current Linux templates use the LSI parallel controller, in which case the controler name we are looking for is&nbsp;<em><strong>mptspi</strong></em>
    <br /><em><strong>grep mptspi&nbsp;/sys/class/scsi_host/host?/proc_name<br /></strong></em>
    <br />The returned value should look something like: "/sys/class/scsi_host/host3/proc_name:mptspi" &nbsp;From these results you can see we are dealing with "host3"
    <br />
    <br />In the case of another SCSI controler type this value will differ, the VMware para-virtual controller for example would be named&nbsp;<em><strong>vmw_pvscsi</strong></em><strong>&nbsp;</strong>so we would run
    <br /><strong>grep</strong><em><strong> scsi /sys/class/scsi_host/host?/proc_name</strong></em>
    <br />
    <br />The returned value should look something like: "/sys/class/scsi_host/host2/proc_name:vmw_pvscsi" &nbsp; From these results you can see we are dealing with "host2"
    <br />
    <br />Now run the following command to rescan the host number we identified
    <br />
    <br /><em><strong>echo "- - -" &gt; /sys/class/scsi_host/host3/scan<br /></strong></em>
  </li>
  <li>Run "fdisk -l" again and you should now see the new drive detected in the OS. Make a note of the device name (for this example we will assume /dev/sdd)</li>
  <li>The control site normally deploys partition-less file systems and as that is what the control site is compatible with we will do the same here (advanced users may create any partitioning they like however it may not be compatible with the control site)
    <br
    />The following command creates a new ext4 filesystem directly on the drive with no partitioning.
    <br />
    <br /><em><strong>mkfs -t ext4 /dev/sdd</strong></em>
    <br />
    <br />
  </li>
  <li>Now that the drive has been added and formatted we must mount it somewhere. For this example we will mount it to "/data"
    <br />Run the following command to create a mount point (/data can be replaced with whatever you like)
    <br />
    <br />
    <br /><em><strong>mkdir /data</strong></em>
    <br />
    <br />
  </li>
  <li>As the control site normally mounts by UUID we will do the same here. Run the following command and take note of the UUID for the new drive
    <br />
    <br /><em><strong>blkid</strong></em>
    <br />
    <br />
  </li>
  <li>Edit the fstab, adding the UUID, mount point and necessary options as per the normal fstab format (&lt;device&gt; &lt;mountpoint&gt; &lt;filesystemtype&gt;&lt;options&gt; &lt;dump&gt; &lt;fsckorder&gt;)
    <br />
    <br /><em><strong>vi /etc/fstab</strong></em>
    <br />
    <br />
  </li>
  <li>Mount using the new entry in the fstab by running:
    <br />
    <br /><em><strong>mount -a</strong></em>
    <br />
    <br />
  </li>
  <li>Confirm everything looks correct by checking the free space on the drives
    <br />
    <br /><strong><em>df -h</em></strong>
  </li>
</ol>


<div>&nbsp;</div>
<div>&nbsp;</div>
