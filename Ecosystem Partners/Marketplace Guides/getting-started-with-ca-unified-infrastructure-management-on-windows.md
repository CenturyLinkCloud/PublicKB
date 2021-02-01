{{{
  "title": "Getting Started With CA Unified Infrastructure Management on Windows (CA UIM)",
  "date": "11-13-2015",
  "author": "Ben Hill",
  "attachments": [],
  "contentIsHTML": false
}}}


![CA Technologies Logo](../../images/ca-technologies-logo.png)

### Technology Profile

CA Unified Infrastructure Management (CA UIM) is a scalable IT monitoring solution that provides 360-degree visibility into systems and infrastructure performance. It creates a single, unified architecture for both traditional and cloud environments, enabling customers to proactively monitor performance and availability and to ensure that end customers are up and running. See more at [www.ca.com](http://www.ca.com).

### Contact CA Technologies
* [Email & phone support](https://www.ca.com/us/contact/call-me.aspx)

### Description
CA Technologies has integrated their _CA Unified Infrastructure Management_ (CA UIM) with the Lumen Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this IT monitoring solution. See more at [CA Unified Infrastructure Management](http://www.ca.com/us/opscenter/ca-unified-infrastructure-management.aspx?intcmp=searchresultclick&resultnum=1).

### Audience
Lumen Cloud users looking to enhance the monitoring capabilities of their Lumen Cloud Environment.

### Impact
After reading this article, the user should be able to install UIM for Windows on a Lumen Cloud server.

### Prerequisites
* Access to the Lumen Cloud platform as an authorized user.
* MS-SQL Database server with superuser login credentials.
* Enable default MS-SQL server listening port `1433`.

### Postrequisites
None

### Deploying UIM for Windows on a New Server
CA UIM is available as a Blueprint for deployment on a new server.

#### Steps to deploy to New Server Blueprint
1. Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.

2. Search for *CA UIM on Windows*.

3. Click the Blueprint icon for *CA UIM on Windows*.

4. Configure the following parameters.
   * Enter Password.
   * Choose Your Group.
   * Choose Your Network.
   * Choose Primary & Secondary DNS.
   * Choose Server Type.
   * Choose Service Level.
   * Enter Sever Name.
   * Enter Database Host Name.
   * Enter Database Name.
   * Enter Database Username.
   * Enter Database Password.
   * Enter UIM Admin Password.
   * Click `next: step 2`.

5. Review and Confirm the Blueprint.

6. Deploy the Blueprint.

7. Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.

8. The Blueprint will run for approximately 20 minutes, and may complete with a 'failed' status.
   * This is due to a timeout caused by the installer running long. If it occurs in the step labeled 'Install CA UIM Single Server on Windows stage3', the message may be ignored.
   * Wait 5 to 10 minutes for the process to complete.

9. Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete.
   * Please do not use the application until you have received this email notification.

10. Access the UIM application through a web browser pointed at the server address.


#### Frequently Asked Questions
For more information about UIM, click on the following links:
* [Getting Started - CA Unified Infrastructure Management](https://wiki.ca.com/display/UIM82/Getting+Started)
* [Demo Video - CA Unified Infrastructure Management Demo](http://www.ca.com/us/opscenter/ca-unified-infrastructure-management.aspx)

#### Issues related to deploying UIM Blueprints on Lumen Cloud
* Contact [our sales team](mailto:sales@ca.com).

#### Who should I contact for support?
* For issues related to deploying the UIM Blueprint on Lumen Cloud, licensing or accessing the deployed software, please visit the [CA Support Website](http://www.ca.com/us/support.aspx?intcmp=headernav).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or through the [Lumen Cloud Support website](https://support.ctl.io/hc/en-us/requests/new).
