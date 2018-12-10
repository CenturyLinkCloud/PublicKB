{{{
  "title": "Supported Guest Operating Systems for OVA/OVF Import",
  "date": "11-24-2015",
  "author": "Jacob Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
CenturyLink Cloud customers may wish to import OVA/OVF Guest Operating Systems to the platform via a [Service Task](//www.ctl.io/products/support/service-tasks.md). Customers frequently request a list of the supported Guest Operating Systems the CenturyLink Cloud supports for Import and this KB is meant to address this query.

Ensure your OVF meets requirements for import they are listed here in the KB under Service tasks > Best Practices and preparation for a virtual machine OVF import.

### Prerequisites
* A CenturyLink Cloud Account

### Exclusions
* Industry packaged Virtual Appliances from vendors, including but not limited to, Citrix VPX, F5 VE, SoftNAS, should be vetted with CenturyLink Cloud Sales to validate compatibility. Many Virtual Appliances are part of our ecosystem program and have been validated.  The support of these packaged virtual appliances are not the focus of this article.

### Supported Operating Systems List
* CentOS 5 | 64-bit
* CentOS 6 | 64-bit
* CentOS 7 | 64-bit
* Debian 6 | 64-bit
* Debian 7 | 64-bit
* RedHat Enterprise Linux 5 | 64-bit
* RedHat Enterprise Linux 6 | 64-bit
* RedHat Enterprise Linux 7 | 64-bit
* Ubuntu 12 LTS | 64-bit
* Ubuntu 14 LTS | 64-bit
* Ubuntu 16 LTS | 64-bit
* Windows 2008 R2 Enterprise | 64-bit
* Windows 2008 R2 Standard | 64-bit
* Windows 2008 R2 Datacenter Edition | 64-bit
* Windows 2012 Datacenter Edition | 64-bit
* Windows 2012 R2 Datacenter Edition | 64-bit

### Frequently Asked Questions

**Q: I run Xen, KVM, Hyper-V or other x86/x64 Virtualization Services.  Can I import images from these technologies into CenturyLink Cloud?**

A: Customers must convert their virtual servers to an OVF format prior to import (manual or self-service) to the CenturyLink Cloud.  As long as the operating system is supported as shown above an import is possible once the VM is converted to OVF.  

**Q: I run Intel IA64 or Oracle SPARC hardware platforms can I import a server based on this technology into CenturyLink Cloud?**

A: No, hardware specific platforms that are not x86/x64 based cannot be imported, operated or deployed on CenturyLink Cloud

**Q: I leverage [HPVM](//en.wikipedia.org/wiki/HP_Integrity_Virtual_Machines), [Solaris Containers](//en.wikipedia.org/wiki/Solaris_Containers), [IBM PowerVM](//en.wikipedia.org/wiki/PowerVM) or other Virtualization Services outside of the x86/x64 community.  Can I import these services into CenturyLink Cloud?**

A: No, these other industry virtualization technologies cannot be leveraged on CenturyLink Cloud.
