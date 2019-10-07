{{{
"title": "Cloud Platform - Release Notes: September 17, 2019",
"date": "09-17-2019",
"author": "Anthony Hakim",
"keywords":["centurylink", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (5)

#### Application Lifecycle Management

##### New Origin preset tag

Application Lifecycle Management now supports a new preset tag called Origin, which refers to the Cloud Application Manager environment URL that triggers a deployment. For more information about preset tags, please refer to this [KB article](../../Cloud Application Manager/Administering Your Organization/resource-tags.md)

##### Support for the AWS Europe (Stockholm) region

Application Lifecycle Management now supports another AWS region: Europe (Stockholm) and its corresponding availability zones, with the API name of eu-north-1. Once you synchronize your AWS provider in Cloud Application Manager, you will be able to select the availability zones corresponding to the new region in your Deployment Policy boxes.

##### New CloudFormation type supported

Application Lifecycle Management now supports an additional CloudFormation type to be used in CloudFormation template boxes. This additional types is: "AWS::Config::OrganizationConfigRule". Users can choose this new resource type in the template definition of any CloudFormation template box, or update any existing template instance to use it.

#### Managed Services Anywhere

##### New Public Checks Catalog

Managed Services Anywhere has provided a public website that provides details of all the configurable checks within the Monitoring Catalog. Now, whether a current CAM customer or prospective CAM customer, all can review the catalog without the need for a CAM login. As checks are added, the MSA Checks Catalog will dynamically be updated providing customers an always current list of checks.

#### Dedicated Cloud Compute (DCC)

##### DCC UI

The DCC UI have been updated to display Virtual Intelligent Hosting Instance (VIHI) CPU and Memory utilization metrics, similar to the VM metrics displayed in SavvisStation Portal Compute Dashboard.

#### Redhat Upgrades 

##### Red Hat 6 & Red Hat 7 Upgrades

The CenturyLink Cloud team is providing notice regarding a technology update for Red Hat 6 & Red Hat 7 machines on all CenturyLink Cloud accounts. In an effort to provide the quality service our customers expect from CenturyLink, we will be automatically updating all Red Hat 6 & Red Hat 7 machines to point to the new RHUI 3.X which will allow customers to continue to receive crucial Red Hat package updates. 

On October 2, 2019, beginning at 10am CST, the CenturyLink Cloud team will begin the updates. The updates are anticipated to take around five hours, however during the update, Customers’ virtual machines will have full accessibility and no reboot is needed. 

There is no action required on your part to perform the update, however, if you would like to perform the update before the automated upgrade, you can do so by running the Blueprint “Upgrade to RHUI 3” on your Red Hat machines. 

That Blueprint can be found by following this link and logging into your CenturyLink Cloud account: https://control.ctl.io/Blueprints/Browser/Details/16667.  
 
