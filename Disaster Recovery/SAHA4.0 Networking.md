{{{
  "title": "SafeHaven-4-Network Requirements",
  "date": "01-06-2017",
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
* Internet access (see the last section for details)

### SRN
There are 3 logically separated networks which can be arbitrarily combined into actual NIC interface in real implementations.
* SafeHaven cluster service network
* SafeHaven data replication network
* Local network

**1. On SafeHaven Cluster Service Network**
* TCP/22: ssh (remote management and start/stop safehaven-service via CMS)
* TCP/20082: SafeHaven cluster communication with peer SRNs and CMS, **SSL encrypted**
* UDP/20082: SafeHaven cluster heartbeat communications with peer SRNs and CMS
* Internet access (see the last section for details)

**2. On SafeHaven Data Replication Network**

* TCP/22: ssh (remote SRN establishes a SSH tunnel to master SRN for actual data replication)

**3. On Local Network**

* TCP/80: http (web server to provide binaries downloads and certificates for protected servers)
* TCP/3260: iSCSI (iSCSI targets to be connected by protected servers for local replication)
* TCP/5671: RabbitMQ (local communication between SRN and protected servers), **SSL encrypted**

#### Networking Requirement to Make API Calls

* For VMware site, the SRN within it needs to have a network connectivity to the vCenter server to make vSphere API calls
* For CLC site, the SRN within it needs to have access to https://api.ctl.io/

### Windows Machine Running the GUI

* It needs to have network connectivity to the CMS, ie, access TCP port 20081 of the CMS.
* If there is a VMware site, this client machine also needs network connectivity to the vCenter server, ie, it should be able to run VMware vSphere client and connect to the vCenter server.

### About Internet Access

Once installed, the SafeHaven cluster does not need Internet to operate as long as there is a way for the customer to use the GUI to login to CMS and the API calls  from SRNs can reach the service it needs to contact. But as a general rule, it is a lot easier to assume all nodes have access to Internet as ongoing clients and this normally does not impose any significant security risk since there is no service provided to the internet.

#### The SafeHaven Cluster Installation Phase

In order to finish the installation of the SafeHaven-4 cluster, the CMS/SRN nodes needs to 
* download the debian package specified by the user via the GUI cluster installation wizard
* install necessary dependency packages from 
  * standard Ubuntu release repositories for standard Ubuntu packages. A typical URL is http://us.archive.ubuntu.com/ubuntu/. However, the actual URL used might be a selected mirror that has better connectivity.
  * or the specific release URLs for those packages not shipped as part of the standard Ubuntu distribution. For example, the ansible winrm package is downloaded from https://github.com/diyan/pywinrm directly. 

In summary, it is difficult to come up with a comprehensive list of URLs that needs to be white listed in the firewall rules to allow access. It is recommended to temporarily allow outgoing Internet connections during the installation phase, at least temporarily.

#### Normal Operation Phase

During normal operations, there is only one possible outgoing Internet access which is made by the CLC SRN (if any) to make CLC API calls and it is made to the https://api.ctl.io/ URL.


#### Code Update

The SafeHaven releaes note page (like [this for SafeHaven-4.0.0](https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-4.0.0-release/)) contains links to the debian package which is using URL like https://download.safehaven.ctl.io/. For example, the SafeHaven-4.0.0 debian package is at https://download.safehaven.ctl.io/SH-4.0.0/safehaven-4.0.0.deb.

#### Summary and Recommendation to Firewall Internet Access White Listing

* Temporarily allow all Internet acess (http and https) during cluster installation phase.
* White list https://*.ctl.io/ which could cover anything provided by CenturyLink Cloud.

