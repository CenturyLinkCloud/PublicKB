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
(../../images/cloud-application-manager/mgd_mssql-1.JPG "Step 1 and 2")
3.	Select the Configure (Gear) dropdown 
4.	Select “Clone”:
![alt text](PublicKB/images/cloud-application-manager/mgd_mssql-2.JPG "Step 3 and 4")
5.	Modify the Cloned Deployment Policy with your details (Icon, Name, Description) 
6.	Select Save
![alt text](PublicKB/images/cloud-application-manager/mgd_mssql-3.JPG "Step 5 and 6")
7.	Edit your new Deployment Policy with your environment specific details (Resource, Placement and Network) and Save. 
**NOTE:  The CenturyLink recommended Instance type is selected in the SAMPLE Managed MS SQL deployment.  Modification of this Instance type may result in significant performance issues.**
**Disk configuration settings should remain as configured in SAMPLE Managed MS SQL deployment policy.**
![alt text](PublicKB/images/cloud-application-manager/mgd_mssql-4.JPG "Step 7a")
![alt text](PublicKB/images/cloud-application-manager/mgd_mssql-5.JPG "Step 7b")
8.	In Boxes, Deployment Policies, search for “CenturyLink Managed SQL Server”
9.	Select CenturyLink Managed SQL Server Script Box
![alt text](PublicKB/images/cloud-application-manager/mgd_mssql-6.JPG "Step 8 and 9")
10.	Select Deploy
![alt text](PublicKB/images/cloud-application-manager/mgd_mssql-7.JPG "Step 10")
11.	Update the Details of the instance that is to be deployed, selecting the appropriate Deployment Policy for your desired environment.
12.	Select Deploy
![alt text](PublicKB/images/cloud-application-manager/mgd_mssql-8.JPG "Step 11 and 12")
