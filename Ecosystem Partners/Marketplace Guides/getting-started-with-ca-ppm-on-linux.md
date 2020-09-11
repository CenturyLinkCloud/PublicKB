{{{
  "title": "Getting Started With CA PPM on Linux",
  "date": "11-13-2015",
  "author": "Ben Hill",
  "attachments": [],
  "contentIsHTML": false
}}}

![CA Technologies Logo](../../images/ca-technologies-logo.png)

### Technology Profile
CA Project and Portfolio Management (CA PPM) helps business leaders to deliver the “right” products and applications to market faster and with less risk. Only CA PPM connects strategy to execution across the entire enterprise portfolio with relevant and immediate visibility needed to improve project ROI. - See more at [www.ca.com](http://www.ca.com).

### Contact CA Technologies
* [Email & phone support](https://www.ca.com/us/contact/call-me.aspx)

### Description
CA Technologies has integrated their _CA Project and Portfolio Management_ (CA PPM) solution with the CenturyLink Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this project and portfolio management solution. - See more at [CA PPM](http://www.ca.com/us/intellicenter/ca-ppm.aspx).

### Audience
CenturyLink Cloud users looking for a Project & Portfolio Management solution.

### Impact
After reading this article, the user should be able to install CA PPM for Linux on a CenturyLink Cloud server.

### Prerequisites
* Access to the CenturyLink Cloud platform as an authorized user.
* For a complete listing of prerequisites and guidelines to install CA PPM  please see: [CA PPM Wiki](https://wiki.ca.com/ca-ppm/14-3).

### Postrequisites
None

### Deploying PPM for Linux on a New Server
CA PPM is available as a Blueprint for deployment on a new server.

#### Steps to deploy to New Server Blueprint
1. Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.

2. Search for *CA PPM14-3 Linux*.

3. Click the Blueprint icon for *CA PPM14-3 Linux*.

4. Configure the following parameters.
   * Enter Password.
   * Choose Your Group.
   * Choose Your Network.
   * Choose Primary & Secondary DNS.
   * Choose Server Type.
   * Choose Service Level.
   * Enter Sever Name.
   * Enter Database Host Name.
   * Enter Database SID.
   * Enter Database Username.
   * Enter Database Password.
   * Enter Database System Username.
   * Enter Database System Password.
   * Enter DBHOST Administrator User.
   * Click `next: step 2`.

  5. Review and Confirm the Blueprint.

  6. Deploy the Blueprint.

  7. Monitor the Deployment Queue to view the progress of the Blueprint.
     * To monitor progress, click **Queue** from the Nav Menu on the left.
     * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

  8. You can access the application with (http://ip:8090/) and (http://ip:80/).

#### Frequently Asked Questions
For more information about PPM, click on the following links:
* CA PPM - [Getting Started Wiki](https://wiki.ca.com/ca-ppm/14-3/getting-started)

#### Who should I contact for support?
* For issues related to deploying the PPM Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [CA support website](http://www.ca.com/us/support.aspx?intcmp=headernav).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or through the [CenturyLink Cloud support website](https://support.ctl.io/hc/en-us/requests/new).
