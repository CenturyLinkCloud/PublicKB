{{{
  "title": "Migrating an AppFog Add-on to V2 for Partners",
  "date": "5-28-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### Purpose

To describe changes that current AppFog Add-on Partners need to make in order to integrate with the new Add-on Engine marketplace. The new Add-on Engine marketplace is made available to the NextGen AppFog users to provision and bind services to their applications.

### Benefits

Provides an additional channel for Partner services through the CenturyLink Cloud Ecosystem

### Audience

- AppFog Add-on Partners
 
### What's Included

- Changes to Add-on service manifests
- Changes to Add-on Partner provisioning API
- Operational considerations for Add-ons

### Partner Action Items

- Create Partner service manifest to support Add-on Engine
- Create Partner provisioning API to support Add-on Engine
- Whitelist Add-on Engine domain to access Partner provisioning API

---

### Introduction

Integrating your Partner service with the CenturyLink Add-on Engine marketplace is similar to the existing AppFog Add-on Partner integration approach. The current AppFog Add-on Partner documentation is located here:

https://support.appfog.com/hc/en-us/articles/203350577-Become-an-Add-on-Partner

There are changes to be made to the Partner manifest and provisioning API to integrate with Add-on Engine. The following sections will describe the details around these needed changes.

### Changes to Add-on service manifests

There are multiple small changes to how the Add-on Engine manifest is configured compared to AppFog Add-on manifests. Here is an example Add-on Engine manifest:


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
    "production": {
      "base_url": "https://sudosandwich.io/"
    },
    "test": {
      "base_url": "https://staging.sudosandwich.io/"
    },
    "password": "correcthorsebatterystaple"
  }
}
```

#### Manifest Attributes

- `id` - The add-on id. All lowercase, no spaces or punctuation. This must be a unique name for your service. Also used as username in HTTP Basic Auth requests to partner provisioning API endpoints.
- `name` - The friendly, short description of your service. Best if kept under 80 characters.
- `api/production/base_url` - The production URL of the provisioning service API endpoint.
- `api/test/base_url` - The test URL of the provisioning service API endpoint used for local development testing.
- `api/password` - The password used by Add-on Engine to authenticate against the partner provisioning API endpoints via HTTP Basic Auth.
- `plans/id` - The unique identifier for the plan that will be be sent to the partner provision API endpoint.
- `plans/name` - The display name of the plan that will be offered as a version of the service.
- `plans/description` - The friendly, short description of the plan that will be offered as a version of the service.

#### Differences from Existing AppFog Add-on Manifest

- `username`, `sso_salt`, `config_vars`, `api/production/sso_url`, `api/test/sso_url`, `plans/price` and `plans/price_unit` are not valid attributes anymore
- `api/production` and `api/test` must be a valid JSON objects each with a `base_url` attribute defined.
- The top level attribute `test` is no longer valid outside of the `api` object

### Changes to Add-on Partner provisioning API

There are some changes in the provisioning request and response body expectations to support integration with the Add-on Engine. In the example provisioning request for the current AppFog Add-ons, it shows a POST like the following:

```
POST [base_url]/phpfog/resources
{
  "customer_id":"user@email.com",
  "plan":"free",
  "callback_url":"https://path_to_resource",
  "options":{}
}
```

There are a few assumptions in this provisioning request. First, the `customer_id` is assumed to be a single user's email address. The Add-on Engine does not send a customer unique identifier in the request since service provisioning is made for an account that may have many members. Also, there is no concept of `callback_url` at this time in the Add-on Engine. This `callback_url` was provided as a way for partners to update a service instance's data after provisioning has occured. This is useful for instances such as security issues in the partner's platform that results in updating the credentials for all service instances. Add-on Engine will be looking at an approach for providing this capability in the future.

Here is an example of the Add-on Engine provision request:

```
POST [base_url]
{
  uuid: [Add-on Engine generated service instance ID],
  plan: [plan ID from partner manifest],
  region: 'us-east',
  options: {}
}
```

Here is a description of each body attribute:

| Attribute | Value                                              |
| --------- | -----------------                                  |
| `uuid`    | Add-on Engine generated unique service instance ID |
| `plan`    | Plan ID from Partner defined manifest              |
| `region`  | Region that service is being provisioned for       |
| `options` | Currently not populated from Add-on Engine.        |

The response from the `POST [base_url]` request should look similar to:

```
{
  "id": [Partner unique identifier for service instance provisioned],
  "[VARIABLES]": [variables to be provided to service instance consumer],
  ...
}
```

The Partner API response can provide any number of variables. For instance, a MySQL service might provide a response like:

```
{
  "id": "1111-2222-333-44444"
  "hostname": "mysqlhost.partner.com",
  "jdbcUrl": "jdbc:mysql://mysqlhost.partner.com:3306/db-abc123?user=G3nU$3r\u0026password=correcthorsebatterystaple",
  "name": "db-abc123",
  "password": "correcthorsebatterystaple",
  "port": 3306,
  "uri": "mysql://G3nU$3r:correcthorsebatterystaple@mysqlhost.partner.com:3306/db-abc123?reconnect=true",
  "username": "G3nU$3r"
}
```

All of the attributes and their values returned in the provision response body are then provided to the consumer of the service instance.

The deprovision request has only been slightly modified. The current AppFog Add-ons expect the URL to be `[base_url]/phpfog/resources/:id`. The path `/phpfog/resources` is no longer needed for Add-on Engine integration. Here is an example request:

```
DELETE [base_url]/:uuid
```

The `:uuid` that we send is the `uuid` that Add-on Engine generates as unique service instance ID from original POST to provision the service instance. The expected successful response is still:

```
200 ok
```

### Operational considerations for Add-ons

#### Create New API for Add-on Engine

We recommend that you create new Add-on Engine supporting service provisioning API endpoints rather than modifying the existing AppFog Add-on supporting API. The current AppFog will continue to be available to customers some amount of time after Add-on Engine has launched. We are working on a migration strategy that can be used during the overlap of the Add-on Engine and current AppFog services.