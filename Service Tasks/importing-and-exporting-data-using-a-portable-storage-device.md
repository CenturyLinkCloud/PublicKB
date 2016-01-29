{{{
  "title": "Importing and Exporting data using a portable storage device",
  "date": "9-29-2015",
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
* All data must be encrypted, the following tools are recommended:
  * BitLocker for Windows if using a supported OS version
  * GnuPrivacyGuard (GPG) for Windows if BitLocker is not supported
  * dm-crypt or GPG for Linux OS variants
* Include all power sources and connection cables required for the device
* USB 2.0 or above
* Limit 1 TB/drive

### Device retention
Portable devices will not be kept for more than 5 days after the transfer is completed. If arrangements have not been made to return the device. The device will be detached and destroyed.

### Domain specific NTFS ACLs
If you are using domain specific ACLs. You must grant the "everyone" group full permissions. Without these permissions we will not have acces to copy or wipe data.

### Detailed Steps

##### Requesting an Import
Create a Ticket through the Centurylink Cloud Ticketing system
  * Indicate the datacenter where the portable device will be sent
  * Indicate the ship date and expected arrival date of the device
  * Provide the password for the encryption only via the ticket
  * Provide the location address to send the device after the data copy is completed
  * Provide the account or sub-account information for the data destination
  * Provide any more details about the data to be imported
  * Provide pre-paid shipping method and/or Fedex account number to be charged for return shipping.

##### Import Process
1. Ship or deliver portable device to the datacenter - include the support ticket number (created in the Request steps above) on/with the package.

2. Our team will receive the device, connect the device to our network and begin the process to copy the data.

3. Our team will update the ticket for this request as we progress with the work.

4. Once the data is copied and the request is completed, Centurylink Cloud will wipe the portable data drive and ship the device back to the address noted in the request, via the pre-paid return shipping method provided.

##### Requesting an Export
1. Create a Ticket though the Centurylink Cloud Ticketing system.
  * Indicate the datacenter where the portable device will be sent
  * Indicate when the portable device will be sent
  * Provide tracking information for the shipment

2. Ship or deliver the portable device to the datacenter
  * Your device will be received by the datacenter team
  * Our team will connect the device to our network and begin the process to export the data and copy the data to the portable device
  * Our team will update the ticket for this request as we progress with the work
  * Once the data is copied and the request is completed, Centurylink Cloud will encrypt the portable data drive, set a password and ship the device back to the address noted in the request
  * You will receive the password via a different delivery method

### FAQs

**Q: Will CenturyLink Cloud provide for shipping costs?**

A: No, shipping costs will be the responsible of the customer. When Centurylink Cloud sends the device back, we will charge the cost of shipping to your account.

**Q: Can I provide unencrypted data?**

A: No, we will not accept any portable devices that are not encrypted. We will not ship any data out of the data center that is not encrypted. 

**Q: Where can I ship data?**

A: Data must come from the country in which the datacenter is located. We will not ship data out of the country of origin.

**Q: What are the CenturyLink Cloud data centers located?**

A: Check out our [Data Centers Location page](//www.ctl.io/data-centers) for detailed information about where you can find our datacenters.

**Q: What limitations of liability are imposed?**

A: CenturyLink Cloud is not responsible for the loss or damage of the device, please ensure that you have a back up of your data.
