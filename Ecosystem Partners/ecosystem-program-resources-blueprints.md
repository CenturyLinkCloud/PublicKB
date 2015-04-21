{{{
  "title": "Ecosystem Program Partner Resource Guide - Blueprints",
  "date": "3-16-2015",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": false
}}}


CenturyLink [Ecosystem Program Partner Members](../Ecosystem Partners/centurylink-cloud-ecosystem-program-guide.md) gain access to a bevy of [resources](../Ecosystem Partners/ecosystem-program-resources.md) that make integrations easy.

Integrating with the CenturyLink Cloud Blueprints orchestration engine enables customers to deploy your software on their existing servers or to create the workflow for a complex multi-server/multi-service solution suite.  This integration format provides a unified deployment experience for users and is the preferred integration method when available.

### Core Documentation

Reference the following key pages from the CenturyLink Cloud [Knowledge Base](http://www.centurylinkcloud.com/knowledge-base):

* [Blueprints Category](../../Blueprints/) in the Knowledge Base
* Best Practices in [Packages](../Blueprints/packages-best-practices.md) and [Blueprints](../Blueprints/blueprints-best-practices.md)
* [Package and Blueprint maximums](../Blueprints/blueprint-package-and-template-maximum-limits.md)
* [Naming conventions for Public Packages and Blueprints](../Blueprints/creating-public-blueprint-packages.md)
* [How to Build a Blueprint](../Blueprints/how-to-build-a-blueprint.md)


### Contributed Resources

* [Blueprint Package Manifest Builder Wizard](http://centurylinkcloud.github.io/Ecosystem/BlueprintManifestBuilder/) ([KB Instructions for use](../Blueprints/blueprint-package-manifest-builder-wizard.md))
* [CenturyLink Cloud Ecosystem Github Repo](https://github.com/CenturyLinkCloud/Ecosystem/tree/master/Blueprints) containing reference patterns, support tools, and the actual packages used in some of our public Blueprints
* [Blueprint Broker](https://github.com/CenturyLinkCloud/Ecosystem/blob/master/Blueprints/Blueprint%20Broker/README.md) is a cross-platform toolset that includes a discovery service, encrypted key-value store to maintain state, and a mailer tool enabling high-impact post-deployment communication


### Blueprint QA Process Requirements

Before a Blueprint can be publicly published it must pass a CenturyLink led QA process which includes testing for the following:

* Naming adheres to the [Naming conventions for Public Packages and Blueprints](../Blueprints/creating-public-blueprint-packages.md) style guide.
* Any new servers deployed as part of the Blueprint must be be fully patched before release.  Blueprint packages exist for Linux and Windows to support this.
* Allocates public IP address only if public access is required.  Default access mechanism is via private IP.
* QA analyst can deploy without errors
