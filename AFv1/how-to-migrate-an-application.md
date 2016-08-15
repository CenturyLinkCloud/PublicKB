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

When migration is complete your billing subscription can be canceled from the [Account](https://console.appfog.com/#account) page of the web console. Please be sure to cancel your subscription as we are not aware when individual user migration is complete. The billing system will not automatically prorate the subscription and issue a refund. If applicable, please open a [Support Ticket](https://support.appfog.com/tickets/new) or email support@appfog.com to receive a prorated refund of your subscription.

### Export an Application from AppFog v1
Users may export their app code either from the command line or the web console:
* Using the AF tool from the command line will create a new directory in your current working directory using the appname. The last pushed code is then downloaded into the new directory:
<pre>af pull &lt;appname&gt;</pre>
* From the web console navigate to the Mission Control page of the application. Then select the "Download Source Code" button in the upper left corner to download a zip file of the app.

### Deploy an App on AppFog v2
* Create a [CenturyLink Cloud](https://www.ctl.io) account if you do not already have one.
* [Enable AppFog in the Control Portal](../AppFog/getting-started-with-appfog.md)
* [Install the Cloud Foundry CLI tool](../AppFog/login-using-cf-cli.md)
* [Deploying an Application](../AppFog/deploy-an-application.md)
* [Setup Custom Domain for Application](../AppFog/setup-custom-domain-for-appfog-app.md)
