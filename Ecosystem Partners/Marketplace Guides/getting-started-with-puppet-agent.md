{{{
  "title": "Getting Started with Puppet Agents - Blueprint",
  "date": "6-23-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the reader should feel comfortable deploying a Puppet Agent on CenturyLink Cloud.

### Partner Profile

<img src="/knowledge-base/images/puppet/puppet_labs_logo.jpg" style="border:0;float:right;max-width: 100px;">

Puppet is a configuration management solution that allows you to define the state of your IT infrastructure, and then automatically enforces the desired state.

https://puppetlabs.com/puppet/puppet-open-source


### Description

Puppet agent integration is now supported on the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this solution.

Open Source Puppet is a declarative, model-based configuration management solution that lets you define the state of your IT infrastructure, using the
Puppet language. Open Source Puppet then automatically enforces the correct configuration to ensure the right services are up and running, on the
right platforms.

You can run Puppet on all major Linux and Unix platforms, Mac OS X, and Windows. It is available to download and use under the Apache 2.0 license.



### Audience

CenturyLink Cloud Users

### Deploying via Blueprint Packages

Puppet agents are often best deployed as part of a new server build, especially when designed a standardized infrastructure service catalog.
CenturyLink has made two packages available for inclusion in your own Blueprints:

* [Install Puppet Agent Bridge on Linux](https://control.ctl.io/Blueprints/Packages/Details?uuid=775bb824-579d-4c8d-8955-c69a94a2ba1a&classification=Script&type=AccountLibrary)
* [Install Puppet Agent Bridge on Windows](https://control.ctl.io/Blueprints/Packages/Details?uuid=735bb844-579d-4c8d-8255-c69a94a2ba1a&classification=Script&type=AccountLibrary)

Both of these take a single parameter as design-time that defines the FQDN for your prefered Puppet Master.  This setting is retained and need not
be resupplied with each deployment.


### Deploying on an Existing Server using Blueprints

Add a Puppet Agent to an existing Linux server using the preconfigured Blueprint.


#### Steps


1. **Locate the Blueprint in the Blueprint Library**

  <img src="/knowledge-base/images/puppet/agent_blueprint_tiles.png" style="border:0;max-width:250px">

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for “Puppet Agent” in the keyword search on the right side of the page.

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  <img src="/knowledge-base/images/puppet/deploy_agent_parameters.png" style="max-width:450px;">

  * **Puppet Master** - Enter the FQDN of an existing Puppet Master server
  * **Execute on Server ** - Select the existing server on which to execute this Blueprint


4. **Review and Confirm the Blueprint**

5. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within 15 to 20 minutes.

### About Community Releases on CenturyLink Cloud

CenturyLink Cloud publishes a variety of packaged and certified community releases of OSS or otherwise generally available software solutions.
These certifications are limited to successful deployment of assets on cloud servers and do not extend onto ongoing software configuration, garauntees,
or support.

Have a suggestion for other software to include within the CenturyLink Cloud Blueprints Library?  Email ecosystem@CenturyLinkCloud.com.


### Frequently Asked Questions

**Where do I obtain my license?**

This is a release of the Puppet Community Edition.  For Enterprise deployments or commercial support engage Puppet Labs directly.

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
* For all Puppet related issues direct questions towards the Puppet user community.
