{{{
  "title": "How To: Clone a Virtual Machine OS Instance",
  "date": "8-12-2015",
  "author": "Chris Little",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview

A clone is a copy of an existing virtual machine. When the cloning operation is complete, the clone is a separate virtual machine. The resulting clone is an independent copy of a virtual machine and shares nothing with the source virtual machine after the cloning operation. Ongoing operation of a clone is entirely separate from the source virtual machine.

### Exclusions

* Cloning is unsupported for customers who leverage virtual machines with the multi-vNIC feature

### Important Notices

Customers using the clone function for Windows Servers should carefully review the [Microsoft Sysprep for Server Roles technet article](//technet.microsoft.com/en-us/library/hh824835.aspx). Sysprep is a component of creating a clone and as such certain OS Roles are not supported in the clone process.

Additional attached disks from the source server are not automatically attached to the clone. If these disks are intended to be attached to the clone then this is a manual process on the guest operating system.

Cloning is not supported from powered off servers. The source server must be powered on in order to clone as a new virtual machine.

### Steps

1. Navigate to the Virtual Machine you wish to clone. From the "action" menu, select the "clone" option.

    ![Clone Server Menu](../images/how-to-clone-a-virtual-machine-os-instance-01.png)

2. The Clone Server form is used to input critical data points (server name, administrator password, network VLAN, storage type) for the resulting virtual machine clone.

    ![Clone Server Create Screen ](../images/how-to-clone-a-virtual-machine-os-instance-02.png)

3. Customers can monitor the Queue for status of the Clone process or wait for email notification.

    ![Clone Queue](../images/how-to-clone-a-virtual-machine-os-instance-03.png)
