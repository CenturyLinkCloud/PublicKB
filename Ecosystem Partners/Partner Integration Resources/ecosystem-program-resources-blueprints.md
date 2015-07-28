{{{
  "title": "Ecosystem Program Partner Resource Guide - Blueprints",
  "date": "6-17-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

CenturyLink [Ecosystem Program Partner Members](centurylink-cloud-ecosystem-program-guide.md) gain access to a bevy of [resources](ecosystem-program-resources.md) that make integrations easy.

Integrating with the CenturyLink Cloud Blueprints orchestration engine enables customers to deploy your software on their existing servers or to create the workflow for a complex multi-server/multi-service solution suite.  This integration format provides a unified deployment experience for users and is the preferred integration method when available.

### Core Documentation

Reference the following key pages from the CenturyLink Cloud [Knowledge Base](http://www.ctl.io/knowledge-base):

* [Blueprints Category](../../Blueprints/) in the Knowledge Base
* Best Practices in [Packages](../../Blueprints/packages-best-practices.md) and [Blueprints](../../Blueprints/blueprints-best-practices.md)
* [Package and Blueprint maximums](../../Blueprints/blueprint-package-and-template-maximum-limits.md)
* [Naming conventions for Public Packages and Blueprints](../../Blueprints/creating-public-blueprint-packages.md)
* [How to Build a Blueprint](../../Blueprints/how-to-build-a-blueprint.md)


### Contributed Resources

* [bpformation](https://github.com/CenturyLinkCloud/bpformation) - CLI and Python SDK used for managing Blueprints and Packages.  Easily and repeatably import, export, and update using a json object file as the authoritative representation of your Blueprint in lieu of using the web-based control portal
* [Blueprint Package Manifest Builder Wizard](http://centurylinkcloud.github.io/blueprint-package-manifest-builder/) ([KB Instructions for use](../../Blueprints/blueprint-package-manifest-builder-wizard.md))
* [CenturyLink Cloud Ecosystem Github Repo](https://github.com/CenturyLinkCloud/Ecosystem/tree/master/Blueprints) containing reference patterns, support tools, and the actual packages used in some of our public Blueprints
* [Blueprint Broker](https://github.com/CenturyLinkCloud/bpbroker) is a cross-platform toolset that includes a discovery service, encrypted key-value store to maintain state, and a mailer tool enabling high-impact post-deployment communication


### Blueprint QA Process Requirements

Before a Blueprint can be publicly published it must pass a CenturyLink led QA process which reviews functionality, compliance, and documentation:

##### Functionality

* QA analyst can deploy without errors.
* Deployment user experience in line with customer expectations


##### Compliance

* Any new servers deployed as part of the Blueprint must be be fully patched before release.  Blueprint packages exist for Linux and Windows to support this.
* Allocates public IP address only if public access is required.  Default access mechanism is via private IP (using client/remote VPN or other direct connect method).
* Some integrations may require reviews from Security, Commercial Compliance, or other subject matter experts


##### Documentation

* Naming adheres to the [Naming conventions for Public Packages and Blueprints](../../Blueprints/creating-public-blueprint-packages.md) style guide.
* [Knowedgebase](https://www.ctl.io/knowledge-base/) article content provides the information necessary to successfully deploy and get started with the solution.  Links to more in-depth general documentation or CenturyLink Cloud specific language is encouraged.
* Documentation supports deployment experience


### Ongoing Blueprints QA

CenturyLink customers trust that all services available as part of the [Marketplace Provider Program](https://www.ctl.io/marketplace/program/)
will deploy and function as expected.  To that end CenturyLink maintains quality throughout the Marketplace by executring an ongoing testing service
that validates successful deployment and operation of all public Blueprints on a regular basis.
