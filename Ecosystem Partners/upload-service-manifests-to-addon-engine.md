{{{
  "title": "Upload Service Manifests to Add-on Engine",
  "date": "06-04-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Purpose

To describe how Partners can add their services to the CenturyLink Cloud Add-ons Marketplace. The new Add-on Engine marketplace is made available to the NextGen AppFog users, as the first consumers, to provision and bind services to their applications.

### Benefits

Provides an additional channel for Partner services through the CenturyLink Cloud Ecosystem

### Audience

- AppFog Add-on Partners
 
### What's Included

- How to create a Service Manifest
- How to use `kiri` CLI to upload Service Manifest
- How to test service provisioning using `kiri` CLI
- How Service Manifests are published to Add-ons marketplace

### Partner Action Items

- Create Service Manifest
- Create API to support provisioning Add-on
- Download `kiri` CLI
- Upload Service Manifest
- Test Service provisioning using `kiri` CLI

---

### Introduction

The CenturyLink Cloud Add-ons Marketplace allows application developers to quickly and easily provision Partner services. Partners can use the `kiri` CLI (command line interface) to upload their Service Manifest that includes information on how to provision service instances for a given service plan. This article will describe how Partners can create, upload and test their Service Manifest against their Add-on API.

### Service Manifest

The CenturyLink Cloud Add-on Service Manifest describes how to provision service instances and what service plans can be provisioned. Here is an example Service Manifest that will be used to explain how Partners can create their own.

#### Example Add-on Engine Manifest

```
{
  "id": "sudosandwich",
  "name": "Sudo me a sandwich",
  "plans": [
    {
      "id": "free",
      "name": "free",
      "description": "Get your free version of a sandwich"
    }
  ],
  "api": {
    "config_vars": ["MYSANDWICH"],
    "sso_salt": "STATISTICALLY.SIGNIFICANT",
    "production": {
      "base_url": "https://api.sudosandwich.io/",
      "sso_url": "https://dashboard.sudosandwich.io/"
    },
    "test": {
      "base_url": "https://api.staging.sudosandwich.io/",
      "sso_url": "https://dashboard.staging.sudosandwich.io/"
    },
    "password": "correcthorsebatterystaple"
  }
}
```

#### Manifest Attributes

- `id` - The add-on id. All lowercase, no spaces or punctuation. This must be a unique name for your service. Also used as username in HTTP Basic Auth requests to partner provisioning API endpoints.
- `name` - The friendly, short description of your service. Best if kept under 80 characters.
- `api/config_vars` - An array of attribute names to pull from provision response and expose to consumers of the service instance such as URL and credentials. We recommend these are UPPER_CASE formatted.
- `api/sso_salt` - Single sign-on salt for connecting with service instance service instance management partner site.
- `api/production/base_url` - The production URL of the provisioning service API endpoint.
- `api/production/sso_url` - The production URL to send service consumers to manage service instances on partner site.
- `api/test/base_url` - The test URL of the provisioning service API endpoint used for local development testing.
- `api/test/sso_url` - The test URL to send service consumers to manage service instances on partner site.
- `api/password` - The password used by Add-on Engine to authenticate against the partner provisioning API endpoints via HTTP Basic Auth.
- `plans/id` - The unique identifier for the plan that will be be sent to the partner provision API endpoint.
- `plans/name` - The display name of the plan that will be offered as a version of the service.
- `plans/description` - The friendly, short description of the plan that will be offered as a version of the service.

### Partner Add-on API

The CenturyLink Cloud Add-on Marketplace will make calls to the Partner Add-on API that supports the following provision and deprovision requests. These requests will be sent to the `api/production/base_url` and `api/test/base_url` URL using HTTP verbs: POST for provision and DELETE for deprovision.

#### API Authentication

Authentication is based on HTTP basic authentication with username `id` and password `api/password` from Service Manifest.

#### Provisioning API Endpoint

Here is an example of the Add-on Engine provision request:

```
POST [base_url]
{
  uuid: [Add-on Engine generated service instance ID],
  plan: [plan ID from partner manifest],
  callback_url: "https://addons.ctl.io/vendor/[uuid]"
  region: "useast",
  options: {}
}
```

Here is a description of each body attribute:

| Attribute      | Value                                                |
| ---------      | -----------------                                    |
| `uuid`         | Add-on Engine generated unique service instance ID   |
| `plan`         | Plan ID from Partner defined manifest                |
| `callback_url` | URL partner can use to access creator's Account info |
| `region`       | Region that service is being provisioned for         |
| `options`      | Currently not populated from Add-on Engine.          |

The response from the `POST [base_url]` request should look similar to:

```
{
  "id": [Partner unique identifier for service instance provisioned],
  "config": {
    "[VARIABLES]": [variables to be provided to service instance consumer],
    ...
  }
}
```

The provision response must include an `id` value that represents the service instance unique identifier from the Partner's side. The Partner API response can provide any number of additional variables. For instance, a MySQL service might provide a response like:

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

All of the attributes and their values returned in the provision response body's `config` block are then provided to the consumer of the service instance.

#### Deprovision API Endpoint

The deprovision API endpoint uses the same `[base_url]` as the provision API endpoint except that it is called with the HTTP DELETE verb. Here is an example request:

```
DELETE [base_url]/:id
```

The `:id` that we send is the `id` that was returned in the provision response for the service instance. The expected successful response is:

```
200 OK
```


### Using `kiri` CLI

After implementing an Add-on API and creating a manifest for a Partner service, the Service Manifest can be uploaded and tested using the `kiri` CLI. The `kiri` CLI binary release can be downloaded for a specific platform (Windows, Mac, and Linux) from this URL:

[http://kiri.ctl.io](http://kiri.ctl.io)

Once you've downloaded the appropriate `kiri` CLI binary for your platform and placed it on your PATH environment variable, the next steps are to upload and test your Service Manifest.

#### Login to Add-on Marketplace

The `kiri` CLI must be authenticated to a target Add-on Marketplace server using valid CenturyLink Cloud Control Portal credentials.

```
$ kiri login myusername --authendpoint https://api.ctl.io
```

Once authenticated you can now upload and test Service Manifests located in your CenturyLink Cloud Control account. This ensures that one Partner is not able to see another Partner's Service Manifests.

#### Upload Service Manifest

Once you are logged in, you can upload a service manifest.

```
$ kiri manifest upload sudosandwich.json
```

If there are any validation errors in your service manifest it will log those to the console. Fix the manifest errors and try to upload again.

#### Test Service Manifest

Once your service manifest is uploaded successfully, you can test provision and deprovision of a service instance using the Service Manifest defined `api/test/base_url` URL value.

```
$ kiri test provision sudosandwich 1234567890
```

This provisions an instance of the `sudosandwich` service with a fake instance ID `1234567890` so we can use this to deprovision the instance later. If successful, you can deprovision the service instance.

```
$ kiri test deprovision sudosandwich 1234567890
```

#### Callback

The provision post request includes a callback url. This url is protected via basic auth using your addonid:password, and will provide the same info as the provisioning call 
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

### Add-on publishing process

Once a service manifest is uploaded to Add-on Marketplace server and the test provisioning is working as expected, please submit a ticket to publish the service by sending email to <a href="mailto:support@ctl.io">support@ctl.io</a>. To help direct your ticket to our team, please put `[ADDON]` into subject of email.

Our typical process will be to enable the Add-on for your Partner CenturyLink Cloud account on AppFog so you can run a production test with a deployed application. If that works as expected then we'll publish it officially to the Add-on Marketplace.
