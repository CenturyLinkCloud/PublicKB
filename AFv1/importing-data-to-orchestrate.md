{{{
  "title": "Importing Data to Orchestrate on AppFog v2",
  "date": "11-04-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

### Overview

This article will provide an overview of our [CenturyLink Orchestrate Database Service](https://orchestrate.io/) and how it can be consumed by applications deployed to AppFog.


You can find available service offerings via the Cloud Foundry CLI by running the following command in a terminal window:

```
$ cf marketplace
...
service       plans                           description   
ctl_mysql     micro, small, medium, large     CenturyLink's BETA MySQL DBaaS.  For development use only; not subject to SLAs.
orchestrate   free                            Orchestrate DBaaS
```

### Create an Orchestrate Service Instance

To create a new CenturyLink Orchestrate service instance, we can use the Cloud Foundry CLI. In order to do this you must be [logged into an AppFog region](../AppFog/login-using-cf-cli.md). The following command will create a new CenturyLink Orchestrate service instance named `newdb`:

```
$ cf create-service orchestrate free newdb
```

The `cf create-service` command will provision a new Orchestrate instance that can later be bound to an application deployed to AppFog.

### Bind Orchestrate to the Application

To bind the Orchestrate service instance to an [application deployed to AppFog](../AppFog/deploy-an-application.md) you can use the `cf bind-service` command:

```
$ cf bind-service myapp newdb
```

This will add the CenturyLink Orchestrate service instance access credentials into the `myapp` application's runtime environment. To view these Orchestrate service instance credentials use the `cf env` command and they will be located in the VCAP_SERVICES environment variable which is a convention for Cloud Foundry enabled services:

```
$ cf env myapp
...
System-Provided:
{
 "VCAP_SERVICES": {
  "ctl_mysql": [
   {...}
  ],
  "orchestrate": [
   {
    "credentials": {
     "ORCHESTRATE_API_HOST": "<HOST_ADDRESS>",
     "ORCHESTRATE_API_KEY": "<API_KEY>",
     "ORCHESTRATE_API_URL": "<API_URL>"
    },
    "label": "orchestrate",
    "name": "example-db",
    "plan": "free",
    "tags": []
   }
  ]
 }
}
```
Follow Orchestrate's documentation on [Importing Data](https://orchestrate.io/docs/data-import).

To learn about using Orchestrate please visit
* [Orchestrate Dev Resources](https://orchestrate.io/docs)
* [Orchestrate API](https://orchestrate.io/docs/apiref#overview)
