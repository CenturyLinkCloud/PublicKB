{{{
"title": "Catalog",
"date": "12-28-2018",
"author": "Julio Castanar and Guillermo Sánchez",
"keywords": ["cam", "catalog", "catalog services", "catalog featured", "catalog plugin", "marketplace", "publish", "public", "private", "script box", "information box"],
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Catalog](#catalog)
* [Catalog Categories](#catalog-categories)
* [Publish and add content to the catalog](#publish-and-add-content-to-the-catalog)
* [Catalog elements usage](#catalog-elements-usage)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article is meant to assist Cloud Application Manager customers who wants to review and use the box catalog.  

The Cloud Application Manager catalog is a collection of boxes and services for **public use** by any Cloud Application Manager user of any organization.

### Audience

All Cloud Application Manager users

### Prerequisites

* Access to Cloud Application Manager [Applications site](https://cam.ctl.io/#/dashboard) (Application Lifecycle Management module) as an authorized user of an active Cloud Application Manager organization.

### Catalog

Catalog consists of public boxes and services grouped by categories.

A publisher creates a box and can make it public by requesting to publish it and by assigning it a category. Once reviewed and approved, the box will be included into the public catalog.

These boxes can be script boxes or information boxes. Catalog script boxes can be deployed by anyone who wants to provision an instance with the box provided functionality. Catalog information boxes provide a description of a service or component and display a link to access more information on how to use or subscribe for that service or component.

The publisher decides if the scripts in a catalog box are hidden or visible (open source). When the scripts are public, they are displayed in the box details and can be then edited through the instance lifecycle editor when the box has been deployed. Any open source catalog box can also be cloned and used as a baseline for our own box implementation.

The Catalog page displays all boxes added to the public catalog. These boxes are shown to all Cloud Application Manager users in all organizations.

### Catalog Categories

The Catalog page classifies all boxes by categories. You can see all catalog categories at a glance, with the initial boxes of each category, or you can see a single category. To show all boxes in one category select it in the left side menu or click on *select all* at the right side for every category line when the `All` categories option is selected.  

![Cloud Application Manager catalog menu](../../images/cloud-application-manager/getting-started-login-9.png)

The following sections explain some categories in Catalog. Due to the dynamic nature of the Catalog, actual available categories and boxes may vary:

#### Featured

This category shows relevant elements used in public catalog.

![Cloud Application Manager catalog featured](../../images/cloud-application-manager/catalog/cam-catalog-featured.png)

**Examples**:

SharePoint Farm, JBoss Sample Application, etc.

#### Managed Services Anywhere

This category groups boxes related to Managed Services, to enable it or perform services in server machines. Some of them are customized for a better performance in the provider site.

Of special interest is **CenturyLink Management Appliance** which is a public box and you can see its code. In a few steps you can deploy an appliance in a region

![Cloud Application Manager catalog Managed Services Anywhere](../../images/cloud-application-manager/catalog/cam-catalog-managed-services.png)

**Examples**:

CenturyLink Managed SQL Server, CenturyLink Managed IIS, CenturyLink Managed Apache HTTP Server, CenturyLink Managed Tomcat, CenturyLink Management Appliance, Managed Application Windows, etc.

#### Plugins

Mainly, in this category you will find information boxes for some applications or scripts that provide utilities and functions to your environment.

![Cloud Application Manager catalog Managed Services Anywhere](../../images/cloud-application-manager/catalog/cam-catalog-plugins.png)

**Examples**:

Jenkins CI plugin, Jenkins Kubernetes CI plugin, etc.

#### Services

Here you can find boxes explaining some available cloud services in Cloud Application Manager. External partners can use this category to offer their services through the Catalog as a marketplace.

![Cloud Application Manager Catalog Services](../../images/cloud-application-manager/catalog/cam-catalog-services.png)

**Examples**:

Amazon Web Services, Microsoft Azure, CenturyLink Simple Backup Service, etc.

#### Other

This category includes all the other boxes not included in a specific category.

![Cloud Application Manager catalog other](../../images/cloud-application-manager/catalog/cam-catalog-other.png)

**Examples**:

Oracle Database Service, Memcached Service, etc.

### Publish and add content to the catalog

A user can also [request to publish](../Tutorials/publish-script-box.md) one of his defined boxes to this public catalog, to make it available for all Cloud Application Manager users from all organizations, by sending a Publish box request from a box version.

This feature can be used as a **marketplace** by Cloud Application Manager customers willing to provide their applications and services through the Cloud Application Manager catalog to any other customer.

Published box in Catalog can be public (shows its code to the user, allows editing the code through the Lifecycle Editor when deployed and allows cloning of the box) or private (scripts code is hidden, cloning of the box is not allowed). A published box can have different versions.

### Catalog elements usage

A catalog element is a **Script Box**, so you can perform the same functions as described in [boxes](boxes.md).  
You can create an instance of this catalog box by deploying it. Besides that, you can clone it if it was published as open source.

![Cloud Application Manager catalog usage script](../../images/cloud-application-manager/catalog/cam-catalog-usage1.png)

Other elements in the Catalog are **information boxes**. They provide documentation only. Clicking on them show information regarding how to use them and a link to additional information or subscription details.

![Cloud Application Manager catalog usage info](../../images/cloud-application-manager/catalog/cam-catalog-usage2.png)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at \ProgramData\ElasticBox\Logs\elasticbox-agent.log
