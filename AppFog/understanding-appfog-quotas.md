{{{
  "title": "Understanding AppFog Quotas",
  "date": "09-08-2015",
  "author": "Robert Brumfield",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

Application developers
Control administrators

### Quotas

Every Account that has enabled an Account gets an Organization in AppFog.  Organizations in AppFog contain Spaces that serve as a way to organize applications.  By default, each Organization gets three Spaces, Dev, QA, and Prod.  A user may add additional Spaces.  Quotas may be applied at both the Organization level and the Space level.

Every Organization has a quota that defines the resources they can use when deploying apps.  This is defined by AppFog and cannot be changed except via ticket to [https://support.ctl.io](https://support.ctl.io). The resources limited by quota are total memory, instance memory, routes, and service instances.  

| resource | description |
| -------- | ----------- |
| *total memory* | Total amount of memory that can be used across all apps in all spaces (default: 10G) |
| *instance memory* | Amount of memory a single instance can use (subject to total memory limits). (default: unlimited) |
| *routes* | Total number of routes an organization may use.  These are typically used by each deployed app. (default: 1000) |
| *service instances* | Services added to an organization via cf-create-service (default: 100) |

Users in the Organization Manager role for AppFog, can assign quota to Spaces.  This will allocate a portion of the Organizations total memory to a space.

Space quotas must be managed with the CloudFoundry cli tool, cf.  

Creating space quotas: ``` cf create-space-quota myquota -i -1 -m 5G -r 100 -s 100 ```

Apply the quota to a space: ``` cf set-space-quota QA myquota ```

See all space quotas: ``` cf space-quotas ```


### Further information

[Getting started with the cf cli](http://docs.cloudfoundry.org/devguide/installcf/whats-new-v6.html)

[Roles in CloudFoundry](http://docs.cloudfoundry.org/concepts/roles.html)
