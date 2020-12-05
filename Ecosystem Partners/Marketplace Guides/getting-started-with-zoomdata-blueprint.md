{{{
  "title": "Getting Started with Zoomdata - Blueprint",
  "date": "09-30-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![Zoomdata Logo](../../images/ecosystem-zoomdata-logo.png)

### Partner Profile
Zoomdata – The Fastest Visual Analytics for Big Data
[http://www.zoomdata.com](http://www.zoomdata.com).

#### Contact Zoomdata
##### Customer Sales and Support:
* Support Email - [support@zoomdata.com](mailto:support@zoomdata.com)
* Support Telephone - (888) 600-6996
* Sales Email - [sales@zoomdata.com](mailto:sales@zoomdata.com)

### Description
Zoomdata has integrated their technology with the Lumen Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this visual analytics solution.

Zoomdata is the world’s fastest solution for visual analytics of big data. Zoomdata enables business users to visually consume and interact with all the data in the modern enterprise. While specifically built for modern data sources -- including Cloudera -- Zoomdata also works with relational databases and popular cloud applications. Using patented Data Sharpening and Micro-query technologies, Zoomdata empowers business users to visually consume data in seconds, even across billions of rows of data. Zoomdata Fusion enables interactive analytics across disparate data sources, bridging modern and legacy data architectures, blending real-time streams and historical data, and unifying enterprise data on-premises and in the cloud. Zoomdata brings visual analytics to all business users -- not just data analysts -- via an intuitive user interface that can be used out of the box or embedded in custom applications.

Technology from Zoomdata helps Lumen Cloud customers visually consume and interact with Lumen Cloud data services by implementing Zoomdata Server - now available as part of the Lumen Cloud Blueprint Engine.

### Audience
Lumen Cloud Users, Big Data Enthusiasts

### Impact
After reading this article, the user should feel comfortable getting started using the partner technology on Lumen Cloud.

After executing the steps in this Getting Started document, the users will have a functioning Zoomdata Server with which they can start developing big data discovery and self-service visual analytics solutions.

* Getting started with Zoomdata on Lumen Cloud

### Offer
Zoomdata has included a free 30 day trial in a specifi Trial Blueprint. If you are deploying the Zoomdata Production Server or Installing the Zoomdata Server on Existing Hardware please complete [this contact form](http://www.zoomdata.com/centurylink) so that a Zoomdata representative can help you setup a license on your Zoomdata Server.

### Prerequisite
Zoomdata is designed to deliver visual analytics for big data deployments. Through a library of big data connectors, that include Cloudera, Hortonworks, MongoDB, Spark, MySQL, SQLServer and Solr, Zoomdata makes it easy to connect, stream and visualize your big data deployments.

Zoomdata runs best on CentOS v6.5, with a server that has a minimum of 4 ours, and 16GB or RAM.

### Deploy Zoomdata Blueprint
Follow these step by step instructions to deploy Zoomdata.

1. Open the Blueprint Library.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.

2. Search for the Blueprint.
   * To search for the Zoomdata Blueprint, type “Zoomdata” under “Refine Results” in the right panel and click the `Go` button.

3. Choose the Blueprint.
   * There are three Zoomdata Blueprints are available for installations.
   * Trial Server: This minimum configuration is perfect for testing out Zoomdata for a 30 day trial.
   * Production Server:  This configuration has been optimized for a production environment. Please contact [sales@zoomdata.com](mailto:sales@zoomdata.com) to purchase a license.
   * Install Zoomdata Server on Linux: This configuration can be applied to any hardware configuration. Please contact [sales@zoomdata.com](mailto:sales@zoomdata.com) to purchase a license.

4. Choose and Deploy the Blueprint.
   * Click the `deploy blueprint` button to begin configuring your installation.

5. Configure the Blueprint.
   Ensure the following options are configured:
   * Key fields to complete are the password and the Primary DNS field (select ZDHost).
   * The Auto Patching and Install MongoDB sections should be left with their default settings.
   * The Install Zoomdata section requires Company Name, First Name, Last Name, Email Address and Phone Number. The Spark JVM Memory setting is optional and used by Zoomdata for SparkIT functionality and DataFrames. Leave this field blank if your server has less than 10 GB of RAM. Specify in GB. For example: XXg where XX is the amount of RAM to allocate. Leave at least 3 GB to your OS.

6. Review and Confirm the Blueprint.
   * You will come to a confirmation view of what your Blueprint looks like.
   * Verify your configuration details.
   * Click the `deploy blueprint` button.

7. Monitor the Activity Queue.
   * The job will be submitted into a queue and you will be taken to a monitoring page where you can see the progress of each step the Blueprint goes through.
   * To monitor progress, click **Queue** from the Nav Menu on the left.

8. Jump In!
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete.
   * Please do not use the application until you have received this email notification.

### Access and use Zoomdata
Follow these steps to access and use the Zoomdata software.
1. Access the VM.
   * Please log in to your server using the VPN access.
   * [Click here for VPN configuration instructions](../../Network/Lumen Cloud/how-to-configure-client-vpn.md).

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no Zoomdata license costs or additional fees bundled in. To take advantage of the 30 day free trial, select the Zoomdata Trial Version.

### Frequently Asked Questions

#### Where do I get my Zoomdata License?
* The Zoomdata on Lumen Cloud is provided in a bring-your-own-license model. Please contact [sales@zoomdata.com](mailto:sales@zoomdata.com) to activate your Zoomdata license.

#### Is there documentation available for Zoomdata?
* Yes. Please visit [http://docs.zoomdata.com/zoomdata-docs-portal](http://docs.zoomdata.com/zoomdata-docs-portal) for complete documentation.

#### Who should I contact for support?
* For issues related to deploying the Zoomdata Blueprint on Lumen Cloud, please contact [support@zoomdata.com](mailto:support@zoomdata.com) or via telephone: (888) 600-6996.
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new).
