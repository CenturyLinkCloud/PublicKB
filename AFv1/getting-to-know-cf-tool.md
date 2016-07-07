{{{
  "title": "Getting To Know The CLI cf Tool",
  "date": "02-08-2016",
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

### The AppFog v2 cf CLI Tool
There are similarities and differences between the AppFog v2 `cf` CLI tool and the AppFog v1 `af` tool. This article is intended to provide some of the new `cf` tool syntax for AppFog v1 users. More information about the `cf` tool can be found in our [Using the Cloud Foundry CLI Tool](../AppFog/using-cloud-foundry-cli-tool.md) article, or from the CLI run `cf help`. For detail on a specific command use `cf help <COMMAND>`.

At this time the AppFog v2 web console offers the option to start, stop, scale, restage, or delete an application. Additionally, environment variables can be viewed, created, or deleted through the web interface. All other actions must be taken using the CLI tool. Each individual application page will also display the current hourly rate for that application.

##### Pushing an Application
To deploy your application to AppFog v2 use `cf push <YOUR_APPNAME>`. There is not an `update` command as on AppFog v1, use `cf push <YOUR_APPNAME>` when updating. AppFog v2 does not run a diff when updating an application. The entire code base is uploaded every time. For large application's more information can be found in the Cloud Foundry [Deploying a Large Application](https://docs.cloudfoundry.org/devguide/deploy-apps/large-app-deploy.html) documentation. AppFog v2 does not provide a `pull` command to download the last pushed source code. We recommend using a version control repository to maintain your source code.

##### Custom Domains
Before mapping a custom domain to an application on AppFog v2 the domain needs to be created. Simply use `cf create-domain <YOUR_ORG> <YOUR_DOMAIN>`. Then map the domain to your application using `cf map-route <YOUR_APPNAME> <YOUR_DOMAIN>`. More information is available in the [Setup Custom Domain for Application](../AppFog/setup-custom-domain-for-appfog-app.md) article.

##### Services
Users are able to connect directly to their services on AppFog v2 so there is not a `tunnel` command. There is also not an `export-service` command. To obtain a backup of your service connect directly to the service using the credentials in the VCAP_SERVICES environment variable.

To list available services with AppFog v2 use `cf marketplace`. For detailed information on a specific service use `cf marketplace -s <SERVICE>`.

To create a service instance use `cf create-service <SERVICE_TYPE> <SERVICE_PLAN> <YOUR_SERVICE_NAME>`. For example, `cf create-service ctl_mysql micro example-db`.

##### Application Health and Status
Use the command `cf app <YOUR_APPNAME>` to provide the status and resource usage of your application.

##### Scaling an Application
To scale the number of instances use `cf scale <YOUR_APPNAME> -i <NUMBER_OF_INSTANCES>`. To scale the memory allocation use `cf scale <YOUR_APPNAME> -m <DESIRED_MEMORY>`

##### Environment Variables
To set an environmnet variable use `cf set-env <YOUR_APPNAME> <VARIABLE_NAME> <VARIABLE_VALUE>`. To view an application's environment variables use `cf env <YOUR_APPNAME>`. The VCAP_SERVICES environment variable is displayed using the `cf env` command on AppFog v2.
