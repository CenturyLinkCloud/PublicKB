{{{
  "title": "Determine Storage Requirements",
  "date": "12-27-2017",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to determine storage requirements for the DR setup. Storage is attached to the Production and Recovery SRN's.

### Assumptions
User has gathered the required production server information. Refer to [Gather Production Server Information](Gather Production Server Information.md) for more information.

### SafeHaven Replication Node(SRN)
SafeHaven Replication Node(SRN) is an Ubuntu 16 based lightweight virtual appliance(virtual machine)which transfers and retains production data.Depending on the O.S. Type of servers being protected and the mode of replication(Local Cache or Local Replica) selected, required amount of storage is attached on both the Production and Recovery SRN appliances.

### When Production SRN is in Lumen Cloud/ VMWare/ Manual - Storage Requirements

#### Local Cache for Windows Servers
For Windows Production Servers, **Local Cache** mode is selected where storage amounting to **10% of the total provisioned storage on the Production Server** is attached to the Production SRN. This Local Cache attached to the Production SRN acts as a buffer and transfers the production data coming from the Production Servers over to the Recovery SRN in AWS. This mode of replication saves storage related costs as the users do not have to pay for an additonal full copy of data on the Production SRN.

#### Local Replica for Linux Servers
For Linux Production Servers, Local Replica mode is selected where storage amounting to **100% of the total used storage(full copy of data) + an additional 5% of the total used storage(for Checkpoints)** on the Production Server = **105% of the total used storage on the Production Server** is attached to the Production SRN.

**NOTE**: Local Replica is not available for Windows.

### When Recovery(DR) SRN is in AWS - Storage Requirements
As the Recovery SRN retains a full copy of the production data called "Remote Replica", storage amounting to **100% of the total provisioned storage(full copy of data)** on the Production Server is attached to the Recovery SRN as EBS Volumes automatically.

### When Recovery(DR) SRN is in Lumen Cloud - Storage Requirements
**For both Windows and Linix Protection groups**, storage amounting to **125% of the total provisioned storage** is attached to the Recovery SRN.

Out of this, 100% of the provisioned storage is used to store a replica on the DR site, and 25% is used by default for storing checkpoints. If a user needs to store more checkpoints, more checkpoints storage can be allocated.

**Next Step** is to [Setup AWS for SafeHaven-5 Using CloudFormation](../SafeHaven 5 General/Setup AWS for SafeHaven-5 using CloudFormation.md)
