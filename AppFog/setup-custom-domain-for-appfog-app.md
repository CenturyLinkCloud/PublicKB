{{{
  "title": "Setup Custom Domain for Application",
  "date": "07-17-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Audience

Application developers

### Overview

When an application is deployed to AppFog a URL is generated based on a route and domain. An example for an application that is deployed to the AppFog US East region named `myapp` would be:

```
myapp.useast.appfog.ctl.io
```

The default domain in the AppFog US East region is `useast.appfog.ctl.io` and the application's name is typically used for the route, or sub-domain, in the URL. Setting up a custom domain for your application involves creating a custom domain and route. The following sections will step you through this process.

### Pre-requisites

In order to setup a custom domain for applications on AppFog you must be logged in from the command line. If you are not familiar with accessing AppFog from the command line follow the instructions in the instructions in [Login to AppFog using the Cloud Foundry CLI](login-using-cf-cli.md) article before moving onto the following sections.

### Setup Custom Domain

AppFog provides the ability to manage a custom domain within each region. For the purposes of this article we will be using `sudomesandwich.io` as the example domain and `ACME` as example AppFog account name. In order to use the `sudomesandwich.io` domain with our application deployment, un the following command:

```
$ cf create-domain ACME sudomesandwich.io
Creating domain sudomesandwich.io for org ACME as me...
OK
```

In order to verify that the domain is now available for use in AppFog application routing for your account, run the follow command:

```
$ cf domains
Getting domains in org ACME as me...
name                   status   
useast.appfog.ctl.io   shared  
sudomesandwich.io      owned  
```

You should see your domain in the list with a status of `owned`.

### Setup Custom Route

You can map your application to a custom route with a specified domain now using the `cf map-route` command:

```
$ cf map-route myapp sudomesandwich.io
```

Now if a request for `myapp.sudomesandwich.io` were to come to AppFog it would be routed to the `myapp` application.

### Setting Up DNS with 3rd Party Provider

In order for the users to access your application at the custom domain there needs to be a DNS (domain name service) entry that describes how to route traffic to AppFog. With your DNS provider, you then can map a CNAME record to the custom domain, for instance to map `myapp.sudomesandwich.io` you would have a CNAME record like this:

`CNAME 1 min hello-node.useast.appfog.ctl.io.`

### Additional Information

For more information on additional capabilities in Cloud Foundry for custom domains (on which AppFog is based), please check out this page on the Cloud Foundry Foundation documentation site:

http://docs.cloudfoundry.org/devguide/deploy-apps/domains-routes.html