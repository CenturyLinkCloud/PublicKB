{{{ "title": "CenturyLink Cloud Public IP Listing",
"date": "07-06-2016",
"author": [],
"attachments": [],
"contentIsHTML": false
}}}


CenturyLink Cloud customers may wish to add a public IP to specific [virtual machine](https://www.ctl.io/servers/) or [Bare Metal](https://www.ctl.io/bare-metal/) server in their cloud environment to deliver services. Public IPs are delivered using a 1 to 1 NAT model.

### General Notes & Best Practices

* All public IPs deployed on the platform have [hairpinning](https://www.ctl.io/knowledge-base/network/hairpin-nats/) enabled.
* In its current iteration setting a source IP filter will secure all public ports, single ports or port ranges specified by the customer. Customers can leverage OS based [firewall services](https://www.ctl.io/cloud-firewall/) if they wish to secure public services in a more granular fashion.
* Customers are encouraged to leverage the source IP filter unless delivering completely open public Internet services to their user community.
* Customers should avoid opening RDP or SSH to their virtual machines to the public Internet. As such the following are recommended access methods.

1. Use the free OpenVPN client included in every CenturyLink Cloud Account. Refer to [How To Configure Client VPN](https://www.ctl.io/knowledge-base/network/how-to-configure-client-vpn/). This is the ideal solution for individuals who are mobile and not in fixed office or data center locations.
2. Build an IPSEC VPN Tunnel from a remote office or data center location. Refer to [Creating a Self-Service IPSEC Site-to-Site VPN Tunnel](https://www.ctl.io/knowledge-base/network/creating-a-self-service-ipsec-site-to-site-vpn-tunnel/). IPSEC VPN tunnels are best for remote access to Cloud Virtual Machines when administrators are in centralized offices or data centers.
3. If either of the previous options are not feasible customers should at a minimum use the source IP filter service on the public IP and pair that with local OS firewall policies within the guest VM.
4. Refer to [How to Add Public IP to servers](https://www.ctl.io/knowledge-base/network/how-to-add-public-ip-to-virtual-machine/), for further instructions.

### Public IP Listing

Below is the current CenturyLink public IP listing. It is updated regularly as public IPs are created.

**AU1:**
    routes:
        - 65.127.194.144/29
        - 65.151.184.0/23
**CA1:**
    routes:
        - 216.187.73.144/28
        - 64.69.71.128/25
        - 65.39.180.0/24
        - 65.39.184.0/25
        - 216.187.110.0/24
**CA2:**
    routes:
        - 70.33.239.96/28
        - 66.155.96.0/24
        - 66.155.100.0/24
        - 69.28.224.128/25
        - 70.33.208.0/25
        - 70.33.239.128/25
        - 107.6.43.0/24
**CA3:**
    routes:
        - 206.152.25.96/28
        - 206.152.32.0/21
**DE1:**
    routes:
        - 66.155.5.0/28
        - 66.155.4.0/24
        - 66.155.94.0/24
**GB1:**
    routes:
        - 176.74.176.144/28
        - 66.155.18.0/24
        - 66.155.19.0/24
        - 66.155.27.0/24
        - 66.155.28.0/24
        - 176.74.168.0/25
        - 176.74.179.0/25
**GB3:**
    routes:
        - 206.142.225.192/28
        - 206.142.240.0/21
**IL1:**
    routes:
        - 64.94.35.32/28
        - 64.74.98.0/24
        - 66.150.98.0/23
        - 66.150.105.0/24
        - 66.151.15.0/24
        - 69.25.149.0/24
        - 72.5.203.0/24
        - 74.217.15.0/24
**NE1:**
    routes:
        - 148.156.0.0/28
**NY1:**
    routes:
        - 74.217.51.192/28
        - 74.201.135.0/24
        - 74.201.140.0/24
        - 74.201.226.0/24
        - 74.201.232.0/24
        - 74.201.237.0/24
        - 74.201.240.0/24
**SG1:**
    routes:
        - 205.139.20.0/28
        - 205.139.16.0/22
**UC1:**
    routes:
        - 64.15.180.16/28
        - 64.15.182.0/24
        - 64.15.184.0/21
**UT1:**
    routes:
        - 8.22.8.0/28
        - 8.22.9.0/24
        - 8.23.156.0/24
**VA1:**
    routes:
        - 206.128.131.32/28
        - 206.128.134.0/23
        - 206.128.137.0/24
        - 206.128.152.0/21
        - 206.128.173.0/24
        - 206.128.176.0/23
**WA1:**
    routes:
        - 64.94.142.8/29
        - 64.94.114.0/24
        - 64.94.138.0/24
        - 66.150.160.0/25
        - 66.150.174.0/24
        - 70.42.161.0/24
        - 70.42.168.0/24

### Frequently Asked Questions

Q: **What happens to my Public IP if I use the pause, power off or archive services in CenturyLink Cloud?**

A: Public IP addresses are static and using any of these features does not remove the public IP services from the server. The only time a public IP is removed from a server is a) when the server is deleted b) the customer removes the public IP in the GUI or API

Q: **How are customers billed for public IP addresses?**

A: Customers are billed a nominal fee per public IP on a monthly basis. Public IPs are not an hourly billing service and as such using a public IP even for an hour will result in a nominal charge for the public IP address.

Q: **What is the maximum number of Public IPs that can be bound to a server?**

A: As the platform uses a 1 to 1 NAT (public to private) and /24 network sizes the current maximum number of public IPs is 219 per VM. Bare Metal servers are only permitted a single public IP currently.

Q: **Who do I contact for support or questions regarding Public IP listings?**

A: For issues related to cloud infrastructure (VM's, network, and so on) or if you experience a problem deploying the Blueprint or Script Package, open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io), through the CenturyLink Cloud Support website, or you can reach Customer Support at 1.888.638.6771
M – F, 8am to 6pm.
