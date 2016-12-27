{{{
  "title": "SafeHaven-4-Network Requirements",
  "date": "11-29-2016",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article covers different TCP and UDP ports required to be opened on CMS, SRN, and local guest for SafeHaven 4.0.

### CMS
* TCP/22: ssh (remote management)
* TCP/20081: SafeHaven cluster communication with SRNs and GUI, **SSL encrypted**
* UDP/20081: SafeHaven cluster heartbeat communications with SRNs

### SRN
There are 3 logically separated networks which can be arbitrarily combined into actual NIC interface in real implementations.
* SafeHaven cluster service network
* SafeHaven data replication network
* Local network

**1. On SafeHaven Cluster Service Network**
* TCP/22: ssh (remote management and start/stop safehaven-service via CMS)
* TCP/20082: SafeHaven cluster communication with peer SRNs and CMS, **SSL encrypted**
* UDP/20082: SafeHaven cluster heartbeat communications with peer SRNs and CMS

**2. On SafeHaven Data Replication Network**

* TCP/22: ssh (remote SRN establishes a SSH tunnel to master SRN for actual data replication)

**3. On Local Network**

* TCP/80: http (web server to provide binaries downloads and certificates for protected servers)
* TCP/3260: iSCSI (iSCSI targets to be connected by protected servers for local replication)
* TCP/5671: RabbitMQ (local communication between SRN and protected servers), **SSL encrypted**
