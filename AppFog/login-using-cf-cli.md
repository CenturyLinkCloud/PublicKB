{{{
  "title": "Login to AppFog using the Cloud Foundry CLI",
  "date": "04-10-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### IMPORTANT NOTE

AppFog v2, the upcoming CenturyLink Cloud integrated public Platform-as-a-Service (PaaS), is not available to all customers at this time. We are current in a Limited Beta program with specific customers. AppFog v2 will be available in Open Beta later in 2015.

The current AppFog service at [http://www.appfog.com/](http://www.appfog.com/) is still available and will continue to be in service even after AppFog v2 is made generally available. Please feel free to sign up for the current AppFog service [here](https://console.appfog.com/signup).

### Audience

Currently, this article is to support customers in the Limited Beta program.

### Overview

In this article we will install the [Cloud Foundry Command Line Interface (CLI)](https://github.com/cloudfoundry/cli/) so that we can login to AppFog from the command line. Currently, AppFog only supports deployment of applications and provisioning services via the command line. This article will focus on authenticating to AppFog using your CenturyLink Control Portal credentials. Other articles will go into detail on how to use other Cloud Foundry CLI commands to interact with AppFog capabilities.

### Install Cloud Foundry CLI

Download the appropriate binary distribution of the Cloud Foundry CLI from [here](https://github.com/cloudfoundry/cli/blob/master/README.md#downloads). Install the downloaded binary distribution of Cloud Foundry CLI. To verify Cloud Foundry CLI is installed run the following command from a terminal shell:

```
$ cf -v
cf version 6.10.0-b78bf10-2015-02-11T22:25:45+00:00
```

### Login to AppFog

Now that we have the Cloud Foundry CLI installed, lets login to AppFog. Go to the AppFog overview page in the Control Portal by navigation using the “AppFog" link listed in the drop down navigation bar:

![AppFog in Dropdown Navigation](../images/appfog-in-dropdown-nav.png)

Or you may also navigate to AppFog via the icon on the left-side vertical navigation bar:

![AppFog icon in Vertical Navigation](../images/appfog-icon-nav.png)

Now navigate to the "US East" AppFog region from the left-side navigation tree:

![AppFog Organization Overview in US East Region](../images/appfog-org-overview.png)

Copy the full `cf login` shell command from the "Overview" tab. The command should look similar to:

```
cf login -a https://api.useast.appfog.ctl.io -o C007 -u csterling_demo
```

Now paste the `cf login` command into a terminal shell and run it. You should be prompted for your CenturyLink Cloud Control Portal password.

![AppFog Login Prompt](../images/cf-cli-login-prompt.png)

Please type in your password and hit enter. After successfully authenticating with your credentials, you should be prompted for which AppFog Space to target for application deployments:

![AppFog Space Target Prompt](../images/cf-cli-space-prompt.png)

Choose Space number 1 "Dev" as shown in the image above. You are now logged in and ready to learn more about AppFog capabilities.
