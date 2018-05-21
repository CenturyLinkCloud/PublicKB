{{{
  "title": "AppFog Regions",
  "date": "03-09-2016",
  "author": "Matt Cholick",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

Application developers

### Regions & Region Scope

AppFog exists across these regions
* **US East**
* **US West**

Each region's scope is completely independent. This is important to keep in mind with respect
to routes, domains, and services: these are all independent across regions. For example, an
application claiming a route in one region will have no effect on other regions.

When deploying an application without specifying a domain, the application will use the region's default
domain. Each region has its own default domain. To see the default domain, run `cf domains`:
```
$ cf domains
Getting domains in org CLAF as admin...
name                   status
useast.appfog.ctl.io   shared
```

Users are another thing to keep in mind when working with regions.
A user added to the US East region will not automatically be added to the US West region. See
[Getting Started with AppFog](getting-started-with-appfog.md)
for more information on creating regions and spaces or
[Manage AppFog Region and Space Membership](manage-appfog-membership.md)
for more information on managing users.

### Working with Regions

While working in the UI, you will always be in the context of a specific region. This is also true from
the command line.

To work with the US East region, type:
```
cf login -a https://api.useast.appfog.ctl.io
```

To work with the US West region, type:
```
cf login -a https://api.uswest.appfog.ctl.io
```

If you find yourself switching across regions often, [cfenv](https://github.com/nebhale/cfenv) can be useful tool
for changing context while avoiding repeated logins.

### Further information

[Getting started with the cf cli](http://docs.cloudfoundry.org/cf-cli/getting-started.html)
