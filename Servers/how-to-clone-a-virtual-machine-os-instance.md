{{{
  "title": "How To: Clone a Virtual Machine OS Instance",
  "date": "7-28-2014",
  "author": "Chris Little",
  "attachments": []
}}}

### Overview

A clone is a copy of an existing virtual machine. When the cloning operation is complete, the clone is a separate virtual machine. The resulting clone is an independent copy of a virtual machine and shares nothing with the source virtual machine after the cloning operation. Ongoing operation of a clone is entirely separate from the source virtual machine.

### Important Notices

Customers using the clone function for Windows Servers should carefully review the [Microsoft Sysprep for Server Roles technet article](http://technet.microsoft.com/en-us/library/hh824835.aspx). Sysprep is a component of creating a clone and as such certain OS Roles are not supported in the clone process.

Cloning is not supported from powered off servers. The source server must be powered on in order to clone as a new virtual machine.

### Steps

1. Navigate to the Virtual Machine you wish to clone. From the "action" menu, select the "clone" option.

  ![Clone Server Menu](https://t3n.zendesk.com/attachments/token/mU4R9Fwije2bZcA2xymt02Tru/?name=clone-server-menu.png)

2. The Clone Server form is used to input critical data points (server name, administrator password, network VLAN, storage type) for the resulting virtual machine clone.

  ![Clone Server Create Screen ](https://t3n.zendesk.com/attachments/token/qUc3FEo8lyKjAK9sIHmIDkWw5/?name=clone-server-create-screen.png)

3. Customers can monitor the Queue for status of the Clone process or wait for email notification.

  ![Clone Queue](https://t3n.zendesk.com/attachments/token/9lRiBdqZZx6byx1A8Sk3TwNUI/?name=clone-queue.png)
