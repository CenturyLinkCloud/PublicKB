{{{
  "title": "Gather Production Server Information",
  "date": "12-27-2017",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article covers the information a user needs to gather before protecting a Production Server using SafeHaven.
This article does not cover any other aspect of the DR setup.

### Production Server Information
Production Servers can either be Windows or Linux. Please refer to [SafeHaven 5.0 Use Case and Support Matrix](../SafeHaven 5 General/SafeHaven-5.0-Use-Case-and-Support-Matrix.md) for more information.

Gather the following information for the servers you want to protect:

1. Server Name
2. O.S. Type
3. Number of vCPU
4. RAM
5. Production Server Size (Storage) that has to be protected  
    a. Provisioned Storage for Windows  
    b. Used Storage for Linux
6. Network/VLAN Information/I.P. Address
7. Server dependencies(grouping servers together)

Apart from this other information regarding Domain Controllers, DNS Servers, transaction rate of SQL Servers, etc. have to be gathered as it impacts the overall disaster recovery setup. CenturyLink's onboarding resource will provide guidance on this.

**Next Step** is to [Determine Storage Requirements](Determine Storage Requirements.md)
