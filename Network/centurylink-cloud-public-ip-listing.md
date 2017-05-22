{{{ "title": "CenturyLink Cloud Public IP Listing",
"date": "11-7-2016",
"author": "Brandy Smith",
"attachments": [],
"contentIsHTML": false
}}}


CenturyLink Cloud customers may wish to add a public IP to a specific [virtual machine](//www.ctl.io/servers/) or [Bare Metal](//www.ctl.io/bare-metal/) server in their cloud environment to deliver services. Public IPs are delivered using a 1 to 1 NAT model.

### General Notes & Best Practices

* All public IPs deployed on the platform have [hairpinning](../Network/hairpin-nats.md) enabled.
* In its current iteration setting a source IP filter will secure all public ports, single ports or port ranges specified by the customer. Customers can leverage OS based [firewall services](//www.ctl.io/cloud-firewall/) if they wish to secure public services in a more granular fashion.
* Customers are encouraged to leverage the source IP filter unless delivering completely open public Internet services to their user community.
* Customers should avoid opening RDP or SSH to their virtual machines to the public Internet. As such the following are recommended access methods.
 * Use the free OpenVPN client included in every CenturyLink Cloud Account. Refer to [How To Configure Client VPN](../Network/how-to-configure-client-vpn.md). This is the ideal solution for individuals who are mobile and not in fixed office or data center locations.
 * Build an IPSEC VPN Tunnel from a remote office or data center location. Refer to [Creating a Self-Service IPSEC Site-to-Site VPN Tunnel](../Network/creating-a-self-service-ipsec-site-to-site-vpn-tunnel.md). IPSEC VPN tunnels are best for remote access to Cloud Virtual Machines when administrators are in centralized offices or data centers.
 * If either of the previous options are not feasible customers should at a minimum use the source IP filter service on the public IP and pair that with local OS firewall policies within the guest VM.
 * Refer to [How to Add Public IP to servers](../Network/how-to-add-public-ip-to-virtual-machine.md), for further instructions.

### Public IP Listing

Below is the current CenturyLink public IP listing. It is updated regularly as public IPs are created.

**Data Center**|**IP Blocks**
---------------|----------
AU1|65.127.194.144/29<br>65.151.184.0/23<br>65.151.186.0/23
CA1|216.187.73.144/28<br>64.69.71.128/25<br>65.39.180.0/24<br>65.39.184.0/25<br>216.187.110.0/24<br>65.151.128.0/23<br>65.151.130.0/23
CA2|70.33.239.96/28<br>66.155.96.0/24<br>66.155.100.0/24<br>69.28.224.128/25<br>70.33.208.0/25<br>70.33.239.128/25<br>107.6.43.0/24
CA3|206.152.25.96/28<br>206.152.32.0/21<br>206.152.45.0/24
DE1|66.155.5.0/28<br>66.155.4.0/24<br>66.155.94.0/24<br>66.155.95.0/24
DE3|65.151.172.0/22
GB1|176.74.176.144/28<br>66.155.18.0/24<br>66.155.27.0/24<br>66.155.28.0/24<br>176.74.168.0/25<br>176.74.179.0/25<br>66.155.19.0/24<br>65.151.144.0/22
GB3|206.142.225.192/28<br>206.142.240.0/21<br>207.82.88.0/24
IL1|64.94.35.32/28<br>64.74.98.0/24<br>66.150.105.0/24<br>66.151.15.0/24<br>69.25.149.0/24<br>72.5.203.0/24<br>74.217.15.0/24<br>72.5.194.0/24<br>64.74.229.0/24
NY1|74.217.51.192/28<br>74.201.135.0/24<br>74.201.140.0/24<br>74.201.226.0/24<br>74.201.232.0/24<br>74.201.237.0/24<br>74.201.240.0/24<br>74.201.165.0/24
SG1|205.139.20.0/28<br>205.139.16.0/22<br>205.139.24.0/25
UC1|64.15.180.16/28<br>64.15.182.0/24<br>64.15.183.0/24<br>64.15.184.0/21<br>64.15.176.0/24<br>64.211.224.0/25
UT1|8.22.8.0/28<br>8.22.9.0/24<br>8.23.156.0/24
VA1|206.128.131.32/28<br>206.128.134.0/23<br>206.128.137.0/24<br>206.128.152.0/21<br>206.128.173.0/24<br>206.128.176.0/23<br>206.128.136.0/24
VA2|65.117.187.16/29<br>65.151.188.0/23<br>70.42.161.0/24<br>70.42.168.0/24<br>69.25.131.0/24<br>66.150.9.112/28<br>64.94.143.192/26<br>63.251.170.192/27<br>63.251.167.64/26
WA1|64.94.142.8/29<br>64.94.114.0/24<br>64.94.138.0/24<br>66.150.160.0/25<br>66.150.174.0/24<br>70.42.161.0/24<br>70.42.168.0/24<br>64.94.119.0/24<br>66.150.9.112/28<br>64.94.143.192/26<br>63.251.170.192/27<br>63.251.167.64/26

### Frequently Asked Questions

**Q: What happens to my Public IP if I use the pause, power off or archive services in CenturyLink Cloud?**

A: Public IP addresses are static and using any of these features does not remove the public IP services from the server. The only time a public IP is removed from a server is a) when the server is deleted b) the customer removes the public IP in the GUI or API

**Q: How are customers billed for public IP addresses?**

A: Customers are billed a nominal fee per public IP on a monthly basis. Public IPs are not an hourly billing service and as such using a public IP even for an hour will result in a nominal charge for the public IP address.

**Q: What is the maximum number of Public IPs that can be bound to a server?**

A: As the platform uses a 1 to 1 NAT (public to private) and /24 network sizes the current maximum number of public IPs is 219 per VM. Bare Metal servers are only permitted a single public IP currently.

**Q: My server is housed in a datacenter in a non-US country.  Why do geolocation services show me as being in the United States?**
 
 A:  All IPs in CenturyLink Cloud datacenters worldwide are registered to a mailing address in the United States via a third-party registrar.  As such, most GeoIP services will show the IPs as being in the US, rather than in the country the datacenter is housed in.  This is an effect of our relationship with our registrars and cannot be changed either per customer or per datacenter.
 
**Q: Who do I contact for support or questions regarding Public IP listings?**

A: For service issues [please contact support.](../Support/how-do-i-report-a-support-issue.md)
