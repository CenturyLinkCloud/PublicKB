{{{
"title": "Main changes in this release",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Main changes in this release

This article covers the main API changes to the endpoints for boxes, instances, workspaces, and profiles.

**In this article:**
* What’s new
* Sample API calls
* Schema

### What’s new

|  Endpoint     | Added, Changed, or Removed   |
|---------------|------------------------------|
|  Instances    | **Added** <br>    + **New Endpoint** that updates an active instance by applying a box version.<br>       + PUT /services/instances/{instance_id}/pull.<br><br>+ Parameters: automatic_updates, box, policy_box <br>+ PUT /services/instances/{instance_id}<br> + GET /services/instances<br><br> + Parameters: automatic_updates, box, policy_box, instance_tags, ipv4_address (only for [deploying using the ElasticBox agent on any infrastructure](./deploying-on-anyinfra.md)). <br> + POST /services/instances <br> + POST /services/instances/dryrun <br><br> **Removed** <br> + Parameter: environment.<br> + PUT /services/instances/{instance_id} <br> + GET /services/instances <br> + Parameter: environment, profile, variables. <br> + POST /services/instances <br> + POST /services/instances/dryrun |
|  Boxes    | **Added**<br>  **Changed**<br> The boxes endpoint accepts four box types now. When you call a box, use one of the following schemas:<br> + Script box <br> + Deployment policy box <br> + CloudFormation box <br> + Docker container box <br> <br> **Removed** <br>  Parameters: <br> + tags are deprecated. Use requirements or claims instead. <br> + service |
| Workspaces | **Removed**  <br> This particular operation on the workspaces endpoint:  <br> + GET /services/workspaces/{workspace_id}/profiles |
| Profiles | **Removed** <br> All operations on the profiles endpoint are deprecated and replaced by deployment policy boxes <br> + GET /services/profiles <br> + POST /services/profiles <br> + GET /services/profiles/{profile_id} <br> + PUT /services/profiles/{profile_id} <br> + DELETE /services/profiles/{profile_id} |
| Organizations	| **Removed** <br> + Parameter: admin_boxes <br> + GET /services/organizations/{organization_name} <br> + POST /services/organizations <br> + PUT /services/organizations/{organization_name} |
| Providers | **Removed** <br> + Parameter: admin_box <br> + GET /services/providers <br> + POST /services/providers <br> + GET /services/providers/{provider_id} <br> + PUT /services/providers/{provider_id} |

___


### Instances

**Endpoint**

PUT /services/instances/{instance_id}/pull

New endpoint that updates an active instance by applying a box version.

**Request**

| Parameter | Type | Description |
|----------------|--------|----------------|
| box_id | string | Required. ID of the box version used to update the instance. The version should relate to the box currently deployed on the instance. |

**Response**

None.

___


### Boxes

**Script box**

* Deployment policy box
* CloudFormation box
* Docker container box
* Script Box

This box’s type behaves just like the old boxes.

**Endpoint**

/services/boxes

**Schema**

**http://elasticbox.net/schemas/boxes/script**

**New parameters**

| Parameter | Type | Description |
|---------------|---------|----------------|
| automatic_updates | string | Required. Specify an option: off, major, minor, or patch. Default is off. |
| draft_from | guid | Optional. ID of the box version that this box is a draft from. |
| requirements | array | Required. Contains strings like tags. Specifies the runtime technologies the box requires to deploy. |

**Changed parameters**

| Parameter | Type | Description |
|---------------|---------|----------------|
| events | object | Optional. Contains these events: pre_configure, configure, pre_install, install, pre_start, start, stop, post_stop, dispose, post_dispose. Each refers to a blob of the script. <br> **Note:** The post_install, post_configure, and post_start events are deprecated. The new events are pre_install, pre_configure, and pre_start.
| version | object	| Optional. Requires these properties: <br> + box: Of type guid. Identifies the ID of the box to which the version belongs. <br> + description. Of type string, describes the change to the box version. <br> + number. Of type object, specifies the version number as an integer in this format: major, minor, and patch. For example to represent version 1.4.5, you would specify major:1, <br> minor:4, patch:5. |

**Deployment Policy Box**

This box type replaces the old deployment profiles, but it contains the same information of a deployment profile including box properties.

**Note:** In contrast with Script Boxes, the deployment policy boxes do not include these parameters: **events**, **requirements**.

**Endpoint**

/services/boxes

**Schema**

**http://elasticbox.net/schemas/boxes/policy**

**New parameters**

| Parameter | Type | Description |
|---------------|---------|----------------|
| profile | object | Required. Describes all the properties to deploy an instance of a box. Contains the same data as the old deployment profile endpoint. |
| provider_id | object | Required. Specifies the ID of the provider. |
| draft_from | guid | Optional. ID of the box version that this box is a draft from. |
| claims | array | Required. An array of strings, specifies the requirements applied to a box. |
| automatic_updates | string | Required. Specify an option: off, major, minor, or patch. Default is off. |

___


### CloudFormation Box

**Note:** In contrast with Script Boxes, the CloudFormation boxes do not include the parameter: **events**.

**Endpoint**

/services/boxes

**Schema**

**http://elasticbox.net/schemas/boxes/cloudformation**

**New parameters**

| Parameter | Type | Description |
|---------------|---------|----------------|
| profile | object | Describes all the properties to deploy an instance of a box. Contains the same data as the old deployment profile endpoint. Only accepts AWS information. It is not required by CloudFormation template boxes |
| automatic_updates | string | Required. Specify an option: off, major, minor, or patch. Default is off. |
| provider_id | object | Required. Specifies the ID of an AWS provider. |
| type | object |	Required. Specifies a service. Accepted values are as follows: CloudFormation Service, MySQL Database Service, Microsoft SQL Database Service, Oracle Database Service, PostgreSQL Database Service, Memcached Service, S3 Bucket, Dynamo DB Domain. |
| draft_from | guid | Optional. ID of the box version that this box is a draft from. |
| requirements | array | Required. Contains strings like tags. Specifies the runtime technologies a box requires to deploy. |

___


**Docker Container Box**

**Endpoint**

/services/boxes

**Schema**

**http://elasticbox.net/schemas/boxes/docker**

**New parameters**

| Parameter | Type | Description |
|---------------|---------|----------------|
| dockerfile | object | Optional. Refers to the schema of the blob that contains the dockerfile script. This replaces the Docker box variable previously known as DOCKER_FILE. |
| automatic_updates | string | Required. Specify an option: off, major, minor, or patch. Default is off. |
| draft_from | guid | Optional. ID of the box version that this box is a draft from. |
| requirements | array | Required. Contains strings like tags. Specifies the runtime technologies a box requires to deploy. |

___


### Sample API Calls
* Boxes
* Instances
* Organizations
* Providers
* Deploy instance request
* Instance
* Version
* Boxes

**GET /services/boxes**

This request returns boxes of all types: script, policy, cloudformation, and docker.

**Request**

None.

**Response**

Returns an array of the boxes (cloudformation, docker, script, policy).

```
{
    "description": "Cookbook with a simple recipe",
    "automatic_updates": "off",
    "requirements": [
        "linux"
    ],
    "name": "Chef Cookbook",
    ...
     "schema": "http://elasticbox.net/schemas/boxes/script"
}
},
{
     "automatic_updates": "off",
    "requirements": [],
    "name": "MyCloudFormation",
     ...
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation"
},
{
    "automatic_updates": "off",
    "requirements": [
        "docker"
    ],
    "name": "Docker RabbitMQ",
"dockerfile": {
        "url": "/services/blobs/download/54feda7093abba06c7591422/Dockerfile",
        "upload_date": "2015-03-10 11:50:07.960399",
        "length": 30,
        "content_type": "text/x-shellscript"
    },
    "schema": "http://elasticbox.net/schemas/boxes/docker"
}
```

**PUT /services/boxes/{box_id}/diff**

**Request**

Box schema.

```
{
  "profile": {
      "instances": 1,
      "keypair': 'test_keypair",
      "location': 'SimulatedLocation",
      "image': 'test",
      "flavor': 'test.small",
      "schema': 'http://elasticbox.net/schemas/test/compute/profile"
  },
  "provider_id": "720d78f5-1139-4526-872f-bcddcd20b9b7",
  "automatic_updates": "off",
  "deleted": None,
  "variables": [

  ],
  "name": "MyPolicy",
  "version": {
      "box": "596ea6d6-faeb-46f7-bcd8-bd2b7fc2db15",
      "number": {
          "major": 0,
          "minor": 1,
          "patch": 1
      },
      "workspace": "operations",
      "description": "SmallVMtype"
  },
  "claims": [
      "linux"
  ],
  "draft_from": "54cbac10-44a0-4c4f-8580-f0f66e34d9dd",
  "schema": "http://elasticbox.net/schemas/boxes/policy"
}
```

**Response**

The diff JSON has changed, it now includes the property ‘box_profile_properties’ if using a deployment policy box.

```
{
  "box_variables": {
      "removed": [],
      "files_diff": [],
      "added": [],
      "changed": []
  },
  "box_profile_properties": {
      "title": "Modified Box Profile properties",
      "removed": [],
      "added": [],
      "changed": [
          {
              "new": "test.small",
              "name": "flavor",
              "previous": "test.micro"
          }
      ]
  },
  "box_details": {
      "removed": [],
      "added": [],
      "changed": []
  },
  "box_events": [],
  "changed": true
}
```

___


**Instances**

**GET /services/instances**

**Removed parameter**

environment

**New parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| automatic_updates | string | Required. Specify an option: off, major, minor, or patch. Default is off. |
| box | string | Required. ID of the box (not version) deployed on the instance. |
| policy_box | string | Optional. Is a deployment policy or a CloudFormation box. |

**Request**

None.

**Response**

Array of instance schema.

```
[
    {
        "automatic_updates": "off",
        "box" : "f61a336d-4807-4220-891f-e56ef8c54326",
        "name": "TestBox",
        "policy_box" : {
            "profile" : {
               "image" : "test",
               "instances" : 1,
               "keypair" : "test_keypair",
               "location" : "Simulated Location",
               "flavor" : "test.micro",
               "schema" : "http://elasticbox.net/schemas/test/compute/profile"
            },
            "provider_id" : "26fd7fac-ff2a-4e24-a01d-708bff07fb9a",
            "automatic_updates" : "off",
            ...
            "claims" : [],
            "schema" : "http://elasticbox.net/schemas/boxes/policy"
        },

        "boxes": [
           ...
        ],
      ...
        "operation": "deploy",
    },
...
]
```

**POST /services/instances**

**Removed parameters**

environment, profile, variables

**New parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| automatic_updates | string | Required. Specify an option: off, major, minor, or patch. Default is off. |
| box | object | Required. Contains two parameters: <br> + id: Of type string, is the ID of the script box (not version) to deploy on the instance. <br> + variables: Of type array, are the variables from the script box. |
| policy_box | object | Required. Contains two parameters: <br> + id: Of type string, is the ID of the deployment policy box (not version) to deploy on the instance. <br> + variables: Of type array, are the variables from the deployment policy box. |
| instance_tags | Array | Optional. Custom tags to describe an instance. |
| ipv4_address | string | Optional. IP address of the machine where you want to run the ElasticBox agent to deploy a box. |

**Request**

Contains the schema to deploy an instance.

```
{
  "box": {
      "variables": [

      ],
      "id": "32375764-f73a-41ca-8268-12ac1785586e"
  },
  "automatic_updates": "off",
  "name": "TestBox",
  "policy_box": {
      "variables": [

      ],
      "id": "e109e536-e437-4707-8048-cbf8b09c9307"
  },
  "environment": "TestBox",
  "instance_tags": [

  ],
  "schema": "http://elasticbox.net/schemas/deploy-instance-request"
}
```

**Response**

Returns the schema of the deployed instance.

```
{
  "box": "6c714599-f045-4476-9068-5c34effa618f",
  "policy_box": {
      "profile": {
          "image": "test",
          "instances": 1,
          "keypair": "test_keypair',
          "location": "SimulatedLocation",
          "flavor": 'test.micro",
          "schema": 'http://elasticbox.net/schemas/test/compute/profile'
      },
      'provider_id': 'ffe0da74-c96a-413d-b534-8f112f051043',
      'automatic_updates': 'off',
      'name': 'admin_box-2ec08eb02dDeployPolicy',
      ...
      'claims': [
          'linux'
      ],
      'schema': 'http://elasticbox.net/schemas/boxes/policy'
  },
  'automatic_updates': 'off',
  'name': 'TestBox',
  'boxes': [
      {
   ...
      }
  ],
  'operation': 'deploy',
  'schema': 'http://elasticbox.net/schemas/instance'
}
```

___


**Organizations**

**GET /services/organizations/{organization_name}**

**Removed parameter**

admin_boxes

**Request**

None.

**Response**

Returns the organization schema.

```
{
  "schema": "http://elasticbox.net/schemas/organization",
  "name": "elasticbox",
  "features": {
           "cost_center": false,
           "custom_pricing": false,
           "onboard_checklist": false,
           “provider_sharing": true,
           "reporting": false
  },
  ...
       "webhooks": []
}
```

___


**Providers**

**GET /services/providers**

**Removed parameter**

admin_box

**Request**

None.

**Response**

Returns an array of the provider schema.

```
{
      "state": "ready",
      "services": [
          {
              "name": "Linux Compute"
          }
      ],
      "type": "Test Provider",
      ...
      "name": "report-c04cbc85dc"
}
```

___


### Schema

* Organization
* Provider
* Script Box
* Policy box
* Container Box
* CloudFormation Box

**Organization**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/organization",
    "additionalProperties": false,
    "allOf": [
        {
            "$ref": "http://elasticbox.net/schemas/object-timestamp"
        },
        {
            "type": "object",
            "required": [
                "schema",
                "name",
                "domains",
                "administrators",
                "authentication",
                "features",
                "cost_centers"
            ],
            "properties": {
                "authentication": {
                    "type": "object",
                    "required": [
                        "github",
                        "google",
                        "password",
                        "ldap"
                    ],
                    "default": {
                        "github": true,
                        "google": true,
                        "ldap": false,
                        "ldap_config": {},
                        "password": true
                    },
                    "properties": {
                        "github": {
                            "type": "boolean",
                            "default": true
                        },
                        "google": {
                            "type": "boolean",
                            "default": true
                        },
                        "ldap": {
                            "type": "boolean",
                            "default": false
                        },
                        "ldap_config": {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "sources": {
                                    "type": "array",
                                    "default": [],
                                    "items": {
                                        "type": "object",
                                        "required": [
                                            "host"
                                        ],
                                        "properties": {
                                            "base_dn_filter": {
                                                "type": "string",
                                                "maxLength": 512
                                            },
                                            "email_field": {
                                                "type": "string",
                                                "maxLength": 256
                                            },
                                            "group_dn_filter": {
                                                "type": "string",
                                                "maxLength": 512
                                            },
                                            "groups_dn": {
                                                "type": "string",
                                                "maxLength": 512
                                            },
                                            "host": {
                                                "type": "string",
                                                "maxLength": 256
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        "password": {
                            "type": "boolean",
                            "default": true
                        }
                    }
                },
                "features": {
                    "type": "object",
                    "required": [
                        "provider_sharing",
                        "cost_center",
                        "onboard_checklist",
                        "reporting"
                    ],
                    "default": {
                        "cost_center": false,
                        "custom_pricing": false,
                        "onboard_checklist": false,
                        "provider_sharing": true,
                        "reporting": false
                    },
                    "properties": {
                        "cost_center": {
                            "type": "boolean",
                            "default": false
                        },
                        "custom_pricing": {
                            "type": "boolean",
                            "default": false
                        },
                        "onboard_checklist": {
                            "type": "boolean",
                            "default": false
                        },
                        "provider_sharing": {
                            "type": "boolean",
                            "default": true
                        },
                        "reporting": {
                            "type": "boolean",
                            "default": false
                        }
                    }
                },
                "icon": {
                    "type": "string",
                    "maxLength": 256
                },
                "name": {
                    "type": "string",
                    "maxLength": 256
                },
                "schema": {
                    "type": "string",
                    "enum": [
                        "http://elasticbox.net/schemas/organization"
                    ]
                },
                "theme": {
                    "type": "string",
                    "maxLength": 256
                },
                "administrators": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 64
                    }
                },
                "cost_centers": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "object",
                        "required": [
                            "name",
                            "workspaces",
                            "quotas"
                        ],
                        "additionalProperties": false,
                        "properties": {
                            "name": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 125
                            },
                            "quotas": {
                                "type": "array",
                                "default": [],
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "cost": {
                                            "type": "integer",
                                            "description": "Quota in in decimal of the currency units per month."
                                        },
                                        "provider": {
                                            "$ref": "http://elasticbox.net/schemas/guid"
                                        }
                                    }
                                }
                            },
                            "workspaces": {
                                "type": "array",
                                "default": [],
                                "items": {
                                    "type": "string",
                                    "minLength": 1,
                                    "maxLength": 64
                                }
                            }
                        }
                    }
                },
                "domains": {
                    "type": "array",
                    "default": [],
                    "properties": {
                        "items": {
                            "type": "string",
                            "maxLength": 256
                        }
                    }
                },
                "providers": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "object",
                        "required": [
                            "description",
                            "enabled",
                            "pricing",
                            "type"
                        ],
                        "properties": {
                            "type": {
                                "type": "string",
                                "enum": [
                                    "Amazon Web Services",
                                    "Amazon Web Services GovCloud",
                                    "Cloudstack",
                                    "Google Compute",
                                    "Microsoft Azure",
                                    "Rackspace",
                                    "SoftLayer",
                                    "Openstack",
                                    "Test Provider",
                                    "VMware vCloud Director",
                                    "VMware vSphere"
                                ]
                            },
                            "description": {
                                "type": "string",
                                "maxLenght": 256
                            },
                            "enabled": {
                                "type": "boolean",
                                "default": false
                            },
                            "pricing": {
                                "type": "array",
                                "default": [],
                                "items": {
                                    "type": "object",
                                    "oneOf": [
                                        {
                                            "$ref": "http://elasticbox.net/schemas/gce/compute/pricing"
                                        },
                                        {
                                            "$ref": "http://elasticbox.net/schemas/aws/compute/pricing"
                                        },
                                        {
                                            "$ref": "http://elasticbox.net/schemas/azure/compute/linux/pricing"
                                        },
                                        {
                                            "$ref": "http://elasticbox.net/schemas/azure/compute/windows/pricing"
                                        }
                                    ]
                                }
                            }
                        }
                    }
                },
                "tags": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "object",
                        "required": [
                            "name",
                            "type"
                        ],
                        "additionalProperties": false,
                        "properties": {
                            "type": {
                                "enum": [
                                    "Location",
                                    "Custom",
                                    "Workspace",
                                    "Workspace name",
                                    "Workspace ID",
                                    "Provider",
                                    "Provider name",
                                    "Environment",
                                    "Box",
                                    "Box name",
                                    "User ID",
                                    "Email",
                                    "User email",
                                    "Service Instance ID",
                                    "Service ID",
                                    "Instance ID"
                                ]
                            },
                            "name": {
                                "type": "string",
                                "minLength": 1,
                                "maxLength": 125
                            },
                            "value": {
                                "type": "string",
                                "maxLength": 254
                            }
                        }
                    }
                },
                "webhooks": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 512,
                        "not": {
                            "type": "null"
                        }
                    }
                }
            }
        }
    ]
}
```

___


**Provider**

This schema uses a CloudStack example.

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/gce/provider",
    "type": "object",
    "additionalProperties": false,
    "allOf": [
        {
            "$ref": "http://elasticbox.net/schemas/object-base"
        },
        {
            "$ref": "http://elasticbox.net/schemas/shareable"
        },
        {
            "type": "object",
            "required": [
                "schema",
                "icon",
                "type",
                "email",
                "credentials",
                "project_id",
                "state",
                "services",
                "deleted",
                "organization"
            ],
            "properties": {
                "type": {
                    "type": "string",
                    "default": "Google Compute",
                    "enum": [
                        "Google Compute"
                    ]
                },
                "credentials": {
                    "type": "object",
                    "oneOf": [
                        {
                            "type": "object",
                            "additionalProperties": false,
                            "properties": {
                                "key": {
                                    "type": "string",
                                    "maxLength": 4096
                                }
                            }
                        },
                        {
                            "type": "object",
                            "required": [
                                "refresh_token"
                            ],
                            "additionalProperties": false,
                            "properties": {
                                "access_token": {
                                    "type": "string",
                                    "maxLength": 4096
                                },
                                "refresh_token": {
                                    "type": "string",
                                    "maxLength": 4096
                                }
                            }
                        }
                    ]
                },
                "deleted": {
                    "type": "string",
                    "maxLength": 2048,
                    "default": null
                },
                "email": {
                    "type": "string",
                    "maxLength": 2048
                },
                "icon": {
                    "type": "string",
                    "maxLength": 256,
                    "default": "images/platform/google.png"
                },
                "organization": {
                    "type": "string",
                    "maxLength": 256,
                    "description": "The name of the organization that owns this provider."
                },
                "project_id": {
                    "type": "string",
                    "maxLength": 2048
                },
                "schema": {
                    "type": "string",
                    "enum": [
                        "http://elasticbox.net/schemas/gce/provider"
                    ]
                },
                "state": {
                    "type": "string",
                    "default": "initializing",
                    "enum": [
                        "initializing",
                        "processing",
                        "ready",
                        "deleting",
                        "unavailable"
                    ]
                },
                "services": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "object",
                        "oneOf": [
                            {
                                "$ref": "http://elasticbox.net/schemas/gce/compute/linux"
                            }
                        ]
                    }
                }
            }
        }
    ]
}
```

___


**Script Box**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/boxes/script",
    "type": "object",
    "additionalProperties": false,
    "description": "Schema for a Script box",
    "allOf": [
        {
            "$ref": "http://elasticbox.net/schemas/object-base"
        },
        {
            "$ref": "http://elasticbox.net/schemas/shareable"
        },
        {
            "$ref": "http://elasticbox.net/schemas/versionable"
        },
        {
            "type": "object",
            "required": [
                "automatic_updates",
                "deleted",
                "organization",
                "requirements",
                "schema",
                "visibility"
            ],
            "properties": {
                "automatic_updates": {
                    "type": "string",
                    "default": "off",
                    "enum": [
                        "major",
                        "minor",
                        "patch",
                        "off"
                    ]
                },
                "deleted": {
                    "type": "string",
                    "maxLength": 2048,
                    "default": null
                },
                "events": {
                    "type": "object",
                    "default": {},
                    "properties": {
                        "configure": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "dispose": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "install": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "post_dispose": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "post_stop": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "pre_configure": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "pre_install": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "pre_start": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "start": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        },
                        "stop": {
                            "$ref": "http://elasticbox.net/schemas/file-reference"
                        }
                    }
                },
                "icon": {
                    "type": "string",
                    "maxLength": 256
                },
                "organization": {
                    "type": "string",
                    "maxLength": 256,
                    "description": "The name of the organization that owns this box."
                },
                "requirements": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/name"}
                },
                "schema": {
                    "type": "string",
                    "enum": [
                        "http://elasticbox.net/schemas/boxes/script"
                    ]
                },
                "visibility": {
                    "type": "string",
                    "default": "workspace",
                    "enum": [
                        "public",
                        "workspace",
                        "organization"
                    ]
                },
                "tags": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "$ref": "http://elasticbox.net/schemas/name"
                    }
                },
                "variables": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "$ref": "http://elasticbox.net/schemas/variable"
                    }
                }
            }
        }
    ]
}
```

___


**Policy Box**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/boxes/policy",
    "type": "object",
    "additionalProperties": false,
    "description": "Schema for a Policy box",
    "allOf": [
        {
            "$ref": "http://elasticbox.net/schemas/object-base"
        },
        {
            "$ref": "http://elasticbox.net/schemas/shareable"
        },
        {
            "$ref": "http://elasticbox.net/schemas/versionable"
        },
        {
            "type": "object",
            "required": [
                "automatic_updates",
                "claims",
                "deleted",
                "organization",
                "profile",
                "provider_id",
                "schema",
                "visibility"
            ],
            "properties": {
                "automatic_updates": {
                    "type": "string",
                    "default": "off",
                    "enum": [
                        "major",
                        "minor",
                        "patch",
                        "off"
                    ]
                },
                "deleted": {
                    "type": "string",
                    "maxLength": 2048,
                    "default": null
                },
                "icon": {
                    "type": "string",
                    "maxLength": 256
                },
                "organization": {
                    "type": "string",
                    "maxLength": 256,
                    "description": "The name of the organization that owns this box."
                },
                "profile": {
                    "type": "object",
                    "anyOf": [
                        {"$ref": "http://elasticbox.net/schemas/aws/ec2/profile"},
                        {"$ref": "http://elasticbox.net/schemas/azure/compute/linux/profile"},
                        {"$ref": "http://elasticbox.net/schemas/azure/compute/windows/profile"},
                        {"$ref": "http://elasticbox.net/schemas/cloudstack/compute/profile"},
                        {"$ref": "http://elasticbox.net/schemas/openstack/compute/profile"},
                        {"$ref": "http://elasticbox.net/schemas/vcloud/compute/profile"},
                        {"$ref": "http://elasticbox.net/schemas/vsphere/compute/profile"},
                        {"$ref": "http://elasticbox.net/schemas/gce/compute/profile"},
                        {"$ref": "http://elasticbox.net/schemas/test/compute/profile"},
                        {"$ref": "http://elasticbox.net/schemas/softlayer/compute/profile"},
                        {"$ref": "http://elasticbox.net/schemas/byoi/compute/profile"}
                    ],
                    "description": "The policy to define a new instance or the reference to an existing instance"
                },
                "provider_id": {
                    "$ref": "http://elasticbox.net/schemas/guid",
                    "description": "The provider ID"
                },
                "claims": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/name"}
                },
                "schema": {
                    "type": "string",
                    "enum": [
                        "http://elasticbox.net/schemas/boxes/policy"
                    ]
                },
                "tags": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/name"}
                },
                "variables": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/variable"}
                },
                "visibility": {
                    "type": "string",
                    "default": "workspace",
                    "enum": [
                        "public",
                        "workspace",
                        "organization"
                    ]
                }
            }
        }
    ]
}
```

___


**Container Box**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/boxes/docker",
    "type": "object",
    "additionalProperties": false,
    "description": "Schema for a docker box",
    "allOf": [
        {
            "$ref": "http://elasticbox.net/schemas/object-base"
        },
        {
            "$ref": "http://elasticbox.net/schemas/shareable"
        },
        {
            "$ref": "http://elasticbox.net/schemas/versionable"
        },
        {
            "type": "object",
            "required": [
                "automatic_updates",
                "deleted",
                "organization",
                "requirements",
                "schema",
                "visibility"
            ],
            "properties": {
                "automatic_updates": {
                    "type": "string",
                    "default": "off",
                    "enum": [
                        "major",
                        "minor",
                        "patch",
                        "off"
                    ]
                },
                "deleted": {
                    "type": "string",
                    "maxLength": 2048,
                    "default": null
                },
                "events": {
                    "type": "object",
                    "default": {},
                    "properties": {
                        "configure": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "dispose": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "install": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "post_dispose": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "post_stop": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "pre_configure": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "pre_install": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "pre_start": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "start": {"$ref": "http://elasticbox.net/schemas/file-reference"},
                        "stop": {"$ref": "http://elasticbox.net/schemas/file-reference"}
                    }
                },
                "icon": {
                    "type": "string",
                    "maxLength": 256
                },
                "organization": {
                    "type": "string",
                    "maxLength": 256,
                    "description": "The name of the organization that owns this box."
                },
                "requirements": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/name"}
                },
                "schema": {
                    "type": "string",
                    "enum": ["http://elasticbox.net/schemas/boxes/docker"]
                },
                "variables": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/variable"}
                },
                "visibility": {
                    "type": "string",
                    "default": "workspace",
                    "enum": [
                        "public",
                        "workspace",
                        "organization"
                    ]
                },
                "dockerfile": {
                    "$ref": "http://elasticbox.net/schemas/file-reference"
                }
            }
        }
    ]
}
```

___


**CloudFormation Box**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/boxes/cloudformation",
    "type": "object",
    "additionalProperties": false,
    "description": "Schema for a Cloud Formation box",
    "allOf": [
        {
            "$ref": "http://elasticbox.net/schemas/object-base"
        },
        {
            "$ref": "http://elasticbox.net/schemas/shareable"
        },
        {
            "$ref": "http://elasticbox.net/schemas/versionable"
        },
        {
            "type": "object",
            "required": [
                "automatic_updates",
                "deleted",
                "organization",
                "requirements",
                "schema",
                "visibility",
                "type"
            ],
            "properties": {
                "automatic_updates": {
                    "type": "string",
                    "default": "off",
                    "enum": [
                        "major",
                        "minor",
                        "patch",
                        "off"
                    ]
                },
                "deleted": {
                    "type": "string",
                    "maxLength": 2048,
                    "default": null
                },
                "icon": {
                    "type": "string",
                    "maxLength": 256
                },
                "organization": {
                    "type": "string",
                    "maxLength": 256,
                    "description": "The name of the organization that owns this box."
                },
                "profile": {
                    "type": "object",
                    "anyOf": [
                        {
                            "$ref": "http://elasticbox.net/schemas/aws/cloudformation/profile"
                        },
                        {
                            "$ref": "http://elasticbox.net/schemas/aws/rds/profile"
                        },
                        {
                            "$ref": "http://elasticbox.net/schemas/aws/elasticache/profile"
                        },
                        {
                            "$ref": "http://elasticbox.net/schemas/aws/ddb/profile"
                        },
                        {
                            "$ref": "http://elasticbox.net/schemas/aws/s3/profile"
                        }
                    ]
                },
                "provider_id": {
                    "$ref": "http://elasticbox.net/schemas/guid",
                    "description": "The provider ID"
                },
                "requirements": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/name"}
                },
                "schema": {
                    "type": "string",
                    "enum": ["http://elasticbox.net/schemas/boxes/cloudformation"]
                },
                "tags": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/name"}
                },
                "variables": {
                    "type": "array",
                    "default": [],
                    "items": {"$ref": "http://elasticbox.net/schemas/variable"}
                },
                "visibility": {
                    "type": "string",
                    "default": "workspace",
                    "enum": [
                        "public",
                        "workspace",
                        "organization"
                    ]
                },
                "type": {
                    "type": "string",
                    "default": "CloudFormation Service",
                    "enum": [
                         "CloudFormation Service",
                         "MySQL Database Service",
                         "Microsoft SQL Database Service",
                         "Oracle Database Service",
                         "PostgreSQL Database Service",
                         "Memcached Service",
                         "S3 Bucket",
                         "Dynamo DB Domain"
                    ]
                },
                "template": {
                    "$ref": "http://elasticbox.net/schemas/file-reference"
                }
            }
        }
    ]
}
```

___


**Deploy Instance Request**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/deploy-instance-request",
    "type": "object",
    "required": [
        "automatic_updates",
        "box",
        "name",
        "schema"
    ],
    "additionalProperties": false,
    "description": "Schema for a deployment instance request",
    "properties": {
        "automatic_updates": {
            "type": "string",
            "default": "off",
            "enum": [
                "major",
                "minor",
                "patch",
                "off"
            ]
        },
        "box": {
            "type": "object",
            "required": [
                "id",
                "variables"
            ],
            "additionalProperties": false,
            "properties": {
                "id": {
                    "$ref": "http://elasticbox.net/schemas/guid"
                },
                "variables": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "$ref": "http://elasticbox.net/schemas/variable"
                    }
                }
            }
        },
        "name": {
            "type": "string",
            "minLength": 1,
            "maxLength": 30
        },
        "instance_tags": {
            "type": "array",
            "default": [],
            "items": {"$ref": "http://elasticbox.net/schemas/name"}
        },
        "lease": {
            "type": "object",
            "required": [
                "expire",
                "operation"
            ],
            "additionalProperties": false,
            "properties": {
                "expire": {
                    "type": "string",
                    "maxLength": 2048
                },
                "operation": {
                    "type": "string",
                    "enum": [
                        "shutdown",
                        "terminate"
                    ]
                }
            }
        },
        "owner": {
            "type": "string",
            "minLength": 1,
            "maxLength": 64
        },
        "ipv4_address": {
            "type": "string",
            "maxLength": 15
        },
        "policy_box": {
            "type": "object",
            "required": [
                "id",
                "variables"
            ],
            "additionalProperties": false,
            "properties": {
                "id": {
                    "$ref": "http://elasticbox.net/schemas/guid"
                },
                "variables": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "$ref": "http://elasticbox.net/schemas/variable"
                    }
                }
            }
        },
        "schema": {
            "type": "string",
            "enum": [
                "http://elasticbox.net/schemas/deploy-instance-request"
            ]
        }
    }
}
```

___


**Instance**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas/instance",
    "type": "object",
    "additionalProperties": false,
    "allOf": [
        {
            "$ref": "http://elasticbox.net/schemas/object-timestamp"
        },
        {
            "$ref": "http://elasticbox.net/schemas/shareable"
        },
        {
            "required": [
                "automatic_updates",
                "box",
                "boxes",
                "deleted",
                "id",
                "name",
                "operation",
                "schema",
                "service",
                "state",
                "tags"
            ],
            "properties": {
                "id": {
                    "type": "string",
                    "maxLength": 36
                },
                "automatic_updates": {
                    "type": "string",
                    "default": "off",
                    "enum": [
                      "major",
                      "minor",
                      "patch",
                      "off"
                    ]
                },
                "box": {
                    "$ref": "http://elasticbox.net/schemas/guid"
                },
                "deleted": {
                    "type": "string",
                    "maxLength": 2048,
                    "default": null
                },
                "policy_box": {
                    "type": "object",
                    "anyOf": [
                        {
                            "$ref": "http://elasticbox.net/schemas/boxes/policy"
                        },
                        {
                            "$ref": "http://elasticbox.net/schemas/boxes/cloudformation"
                        }
                    ]
                },
                "icon": {
                    "type": "string",
                    "maxLength": 256
                },
                "lease": {
                    "type": "object",
                    "required": [
                        "expire",
                        "operation",
                        "released"
                    ],
                    "additionalProperties": false,
                    "properties": {
                        "expire": {
                            "type": "string",
                            "maxLength": 2048
                        },
                        "operation": {
                            "type": "string",
                            "enum": [
                                "shutdown",
                                "terminate"
                            ]
                        },
                        "released": {
                            "type": "boolean",
                            "default": false
                        }
                    }
                },
                "name": {
                    "$ref": "http://elasticbox.net/schemas/name"
                },
                "operation": {
                    "type": "string",
                    "enum": [
                        "deploy",
                        "shutdown",
                        "shutdown_service",
                        "poweron",
                        "reinstall",
                        "reconfigure",
                        "terminate",
                        "terminate_service",
                        "snapshot"
                    ]
                },
                "schema": {
                    "type": "string",
                    "enum": [
                        "http://elasticbox.net/schemas/instance"
                    ]
                },
                "service": {
                    "type": "object",
                    "required": [
                        "id",
                        "machines"
                    ],
                    "additionalProperties": false,
                    "properties": {
                        "id": {
                            "type": "string",
                            "maxLength": 30
                        },
                        "type": {
                            "$ref": "http://elasticbox.net/schemas/service-type"
                        },
                        "machines": {
                            "type": "array",
                            "default": [],
                            "items": {
                                "$ref": "#/definitions/instance-machine"
                            }
                        }
                    }
                },
                "state": {
                    "type": "string",
                    "enum": [
                        "processing",
                        "done",
                        "unavailable"
                    ]
                },
                "boxes": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "$ref": "http://elasticbox.net/schemas/box"
                    }
                },
                "tags": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "$ref": "http://elasticbox.net/schemas/name"
                    }
                },
                "variables": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "$ref": "http://elasticbox.net/schemas/variable"
                    }
                }
            }
        }
    ],
    "definitions": {
        "instance-machine": {
            "type": "object",
            "required": [
                "name",
                "state",
                "workflow"
            ],
            "additionalProperties": false,
            "properties": {
                "name": {
                    "$ref": "http://elasticbox.net/schemas/name"
                },
                "state": {
                    "type": "string",
                    "enum": [
                        "processing",
                        "done",
                        "unavailable"
                    ]
                },
                "workflow": {
                    "type": "array",
                    "default": [],
                    "items": {
                        "type": "object",
                        "required": [
                            "event"
                        ],
                        "additionalProperties": false,
                        "properties": {
                            "box": {
                                "type": "string",
                                "pattern": "^[a-zA-Z0-9_\\.]*$"
                            },
                            "event": {
                                "type": "string",
                                "maxLength": 256
                            },
                            "script": {
                                "type": "string",
                                "maxLength": 512
                            }
                        }
                    }
                }
            }
        }
    }
}
```

___


**Version**

```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "id": "http://elasticbox.net/schemas//versionable",
    "type": "object",
    "properties": {
      "draft_from": {
        "$ref": "http://elasticbox.net/schemas/guid"
    },
        "version": {
            "type": "object",
            "required": [
                "box",
                "description",
                "number"
            ],
            "properties": {
                "box": {
                    "$ref": "http://elasticbox.net/schemas/guid"
                },
                "description": {
                    "type": "string",
                    "maxLength": 2048
                },
                "number": {
                    "type": "object",
                    "required": [
                        "major",
                        "minor",
                        "patch"
                    ],
                    "properties": {
                        "major": {
                            "type": "integer",
                            "minimum": 0
                        },
                        "minor": {
                            "type": "integer",
                            "minimum": 0
                        },
                        "patch": {
                            "type": "integer",
                            "minimum": 0
                        }
                    }
                },
                "workspace": {
                    "type": "string",
                    "maxLength": 64
                }
            }
        }
    }
}
```
