{{{
  "title": "How to Migrate an AppFog Add-on to V2",
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
- Add-on publishing process
- Operational considerations for Add-ons

### Partner Action Items

- Create Partner service manifest to support Add-on Engine
- Create Partner provisioning API to support Add-on Engine
- Whitelist Add-on Engine domain to access Partner provisioning API

---

### Introduction

Integrating your Partner service with the CenturyLink Add-on Engine marketplace is similar to the [existing AppFog Add-on Partner integration approach](../../AppFog/Legacy Version 1/become-an-add-on-partner.md).

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

#### Differences from Existing AppFog Add-on Manifest

- `plans/price` and `plans/price_unit` are not valid attributes anymore
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

There are a few assumptions in this provisioning request. First, the `customer_id` is assumed to be a single user's email address. The Add-on Engine does not send a customer unique identifier in the request since service provisioning is made for an account that may have many members.

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

The deprovision request has only been slightly modified. The current AppFog Add-ons expect the URL to be `[base_url]/phpfog/resources/:id`. The path `/phpfog/resources` is no longer needed for Add-on Engine integration. Here is an example request:

```
DELETE [base_url]/:id
```

The `:id` that we send is the `id` that was returned in the provision response for the service instance. The expected successful response is:

```
200 ok
```

### Operational considerations for Add-ons

#### Create New API for Add-on Engine

We recommend that you create new Add-on Engine supporting service provisioning API endpoints rather than modifying the existing AppFog Add-on supporting API. The current AppFog will continue to be available to customers some amount of time after Add-on Engine has launched. We are working on a migration strategy that can be used during the overlap of the Add-on Engine and current AppFog services.
