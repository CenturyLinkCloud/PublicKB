{{{
  "title": "Getting Started with AppFog",
  "date": "04-10-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Audience

Application developers

### AppFog Overview

AppFog is a public Platform-as-a-Service (PaaS) that makes deploying scalable, robust, high performing [cloud-ready applications](http://12factor.net) fast and easy for developers. AppFog enables developers to focus on writing great applications without having to worry about managing the underlying infrastructure. The result is increased agility and productivity, more efficient use of resources, and a simplified deployment and management experience.

![Work on code, not infrastructure](../images/appfog-vs-traditional.png)

AppFog supports the followng common application runtimes: Java, Node.js, PHP, Python, Go, Ruby, and Static Websites. Integrating with services such as databases, messaging middleware, load balancing, monitoring and more are easily provisioned through the AppFog Marketplace.

### Enable AppFog in Control Portal

Go to https://control.ctl.io, login, and you should see “AppFog" listed in the drop down navigation bar:

![AppFog in Dropdown Navigation](../images/appfog-in-dropdown-nav.png)

You may also navigate to AppFog via the icon on the left-side vertical navigation bar:

![AppFog icon in Vertical Navigation](../images/appfog-icon-nav.png)

Navigate to AppFog using either navigation approach and now it is time to enable deployment to AppFog regions, US East and/or US West. Each region has its own "add region" button to enable it in your AppFog:

![AppFog Overview](../images/appfog-overview.png)

If the region has already been enabled then there the region will be a link to the region overview page and no "add region" button will be displayed on the region row.

### Where to Go From Here?

Now that you have AppFog enabled on your account you can manage membership to regions and spaces, login from terminal and deploy an application.

* [Manage AppFog Region and Space Membership](manage-appfog-membership.md)
* [Login to AppFog using Cloud Foundry CLI](login-using-cf-cli.md)
* [Deploy an Application to AppFog](deploy-an-application.md)
