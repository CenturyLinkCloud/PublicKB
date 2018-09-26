{{{ "title": "CenturyLink Cloud Public IP Listing",
"date": "08-22-2018",
"author": "Erik Jensen",
"attachments": [],
"contentIsHTML": false
}}}


CenturyLink Cloud customers may wish to add a public IP address to a specific [virtual machine](//www.ctl.io/servers/) or [Bare Metal](//www.ctl.io/bare-metal/) server in their cloud environment to deliver services. Public IP addresses are delivered using a 1-to-1 NAT model.

### General Notes & Best Practices

* All public IPs deployed on the platform have [hairpinning](../Network/hairpin-nats.md) enabled.
* In its current iteration setting a source IP filter will secure all public ports, single ports or port ranges specified by the customer. Customers can leverage OS based [firewall services](//www.ctl.io/cloud-firewall/) if they wish to secure public services in a more granular fashion.
* Customers are encouraged to leverage the source IP filter unless delivering completely open public Internet services to their user community.
* As a security best practice, we strongly encourage our customer to avoid opening RDP (3389) or SSH (22) to their virtual machines over the public IP address. Please review the following recommended access methods for RDP and SSH to the VM which will help ensure a strong security posture to your VM infrastructure.

  1. Use the free OpenVPN client included in every CenturyLink Cloud Account. Refer to [How To Configure Client VPN](../Network/how-to-configure-client-vpn.md). This is the ideal solution for individuals who are mobile and not in fixed office or data center locations.

  2. Build an IPSEC VPN Tunnel from a remote office or data center location. Refer to [Creating a Self-Service IPSEC Site-to-Site VPN Tunnel](../Network/creating-a-self-service-ipsec-site-to-site-vpn-tunnel.md). IPSEC VPN tunnels are best for remote access to Cloud Virtual Machines when administrators are in centralized offices or data centers.

* If either of the previous options are not feasible customers should at a minimum use the source IP filter service on the public IP and pair that with local OS firewall policies within the guest VM.
 * Refer to [How to Add Public IP to servers](../Network/how-to-add-public-ip-to-virtual-machine.md), for further instructions.

### Public IP Listing

Below is the current CenturyLink public IP listing. It is updated regularly as public IP (CIDR) blocks are assigned in the data centers.

**Data Center**|**IP Blocks**
---------------|----------
AU1|65.127.194.144/29<br>65.151.184.0/22
CA1|64.69.71.128/25<br>65.39.180.0/24<br>65.39.184.0/25<br>65.151.128.0/22<br>216.187.73.144/28<br>216.187.110.0/24
CA2|65.151.132.0/23<br>66.155.96.0/24<br>66.155.100.0/24<br>69.28.224.128/25<br>70.33.208.0/25<br>70.33.239.96/28<br>70.33.239.128/25<br>107.6.43.0/24
CA3|206.152.32.0/21<br>206.152.45.0/24
DE1|66.151.140.0/23<br>66.155.4.0/24<br>66.155.94.0/24
DE3|65.151.172.0/22
GB1|66.155.18.0/23<br>66.155.27.0/24<br>66.155.28.0/24<br>176.74.168.0/25<br>176.74.179.0/25
GB3|206.142.240.0/21<br>207.82.88.0/24
IL1|64.74.98.0/24<br>64.74.229.0/24<br>64.94.35.32/28<br>66.150.98.0/23<br>66.150.105.0/24<br>69.25.149.0/24<br>72.5.194.0/24<br>72.5.203.0/24<br>74.201.4.0/24<br>74.217.15.0/24
NY1|74.201.135.0/24<br>74.201.140.0/24<br>74.201.165.0/24<br>74.201.226.0/24<br>74.201.232.0/24<br>74.201.237.0/24<br>74.201.240.0/24
SG1|205.139.16.0/22<br>205.139.24.0/25
UC1|64.15.176.0/24<br>64.15.180.16/28<br>64.15.182.0/24<br>64.15.183.0/24<br>64.15.184.0/21<br>64.211.224.0/25
VA1|206.128.134.0/23<br>206.128.136.0/23<br>206.128.152.0/21<br>206.128.173.0/24<br>206.128.176.0/23
VA2|65.151.188.0/22
WA1|64.94.142.8/29<br>64.94.114.0/24<br>64.94.138.0/24<br>66.150.160.0/25<br>66.150.174.0/24<br>69.25.131.0/24<br>70.42.161.0/24<br>70.42.168.0/24

### Frequently Asked Questions

**Q: What happens to my Public IP address if I use the pause, power off or archive services in CenturyLink Cloud?**

A: Public IP addresses are static and using any of these features does not remove the public IP services from the server. The only time a public IP is removed from a server is a) when the server is deleted b) the customer removes the public IP in the GUI or API

**Q: How are customers billed for public IP addresses?**

A: Customers are billed a nominal fee per public IP on a monthly basis. Public IP's are not an hourly billing service and as such using a public IP even for an hour will result in a nominal charge for the public IP address.

**Q: What is the maximum number of Public IP addresses that can be bound to a server?**

A: As the platform uses a 1-to-1 NAT (public to private) and /24 network sizes the current maximum number of public IP's is 219 per VM. Bare Metal servers are only permitted to assign a single public IP.

**Q: My server is housed in a datacenter in a non-US country.  Why do geolocation services show me as being in the United States?**
 
 A:  All IP addresses assigned in CenturyLink Cloud data centers worldwide are registered to a mailing address in the United States via a third-party registrar.  As such, most GeoIP services will show the IP's as being in the US, rather than in the country the datacenter is housed in.  This is an effect of our relationship with our registrars and cannot be changed either per customer or per datacenter.
 
**Q: Who do I contact for support or questions regarding Public IP listings?**

A: For service issues, please [contact Support](../Support/how-do-i-report-a-support-issue.md).
