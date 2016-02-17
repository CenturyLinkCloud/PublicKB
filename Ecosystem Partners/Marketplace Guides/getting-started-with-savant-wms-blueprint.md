{{{
  "title": "Implementing Savant ADC to Automate Your Warehouse Operations",
  "date": "December 15, 2015",
  "author": "Jim Cawley",
  "attachments": [],
  "contentIsHTML": false
}}}

![Savant Software, Inc.](http://www.savantwms.com/images/savant_logo.jpg)

### Technology Profile

This blueprint allows a company to deploy the environment necessary to run Savant Software's ADC or WMS application.

### Description

Savant ADC is an entry level WMS solution targeting small to mid-sized companies. It includes several add-on modules and a seamless upgrade path into Savant's more robust WMS solution.

For more information, please visit http://www.savantwms.com

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should get a functioning cloud server environment upon which they can install and run the Savant ADC or WMS application.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Approved mobile computers with latest browser capabilities.
- Approved barcode printer(s).

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80, 443
  3. Download approved VPN software and remote desktop capabilities.

### Deploying the Single Blueprint

#### Steps to Deploy Blueprint
1. **Locate the Single01 Blueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Single” in the keyword search on the right side of the page.
  3. Locate the 'Single01 Blueprint

2. **Choose and Deploy the Blueprint.**
   Click the "Single01" Blueprint.

3. **Customize the Blueprint**
  1. Build Server
    1. Input Password and Confirm
    2. Accept Default Group
    3. Accept Default Network
    4. Enter Manually Specify for Default Primary and Secondary DNS
    5. Accept Default Server Type
    6. Select Premium Service Level

  2. Server Name
    1. Enter Your Company Name

  3. Install IIS on Windows
    1. Select No for Specify Credentials
    2. Select All for IIS Features

  4. Install Remote Desktop Services on Windows
    1. Select No to Specify Credentials

  5. Install SQL Server on Windows
    1. Select No to Specify Credentials
    2. Enter and Confirm a SA Password
    3. Select Newest (2014) Standard SQL Version
    4. Accept the Following Features
      1. Database Engine Services
      2. Full Text Search
      3. Reporting Services
      4. Management Tools
    5. Accept Default Database Engine Collation
    6. Accept MultiDimensional Analysis Services Mode
    7. Enter SQL Instance Name or Accept Default

4. **Review and Confirm the Blueprint**
  1. Click “next: step 2”
  2. Verify your configuration details.

5. **Deploy the Blueprint**
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Deploy Savant ADC to an existing server (alternate option)

Savant ADC is NOT available as a Script Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on servers.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  License fees and implementation services are not included in this price and are extra.

### About Savant Software, Inc.
CenturyLink Cloud works with [Savant Software, Inc](http://savantwms.com) to provide the Savant ADC or WMS applications

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Savant Software, Inc. Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Savant Software Support website](http:/www.savantwms.com)
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
