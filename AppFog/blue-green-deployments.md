{{{
  "title": "Blue Green Deployments for Zero Planned Downtime",
  "date": "07-24-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Audience

Application developers

### Overview

Deploying the [first version of your application to AppFog is straightforward](deploy-an-application.md). Deploying an update to that application without causing any downtime involves a plan. [Blue Green Deployment](http://martinfowler.com/bliki/BlueGreenDeployment.html) is an approach that AppFog makes approachable due to its foundation, [Cloud Foundry](https://www.cloudfoundry.org/).

The basic steps for executing a Blue Green Deployment are:

* Push initial application with main route (Blue)
* Update application and push with temporary route (Green)
* Map main route to updated (Green) application
* Unmap main route from initial (Blue) application
* Remove temporary route from (Green) application

Now Green application becomes the new Blue application and the process can be repeated for the next deployment. Although the steps are able to be pointed out using the bullets above, there are things to consider all along the way.

### Push Initial Application

If the application has not been deployed before we can push it using the [Cloud Foundry CLI](login-using-cf-cli.md).

```
$ cf push myapp-blue -n myapp
```

If you deployed the application into the US East region on AppFog then the URL for your application would be `myapp.useast.appfog.ctl.io`. The myapp-blue version of the application is now using the main route of `myapp`.

*NOTE: When using Continuous Integration servers and Source Control repositories together you could replace `myapp-blue` with `myapp-[hash from source control]` so that each deployment is associated with a version of your codebase.*

### Deploy Updated Application

After the initial application has been deployed, it is probable that changes will be made the application that need to be deployed. If we just pushed the updated application code to the `myapp` route then AppFog would stop the existing application instance running at that route. This would cause downtime to occur while the new version was deployed to that same route. In order to reduce the risk for downtime we can instead deploy our updated application to a temporary route.

```
$ cf push myapp-green -n myapp-temp
```

Since the update application was given a separate name and mapped to a temporary route, the URL for your application if deployed AppFog's US East region would be `myapp-temp.useast.appfog.ctl.io`.

*NOTE: When using Continuous Integration servers and Source Control repositories together you could replace `myapp-green` with `myapp-[hash from source control]` so that this deployment is associated with a newer version of your codebase.*

### Put Update Application into Main Rotation

Now we can put the updated application into the main rotation by mapping the original route to it.

```
$ cf map-route myapp-green useast.appfog.ctl.io -n myapp
```

And now when requests are sent for `myapp.useast.appfog.ctl.io` they will be load balanced across both versions of the application since both applications are mapped to the `myapp` route.

### Take Initial Application Out of Rotation

After you feel comfortable that the new version of the application is behaving as expected you can take the initial application out of rotation.

```
$ cf unmap-route myapp-blue useast.appfog.ctl.io -n myapp
```

Now all traffic going to `myapp.useast.appfog.ctl.io` will be going to `myapp-green`.

### Remove Temporary Route

When the updated application was deployed we mapped it to a temporary route. We should now remove this temporary route so that it can be used when the next version of the application is deployed using this Blue Green Deployment approach.

```
$ cf unmap-route myapp-green useast.appfog.ctl.io -n myapp-temp
```

Now there should be no route found when requesting `myapp-temp.useast.appfog.ctl.io`.

### Considerations

If you have any data services, or any services that provide state, bound to your application you may want to be careful when deploying a new version. There are techniques for doing incremental updates of your application and for handling multiple versions of data and state across deployments. This article will not go into these topics so we recommend searching for Refactoring Databases and Continuous Delivery topics.