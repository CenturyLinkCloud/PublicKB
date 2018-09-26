{{{
  "title": "Upload Service Manifests to Add-on Engine",
  "date": "06-04-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service was retired on June 29, 2018. The AppFog Platform-as-a-Service is no longer available, including all source code, env vars, and database information.</strong>

### Purpose

The new Add-on Engine marketplace available to the AppFog v2 users to provision and
bind services to their applications.

This document describes how to construct and upload a manifest: a json document which tells the add-on
engine how to interact with a third party service.

### Benefits

Provides an additional channel for Partner services through the CenturyLink Cloud Ecosystem

### Audience

- AppFog Add-on Partners

### What's Included

- Add-on manifest example and explanation
- Add-on publishing process
- Manifest JSON Schema

### Partner Action Items

- Create API to support provisioning Add-on
- Create Service Manifest
- Download `kiri` CLI
- Upload Service Manifest

---

### Introduction

The CenturyLink Cloud Add-ons Marketplace allows application developers to quickly and easily provision
Partner services for AppFog. Partners can use the `kiri` CLI (command line interface) to upload their
Service Manifest that includes information on how to provision service instances for a given service plan.
This article will describe how Partners can create & upload their Service Manifest against their Add-on API.

### Service Manifest

The CenturyLink Cloud Add-on Service Manifest describes how to provision service instances and what
service plans can be provisioned. Here is an example Service Manifest that will be used to explain how Partners
can create their own.

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
- `api/password` - The password used by Add-on Engine to authenticate against the partner provisioning API endpoints via HTTP Basic Auth.
- `api/production/base_url` - The production URL of the provisioning service API endpoint.
- `api/production/sso_url` - The production URL to send service consumers to manage service instances on partner site.
- `api/test/base_url` - The test URL of the provisioning service API endpoint used for local development testing.
- `api/test/sso_url` - The test URL to send service consumers to manage service instances on partner site.
- `plan_updateable` - If true, users can transition across plans (which results in an API call to your service)
- `plans/id` - The unique identifier for the plan that will be be sent to the partner provision API endpoint.
- `plans/name` - The display name of the plan that will be offered as a version of the service.
- `plans/description` - The friendly, short description of the plan that will be offered as a version of the service.

### Using `kiri` CLI

After [implementing the Add-on API](addon-engine-api.md)
and creating a manifest for a Partner service, the Service Manifest
can be uploaded and tested using the `kiri` CLI. The `kiri` CLI binary release can be downloaded for a
specific platform (Windows, Mac, and Linux) from this URL:

[http://kiri.ctl.io](http://kiri.ctl.io)

Once you've downloaded the appropriate `kiri` CLI binary for your platform and placed it on your PATH
environment variable, the next steps are to upload and test your Service Manifest.

#### Login to Add-on Marketplace

The `kiri` CLI must be authenticated to a target Add-on Marketplace server using valid CenturyLink Cloud
Control Portal credentials.

```
$ kiri login myusername
```

Once authenticated you can now upload and test Service Manifests located in your CenturyLink Cloud
Control Portal account. This ensures that one Partner is not able to see another Partner's Service Manifests.

#### Upload Service Manifest

Once you are logged in, you can upload a service manifest.

```
$ kiri manifest upload sudosandwich.json
```

If there are any validation errors in your service manifest it will log those to the console. Fix the
manifest errors and try to upload again.

### Add-on publishing process

Once a service manifest is uploaded to Add-on Marketplace server and the test provisioning is working as
expected, please submit a ticket to publish the service by sending email
to <a href="mailto:support@ctl.io">support@ctl.io</a>. To help direct your ticket to our team,
please put `[ADDON]` into subject of email.

Our typical process will be to enable the Add-on for your Partner CenturyLink Cloud account on AppFog so you
can run a production test with a deployed application. If that works as expected then we'll publish it
officially to the Add-on Marketplace.

#### Manifest JSON Schema

The manifest's [JSON schema](http://json-schema.org/)

```
{
    "type": "object",
    "$schema": "http://json-schema.org/draft-03/schema",
    "id": "AOEManifest",
    "required": true,
    "properties": {
        "api": {
            "type": "object",
            "id": "/api",
            "required": true,
            "properties": {
                "config_vars": {
                    "type": "array",
                    "id": "/api/config_vars",
                    "required": true
                },
                "password": {
                    "type": "string",
                    "id": "/api/password",
                    "required": true
                },
                "production": {
                    "type": "object",
                    "id": "/api/production",
                    "required": true,
                    "properties": {
                        "base_url": {
                            "type": "string",
                            "id": "/api/production/base_url",
                            "required": true
                        },
                        "sso_url": {
                            "type": "string",
                            "id": "/api/production/sso_url",
                            "required": false
                        }
                    }
                },
                "sso_salt": {
                    "type": "string",
                    "id": "/api/sso_salt",
                    "required": false
                },
                "test": {
                    "type": "object",
                    "id": "/api/test",
                    "required": true,
                    "properties": {
                        "base_url": {
                            "type": "string",
                            "id": "/api/test/base_url",
                            "required": true
                        },
                        "sso_url": {
                            "type": "string",
                            "id": "/api/test/sso_url",
                            "required": false
                        }
                    }
                }
            }
        },
        "id": {
            "type": "string",
            "id": "/id",
            "required": true,
            "pattern": "^[a-z][a-z_0-9]+$"
        },
        "name": {
            "type": "string",
            "id": "/name",
            "required": true,
            "minLength": 1
        },
        "tags": {
            "type": "array",
            "id": "/tags",
            "required": false
        },
        "plan_updateable": {
            "type": "boolean",
            "required": false
        },
        "plans": {
            "type": "array",
            "id": "/plans",
            "required": false,
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "id": "/plan_id",
                        "required": true,
                        "pattern": "^[a-z_\\-0-9]+$"
                    },
                    "name": {
                        "type": "string",
                        "id": "/plan_name",
                        "required": true,
                        "pattern": "^[a-z_\\-0-9]+$"
                    },
                    "description": {
                        "type": "string",
                        "id": "/plan_description",
                        "required": true,
                        "minLength": 1
                    }
                }
            }
        }
    }
}
```
