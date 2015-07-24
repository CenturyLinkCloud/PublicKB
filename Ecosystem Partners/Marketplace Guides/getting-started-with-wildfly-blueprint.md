{{{
  "title": "Getting Started with WildFly - Blueprint",
  "date": "05-06-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Description

<img alt="WildFly Logo" src="/knowledge-base/images/bitnami_logos/wildfly-stack-110x117-e2357a2e61beca79ff271fa70ba61797.png" style="border:0;float:right;max-width:250px">
   
After reading this article, the reader should feel comfortable deploying the WildFly stack by Bitnami.

<a href="https://bitnami.com/" rel="no-follow">Bitnami</a> has integrated their <a href="https://bitnami.com/stack/wildfly" rel="no-follow">WildFly stack</a> with the CenturyLink Cloud platform with a single-click deploy solution.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this WildFly solution.

Welcome to the next-generation JBoss AS server, WildFly. Written in Java, WildFly is free and open source application server. Don't let it's agile and lightweight feel fool you: WildFly is a powerful beast that can run extremely fast with a full J2EE stack including Java EE7. This new Java release provides rich enterprise capabilities in frameworks that reduce technical burden and eliminate boiler plate. WildFly also supports the latest standards for REST based data access, including JAX-RS 2, and JSON-P. The Bitnami WildFly stack includes ready-to-run versions of WildFly, Apache, MySQL, and Java, and required dependencies.


### Audience

CenturyLink Cloud Users


### Deploying WildFly on a New Server

WildFly is available as a Blueprint for deployment on a **new server**.

#### Steps


1. **Locate the Blueprint in the Blueprint Library**

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for **WildFly on Linux** in the keyword search on the right side of the page.

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  Set the following parameters in addition to those associated with your server itself (password, network, group, etc.):

  * **Service Password** -  Provide service password 6 chars or more 
  * **Jboss server AJP port** -  AJP connector port default 8009
  * **Jboss server HTTP port** -  WildFly HTTP Connector Port default 8080
  * **Apache server SSL port** - default 443
  * **Jboss server management native port** -  WildFly Management Command Line Console port default 9999
  * **Jboss server management http port** -  WildFly Management HTTP port default 9990
  * **Apache server port** - default 80
  * **Jboss server directory** -  Root Directory directory (must already exist) default /usr/local
  * **JBoss server HTTPS port** -  HTTPS connector port default 8443
  * **Jboss server management https port** -  WildFly Management HTTPS port default 9443

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within five minutes.

7. **Deployment Complete**

  Once the Blueprint has finished executing on your server you may access WildFly by navigating to your server via http.

8. **Enable public access** (optional)

  Servers are built using private IPs only with access with client or IPSEC VPN.  For inbound access from the Internet add a public IP to your master server.

  <a href="../../Network/how-to-add-public-ip-to-virtual-machine.md">
    <img style="border:0;width:50px;vertical-align:middle;" src="../../images/shared_assets/fw_icon.png">
    Adding a public IP to your virtual machine
  </a>



### Deploying WildFly on an existing server (alternate option)

WildFly is available as a Blueprint Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on the same machines

#### Steps


1. **Deploy or Identify an Existing Server**

  Identify the server targeted for WildFly installation.  Operating sustem must be linux.

  See the [Creating a new enterprise cloud server](../../Servers/creating-a-new-enterprise-cloud-server.md) KB for more information on completing this step.

2. **Select to Execute the Package on a Server Group**

  Packages can be executed on one more more servers in a group.  Search for the public script package named **Install WildFly on Linux**.

  See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

3. **Set Parameters**

  Set the following parameters:

  * **Service Password** -  Provide service password 6 chars or more 
  * **Jboss server AJP port** -  AJP connector port default 8009
  * **Jboss server HTTP port** -  WildFly HTTP Connector Port default 8080
  * **Apache server SSL port** - default 443
  * **Jboss server management native port** -  WildFly Management Command Line Console port default 9999
  * **Jboss server management http port** -  WildFly Management HTTP port default 9990
  * **Apache server port** - default 80
  * **Jboss server directory** -  Root Directory directory (must already exist) default /usr/local
  * **JBoss server HTTPS port** -  HTTPS connector port default 8443
  * **Jboss server management https port** -  WildFly Management HTTPS port default 9443

4. **Deploy the Blueprint**

  Once verified, click on the `execute package` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within five minutes.

5. **Deployment Complete**

  Once the Blueprint has finished executing on your server you may access WildFly by navigating to your server via http.

6. **Enable public access** (optional)

  Servers are built using private IPs only with access with client or IPSEC VPN.  For inbound access from the Internet add a public IP to your master server.

  <a href="../../Network/how-to-add-public-ip-to-virtual-machine.md">
    <img style="border:0;width:50px;vertical-align:middle;" src="../../images/shared_assets/fw_icon.png">
    Adding a public IP to your virtual machine
  </a>


### Pricing

The costs listed above in the above steps are for the infrastructure only.


### About Bitnami

CenturyLink Cloud works with [Bitnami](http://www.bitnami.com) to provide open source software integrations to its customers.  Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.


### Frequently Asked Questions

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Bitnami Support website](http://www.bitnami.com/support)

**How do I access WildFly for the first time?**

Nearly all Bitnami stacks can be accessed and configured by navigating to your server with a web browser.


