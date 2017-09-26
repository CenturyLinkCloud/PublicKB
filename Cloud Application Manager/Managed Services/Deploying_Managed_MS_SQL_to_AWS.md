{{{
  "title": "Deploying CenturyLink Managed MS SQL via Cloud Application Manager",
  "date": "09-20-2017",
  "author": "Thomas Broadwell",
  "attachments": [],
  "contentIsHTML": false
}}}

### Introduction
The foundation of Microsoft’s comprehensive data platform, SQL Server delivers breakthrough performance for mission-critical applications – and it gets even better with CenturyLink Cloud and our Managed Microsoft SQL service.
Achieve maximum performance by combining CenturyLink Managed Microsoft SQL Server with CenturyLink Cloud Hyperscale instances and autoscale capabilities. Combine this Microsoft SQL Server AlwaysOn to realize a grid solution that can deliver at least 15,000 IOPS to sustain even the most demanding workloads.

### Overview
Cloud Application Manager’s Managed Services Anywhere allows customers to deploy workloads and delegate the management of the workload to CenturyLink, relieving themselves of the burdens of day to day monitoring, patching and Operational activities.  Through Cloud Application Manager, a customer can provision a new VM instance with MS SQL within their AWS provider and chose to have CenturyLink manage both the Operating System and MS SQL.

**Supported Versions**
*  Microsoft SQL Server 2008 R2
*  Microsoft SQL Server 2012
*  Microsoft SQL Server 2014

**Supported Editions**
*  Standard Edition
*  Enterprise Edition

**Supported Operating Systems**
*	Managed Microsoft Windows Server 2008 R2
*	Managed Microsoft Windows Server 2012

**Supported Services**
*	Support for Microsoft SQL Server Analysis Services (SSAS)
*	Support for Microsoft SQL Server Reporting Services (SSRS)
*	Support for Microsoft SQL Server Integration Services (SSIS)
*	Support for Microsoft SQL Server Database Mirroring
*	Support for Microsoft SQL Server Database Snapshots
*	Support for Microsoft SQL Server Transparent Database Encryption (TDE)
*	Support for Microsoft SQL Server AlwaysOn


#### Deploying Managed MS SQL to your AWS provider with CenturyLink Cloud Application Manager:
1.	In Boxes, Deployment Policies, search for “SAMPLE”
2.	Select SAMPLE Managed MS SQL Deployment Policy 

![mgd-mssql-1.PNG](../../images/cloud-application-manager/mgd_mssql-1.PNG)

3.	Select the Configure (Gear) dropdown 
4.	Select “Clone”:

![mgd_mssql-2.PNG](../../images/cloud-application-manager/mgd_mssql-2.PNG)

5.	Modify the Cloned Deployment Policy with your details (Icon, Name, Description) 
6.	Select Save

![mgd_mssql-3.PNG](../../images/cloud-application-manager/mgd_mssql-3.PNG)

7.	Edit your new Deployment Policy with your environment specific details (Resource, Placement and Network) and Save. 
**NOTE:  The CenturyLink recommended Instance type is selected in the SAMPLE Managed MS SQL deployment.  Modification of this Instance type may result in significant performance issues.**
**Disk configuration settings should remain as configured in SAMPLE Managed MS SQL deployment policy.**

![mgd_mssql-4.PNG](../../images/cloud-application-manager/mgd_mssql-4.PNG)
![mgd_mssql-5.PNG](../../images/cloud-application-manager/mgd_mssql-5.PNG)

8.	In Boxes, Deployment Policies, search for “CenturyLink Managed SQL Server”
9.	Select CenturyLink Managed SQL Server Script Box

![mgd_mssql-6.PNG](../../images/cloud-application-manager/mgd_mssql-6.PNG)

10.	Select Deploy

![mgd_mssql-7.PNG](../../images/cloud-application-manager/mgd_mssql-7.PNG)

11.	Update the Details of the instance that is to be deployed, selecting the appropriate Deployment Policy for your desired environment.
12.	Select Deploy

![mgd_mssql-8.PNG](../../images/cloud-application-manager/mgd_mssql-8.PNG)

##### Help

Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md) for help. Or you may contact [support](http://managedservices.ctl.io) to request help.
