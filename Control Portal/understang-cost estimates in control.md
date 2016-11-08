{{{
  "title": "Understanding Cost Estimates in Control Portal",
  "date": "11-07-2016",
  "author": "Gavin Lai",
  "attachments": [],
  "contentIsHTML": false
}}}


### Contents
- [Overview](#overview)
- [Dashboard](#main-dashboard)
- [Data Center View](#data-center-view)
- [Group View](#connectvpn)
- [Server View](#deployowncloud)
- [Network](#network)
- [Services](#services)
- [Billing](#billing)

### Overview
One of the best features of the Control Portal is the cost estimatation in every level within the account.  In this knowledge article, we will have a look of what are included in each level of the Control Portal.
Monthly and hourly estimates are found in the following level of the Portal:
- Main Dashboard
- Data Centers
- Groups
- Server
- Services (Simple Backup, Object Storage, Relational Database)
- Network
- Monthly Usage Summary

### Main Dashboard
When logging into the CenturyLink Control Portal, the main dashboard is displayed.  There are four estimates at the top of the page.  

![Dashboard](../images/estimator/dashboard.png)

There are four values at the top of the dashboard.  
***Month Estimate*** includes (assuming full usage):
 - All infrastructure costs (CPU, Memory, disk) and OS licenses (where applicable) from all datacenters
 - Managed Services costs (Managed OS, Active Directory, Databases, Web server)
 - Microsoft SQL licenses(account wide)
 - VLANs (across all datacenters) and Site to Site VPNs
 - Shared Load Balancer
 - Object Storage
 - Public IP addresses
 - Simple Backup Usage
 - Relational Database Services
 - Appfog

***Current Hour*** includes:
 - All infrastructure costs (CPU, Memory, disk) and OS licenses (where applicable) from all datacenters
 - Managed Services costs (Managed OS, Active Directory, Databases, Web server)
 - Microsoft SQL licenses(account wide)

***One Time Changes*** includes:
 - Any Service Task charges

***Month to Date***
 - Base on Current Hour data, this is the month to date estimate

For the following views, the estimations are displayed with the following data:
***Month Estimate*** represents the estimation of the usage cost from the creation of the server til the end of the month.  
***Current Hour*** is the cost of the current hour.
***Month to Date*** is the accumulated cost since the creation of the server.

### Data Center View
![Datacenter](../images/estimator/datacenter.png)

Jumping from the main dashboard to an individual data center, the cost estimation will be more data center infrastructure focused.  The list of items included in the cost estimation in the data center level are:
 - All infrastructure costs (CPU, Memory, disk) and OS licenses (where applicable) from the data center
 - Managed Services costs (Managed OS, Active Directory, Databases, Web server)

### Group view
![Group](../images/estimator/group.png)

For an indiviual group, its estimate is similar to the Data Center View.  
 - All infrastructure costs (CPU, Memory, disk) and OS licenses (where applicable) from the data center
 - Managed Services costs (Managed OS, Active Directory, Databases, Web server)

### Server view
![Server](../images/estimator/server.png)

The estimate for a server will show:
 - All infrastructure costs (CPU, Memory, disk) and OS licenses (where applicable) from the data center
 - Managed Services costs (Managed OS, Active Directory, Databases, Web server)

### Network

Under Network menu, the cost of VLANs, Share Load Balanacer, DNS and Site to Site VPN can be found within the configuration page of the service.

For Networks:

![Network](../images/estimator/network.png)

For Load Balancers:

![LoadBalancer](../images/estimator/loadbalancer.png)

Site to Site VPN:

![VPN](../images/estimator/VPN.png)

DNS:

![DNS](../images/estimator/dns.png)

### Services
CenturyLink Cloud offers different services and the cost estimation can be under the individual service page.

Appfog

![Appfog](../images/estimator/appfog.png)

Backup

![Backup](../images/estimator/backup.png)

Object Storage

![ObjectStorage](../images/estimator/objectstorage.png)

Relational DB

![Database](../images/estimator/database.png)


### Billing
![Billing](../images/estimator/billing.png)

If a detail break down of the usage is required, "Usage History" can be found under "Settings" -> "Billing".  In this section, a monthly usage report can be viewed and download for accounting purposes.  The details include:
 - Usage Total of the accounting
 - Group sub-total of each Group
 - Simple Backup Service usage for individual server
 - Microsoft SQL licenses for individual server including server name
 - Managed Services (if applicable) for each server
 - Other license costs
 - Service Task breakdown
 - Bandwidth usage based on data center
 - Public IP per data center
 - Support costs
 - Discount or credit if applicable

Below is a table to summarize the services included in portal cost estimation:

|  -  | CPU | Memory | Disk | OS license | Database License | VLANs | VPN | Load Balancer | Object Storage | Public IP | Simple Backup | Appfog | Relational DB | DNS | Bandwidth |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| Main Dashboard Month Estimate | x | x | x | x | x | x | x | x | x | x | x | x | X | X | |
| Data Center View | x | x | x | x | | | | | | | | | | | |
| Group View | x | x | x | x | | | | | | | | | | | |
| Server View | x | x | x | x | | | | | | | | | | | |
| Network | | | | | | x | | | | | | | | | |
| Load Balancer | | | | | | | | x | | | | | | | |
| Site to Site VPN | | | | | | | x | | | | | | | | |
| DNS  | | | | | | | | | | | | | | x | |
| Appfog | | | | | | | | | | | | x | | | |
| Backup | | | | | | | | | | | x | | | | |
| Object Storage | | | | | | | | | x | | | | | | |
| Relational DB | | | | | | | | | | | | | x | | |
| Billing | x | x | x | x | x | x | x | x | x | x | x | x | x | x | x |
