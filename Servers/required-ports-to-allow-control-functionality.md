{{{
  "title": "Required ports to be opened on a server in order to allow Control functionality",
  "date": "11-13-2015",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview
Customers that prefer to "harden" their servers sometimes inadvertently block communications with the platform. This causes issues with the Control Portal and API functionality such as:

* Cloning a server.

  ![Required ports to allow control functionality](../images/required-ports-to-allow-control-functionality1.png)

* Modifying storage on a server.

  ![Required ports to allow control functionality](../images/required-ports-to-allow-control-functionality2.png)

Use this guide to keep necessary communications between Virtual Machines (VMs) and the Control Portal intact. For additional security-related information, read [Recommended Security Practices for Using CenturyLink Cloud](https://www.ctl.io/knowledge-base/servers/recommended-security-practices-for-using-centurylink-cloud/).

### Linux
For Linux VMs, customers need to ensure that the following ports are running:

* SSH (port 22).

  ![Required ports to allow control functionality](../images/required-ports-to-allow-control-functionality3.png)

### Windows
For Windows VMs, customers need to ensure that the following ports are running:

* WinRM (5985).

  ![Required ports to allow control functionality](../images/required-ports-to-allow-control-functionality4.png)
