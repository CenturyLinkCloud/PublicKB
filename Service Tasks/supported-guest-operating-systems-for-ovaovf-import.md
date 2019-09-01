{{{
  "title": "Supported Guest Operating Systems for OVA/OVF Import",
  "date": "03-20-2019",
  "author": "Matthew Ordman",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
CenturyLink Cloud customers may wish to import OVA/OVF Guest Operating Systems to the platform via a [Service Task](//www.ctl.io/products/support/service-tasks). Customers frequently request a list of the Supported Guest Operating Systems that CenturyLink Cloud supports for Import and this KB addresses that.

### Prerequisites
* A CenturyLink Cloud Account
* Meets requirments for Import (https://www.ctl.io/knowledge-base/service-tasks/best-practices-and-preparation-for-a-virtual-machineovfova-import/)
* OVF must be on the Supported Operating Systems List (https://www.ctl.io/knowledge-base/support/supported-operating-systems/)

### Exclusions
* Industry packaged Virtual Appliances from vendors, including but not limited to, Citrix VPX, F5 VE, SoftNAS, should be vetted with CenturyLink Cloud Sales to validate compatibility. Many Virtual Appliances are part of our ecosystem program and have been validated.  The support of these packaged virtual appliances are not the focus of this article.

### Frequently Asked Questions

**Q: I run Xen, KVM, Hyper-V or other x86/x64 Virtualization Services.  Can I import images from these technologies into CenturyLink Cloud?**

A: Customers must convert their virtual servers to an OVF format prior to import (manual or self-service) to the CenturyLink Cloud.  As long as the operating system is supported as shown above an import is possible once the VM is converted to OVF.  

**Q: I run Intel IA64 or Oracle SPARC hardware platforms can I import a server based on this technology into CenturyLink Cloud?**

A: No, hardware specific platforms that are not x86/x64 based cannot be imported, operated or deployed on CenturyLink Cloud

**Q: I leverage [HPVM](//en.wikipedia.org/wiki/HP_Integrity_Virtual_Machines), [Solaris Containers](//en.wikipedia.org/wiki/Solaris_Containers), [IBM PowerVM](//en.wikipedia.org/wiki/PowerVM) or other Virtualization Services outside of the x86/x64 community.  Can I import these services into CenturyLink Cloud?**

A: No, these other industry virtualization technologies cannot be leveraged on CenturyLink Cloud.
