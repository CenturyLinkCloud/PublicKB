{{{
  "title": "Cloning - Best Practices",
  "date": "11-15-2013",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The Tier 3 platform provides a rich interface for management of your virtual environment. When designing a virtual environment, one will often require consistency across all virtual machines- in the patch level, configuration, or installed applications,
  among others. Tier 3 provides three means of automation and repeat-ability: Clones, Templates, and Blueprints. While all these technologies can be used to produce the same results, there are best practices for each use case. This is the first in a series
  of articles which will illustrate said practices, focusing on cloning.</p>
<p>Cloning a server takes an exact copy of an existing machine. The server is shutdown to ensure that there are no pending operations/information held in memory, and the server contents are copied. The Tier 3 clone server wizard will prompt you for the machine
  group, new name, and network settings. A cloned server is, for most purposes, an exact copy of the source; however, certain underlying settings are changed (UUID, MAC, SID, etc.). Cloning is an easy way to produce alternate copies of existing infrastructure-
  common use cases are migrating servers from “test” to “development” or adding another web server to an existing stack.</p>
<p>It is important to understand the changes enacted by a clone job, to minimize complications. The most impactful changes are:</p>
<ul>
  <li>It is <strong>not</strong> recommended to clone domain member servers, as the clone operation often fails. Additionally, there is the potential for Group Policies to have unknown or undesired effects as well as the potential to cause issues within Active
    Directory.</li>
  <li>
    <p>Virtual machines clones are issued a new Universally Unique IDentifier (UUID). This affect user scripts and API calls to the UUID of the virtual machine.</p>
  </li>
  <li>
    <p>Virtual machines clones are issued new MAC addresses for attached virtual network adapters. This may have an effect on software or licensing that is sensitive to MAC address changes.</p>
  </li>
  <li>
    <p>Guest operating systems for virtual machine clones may share computer names and static IP addresses with their original counterparts. Be sure to account for this prior to power-on.</p>
  </li>
  <li>
    <p>The impact of cloning may vary between Operating Systems- for example, Server 2012 has features built-in to facilitate “cleaner” clones of Virtual Machines than earlier revisions.</p>
  </li>
</ul>