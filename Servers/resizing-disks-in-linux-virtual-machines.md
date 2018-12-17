{{{
  "title": "Resizing Disks in Linux Virtual Machines",
  "date": "09-23-2015",
  "author": "Anthony Hakim",
  "attachments": []
}}}

### Description
Server resource requirements change frequently as environments scale. Storage is one of the most dynamic elements, and is often resized as environments grow and change. The CenturyLink Cloud Control Portal provides a self-service function to accommodate increased storage demands _without_ the need for a reboot. Non-boot and swap disks on a Linux VM will automatically be expanded upon request. Further, their file systems grow to reflect expanded storage.

### Steps


To modify storage allocations, navigate to the server in the Control Portal, then click on it.

  ![Resizing disks in Linux Virtual Machines](../images/resizing-disks-in-linux-virtual-machines1.png)

In the right pane, scroll down to **PARTITIONS**, then click the **edit storage** button.

  ![Resizing disks in Linux Virtual Machines](../images/resizing-disks-in-linux-virtual-machines2.png)

  ![Resizing disks in Linux Virtual Machines](../images/resizing-disks-in-linux-virtual-machines3.png)

To resize the disk, you can either enter the new size (must be greater than the current value), or drag the slider to increase the size of the disk, then click **apply**.

  ![Resizing disks in Linux Virtual Machines](../images/resizing-disks-in-linux-virtual-machines4.png)

The resize disk request will be submitted to the queue.

  ![Resizing disks in Linux Virtual Machines](../images/resizing-disks-in-linux-virtual-machines5.png)

Once complete, you can test using the following commands:

  ![Resizing disks in Linux Virtual Machines](../images/resizing-disks-in-linux-virtual-machines6.png)
  
Related: [Manually expanding file system on Linux machines.](../Servers/manually-expanding-file-system-on-linux-machines.md#part-3-moving-and-expanding-drives-on-older-partitioned-images)
