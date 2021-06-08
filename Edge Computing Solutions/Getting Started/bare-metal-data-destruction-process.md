{{{
    "title":"Bare Metal Data Destruction Process",
    "date":"2/21/2021",
    "author":"Keith Bierman",
    "attachments": [],
    "contentIsHTML": false,
    "sticky": false
}}}

### Description

This article applies specifically to the Edge Bare Metal systems, and explains how we treat any data left on the system when it is returned.

### Details

All local server storage is encrypted on Bare Metal hardware. When a system is released by a customer, it is powered off and a cryptographic erase is performed on all of the Physical storage (SSD, NVMe).  When the cryptographic erase is triggered a new key is generated, thus none of the data is recoverable, even by exotic forensic techniques. Finally, the server hardware controller is factory reset and the system hardware is reconfigured before being put back into service.

Reference:

1. https://csrc.nist.gov/glossary/term/cryptographic_erase#:~:text=Definition(s)%3A,the%20decrypted%20Target%20Data%20infeasible.
