{{{
  "title": "AppFog Add-on Provider App Info API",
  "date": "11-23-2015",
  "author": "Matt Cholick",
  "attachments": [],
  "contentIsHTML": false
}}}

<strong>The AppFog service was retired on June 29, 2018. The AppFog Platform-as-a-Service is no longer available, including all source code, env vars, and database information. More information is available [here](../../AppFog/appfog-retirement-guide.md).</strong>

### Purpose

The new Add-on Engine marketplace is made available to the NextGen AppFog v2 users to provision and bind services to their applications. This document describes the App Info endpoint, which AppFog Add-on Partners can use to retrieve the list of provisioned add-ons.

### Audience

- AppFog Add-on Partners

### Get All Apps

The endpoint to list apps that have installed your add-on is `https://addons.ctl.io/vendor/apps`. This endpoint
is protected with basic auth where the username is the id of your add-on and the password is
the same as that provided in the manifest. For example, this manifest

```
{
  "id": "sudosandwich",
...
  "plans": [
    {
      "id": "free",
      "name": "free",
      "description": "Get your free version of a sandwich"
    }
  ],
  "api": {
    "config_vars": ["MYSANDWICH"],
...
    "password": "correcthorsebatterystaple"
  }
}
```

would call the endpoint:

```
curl -s https://sudosandwich:correcthorsebatterystaple@addons.ctl.io/vendor/apps
```

and receive a response like:

```
[
  {
    "callback_url": "https://addons.ctl.io/vendor/apps/e9f4ad41-e455-4db1-92bd-9cc657a6f75e",
    "plan": "free",
    "provider_id": 12,
    "account_id": "TEST",
    "resource": {
      "uuid": "e9f4ad41-e455-4db1-92bd-9cc657a6f75e"
    }
  }
]
```

with body attributes:

- `callback_url` - The url to call to update a provisioned service's configuration
- `plan` - Plan id as provisioned
- `provider_id` - The unique identifier assigned to the application by your add-on at time of provisioning
- `account_id` - Account alias
- `resource.uuid` - Application id: unique identifier assigned by AppFog

### Get Individual App

You can also ask for an individual app by application id (`resource.uuid` from the previous above call):

```
curl -s https://sudosandwich:correcthorsebatterystaple@addons.ctl.io/vendor/apps/e9f4ad41-e455-4db1-92bd-9cc657a6f75e
```

and receive a response like:

```
{
  "id": "e9f4ad41-e455-4db1-92bd-9cc657a6f75e",
  "account_id": "TEST",
  "callback_url": "https://addons.ctl.io/vendor/apps/e9f4ad41-e455-4db1-92bd-9cc657a6f75e",
  "resource": {
    "uuid": "e9f4ad41-e455-4db1-92bd-9cc657a6f75e"
  },
  "config": {
    "MYSANDWICH": "Grilled Tomato and Brie"
  },
  "region": "useast"
}
```

with additional body attributes:

- `id` - Unique identifier assigned by AppFog
- `config` - The configuration your service has supplied to the app
- `region` - AppFog region

### Update Configuration

Please note that this **requires user action**. Once you've updated a configuration, the user must re-bind the service to an application and re-stage the application. There is no way for an add-on provider to trigger this action, so many changes will require coordination with users.

Update the configuration your service is providing for an application by calling:

```
curl -H 'Content-Type: application/json' \
     -X PUT https://sudosandwich:correcthorsebatterystaple@addons.ctl.io/vendor/apps/e9f4ad41-e455-4db1-92bd-9cc657a6f75e \
     -d '{"config": {"MYSANDWICH": "Tofu Banh Mi"}}'
```

Which will respond identically to getting an individual app.
