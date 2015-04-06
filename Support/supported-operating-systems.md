{{{
  "title": "Supported Operating Systems",
  "date": "4-7-2015",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": false
}}}

### What operating systems are supported in the CenturyLink Cloud?

The following operating systems are supported in CenturyLink Cloud, as of April 2015:

* CentOS 5
* CentOS 6
* Debian 6
* Debian 7
* RedHat Enterprise Linux 5
* RedHat Enterprise Linux 6
* RedHat Enterprise Linux 7
* Ubuntu 12
* Ubuntu 14
* Windows Server 2008 R2
* Windows Server 2012
* Windows Server 2012 R2

**NOTE: Only the 64-bit version of each OS is supported**

### What does it mean for an operating system to be "supported"?

All supported operating systems have a "template" in CenturyLink Cloud that is created, maintained, and managed by CenturyLink Cloud engineers. Templates can be viewed in the "Create Server" screen and accessed via the API. These templates are the basis for all new virtual machines created in the platform.

### Can I build custom templates?

Yes - the only requirement is that each custom template needs to "map" to a supported OS template. For best practices, read this article: ["How To: Create Customer Specific OS Templates"](../Servers/how-to-create-customer-specific-os-templates.md)

### What is your operating system retirement policy?

This is listed [here](../Servers/operating-system-template-retirement-policy.md).

### I'd like to deploy an operating system that is not supported. What are my options?

We do not recommend that you deploy unsupported operating systems in the platform. CenturyLink Cloud SLAs will not apply to virtual machines running an *unsupported* OS. In addition, some features may not work on unsupported OSes. Your options are to request a new OS be supported using our [suggested feature process](mailto:features@centurylinkcloud.com), or to deploy the OS in a traditional hosting environment.
