{{{
  "title": "Getting Started With CA Unified Infrastructure Management on Windows (CA UIM)",
  "date": "10-28-2015",
  "author": "Ben Hill",
  "attachments": [],
  "contentIsHTML": false
}}}


![](http://www.infotechgroup.com/wp-content/uploads/2014/08/CA-Technologies-logo.png)

### Technology Profile

CA Unified Infrastructure Management (CA UIM) is a scalable IT monitoring solution that provides 360-degree visibility into systems and infrastructure performance. It creates a single, unified architecture for both traditional and cloud environments, enabling customers to proactively monitor performance and availability and to ensure that end customers are up and running. - See more at [www.ca.com](http://www.ca.com).

### Contact CA Technologies

- [Email & phone support](https://www.ca.com/us/contact/call-me.aspx)

### Description

CA Technologies has integrated their _CA Unified Infrastructure Management_ (CA UIM) with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this IT monitoring solution. solution. - See more at [CA Unified Infrastructure Management](http://www.ca.com/us/opscenter/ca-unified-infrastructure-management.aspx?intcmp=searchresultclick&resultnum=1).

### Audience

CenturyLink Cloud users looking to enhance the monitoring capabilities of their CenturyLink Cloud Environment.

### Impact

After reading this article, the user should be able to install UIM for Windows on a CenturyLink Cloud server.

### Prerequisites

Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisites
None

### Deploying UIM for Windows on a New Server

CA UIM is available as a Blueprint for deployment on a new server.

#### Steps to deploy to New Server Blueprint

  1. Locate the "Install
  2. Click on the blueprint. Select "Deploy Blueprint" on the resulting screen
  3. Configure the Blueprint. Complete the information below:
	  - Enter Password
	  - Choose your group
	  - Choose your network
	  - Choose Primary and Secondary DNS
	  - Choose the Server Type
	  - Choose Service Level
	  - Enter Sever Name
  4. Review and Confirm Blueprint
  5. Deploy the Blueprint
  6. Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  7. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Steps to deploy to an existing server

  1. Deploy or Identify an existing server
  2. Locate the "Install UIM on Existing Server" blueprint in the Blueprint Library
  3. Select "Deploy Blueprint"
  4. Select the server to be deployed
  5. Select "next: step 2"
  6. Select "Deploy Blueprint"
  7. Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  8. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

#### Frequently Asked Questions

For more information about UIM, click on the following links:

[Getting Started - CA Unified Infrastructure Management](https://wiki.ca.com/display/UIM83/Getting+Started)

[Demo Video - CA Unified Infrastructure Management Demo](http://www.ca.com/us/opscenter/ca-unified-infrastructure-management.aspx)


#### Issues related to deploying UIM Blueprints on CenturyLink Cloud

- Contact [our sales team](mailto:sales@ca.com).

#### Who should I contact for support?

- For issues related to deploying the UIM Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [CA Support Website](http://www.ca.com/us/support.aspx?intcmp=headernav).
- For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or through the [CenturyLink Cloud Support website](https://support.ctl.io/hc/en-us/requests/new).
