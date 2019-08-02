{{{
  "title": "Register SRN within a SafeHaven Console",
  "date": "12-27-2017",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article focusses on how to Register SRNs within the SafeHaven Console for CenturyLink Cloud and AWS.

### Requirements
1. SafeHaven Cluster already installed.
2. CMS and SRNs to have proper network connectivity.

### Assumptions
1. SafeHaven Cluster already installed with proper network connectivity between CMS-SRN and SRN-SRN.
2. Data centers already registered.

### Register SRN
**Right-click** on the any registered **Data Center** within the Navigation Tree and select **Register SRN** from the drop-down menu.

Fill in the following fields:

1. SRN hostname as the **Node Name**.
2. SRN **Root Password** (set at the time of SRN deployment).
3. **Service IP**: SRN IP used to communicate with other SafeHaven Nodes (SRN and CMS). Typically set as the Private IP of the SRN.
4. **WAN Replication IP**: SRN IP used to communicate with the peer SRN for WAN replication. Typically set as the Private IP of the SRN.
5. **Local iSCSI IP**: SRN IP used to communicate with the production/recovery servers in its native Datacenter. Typically set as the Private IP of the SRN. **Note**: This is not required for AWS SRN registration.
6. Do not modify the Service Port (TCP) and Heartbeat Port (UDP).

**NOTE**: Incase SRN has multiple NIC's, Service IP and WAN Replication IP will be the Primary IP of the SRN which has proper network connectivity to other SRN's and CMS. Local iSCSI IP will be set to 0.0.0.0

**NOTE**: Follow the same procedure to register the all the SRN's within the SafeHaven Console. For AWS SRN the Local iSCSI IP and Service IP  are the same.

The above procedure stays the same for CLC/VMWare/Manual sites as the source data centers.

**Next Step** is to [Add SRN Peer](Add SRN Peer.md)
