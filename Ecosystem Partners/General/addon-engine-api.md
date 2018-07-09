{{{
  "title": "Add-on Engine API",
  "date": "04-15-2016",
  "author": "Matt Cholick",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service was retired on June 29, 2018. The AppFog Platform-as-a-Service is no longer available, including all source code, env vars, and database information. More information is available [here](../../AppFog/appfog-retirement-guide.md).</strong>

### Purpose

The new Add-on Engine marketplace available to the AppFog v2 users to provision and
bind services to their applications.

This document describes the API calls needed by a third party service.

### Audience

- AppFog Add-on Partners

---

### Introduction

The CenturyLink Cloud Add-ons Marketplace allows application developers to quickly and easily provision
Partner services for AppFog.
This article will describe the API partners should implement to consume services.

See also [uploading service manifests](upload-service-manifests-to-addon-engine.md) for
instructions on how to enable the add-on.

### Partner Add-on API

The CenturyLink Cloud Add-on Marketplace will make calls to the Partner Add-on API that supports
the following requests:

* **Provision**: creates an instance of a service. A service could be bound to multiple apps
* **Deprovision**: delete a service instance
* **SSO** (optional, but strongly encouraged): Take the user to a dashboard
* **Plan update** (optional): Transition across different plan offerings. Not all transitions need be supported.

#### API Authentication

Authentication is based on HTTP basic authentication with username `id` and password `api/password` from
the [service manifest](upload-service-manifests-to-addon-engine.md).

#### Provision

Example of the Add-on Engine provision request ([base_url] is specified in the manifest):

```
POST [base_url]
{
  "uuid": [Add-on Engine generated service instance ID],
  "plan": [plan ID from partner manifest],
  "callback_url": "https://addons.ctl.io/vendor/[uuid]"
  "region": "useast",
  "clc": {
    "account": [CenturyLink Cloud account]
  }
}
```

Here is a description of each body attribute:

| Attribute      | Value             |
| ---------      | ----------------- |
| `uuid`         | Add-on Engine generated unique service instance ID |
| `plan`         | Plan ID from Partner defined manifest |
| `callback_url` | URL partner can use to access creator's Account info, see [callbacks](../Partner Integration Resources/appfog-addon-provider-app-info-api.md) |
| `region`       | Region that service is being provisioned for, current values could be 'useast' or 'uswest' |
| `clc.account`  | CenturyLink Cloud account alias |

The response from the `POST [base_url]` request should look similar to:

```
{
  "id": [Partner unique identifier for service instance provisioned,
  "config": {
    "[VARIABLES]": [variables to be provided to service instance consumer],
    ...
  }
}
```

The provision response must include an `id` value that represents the service instance unique identifier
from the Partner's side. The Partner API response can provide any number of additional variables. For instance,
a MySQL service might provide a response like:

```
{
  "id": "1111-2222-333-44444",
  "config": {
    "HOSTNAME": "mysqlhost.partner.com",
    "JDBC_URL": "jdbc:mysql://mysqlhost.partner.com:3306/db-abc123?user=G3nU$3r\u0026password=correcthorsebatterystaple",
    "DBNAME": "db-abc123",
    "PASSWORD": "correcthorsebatterystaple",
    "PORT": 3306,
    "MYSQL_URL": "mysql://G3nU$3r:correcthorsebatterystaple@mysqlhost.partner.com:3306/db-abc123?reconnect=true",
    "USERNAME": "G3nU$3r"
  }
}
```

All of the attributes and their values returned in the provision response body's `config` block are then
provided to the consumer of the service instance.


###### Testing Provision with Kiri

The `kiri` CLI must be authenticated to a target Add-on Marketplace server using valid CenturyLink Cloud
Control Portal credentials.

```
$ kiri login myusername --authendpoint https://api.ctl.io
```

Once authenticated you can now upload and test Service Manifests located in your CenturyLink Cloud
Control Portal account. This ensures that one Partner is not able to see another Partner's Service Manifests.

Kiri can make a test provision call and will use the manifests `api.test` block
```
kiri test provision <addon-id> <region> <plan-id> <user-provided-id>
```

#### Deprovision API Endpoint

The deprovision API endpoint uses the same `[base_url]` as the provision API endpoint except that it is
called with the HTTP DELETE verb. Here is an example request:

```
DELETE [base_url]/:id
```

The `:id` that we send is the `id` that was returned in the provision response for the service instance. The
expected successful response is:

```
200 OK
```

###### Testing Deprovision

Kiri can make a test deprovision call and will use the manifests `api.test` block
```
kiri test deprovision <addon-id> <user-provided-id>
```

### Plan update

```
PUT [base_url]/:id
{
  "plan": [new plan ID from partner manifest],
  "clc": {
    "account": [CenturyLink Cloud account]
  }
}
```

The `:id` that we send is the `id` that was returned in the provision response for the service instance. The
expected successful response is:

```
200 OK
```

Not all update paths need to be supported. In the database example, your add-on might support increasing
database size but not allow sizing to a smaller plan if the data won't fit. To not allow
a specific plan change, return a non-ok status code (400 would be an appropriate choice)
and a plain text response body to display to the end user.

###### Testing Update

Kiri can make a test update call and will use the manifests `api.test` block
```
kiri test update <addon-id> <user-provided-id> <new-plan-id>
```

### SSO Flow

The add-on engine generates a `POST` request against your applications manifests `sso_url`. The request
body includes :
* `id`: The `id` that was returned in the provision response for the service instance
* `token`: Token generation method is described below
* `timestamp:` Timestamp the sso request was made

The token is a sha1 hash of `sso_salt` from the manifest, the `id`, and the timestamp. A Node.js example:
```
var crypto = require('crypto');
var hasher = crypto.createHash('sha1');
hasher.update(id + ':' + salt + ':' + timestamp);
var token = hasher.digest('hex');
```

###### Testing SSO

Kiri can make a test deprovision call and will use the manifests `api.test` block
```
kiri test sso <addon-id> <instance-id-generated-by-your-addon>
```

#### Callback

The provision post request includes `callback_url`. This url is protected via basic auth using
your `addonid:password`, and will provide the same info as the provisioning call
as well as the accountId of the provisioned service.

Example calling this:
```
curl -u sudosandwich:correcthorsebatterystaple https://addons.ctl.io/vendor/apps/8e6d510f-0df0-421e-b93f-05d5337fc26d
```

Response:
```
{
  "id": "8e6d510f-0df0-421e-b93f-05d5337fc26d",
  "account_id": "ORG",
  "callback_url": "https://addons.ctl.io/vendor/apps/8e6d510f-0df0-421e-b93f-05d5337fc26d",
  "resource": {
    "uuid": "8e6d510f-0df0-421e-b93f-05d5337fc26d"
  },
  "config": {
    "MYSANDWICH": "Vegetarian club"
  },
  "region": "uswest"
}
```

This endpoint also support listing all the provisioned apps by excluding the id:
```
curl -u sudosandwich:correcthorsebatterystaple https://addons.ctl.io/vendor/apps/
```

Response:
```
[
  {
    "id": "8e6d510f-0df0-421e-b93f-05d5337fc26d",
    "account_id": "ORG",
    "plan": "free",
    "provider_id": "1111-2222-333-44444",
    "callback_url": "https://addons.ctl.io/vendor/apps/8e6d510f-0df0-421e-b93f-05d5337fc26d",
    "resource": {
      "uuid": "8e6d510f-0df0-421e-b93f-05d5337fc26d"
    }
  },
  {
    "id": "e94fbf7e-2b35-4546-aded-0715dba01d92",
    "account_id": "ORG",
    "plan": "free",
    "provider_id": "1111-2222-333-55555",
    "callback_url": "https://addons.ctl.io/vendor/apps/e94fbf7e-2b35-4546-aded-0715dba01d92",
    "resource": {
      "uuid": "e94fbf7e-2b35-4546-aded-0715dba01d92"
    }
  },
]
```

### Additional References

* Add-on engine partner [callbacks](../Partner Integration Resources/appfog-addon-provider-app-info-api.md)
* [Uploading service manifests](upload-service-manifests-to-addon-engine.md)
