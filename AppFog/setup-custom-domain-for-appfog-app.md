{{{
  "title": "Setup Custom Domain for Application",
  "date": "07-17-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

Application developers

### Overview

When an application is deployed to AppFog a URL is generated based on a route and domain. An example for an application that is deployed to the AppFog US East region named `myapp` would be:

```
myapp.useast.appfog.ctl.io
```

The default domain in the AppFog US East region is `useast.appfog.ctl.io` and the US West region is `hello-node.uswest.appfog.ctl.io.`. The application's name is typically used for the route, or sub-domain, in the URL. Setting up a custom domain for your application involves creating a custom domain and route. The following sections will take you through this process.

### Pre-requisites

In order to setup a custom domain for applications on AppFog you must be logged in from the command line. If you are not familiar with accessing AppFog from the command line follow the instructions in the [Login to AppFog using the Cloud Foundry CLI](login-using-cf-cli.md) article before moving onto the following sections.

### Setup Custom Domain

AppFog provides the ability to manage a custom domain within each region. For the purposes of this article we will be using `sudomesandwich.io` as the example domain and `ACME` as example AppFog account name. In order to use the `sudomesandwich.io` domain with our application deployment, run the following command:

```
$ cf create-domain ACME www.sudomesandwich.io
Creating domain sudomesandwich.io for org ACME as me...
OK
```

In order to verify that the domain is now available for use in AppFog application routing for your account, run the follow command:

```
$ cf domains
Getting domains in org ACME as me...
name                   status   
useast.appfog.ctl.io   shared  
www.sudomesandwich.io  owned  
```

You should see your domain in the list with a status of `owned`.

### Setup Custom Route

You can map your application to a custom route with a specified domain now using the `cf map-route` command:

```
$ cf map-route myapp www.sudomesandwich.io
```

Now if a request for `www.sudomesandwich.io` were to come to AppFog it would be routed to the `myapp` application.

### Setting Up DNS with 3rd Party Provider

In order for users to access your application at the custom domain there needs to be a DNS (domain name service) entry that describes how to route traffic to AppFog. AppFog's external IP addresses are not static and should not be used for a DNS A Record. At your DNS provider create a redirect(302) from your root domain `<YOUR_DOMAIN>` routing to `www.<YOUR_DOMAIN>`. For this example, `myapp.sudomesandwich.io` will redirect to `www.myapp.sudomesandwich.io`. This is a fairly standard tool that DNS services provide. If you don’t see an option for it at your domain host, contact their support services and they may be able to do that for you. Once the root domain redirect is established, you then can map a CNAME record pointing to AppFog. Depending on the region your app is deployed either create the CNAME Record directing to `hello-node.uswest.appfog.ctl.io.` or `hello-node.useast.appfog.ctl.io.` For instance, to map `www.myapp.sudomesandwich.io` in the US East region you would have a CNAME record like this:

`CNAME www 1 min hello-node.useast.appfog.ctl.io.`

If your DNS provider is unable to create a redirect from your root domain you many need to consider another DNS provider. Some DNS providers are also offering the option of a CNAME record for your root domain. If this is available you do not need to create a redirect from your root domain, simply create the same CNAME entry as for `www.<YOUR_DOMAIN>`. Remember to also create and map the domain on AppFog if using your root domain.

### Setting up SSL for your custom domain
Setting up SSL certifications to match your custom domain will require the use of a third-party provider, like CloudFlare.  See https://www.cloudflare.com/ssl/ for more information.

### Additional Information

For more information on additional capabilities in Cloud Foundry for custom domains (on which AppFog is based), please check out this page on the Cloud Foundry Foundation documentation site:

http://docs.cloudfoundry.org/devguide/deploy-apps/domains-routes.html
