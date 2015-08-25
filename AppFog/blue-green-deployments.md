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

Deploying the [first version of your application to AppFog is straightforward](deploy-an-application.md). Deploying an update to that application without causing downtime involves a plan. [Blue Green Deployment](http://martinfowler.com/bliki/BlueGreenDeployment.html) is an approach that AppFog makes approachable due to its foundation, [Cloud Foundry](https://www.cloudfoundry.org/). The basic steps for executing a Blue Green Deployment are:

* Push initial application with main route (Blue)
* Update application and push with temporary route (Green)
* Map main route to updated (Green) application
* Unmap main route from initial (Blue) application
* Remove temporary route from (Green) application

Now the updated (Green) application becomes the new Blue application. Then the process can be repeated for the next deployment. Although the steps laid out in the steps above, there are considerations all along the way.

### Push Initial Application

If the application has not been deployed before, push it using the [Cloud Foundry CLI](login-using-cf-cli.md).

```
$ cf push myapp-blue -n myapp
```

If the application was deployed into the US East region on AppFog, the URL for the myapp-blue application would be `myapp.useast.appfog.ctl.io` because it is now using the main route of `myapp`.

*NOTE: When using Source Control for your project, the `myapp-blue` could be replaced with `myapp-[hash from source control]` so that each deployment is associated with a specific version of the repository.*

### Deploy Updated Application

After the initial application has been deployed, it is probable that changes will be made to the application. If we just deployed the updated application code using the main `myapp` route then AppFog would stop the running application instance. This would cause downtime to occur while the new version was deployed. In order to reduce risk of downtime, we can instead deploy our updated application to a temporary route.

```
$ cf push myapp-green -n myapp-temp
```

Since the updated application was given a separate name and mapped to a temporary route, the URL for your application assuming it was also in AppFog's US East region would be `myapp-temp.useast.appfog.ctl.io`.

*NOTE: As described in the previous section, `myapp-green` could be replaced with `myapp-[hash from source control]` so that this deployment is associated with a newer version of the project's source control repository.*

### Put Updated Application into Main Rotation

Now we can put the updated application into the main rotation by mapping the original route to it.

```
$ cf map-route myapp-green useast.appfog.ctl.io -n myapp
```

Now when requests are made to `myapp.useast.appfog.ctl.io` they will be load balanced across both versions of the application as they are both mapped to the main `myapp` route.

### Take Initial Application Out of Rotation

After you feel comfortable that the new version of the application is behaving as expected, you can take the initial application out of rotation.

```
$ cf unmap-route myapp-blue useast.appfog.ctl.io -n myapp
```

Now all traffic going to `myapp.useast.appfog.ctl.io` will be routed to the `myapp-green` application.

### Remove Temporary Route

When the updated application was deployed it was mapped to a temporary route. We should now remove this temporary route so that no lingering routes when the upcoming versions of the application are deployed using the Blue Green Deployment approach.

```
$ cf unmap-route myapp-green useast.appfog.ctl.io -n myapp-temp
```

Now there should be no route found when requesting `myapp-temp.useast.appfog.ctl.io`.

### Considerations

If you have any data services, or any services that provide state, bound to your application, you may want to be careful when deploying a new version. There are techniques for doing incremental updates of an application in which considerations are made for handling multiple versions of data and state across deployments. This article does not go into these topics so we recommend searching for Refactoring Databases and Continuous Delivery for more information.