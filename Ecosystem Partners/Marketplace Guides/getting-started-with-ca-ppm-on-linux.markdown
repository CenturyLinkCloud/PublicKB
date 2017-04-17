{{{
  "title": "Getting Started With CA PPM on Linux",
  "date": "11-13-2015",
  "author": "Ben Hill",
  "attachments": [],
  "contentIsHTML": false
}}}


![](http://www.infotechgroup.com/wp-content/uploads/2014/08/CA-Technologies-logo.png)

### Technology Profile 

CA Project and Portfolio Management (CA PPM) helps business leaders to deliver the “right” products and applications to market faster and with less risk. Only CA PPM connects strategy to execution across the entire enterprise portfolio with relevant and immediate visibility needed to improve project ROI. - See more at [www.ca.com](http://www.ca.com).


### Contact CA Technologies 

- [Email & phone support](https://www.ca.com/us/contact/call-me.aspx)

### Description

CA Technologies has integrated their _CA Project and Portfolio Management_ (CA PPM) solution with the CenturyLink Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this project and portfolio management solution. - See more at [CA PPM](http://www.ca.com/us/intellicenter/ca-ppm.aspx).

### Audience 

CenturyLink Cloud users looking for a Project & Portfolio Management solution.

### Impact 

After reading this article, the user should be able to install CA PPM for Linux on a CenturyLink Cloud server.

### Prerequisites 

- Access to the CenturyLink Cloud platform as an authorized user.
- For a complete listing of prerequisites and guidelines to install CA PPM  please see: [CA PPM Wiki](https://wiki.ca.com/ca-ppm/14-3).

### Postrequisites 

None

### Deploying PPM for Linux on a New Server

CA PPM is available as a Blueprint for deployment on a new server.

#### Steps to deploy to New Server Blueprint 

  1. Access the blueprints library 
  2. Search for _CA PPM14-3 Linux_
  3. Click on blueprint icon for CA PPM14-3 Linux 
  4. Deploy Blueprint 
	  - Enter Password
	  - Choose Your Group
	  - Choose Your Network
	  - Choose Primary & Secondary DNS
	  - Choose Server Type
	  - Choose Service Level
	  - Enter Sever Name
	  - Enter Database Host Name 
	  - Enter Database SID
	  - Enter Database Username 
	  - Enter Database Password
	  - Enter Database System Username 
	  - Enter Database System Password 
	  - Enter DBHOST Administrator User 
	  - Click Next: Step 2
  5. Review and Confirm Blueprint
  6. Deploy the Blueprint
  7. Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  8. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.
  9. You can access the application with (http://ip:8090/) and (http://ip:80/) 
 
#### Frequently Asked Questions 

For more information about PPM, click on the following links:

- CA PPM - [Getting Started Wiki](https://wiki.ca.com/ca-ppm/14-3/getting-started)

#### Who should I contact for support?

- For issues related to deploying the PPM Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [CA support website](http://www.ca.com/us/support.aspx?intcmp=headernav).
- For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or through the [CenturyLink Cloud support website](https://support.ctl.io/hc/en-us/requests/new).
