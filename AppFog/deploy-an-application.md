{{{
  "title": "Deploying an Application",
  "date": "04-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Audience

Application developers

### Overview

We currently support applications using the following application runtimes in AppFog by default:

* [Java](deploy-java-application.md)
* [Node.js](deploy-nodejs-application.md)
* Ruby
* [PHP](deploy-php-application.md)
* Python
* Go
* [Static websites](deploy-static-website.md)

### Deploy Application

Once you have an application to deploy that is based on one of the supported application runtimes, you can deploy that application using the Cloud Foundry CLI. Here are the steps for deploying your application:

* Go to the directory where your application source code is located
* Run the command `cf push [name of app]` to deploy it into AppFog (NOTE: [name of app] must be unique so be clever with name such as “theultimateapp-100”)
* After the process has finished you should see something similar to the following:

![Application Deployed Successfully](../images/appfog-app-deployed.png)

* Copy the URL from “urls” line and open that URL in a browser

You should now see your application running!
