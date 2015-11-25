{{{
  "title": "Installing TimeKeeper Time Synchronization Software",
  "date": "November 6, 2015",
  "author": "FSMLabs",
  "attachments": [],
  "contentIsHTML": false
}}}

![FSMLabs Logo](http://www.fsmlabs.com/img/logo-blue-nav@2x.png)

### Technology Profile

This blueprint will install TimeKeeper software that will allow you to synchronize the time on your systems and monitor the time accuracy.

### Description

For more information, please visit http://www.fsmlabs.com/

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should understand how to install TimeKeeper software

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- TimeKeeper license file available by emailing support@fsmlabs.com

### Postrequisite
 After the installation users should take the following steps
  1. Contact support@fsmlabs.com in order to obtain a TimeKeeper license
  2. Edit /etc/timekeeper.conf or use the web GUI to configure TimeKeeper time sources

### Deploy TimeKeeper to an existing server These are the instructions to be executed for existing server installation.

TimeKeeper is available as a Software Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on servers.

#### Steps
1. **Deploy or Identify an Existing Server**
Identify the server targeted for TimeKeeper installation.  The Operating system must be supported by the Script Package.  The server must be a server within your CenturyLink Cloud account.
2. **Select 'Execute the Package on a Server Group'**
  1. Packages can be executed on one more more servers in a Group.  Search for the public script package named **TimeKeeper**.
  2. See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

2. **Deploy the Script Package**
Once verified, click on the `execute package` button. This will kick off the deployment process and load a page where you can track the progress. Deployment will typically complete within a few minutes.

3. **Monitor the Activity Queue**
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink
Cloud infrastructure only.  Additional licensing is required from FSMLabs.

### About FSMLabs
CenturyLink Cloud works with [FSMLabs](http://www.fsmlabs.c) to provide FSMLabs

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the TimeKeeper Blueprint on CenturyLink
Cloud, Licensing or Accessing the deployed software, please visit the [FSMLabs http://www.fsmlabs.com] and email support@fsmlabs.com
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
