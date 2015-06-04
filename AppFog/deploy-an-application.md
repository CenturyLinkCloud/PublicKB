{{{
  "title": "Deploying an Application",
  "date": "04-21-2015",
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

We currently support applications using the following application runtimes in AppFog by default:

* Java
* [Node.js](deploy-nodejs-application.md)
* Ruby
* PHP
* Python
* Go
* Static websites

### Deploy Application

Once you have an application to deploy that is based on one of the supported application runtimes, you can deploy that application using the Cloud Foundry CLI. Here are the steps for deploying your application:

* Go to the directory where your application source code is located
* Run the command `cf push [name of app]` to deploy it into AppFog (NOTE: [name of app] must be unique so be clever with name such as “theultimateapp-100”)
* After the process has finished you should see something similar to the following:

![Application Deployed Successfully](../images/appfog-app-deployed.png)

* Copy the URL from “urls” line and open that URL in a browser

You should now see your application running!
