{{{ 
  "title": "Getting Started With Waratek Locker – Runtime Application Self Protection", 
  "date": "10-21-2015", 
  "author": "David Egan", 
  "attachments": [], 
  "contentIsHTML": false
}}}

![Waratek Logo](http://cdn.aws.waratek.com/wp-content/themes/waratek/images/logo.png)

### Partner Profile

Waratek, a pioneer in Runtime Application Self Protection, secures applications from logic, network and vulnerability exploits without code changes, agents or hardware devices, placing security within your own control. This enables applications to be run on a public cloud while retaining a level of protection normally only available in the enterprise data center.

In 2015 the RSA Conference’s Innovation Sandbox awarded Waratek the title of Most Innovative Company saying it was *an inventive solution to a ‘massive problem’.*

### Contact Waratek

**Waratek Sales and Support:**

* [Email support](mailto:support@waratek.com)

* [Support Site](https://support.waratek.com/). 

* [Sales and Marketing](mailto:sales@waratek.com)

### Description

Waratek has made their award winning Cloud Based Application Security solution, Locker, available on the CenturyLink Cloud platform, publishing their virtual appliance as a CenturyLink Cloud Partner Template. This KB article should help the reader understand why Runtime Application Self Protection has been described as the "Must Have Emerging Technology’ and why use of it can help you confidently move more of your applications to a cloud based environment.

Waratek Locker provides a secure container for your Java applications and enables a legacy Java application to be run in an up-to-date container to gain modern security fixes. Due to its unique understanding of application logic, Locker is able to secure your application against the OWASP and SANS leading attack vectors, such as SQL injection, with zero false positives.

For more information, please visit [http://www.waratek.com](http://www.waratek.com/). 

### Solution Overview

Waratek Locker is a secure container for Java applications which provides [run-time application self-protection](http://www.waratek.com/runtime-application-self-protection/) ([RASP](http://www.waratek.com/runtime-application-self-protection/)) against [Advanced Persistent Threats](http://www.waratek.com/solutions/threat-forensics/) and [Zero Day attacks](http://www.waratek.com/solutions/zero-day-malware/). This enables applications to be run on a public cloud while retaining a level of protection normally only available in the enterprise data centre.

Locker uses the same technology as Waratek’s flagship [AppSecurity for Java](http://www.waratek.com/products/appsecurity-for-java/) product to provide security monitoring, policy enforcement and attack blocking from within the Java Virtual Machine (JVM). This enables Locker to protect cloud applications against exploits that target vulnerabilities in third party libraries or legacy Java, as well as malware and Advanced Persistent Threats attempting SQL injection attacks.

Vulnerability exploitations protected against include the following:

1. Attacks leveraging unsecured code (including 3rd party libraries)

2. Insertion of malicious code into the runtime environment

3. Unauthorized attempts to extract information from database backends

Applications are deployed in a secure Locker container and are governed by a single rules file. Each rule added to this file will control an aspect of an applications behavior. When a rule detects an attack, one of a series of mitigating actions will occur. These can range from logging and monitoring, to blocking the event. Locker has a default set of rules which block malicious attacks such as File access, Network access and SQL Injection. It is then easy for the application provider to add and customize additional rules giving fine-grained security control.

For further information about Locker please visit: [www.waratek.com/locker](http://www.waratek.com/locker)

### Technology Profile

Waratek Locker is a secure container, which includes an Oracle certified Java virtual machine (JVM) running a standard Apache Tomcat application server. When a Java application is deployed Locker's security technology monitors its runtime environment. When it detects real-time attacks, it is capable of controlling how the application executes and thus secures it from Advanced Persistent Threats (Advanced Persistent Threats). Furthermore, this award-winning and patented technology can detect and prevent malicious attacks without any code changes to an application. 

This CenturyLink Blueprint provides a simple install solution of Waratek Locker on CentOS 6 and Apache Tomcat 7.

It is also possible to use other application servers such as JBoss or Weblogic. (what else should be listed here?) Please contact Waratek to find out more. 

### Audience

CenturyLink Cloud Users desiring a secure Java environment.

### Impact

After reading this article, the user should be able to install Locker on a CenturyLink Cloud server.

### Prerequisites

* Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisites

* None

### Deploying Locker on a New Server

Waratek Locker is available as a Blueprint for deployment on a new server.

**Steps to deploy to New Server Blueprint**

1. Locate the "Install Waratek Locker" Blueprint

2. Click on the blueprint. Select "Deploy Blueprint" on the resulting screen

3. Configure the Blueprint. Complete the information below:

    1. **Enter password.**

    2. **Choose your group.**

    3. **Choose your network.**

    4. **Choose Primary and Secondary DNS.**

    5. **Choose the Server Type.**

    6. **Choose Service Level.**

    7. **Enter Server Name.**

4. Review and Confirm the Blueprint

    8. **Click "next: step 2"**

    9. **Verify your configuration details.**

5. Deploy the Blueprint

    1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.

    2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

* Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.

* Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Steps to deploy to an existing server

1. Deploy or Identify an existing server

2. Locate the "Install Waratek Locker" blueprint in the Blueprint Library

3. Select "Deploy Blueprint"

4. Select the server to be deployed

5. Select "next: step 2"

6. Select "Deploy Blueprint"

7. Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.

8. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Pricing
For pricing and licensing of Locker, please contact [our sales team](mailto:sales@waratek.com).

### Frequently Asked Questions

For more information about Locker, click on the following links: 

Locker User Guide [http://www.waratek.com/resources/guides/locker/](http://www.waratek.com/resources/guides/locker/) 

Locker FAQs [http://www.waratek.com/resources/guides/locker/frequently-asked-questions/](http://www.waratek.com/resources/guides/locker/frequently-asked-questions/) 

### Purchasing Waratek Locker License

* The license provided is a trial to get a full license contact [our sales team](mailto:sales@waratek.com).

### Who should I contact for support?

* For issues related to deploying, configuring Waratek Locker please visit [Waratek Support](https://support.waratek.com/).

* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
