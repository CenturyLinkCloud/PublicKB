{{{
  "title": "Register SRN within a SafeHaven Console",
  "date": "07-25-2018",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article focusses on how to Register SRNs within the SafeHaven Console for Lumen Cloud and AWS.

### Requirements
1. SafeHaven Cluster already installed.
2. CMS and SRNs to have proper network connectivity.

### Assumptions
1. SafeHaven Cluster already installed with proper network connectivity between CMS-SRN and SRN-SRN.
2. Datacenters already registered.

### Register SRN

Please use the following steps for both PROD-SRN and DR-SRN registration 
**Right-click** on the any registered **Data Center** within the Navigation Tree and select **Register SRN** from the drop-down menu.

Fill in the following fields:

1. SRN hostname as the **Node Name**.
2. SRN **Root Password** (set at the time of SRN deployment).
3. **Service IP**: SRN IP used to communicate with other SafeHaven Nodes (SRN and CMS). Typically set as the Private IP of the SRN.
4. **WAN Replication IP**: SRN IP used to communicate with the peer SRN for WAN replication. Typically set as the Private IP of the SRN.
5. **Local iSCSI IP**: SRN IP used to communicate with the production/recovery servers in its native Datacenter. Typically set as the Private IP of the SRN.
6. Do not modify the Service Port (TCP).

**NOTE**: Incase SRN has multiple NIC's, Service IP and WAN Replication IP will be the Primary IP of the SRN which has proper network connectivity to other SRN's and CMS. Local iSCSI IP will be set to 0.0.0.0

**NOTE**: Follow the same procedure to register the all the SRN's within the SafeHaven Console. For AWS SRN the Local iSCSI IP and Service IP  are the same.

The above procedure stays the same for VMWare/Manual sites as the source datacenters.

