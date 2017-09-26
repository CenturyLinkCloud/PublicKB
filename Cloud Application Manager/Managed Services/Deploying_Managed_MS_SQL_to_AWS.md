{{{
  "title": "Deploying CenturyLink Managed MS SQL via Cloud Application Manager",
  "date": "09-20-2017",
  "author": "Thomas Broadwell",
  "attachments": [],
  "contentIsHTML": false
}}}

### Introduction
Cloud Application Manager’s Managed Services Anywhere allows customers to deploy workloads and delegate the management of the workload to CenturyLink, relieving themselves of the burdens of day to day monitoring, patching and Operational activities.  Through Cloud Application Manager, a customer can provision a new instance of MS SQL on their AWS provider and chose to have CenturyLink manage the deployed instance.

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
![mgd_mssql-4.PNG](../../images/cloud-application-manager/mgd_mssql-5.JPG "Step 7b")

8.	In Boxes, Deployment Policies, search for “CenturyLink Managed SQL Server”
9.	Select CenturyLink Managed SQL Server Script Box

![mgd_mssql-6.PNG](../../images/cloud-application-manager/mgd_mssql-6.PNG)

10.	Select Deploy

![mgd_mssql-7.PNG](../../images/cloud-application-manager/mgd_mssql-7.PNG)

11.	Update the Details of the instance that is to be deployed, selecting the appropriate Deployment Policy for your desired environment.
12.	Select Deploy

![mgd_mssql-8.PNG](../../images/cloud-application-manager/mgd_mssql-8.PNG)
