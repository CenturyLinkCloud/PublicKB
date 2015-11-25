
{{{
  "title": " Getting Started with Symas OpenLDAP",
  "date": "11-24-2015",
  "author": "Andrew Brunette",
  "attachments": [],
  "contentIsHTML": false
}}}

![Symas logo](http://symas.com/wp-content/uploads/2013/06/logo1.png)

### Technology Profile

With Symas you can support hundreds of millions of records in one instance, provide low latencies to your users and applications, save on software costs with open source technology, and receive stellar support from recognized industry experts. You will reduce your administrative workload with the most stable self-tuning directory engine, and meet the most stringent compliance and security requirements with our mainframe-class ANSI-standard Role Based Access Control middleware and SDK. Join the growing number of Fortune 100 organizations who run their mission critical directory services on Symas technology.

### Description

This blueprint installs a copy of Symas OpenLDAP Silver on the designated system. Symas OpenLDAP Silver is an LDAP v3 server based on the popular OpenLDAP software, which is noted for its performance, flexibility, and stability. The Silver version features the Lightning Memory-mapped Database but is otherwise limited in that it lacks the ability to act as a replication provider and does not have the ability to communicate with or authenticate to Active Directory or other directory servers. It is therefore best suited for evaluations, proofs of concept, and directories that are not mission-critical. For enterprise-grade directory servers, please consider one of our other Symas OpenLDAP offerings.

For more information, please visit www.symas.com.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be able to install and configure the Symas OpenLDAP software.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Creation of a linux server to install OpenLDAP Silver onto

### Postrequisite
* none

### Deploying the Install Symas OpenLDAP Silver Blueprint

#### Steps to Deploy Blueprint
1. **Locate the Install Symas OpenLDAP SilverBlueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “OpenLdap in the keyword search on the right side of the page.
  3. Locate the 'Install Symas OpenLDAP Silver' Blueprint

2. **Choose and Deploy the Blueprint.**
  1. Click the "Install Symas OpenLDAP Silver" Blueprint.
  2. Click the Deploy button.

3. **Customize the Blueprint**
  1. **<Select server**
    1. Select a server from the dropdown to install onto

4. **Review and Confirm the Blueprint**
  1. Click “next: step 2”
  2. Verify your configuration details.
  3. Click "Deploy Bluprint"

5. **Deploy the Blueprint**
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.


### Access your Timekeeper server
After your Blueprint deploys successfully, if you have already do so, contact FSMLabs for licensing of your software.  The licensing will come with access and usage documentation


### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  The FSMLabs license costs are not bundled in.

### About FSM Labs
CenturyLink Cloud works with [FSM Labs](www.fsmlabs.com) to provide the TimeKeeper software.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the <Partner Name> Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [FSM Labs Support website](mailto: support@fsmlabs.com)
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
