{{{
  "title": "Deploy Microsoft SQL Server using Blueprint",
  "date": "3-11-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

### Overview

CenturyLink Cloud customers can procure and deploy Microsoft SQL Server licensing within the Control Portal. Microsoft SQL Server is licensed via the Microsoft SPLA program. By using the CenturyLink Cloud public blueprint customers have multiple ways to consume and install this business critical database software.

### Prerequisites

* A CenturyLink Cloud Account
* Supported Guest Operating Systems are deployed and in a running state:
    * Windows 2008 R2 Standard 64-bit
    * Windows 2008 R2 Enterprise 64-bit
    * Windows 2008 R2 Datacenter 64-bit
    * Windows 2012 Datacenter 64-bit
    * Windows 2012 R2 Data Center 64-bit
* ~15 GB Free Storage on C:\
* The Supported SQL Server Editions via blueprint are as follows:
    * SQL Server 2008 R2 Web Edition
    * SQL Server 2008 R2 Standard Edition
    * SQL Server 2008 R2 Enterprise Edition
    * SQL Server 2012 Web Edition
    * SQL Server 2012 Standard Edition
    * SQL Server 2012 Enterprise Edition
    * SQL Server 2014 Web Edition
    * SQL Server 2014 Standard Edition
    * SQL Server 2014 Enterprise Edition

### Exceptions

This KB does not apply to [Managed Microsoft SQL Customers.](http://www.centurylinkcloud.com/managed-services/ms-sql)

### General Notes

The following are quick tips/notes based on past experiences with customers leveraging this blueprint

* It is not possible at the current time to install SQL to a drive other than C:\ via blueprint. Customers can modify the SQL database, tempdb, log locations post install to other volumes using SQL tools
* The fee's for Microsoft SQL server will be applied automatically to the customers invoice when using the public blueprint. These fee's are documented in a customers agreement. If you are unsure what these fee's are please contact your account manager.
* Licensing fee's are adjusted based on number of vCPU allocated to a virtual machine. By using tools like Autoscale, customers billing will be modified as vCPU configurations change.

### Installing Microsoft SQL Server using Group Tasks

1. **Navigate to the Servers Menu in Control**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-01.png">

2. **Browse to the Group that houses the VM(s) you want to deploy SQL. Select Action, Execute Package.**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-02.png">

3. **Search for '<strong>SQL</strong>' and select the <strong>Install SQL Server on Windows</strong> blueprint.**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-03.png">

4. **Select SQL Installation Options.**

Input the appropriate parameters based on the SQL server requirements for your application.

Select the VM(s) in the Group you want to deploy SQL. Customers can choose an individual VM or multiple. (Quick Tip: Only supported Guest Operating Systems will be shown)

<img src="../images/deploy-microsoft-sql-server-using-blueprint-04.png">

## Installing Microsoft SQL Server using Blueprints Library

1. **Navigate to the Blueprint Library in Control.**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-05.png">

2. **Search for '<strong>SQL</strong>' and select '<strong>Install SQL Server on Existing Server</strong>.'**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-06.png"><img src="../images/deploy-microsoft-sql-server-using-blueprint-07.png">

3. **Select Deploy blueprint.**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-08.png">

4. **Input the appropriate parameters based on the SQL server requirements for your application and select the Virtual Machine you wish to execute the install against.**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-09.png">

5. **Confirm the virtual machine(s), features and select Deploy Blueprint**

<img src="../images/deploy-microsoft-sql-server-using-blueprint-10.png">
