{{{
  "title": "Migrating an Application",
  "date": "09-25-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

### Export an Application from AppFog v1
Users may export their app code either from the command line or the web console:
* Using the AF tool from the command line will create a new directory in your current working directory using the appname. The last pushed code is then downloaded into the new directory:
<pre>af pull &lt;appname&gt;</pre>
* From the web console navigate to the Mission Control page of the application. Then select the "Download Source Code" button in the upper left corner to download a zip file of the app.

### Deploy an App on AppFog v2
* Create a [CenturyLink Cloud](https://www.ctl.io) account if you do not already have one.
* [Enable AppFog in the Control Portal](../AppFog/getting-started-with-appfog/#enable-appfog-in-control-portal)
* [Install the Cloud Foundry CLI tool](../AppFog/login-using-cf-cli.md)
* [Deploying an Application](../AppFog/deploy-an-application.md)
