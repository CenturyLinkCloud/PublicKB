{{{
  "title": "Cloning - Best Practices",
  "date": "11-15-2013",
  "author": "Jake Malmad",
  "attachments": []
}}}

The CenturyLink Cloud platform provides a rich interface for management of your virtual environment. When designing a virtual environment, one will often require consistency across all virtual machines- in the patch level, configuration, or installed applications, among others. CenturyLink Cloud provides three means of automation and repeat-ability: Clones, Templates, and Blueprints. While all these technologies can be used to produce the same results, there are best practices for each use case. This is the first in a series of articles which will illustrate said practices, focusing on cloning.

Cloning a server takes an exact copy of an existing machine. Cloning is not supported from powered off servers. The source server must be powered on in order to clone as a new virtual machine. The CenturyLink Cloud clone server wizard will prompt you for the machine group, new name, and network settings. A cloned server is, for most purposes, an exact copy of the source; however, certain underlying settings are changed (UUID, MAC, SID, etc.). Cloning is an easy way to produce alternate copies of existing infrastructure. Common use cases are migrating servers from "test" to "development" or adding another web server to an existing stack.

It is important to understand the changes enacted by a clone job, to minimize complications. The most impactful changes are:

- It is **not** recommended to clone domain member servers, as the clone operation often fails. Additionally, there is the potential for Group Policies to have unknown or undesired effects as well as the potential to cause issues within Active Directory.

- Virtual machines clones are issued a new Universally Unique IDentifier (UUID). This affect user scripts and API calls to the UUID of the virtual machine.

- Virtual machines clones are issued new MAC addresses for attached virtual network adapters. This may have an effect on software or licensing that is sensitive to MAC address changes.

- Guest operating systems for virtual machine clones may share computer names and static IP addresses with their original counterparts. Be sure to account for this prior to power-on.

- The impact of cloning may vary between Operating Systems. For example, Server 2012 has features built-in to facilitate "cleaner" clones of Virtual Machines than earlier revisions.
