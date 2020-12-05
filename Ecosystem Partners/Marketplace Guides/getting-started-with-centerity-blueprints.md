{{{
  "title": "Getting started with Centerity Blueprints",
  "date": "2-3-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![Centerity Logo](../../images/coppermine-stack-logo.png)

### Partner Profile
Centerity Monitor is a next-generation, End-to-End IT Monitoring Platform for an organization’s entire IT monitoring needs. Centerity Monitor provides business value and real-time analytics regarding the status, performance and availability of all IT assets whether in the cloud or on premise, in complex, hybrid environments. Centerity’s unique, unified platform, named a Gartner Cool Vendor in 2014, can serve the needs of both IT executives and administrators while providing a complete business intelligence layer across all IT assets via cross technical and functional domain impact and trend analysis.

http://www.Centerity.com

#### Contact Centerity
##### Centerity Sales:
info-us@centerity.com
+1-339-225-7006

##### Centerity Support:
* Email: support@centerity.com
* US & Americas Customers: +1 (339) 225-6064
* EMEA & APAC Customers: +1 (339) 225-7010

### Description
Centerity has integrated their technology with the Lumen Cloud platform and produced several Blueprints. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Cloud APM solution.

Centerity offers integrated monitoring solution with Lumen Cloud platform. This document will guide Lumen users how to use Centerity Monitor in the Lumen cloud with a few easy steps.

![Diagram](https://t3n.zendesk.com/attachments/token/hAxZSNLbzTswDqfATtK7gOONm/?name=bsm.jpg)

### Solution Overview
Centerity Monitor is an enterprise-class and carrier-class, next-generation, unified IT monitoring platform for complex hybrid environments including all physical, virtual, application and cloud assets from the physical (switches, services), network (WAN, LAN, VOIP), application (OS, Standard & non-Standard), virtual (VMware, Hyper-V, Xen), end-user experience (EUX/optional), Big Data (Hadoop, SAP HANA, NoSQL), cloud and Business Service Management (BSM) layers with multi-tenancy and federated scalability.

Centerity Monitor provides a business intelligence layer across all of your IT assets, end-to-end, whether on prem or off, including all physical, virtual, application and cloud assets. Centerity functions as a single unified platform for both executives and administrators delivering real-time performance and availability metrics and business process views with Business Service Management (BSM) and End-User Experience (EUX) functionality.

Centerity Monitor provides accurate real-time measurements of performance and availability against SLAs with drill-down root cause analysis, intelligent alerting, predictive and trend analysis, inventory and asset discovery, CMDB, ticketing, automation, live maps and visual, interactive graphs, in addition to other advanced features.

Centerity Monitor’s business value is to provide business analytics and business intelligence via a unified software platform with superior Time-to-Value (TTV), Total Cost of Ownership (TCO) and Return on Investment (ROI) characteristics.

### Offer
Centerity Systems is offering a subset of its unified IT monitoring platform as part of a no charge, 30 day, one-time trial program for Linux and Windows servers (10 services max) within Lumen’s Cloud. Through this unique offer, users will have access to the Centerity Monitor Dashboard, which provides key metrics, summary views of real-time system health and availability, host and service group status and event status as well as access to all Centerity Monitor reports such as system utilization, usage summary, uptime, trends, and history. Please check with Lumen for any access charges that may apply to using its Cloud.

For this trial, users will have complete access to any of the application metric capture profiles. These are available through Centerity Support:

* Linux  Server
* Active Directory 2012
* IIS 2012
* Exchange 2013
* SCCM 2012
* SharePoint 2013
* Lync 2010
* MSSQL 2008
* MSSQL 2012
* MSSQL 2014

Once the trial period is over, users will have the option of licensing the solution on a prepaid, subscription fee basis.

Centerity will also offer access to its complete enterprise-class and carrier-class solution that includes IT monitoring coverage for all IT assets including assets at the physical, virtual, network, and application layers, in addition to features such as our Business Service Management (BSM), End-User Experience (EUX), Map Dashboards, Inventory, Discovery, Automation, and Policy Manager modules. Please contact Centerity directly for offer and pricing details.

All use of Centerity software, documentation, and services is governed by Centerity’s Software License and Support Agreement or End User License Agreement (EULA). Contact Centerity for details of the agreement.

### Audience
Lumen Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Centerity Monitor technology on Lumen Cloud.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.

### Postrequisite
* Adding an external ip-address to an existing or new Lumen server.
  ![ip.jpg](https://t3n.zendesk.com/attachments/token/kObGC9P2IjP1ate0NexwFNiXz/?name=ip.jpg)

* Allow incoming traffic for port 5666 to an existing or new server.
  ![port.jpg](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)

### Centerity Blueprints
* Install Centerity Windows Agent 64bit - Deploys Centerity Monitor Agent on Windows OS.
* Install Centerity CentOS / Red Hat Agent 64bit - Deploys Centerity Monitor Agent on CentOS / Red Hat Linux OS.


### Install Centerity Windows Agent 64bit Blueprint
1. Locate the Centerity Windows Agent 64bit Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Centerity” in the keyword search on the right side of the page.
   * Locate the Centerity Windows Agent 64 Bit Blueprint.

2. Choose and Deploy the Blueprint. Click the “Centerity Windows Agent 64 Bit” Blueprint.

3. Configure the Blueprint.
   Complete the information below:
   * Execute on Server: The windows server to deploy the Blueprint on.
   * Email: Email address for Centerity user.
   * Password: Centerity Monitor password.
   * IP Address: External IP-address for Centerity to monitor.
   * Host Profile: Select 1-multiple profiles relevant for the Windows environment, according to the installed software.

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click on the `deploy blueprint` button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * YTo monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Install Centerity CentOS / Red Hat Agent 64bit Blueprint
1. Locate the Centerity CentOS / Red Hat Agent 64bit Blueprint.
   * Starting from the Lumen Control Panel, navigate to the Blueprints Library.
   * Search for “Centerity” in the keyword search on the right side of the page.
   * Locate the Centerity CentOS / Red Hat Agent 64bit Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the “Centerity CentOS / Red Hat Agent 64bit” Blueprint.

3. Configure the Blueprint.
   Complete the information below:
   * Execute on Server: The Windows server to deploy the Blueprint on.
   * SSL: SSL / No SSL Agent, depends on the Linux server itself. The openssl and openssl098e packages are required for SSL monitoring.
   * Email: Email address for Centerity user.
   * Password: Centerity Monitor password.
   * IP Address: External IP-address for Centerity to monitor.
   * Host Profile: Select 1-multiple profiles relevant for the Windows environment, according to the installed software.

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Access Centerity Monitor
After your Blueprint deploys successfully, please follow these instructions to access your Centerity Monitor solution:
* Check email to obtain Centerity Login information.
* Log in to the Centerity server via web browser with the provided credentials.
* Review your dashboard and click on the top right question mark for the user guide.
  ![dashboard.jpg](https://t3n.zendesk.com/attachments/token/FC2YHIrUuu0ZvUcuhMVLoAMPq/?name=dashboard.jpg)

* For any further help contact Centerity Support Center support@centerity.com.

### Troubleshooting
#### Windows
Windows Firewall: When Windows firewall is enabled, add an inbound rule to allow traffic for port `5666`.

![i1.jpg](https://t3n.zendesk.com/attachments/token/cCEX4r1ULiOMKzFKmTha6bqB1/?name=i1.jpg)

![i2.jpg](https://t3n.zendesk.com/attachments/token/Y1oeecZtyj0dv54T6BDYU1BaI/?name=i2.jpg)

#### Linux - CentOS / Red Hat
IPTables: When iptables is enabled: add an inbound rule to allow traffic for port `5666`.
1. Edit the iptables startup config file.
   ``bash
   # vi /etc/sysconfig/iptables
   ``

2. Add the following rule.
   ``bash
   -A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 5666 -j ACCEPT
   ``

3. Restart iptables.
   ``bash
   # service iptables restart
   ``

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no Centerity license costs or additional fees bundled in.

### Frequently Asked Questions
Where do I obtain my Centerity Licenses?

#### Contact Centerity Sales:
us-info@centerity.com
+1-339-225-7006

#### Who should I contact for support?
* For issues related to deploying the Centerity Blueprint on Lumen Cloud, licensing or accessing the deployed software, please visit the Centerity Support Website TBD.
* For issues related to cloud infrastructure (VMs, network, etc.), please open a ticket using the Lumen Cloud Support Process.
