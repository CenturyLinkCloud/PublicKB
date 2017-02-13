{{{
  "title": "Importing and Exporting data using a portable storage device",
  "date": "12-26-2016",
  "author": "Dana Bowlin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
CenturyLink Cloud supports importing and exporting data through portable storage devices into our data centers. This article provides an overview of this billable service. Billable charge details can be found [on our pricing page.](//www.ctl.io/pricing) 

### Service Task Prioritization
* Refer to [our ticket prioritization matrix](../Support/ticket-prioritization-matrix.md)

### Audience
* CenturyLink Cloud Customers

### Prerequisites
* All data must be encrypted.  The following tools are supported:
  * BitLocker Compatible Mode for Windows if using a supported OS version
  * 7-Zip for Windows with AES-256 and password
  * GnuPrivacyGuard (GPG) for Windows if BitLocker is not supported
  * dm-crypt, p7zip or GPG for Linux OS variants
* Include all power sources and connection cables required for the device
* USB 2.0 or above
* Drive formatted with NTFS filesystem – FAT32 will not support large files
* Drive cannot have any external locking mechanisms that could require multiple touches to remain available
* For data import, ensure that there is enough disk space available on server
* Prepaid return shipping label

### Device retention
Portable devices will not be kept for more than 5 days after the transfer is completed. If arrangements have not been made to return the device. The device will be detached and destroyed.

### Domain specific NTFS ACLs
If you are using domain specific ACLs. You must grant the "everyone" group full permissions. Without these permissions, we will not have access to copy or wipe data.

### Detailed Steps

##### Requesting an Import/Export
1. Create a Ticket through the CenturyLink Cloud Ticketing system
  * Indicate the datacenter where the portable device will be sent
  * Indicate the expected ship date and expected arrival date of the device
  * Provide the password for the encryption only via the ticket
  * Provide the location address to send the device after the data copy is completed
  * Provide the names of the servers involved
  * Provide details on what needs to be imported/exported (OVA/OVF and/or pathnames to files/directories)
  * Provide any additional details about the data to be imported/exported
  * Provide pre-paid shipping method and/or FedEx account number to be charged for return shipping.

2. Our team will reply with the data center mailing address and a data center logistics ticket number must be included on the shipping label. Note that the logistics number is different than the CenturyLink Cloud ticket number.

##### Import/Export Process
1. Ship or deliver portable device to the datacenter - include the support ticket number (provided by Service Task) on the shipping label.

2. Our team will receive the device, connect the device to our network and begin the process to copy the data.

3. Our team will periodically update the ticket for this request as we progress with the work.

4. Once the data is copied and the request is completed, CenturyLink Cloud will ship the device via the pre-paid return shipping method provided.

Note that the drive will be wiped prior to return shipping if used for import.

If our team needs to apply encryption to an export, a password will be provided in the ticket.


### FAQs

**Q: Will CenturyLink Cloud provide for shipping costs?**

A: No, shipping costs are the responsibility of the customer. The customer should provide prepaid return shipping label in the shipping materials.

**Q: Can I provide unencrypted data?**

A: No, we will not accept any portable devices that are not encrypted. We will not ship any data out of the data center that is not encrypted. 

**Q: Can I use Windows 10 XTS-AES bitlocker encryption? (Windows 10 version 1511 or later)**

A: No, please encrypt drive with compatible mode.

**Q: Can CenturyLink Cloud provide a portable device?**

A: Yes, we can provide a portable device.  Associated cost will be added as a one-time charge to your bill.  Note that this method can take 3-5 business days to procure and ship from our supplier.
 
**Q: Where can I ship data?**

A: Data must come from the country in which the datacenter is located. We will not ship data out of the country of origin.

**Q: What are the CenturyLink Cloud data centers located?**

A: Check out our [Data Centers Location page](//www.ctl.io/data-centers) for detailed information about where you can find our datacenters.

**Q: What limitations of liability are imposed?**

A: CenturyLink Cloud is not responsible for the loss or damage of the device, please ensure that you have a backup of your data.  Customer acknowledges that portable devices contain no malicious content, and will not damage or compromise CenturyLink Cloud equipment.


