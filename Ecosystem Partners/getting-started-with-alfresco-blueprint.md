{{{
  "title": "Getting Started with Alfresco Community - Blueprint",
  "date": "05-04-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Description

<img src="//d33np9n32j53g7.cloudfront.net/assets/stacks/alfresco/img/alfresco-stack-110x117-d14a68c35022e03133afb4e2976c4d99.png" style="border:0;float:right;max-width:250px">

After reading this article, the reader should feel comfortable deploying the Alfresco Community stack by Bitnami.

<a href="https://bitnami.com/" rel="no-follow">Bitnami</a> has integrated their <a href="https://bitnami.com/stack/alfresco" rel="no-follow">Alfresco Community stack</a> with the CenturyLink Cloud platform with a single-click deploy solution.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Alfresco Community solution.

Alfresco was founded in 2005 by John Newton who, many years earlier, cofounded Documentum, one of the pioneers of document management. Alfresco Community is an enterprise-ready, Java-based platform used for document management, records management, image management and more. Features include versioning, Lucene-powered search, federated servers, clustering, roles-based permissions and more. You'll be in good company with Alfresco; other users include NASA, KLM, Merck and Ricoh.


### Audience

CenturyLink Cloud Users


### Deploying Alfresco Community on a New Server

Alfresco Community is available as a Blueprint for deployment on a **new server**.

#### Steps


1. **Locate the Blueprint in the Blueprint Library**

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for **Alfresco Community on linux_TITLE** in the keyword search on the right side of the page.

  <!-- TODO - fake tile screenshot -->

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  Set the following parameters in addition to those associated with your server itself (password, network, group, etc.:

  <!-- TODO - replace with legacy blueprint UI html instead -->

  <div style="margin:1em;color: #838383; background: #f2f2f2; margin:1em; padding: 1em; border:2px solid #e5e5e5;width:500px;">
      <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Service Password</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="***" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Provide service password 6 chars or more</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Tomcat server shutdown port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="8005" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Tomcat Shutdown Port</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Apache server SSL port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="443" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;"></div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Libreoffice port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="8100" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">LibreOffice Server Port</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Username</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Service Username</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">JDBC username</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="user" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Username</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Apache server port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="80" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;"></div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">User's name</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Users Name</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">JDBC database</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="alfresco" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Database name</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Alfresco RMI port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="50500" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Port</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Alfresco_ftp_port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="21" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Port</div>
    </div>
    <br style="clear:both;">
  </div>

  </div>

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within five minutes.

7. **Deployment Complete**

  Once the Blueprint has finished executing on your server you may access Alfresco Community by navigating to your server via http.


8. **Enable public access** (optional)

  Servers are built using private IPs only with access with client or IPSEC VPN.  For inbound access from the Internet add a public IP to your master server.

  <a href="../../network/how-to-add-public-ip-to-virtual-machine/">
    <img style="border:0;width:50px;vertical-align:middle;" src="../images/shared_assets/fw_icon.png">
    Adding a public IP to your virtual machine
  </a>



### Deploying Alfresco Community on an existing server (alternate option)

Alfresco Community is available as a Blueprint Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on the same machines

#### Steps


1. **Deploy or Identify an Existing Server**

  Identify the server targeted for Alfresco Community installation.  Operating sustem must be linux.

  See the [Creating a new enterprise cloud server](../../servers/creating-a-new-enterprise-cloud-server/) KB for more information on completing this step.


2. ** Select to Execute the Package on a Server Group**

  Packages can be executed on one more more servers in a group.  Search for the public script package named **Install Alfresco Community on linux_TITLE**.

  See the [using group tasks to install scripts on groups](../../servers/using-group-tasks-to-install-software-and-run-scripts-on-groups/) KB for more information on how to complete the next few steps.


3. **Set Parameters**

  Set the following parameters:

  <div style="margin:1em;color: #838383; background: #f2f2f2; margin:1em; padding: 1em; border:2px solid #e5e5e5;width:500px;">
      <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Service Password</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="***" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Provide service password 6 chars or more</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Tomcat server shutdown port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="8005" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Tomcat Shutdown Port</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Apache server SSL port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="443" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;"></div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Libreoffice port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="8100" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">LibreOffice Server Port</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Username</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Service Username</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">JDBC username</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="user" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Username</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Apache server port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="80" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;"></div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">User's name</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Users Name</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">JDBC database</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="alfresco" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Database name</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Alfresco RMI port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="50500" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Port</div>
    </div>
    <br style="clear:both;">
  </div>

  <div style="padding: 1em;">
    <label style="font-family: 'Open Sans', Helvetica, Arial, Sans-Serif; font-size:14px; margin: 7px 20px 7px 0; padding-top:7px;color:#333333; text-decoration:underline; text-transform:lowercase; float:left; width:160px;text-align:right;">Alfresco_ftp_port</label>
    <div style="float:left;margin-left:10px;">
      <input style="padding:4px 6px;width:250px;height:34px;" type="text" value="21" disabled="disabled">
      <div style="margin-top:10px; color:#999; font-size:13px; line-height:15px;">Port</div>
    </div>
    <br style="clear:both;">
  </div>

  </div>

4. **Deploy the Blueprint**

  Once verified, click on the `execute package` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within five minutes.

5. **Deployment Complete**

  Once the Blueprint has finished executing on your server you may access Alfresco Community by navigating to your server via http.


6. **Enable public access** (optional)

  Servers are built using private IPs only with access with client or IPSEC VPN.  For inbound access from the Internet add a public IP to your master server.

  <a href="../../network/how-to-add-public-ip-to-virtual-machine/">
    <img style="border:0;width:50px;vertical-align:middle;" src="../images/shared_assets/fw_icon.png">
    Adding a public IP to your virtual machine
  </a>


### Pricing

The costs listed above in the above steps are for the infrastructure only.


### About Bitnami

CenturyLink Cloud works with [Bitnami](http://www.bitnami.com) to provide open source software integrations to its customers.  Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.


### Frequently Asked Questions

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../Support/how-do-i-report-a-support-issue.md).
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Bitnami Support website](http://www.bitnami.com/support)

**How do I access Alfresco Community for the first time?**

Nearly all Bitnami stacks can be accessed and configured by navigating to your server with a web browser.


