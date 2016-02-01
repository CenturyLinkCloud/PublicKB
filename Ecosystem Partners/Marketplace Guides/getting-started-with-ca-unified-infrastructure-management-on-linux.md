{{{
  "title": "Getting Started With CA Unified Infrastructure Management on Linux (CA UIM)",
  "date": "11-13-2015",
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

CA Technologies has integrated their _CA Unified Infrastructure Management_ (CA UIM) with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this IT monitoring solution. - See more at [CA Unified Infrastructure Management](http://www.ca.com/us/opscenter/ca-unified-infrastructure-management.aspx?intcmp=searchresultclick&resultnum=1).

### Audience

CenturyLink Cloud users looking to enhance the monitoring capabilities of their CenturyLink Cloud Environment.

### Impact

After reading this article, the user should be able to install UIM for Linux on a CenturyLink Cloud server.

### Prerequisites

- Access to the CenturyLink Cloud platform as an authorized user
- MS-SQL Database server with superuser login credentials
- Enable default MS-SQL server listening port 1433

### Postrequisites
None

### Deploying UIM for Linux on a New Server

CA UIM is available as a Blueprint for deployment on a new server.

#### Steps to deploy to New Server Blueprint

  1. Access the blueprints library
  2. Search for _CA UIM on Linux_
  3. Click on blueprint icon for CA UIM on Linux
  4. Deploy Blueprint
	  - Enter Password
	  - Choose Your Group
	  - Choose Your Network
	  - Choose Primary & Secondary DNS
	  - Choose Server Type
	  - Choose Service Level
	  - Enter Sever Name
	  - Enter Database Host Name
	  - Enter Database Name
	  - Enter Database Username
	  - Enter Database Password
	  - Enter UIM Admin Password
	  - Click Next: Step 2

  5. Review and Confirm Blueprint
  6. Deploy the Blueprint
  7. Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  8. The blueprint will run for approximately 20 minutes, and may complete with a 'failed' status.  This is due to a timeout due to the installer running long, and if it occurs in the step labeled 'Install CA UIM Single Server on Linux stage3', may be ignored.  Wait 5 to 10 minutes, and the process will complete.
  9. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.
  10. Access the UIM application through a web browser pointed at the server address.


#### Frequently Asked Questions

For more information about UIM, click on the following links:

[Getting Started - CA Unified Infrastructure Management](https://wiki.ca.com/display/UIM82/Getting+Started)

[Demo Video - CA Unified Infrastructure Management Demo](http://www.ca.com/us/opscenter/ca-unified-infrastructure-management.aspx)


#### Issues related to deploying UIM Blueprints on CenturyLink Cloud

- Contact [our sales team](mailto:sales@ca.com).

#### Who should I contact for support?

- For issues related to deploying the UIM Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [CA Support Website](http://www.ca.com/us/support.aspx?intcmp=headernav).
- For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or through the [CenturyLink Cloud Support website](https://support.ctl.io/hc/en-us/requests/new).
