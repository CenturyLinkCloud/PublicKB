{{{
  "title": "How To Publish a Partner Template from a Virtual Appliance",
  "date": "2-25-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}


### Description
This knowledge base article documents the process required for Cloud Ecosystem Program partners to upload and publish Partner Templates to customers of the CenturyLink Cloud platform using an uploaded "virtual appliance" image.

### Audience
- Cloud Ecosystem Program Members
- CenturyLink Cloud Support Personnel

### Impact
For some CenturyLink Cloud Ecosystem Program members, a Virtual Appliance or "custom image" is simply the best model for technology integration and deployment.  CenturyLink Cloud Ecosystem members can upload their VMware-based image technology by following this process.


### Prerequisite
- Cloud Ecosystem Program status - must be at least Candidate
- Supplied Image Files:
    - Must meet the existing OVF image requirements
        http://www.ctl.io/knowledge-base/service-tasks/requirements-for-custom-imagevm-imports
    - Should adhere to Image Best Practices
        http://www.ctl.io/knowledge-base/service-tasks/best-practices-and-preparation-for-a-virtual-machineovfova-import
- Please ensure that company and product name are in any image filenames
- Be aware that importing a virtual appliance or image is considered a billable service task by CenturyLink Cloud Support. These fees will count against an Ecosystem Partner's integration credit.  More information on Service Tasks and pricing can be found here: http://www.ctl.io/knowledge-base/service-tasks/requesting-service-tasks-on-centurylink-cloud


### Publish Partner-Supplied 'Custom Image' Process
This is an easy 3 step process that enables Ecosystem Partners to provide their OVA file via FTP and then request that it be moved to the Ecosystem Partner Global Repository.

#### Step 1 - Open Service Task request and ask for a FTP account to upload the image to
Open a service task request ticket with ServiceTasks@Tier3.com with the following details:

----
TO: ServiceTasks@Tier3.com

SUBJECT:  Custom Image Import Request for CLC Ecosystem Partner

CLC Support Team,

Please create a ticket for the following service task:

Please create a FTP user account in ### Data Center so that we can upload an Partner Template/Image to be imported to the Ecosystem Program Global Repo.  Kindly respond with the login details.  We will upload the image and respond with a follow-up request to import the image to the repo.

Please let me know if you have any questions or issues.

Thank you very much,

your.name.here

----


#### Step 2 - Upload the Image via FTP
Upload your OVA file via FTP to the location provided by the Service Request team.  Please do not use any compression besides .zip format.


#### Step 3 - Request the image to the Global Repo
Please reply to the previous service task request email with the FTP login from ServiceTasks@Tier3.com with the following details:

----
_REPLY TO THE PREVIOUS REQUEST EMAIL TO KEEP THE REQUEST IN ONE TICKET_

CLC Support Team,

Please Import the custom image referenced below to the Ecosystem Program global repo.  Instructions and more information can be found here.

- Ecosystem Partner Name: ##############
- Ecosystem Partner Account Alias: ####
- URL to download image directly: ###############
- Data Center the image was uploaded to via FTP: ###
- Import Image Filename:  ########.ova
- root or Administrator password:  ##########
- Additional Notes or work to be done: ####
- Additional documentation or KB Article Links needed to import the image:  #####

Please let me know if you have any questions or issues.

Thank you very much,

your_name_here

----


### Frequently Asked Questions

#### What are the costs associated with importing a virtual appliance?
Importing a virtual appliance provided by a Cloud Ecosystem Partner aligns with how a customer would import a custom image and is considered a billable service task.  The cost for the Service Task is $195/hr with a 2 hour minimum, making it $390 total.  Additional support required would be $195/hr.  More information on Service Task Fees is available here: http://www.ctl.io/service-tasks#Pricing
