{{{
    "title":"Bare Metal Data Destruction Process",
    "date":"2/21/2021",
    "author":"Keith Bierman",
    "attachments": [],
    "contentIsHTML": false,
    "sticky": false
}}}

### Description

This article applies specifically to the Edge Bare Metal Dell C6420 systems, and explains how we treat any data left on the system when it is returned.

### Details

When a system is released, it is powered off and the Dell Cryptographic Erase command is applied to all of the Physical storage (SSD, NVMe), via Dell's Redfish API [2]. In addition, the iDRAC is factory reset and the system is reconfigured before being put back into service.

To summarize [1], all of the provided storage is automatically encrypted with a key known only to the Dell storage controller hardware. When the Cryptographic erase is triggered, the key is replaced with a new key. Thus none of the data is recoverable, even by exotic forensic techniques.

References:

1.  https://downloads.dell.com/manuals/common/dell-emc-system-erase-poweredge-idrac9.pdf
2.  https://github.com/dell/iDRAC-Redfish-Scripting.git
