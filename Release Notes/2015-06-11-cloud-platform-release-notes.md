{{{
"title": "Cloud Platform - Release Notes: June 11, 2015",
"date": "6-11-2015",
"author": "Mary Cadera",
"attachments": [],
"contentIsHTML": false
}}}

###New Features (4)###

* __Managed OS.__ Clients can leverage our deep expertise in infrastructure and application management and offload critical IT functions for important applications. Managed servers are regularly patched and monitored, so the risks from viruses and other threats are reduced. __Managed OS are now available in three new locations: Singapore (SG1), Toronto (CA3), and Chicago (IL1).__

  Managed OS continue to be available in Virginia (VA1), Santa Clara (UC1) and London (GB3).

* __Patching as a Service.__ Now available for free to all CenturyLink customers using Windows 2012. Our customers can patch their Windows 2012 servers through blueprints or 'execute package' on demand via the Control Portal or API. The service provides the capability to patch servers, know when the patching started and finished as well as list of all patches applied. [You can learn more about Patching as a Service in our KB.](../Servers/patching-as-a-service.md)

* __Orchestrate.__ Our multi-modal managed datatabse service, [Orchestrate](https://www.ctl.io/blog/post/centurylink-acquires-orchestrate/), gives developers a single API for key-value, geospatial, graph, and timeseries data. And it just keeps getting better and better! Check out the new functionality delivered this month, focused on usability and exposing API features:

  * New dashboard query form. Explore the full glory of Orchestrate's API with the newly updated dashboard UI.
  * New bulk write API.  Write up to 250 documents, events, and graph relations in one request.

  Read more about [how you can get started with Orchestrate](//www.orchestrate.io/docs).

* __Network APIs.__ Networking functions are now available via self-service API. Specific capabilities include:
  * Create an intra-DC firewall
  * Get an intra-DC firewall policy
  * Get an intra-DC firewall policy list
  * Update an intra-DC firewall policy

  [**Review the documentation for APIs here.**](//www.ctl.io/api-docs/v2/#firewall-policies)


###Minor Enhancements (3)###

* __Database as a Service.__ Certified Managed MySQL now works with RHEL6 and 7. You can [read more about Managed MySQL in our KB](../Managed Services/getting-started-with-managed-mysql.md).

* __UI improvements.__ The Control Portal continues to get easier on the eye. We've made some light improvements to the UI that we think you'll appreciate.

* __CenturyLink Cloud Status.__ [status.ctl.io](//status.ctl.io/) provides real-time updates on the status of CenturyLink Cloud services, and upcoming maintenance notifications. Notifications surrounding Compute, Network, and Storage are now based on what servers an account has in a specific data center, allowing our customers to get the information they need - and only the information that they need.

  Our KB has more [information about the CenturyLink Cloud Status service.](../General/centurylink-cloud-status-faq.md)


###Online Tools (1)###

* __Blueprint Formation.__ Take our new blueprint formation tool for a spin. [This GitHub repository](//github.com/CenturyLinkCloud/bpformation) contains a command line interface to interact with the CenturyLink Cloud Blueprints packaging and workflow services.

###Notifications (2)###

* __New Domains.__ Effective March 5, the default CenturyLink Cloud domain was updated to control.ctl.io. The URL for SAML users has also been updated to https://[`account-alias`].cloudportal.io (where `account-alias` is your four-letter account identifier). __Please update any code that leverages the CenturyLink Cloud API to ensure that it uses the supported endpoint.__ The legacy domains will continue to operate until July 15.

* __AppFog Limited Beta.__ Beta access for AppFog continues to be available. Based on Cloud Foundry v2, this new platform for applications makes it easier for developers to build and scale cloud-native applications. To sign-up, visit [the AppFog product page](//www.ctl.io/appfog/).


###Ecosystem: New Blueprints (5)###

* [__Pivotal HD + HAWQ.__](../Ecosystem Partners/Marketplace Guides/getting-started-with-pivotal-hd-hawq.md)
This latest entry from Pivotal in our Cloud Marketplace provides the best of both worlds in the data management space - the scalability and flexibility of Hadoop with the structured query support of HAWQ.  This Open Data Platform (ODP) compliant solution contributes to a more standards-based implementation of the Hadoop File System (HDFS), which will over time help accelerate enterprise productivity around this cost-saving, scale-ready technology.

* [__Vormetric.__](../Ecosystem Partners/Marketplace Guides/getting-started-with-vormetric-encryption-agent-deployment-blueprints.md)
This security solution complements our previous integration with Vormetric Security Manager, allowing the deployment of encryption agents to various server endpoints on the CenturyLink Cloud.  With Vormetric, a single infrastructure and management environment protects data wherever it resides with file, volume and cloud storage encryption, tokenization with dynamic data masking, field-level application encryption, sophisticated access control policies, third party and integrated encryption key management.

* [__SoftNAS.__](../Ecosystem Partners/Marketplace Guides/getting-started-with-softnas-cloud-file-gateway-partner-template.md)
SoftNAS is one of the most popular storage technologies in the cloud.  This Partner Template, available via Service Task, provides CenturyLink customers with an enterprise-grade, software-defined, NAS storage gateway to safely and reliably operate their business-critical IT systems and storage folders inside CenturyLink Cloud.

* [__Wordpress.__](../Ecosystem Partners/Marketplace Guides/getting-started-with-wordPress-blueprint.md)
Web publishing is a common workload that can be achieved through a variety of cloud models.  One of the most popular tools for these weblog and content management use cases is Wordpress, which is open source and now easier than ever to deploy in CenturyLink Cloud.  Your content teams can be up and running on Wordpress 4.2 in minutes using the Blueprint automation that can either create a new server or install the software onto an existing machine.

* [__Mojang Minecraft PE.__](../Ecosystem Partners/Marketplace Guides/getting-started-with-minecraft-pe-server-blueprint.md)
Even though our global cloud platform is able to scale to various enterprise workloads, it doesn’t mean we can’t use it to have a little bit of fun.  This blueprint rolls out a Mojang Minecraft Pocket Edition (PE) server that supports iOS and Android gameplay on various personal computing devices.  This solution is a great way to build a safe, customized gaming environment for the family while teaching young engineers how the cloud actually works.


###Open Source Contributions (2)###

* [__Lorry.io.__](//imagelayers.io/) Lorry.io is a CenturyLink Labs open-source project for creating, validating and sharing Docker Compose YAML files. Docker-compose.yml files are used to define and run complex applications with Docker and Docker Compose. Lorry.io can also import Panamax templates and convert them into docker-compose.yml files. For more information, [read this blog post](//www.centurylinklabs.com/lorry-io-pathway-to-docker-composable-apps/) and [browse the wiki here](//github.com/CenturyLinkLabs/lorry).

* **Updates:**

  * [ImageLayers.io](//www.imagelayers.io/) v1.0.2: Support for Mobile views, social sharing buttons and ability to select specific tag for badging images. Learn more on the [ImageLayers wiki](//github.com/CenturyLinkLabs/imagelayers-graph).
  * [Panamax](//www.panamax.io/) (v0.6.3) now supports cAdvisor 0.13.0 and CoreOS 647.2.0.

###Bug Fixes (4)###

* __Roles: Server Scheduler.__ A user with this role can schedule a power op, but they cannot perform a power op from server details. Now, when a user confirms the action, the user is redirected to the queue request and the request is processed.

* __Intra DC Firewall Additions.__ This experimental API has been updated with improved error messaging. When a user attempts to use this process to create a cross DC firewall, a 400 error is provided. The page loads faster too!

* __Billing for Monthly Recurring Charges.__ We have made updates to ensure that previously omitted additional charges for services such as Dedicated Load Balancers and Cross Connects are included on monthly invoices.

* __OVF Import Timeout.__ Importing cross DC OVF files can sometimes take more than 60 minutes. To ease any pain around this, timeouts have been increased from 60 minutes to 120 minutes.
