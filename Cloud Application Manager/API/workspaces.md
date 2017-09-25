{{{
"title": "Workspaces API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false,
"sticky": true
}}}

Manage and perform actions on workspaces.

**Create or List Workspaces**

| Resource |Description |
|----------|------------|
| GET /services/workspaces | Gets the list of workspaces. |
| POST /services/workspace | Creates a new team workspace.   |


**Perform Other Workspace Operations**

| Parameter | Description |
|-----------|-------------|
| GET /services/workspaces/{workspace_id} | Fetches an existing workspace.|
| PUT /services/workspaces/{workspace_id}| Updates an existing workspace.|
| DELETE /services/workspaces/{workspace_id}| Deletes an existing workspace.|
| GET /services/workspaces/{workspace_id}/providers | Gets the cloud providers registered in a workspace. |
| GET /services/workspaces/{workspace_id}/boxes | Gets the boxes in a workspace. |
| GET /services/workspaces/{workspace_id}/instances | Gets the instances in a workspace. |

### GET /services/workspaces

Gets a list of all accessible workspaces. There are two types of workspaces: personal workspaces for a single user and team workspaces that can have many members and organizations.

**Normal Response Codes**

* 200

**Error Response Codes**

* Bad Request (400)

**Request**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| organizations | array | Lists of organizations of the workspace. |
| updated | string | Date of the last update. Example “2015-07-02 10:23:47.748740” |
| name | string | Workspace name. |
| created | string | Creation date. Example “2015-07-02 10:23:47.748740” |
| uri | string | Workspace uri. |
| members | array | Lists members of a team workspace. |
| group_dns | array | List of fully qualified names of LDAP groups to which a user’s personal workspace belongs. You can’t update this field. Present in Personal Workspaces |
| ldap_groups | array | List of fully qualified names of LDAP groups that are members of a workspace. Present in Team Workspaces |
| id | string | Workspace unique identifier. |
| add_provider | xsd:boolean | Indicates true if a personal workspace has a provider. |
| deploy_instance | xsd:boolean | Shows true when there are deployed instances in the personal workspace. |
| email | string | User email, this parameter is used only in personal workspaces. |
| owner | string | Refers to the username that owns the workspace. Present in Team Workspaces |
| icon | string | Workspace icon. |
| schema | string | Schema URI. Either “http://elasticbox.net/schemas/workspaces/personal” or “http://elasticbox.net/schemas/workspaces/team” |

**Response Body**

```
[
   {
      "organizations":[
         "public"
      ],
      "updated":"2014-08-11 23:01:13.703971",
      "name":"brand new workspace",
      "created":"2014-08-11 23:01:13.703971",
      "uri":"/services/workspaces/brand",
      "members":[
                {
                        "role": "collaborator",
                        "workspace": "david"
                },
                {
                        "role": "collaborator",
                    "workspace": "oscar"
                }
      ],
      "owner":"owner_name",
      "id":"brand",
      "schema":"http://elasticbox.net/schemas/workspaces/team"
   },
   {
      "updated":"2014-10-10 17:53:06.342558",
      "take_tour":true,
      "name":"owner_name",
      "icon":"/services/blobs/download/54381cfe17268876881a7b57/headshot.png",
      "created":"2014-03-20 16:32:03.077480",
      "uri":"/services/workspaces/username",
      "email":"username@host.com",
      "add_provider":true,
      "organization":"public",
      "deploy_instance":true,
      "id":"username",
      "schema":"http://elasticbox.net/schemas/workspaces/personal"
   }
]
```

### POST /services/workspaces

Creates a new team workspace and gets the created workspace.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Invalid Data (400)
* Conflict (409)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

| Parameter | Type |Description |
|-----------|------|------------|
| owner | string | User that owns the workspace. |
| schema | string | Workspace schema. Always “http://elasticbox.net/schemas/workspaces/team” |
| organizations | array | List of organizations with access to the workspace. |
| name | string | Workspace name. |
| icon | string | Workspace icon. |
| members | array | List of users with access to the workspace. The role is always collaborator. See example request for more details. |
| ldap_groups | array | List of fully qualified names of LDAP groups that are members of a team workspace. |

**Request Body**

```
{
"schema": "http://elasticbox.net/schemas/workspaces/team",
"name": "Project Elastic",
"members": [
        {
                "role": "collaborator",
                "workspace": "david"
        }
],
"owner": "operations"
}
```

| Parameter | Type |Description |
|-----------|------|------------|
| organizations | array | List of organizations with access to the workspace. |
| updated | string | Date of the last update. |
| name | string | Workspace name. |
| created | string | Creation date. |
| uri | string | Workspace uri. It is: “http://elasticbox.net/schemas/workspaces/team” |
| members | array | List of users with access to the workspace. |
| ldap_groups | array | List of fully qualified names of LDAP groups that are members of a team workspace. |
| owner | string | User that owns the workspace. |
| icon | string | Workspace icon uri. |
| id | string | List of users with access to the workspace. |
| schema | string | Workspace schema uri. |

**Response Body**

```
{
  "organizations": [
    "public"
  ],
  "updated": "2015-07-02 14:38:42.107981",
  "name": "Project Elastic",
  "created": "2015-07-02 14:38:42.107981",
  "deleted": null,
  "uri": "/services/workspaces/project",
  "ldap_groups": [],
  "members": [
    {
      "role": "collaborator",
      "workspace": "david"
    }
  ],
  "owner": "operations",
  "id": "project",
  "schema": "http://elasticbox.net/schemas/workspaces/team"
}
```

### GET /services/workspaces/{workspace_id}

Fetches an existing workspace for the specified workspace ID.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Not Found (404)
* Conflict (409)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

| Parameter | Type |Description |
|-----------|------|------------|
| organizations | array | Lists team workspaces for the account. |
| updated | string | Date of the last update. |
| name | string | Workspace name. |
| created | string | Creation date. |
| uri | string | Workspace uri. |
| members | array | Lists members of a team workspace. |
| group_dns | array | List of fully qualified names of LDAP groups to which a user’s personal workspace belongs. You can’t update this field. |
| ldap_groups | array | List of fully qualified names of LDAP groups that are members of a team workspace.
| id | string | Workspace unique identifier. |
| add_provider | xsd:boolean | Shows true if a personal workspace has a provider. |
| deploy_instance | xsd:boolean | Shows true when there are deployed instances in the personal workspace. |
| email | string | Shows the email of the user that owns the personal workspace. |
| owner | string | Is the owner of a team workspace. |
| schema | string | Schema uri. |

**Response Body**
```
{
  "organizations": [
    "public
  ],
  "updated": "2015-07-02 14:38:42.107981",
  "name": "Project Elastic",
  "created": "2015-07-02 14:38:42.107981",
  "deleted": null,
  "uri": "/services/workspaces/project",
  "id": "project",
  "members": [
    {
      "role": "collaborator",
      "workspace": "david"
    }
  ],
  "owner": "operations",
  "ldap_groups": [],
  "schema": "http://elasticbox.net/schemas/workspaces/team"
}
```

### PUT /services/workspaces/{workspace_id}

Updates an existing workspace, requires the specified id workspace_id.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Invalid Data (400)
* Forbidden (403)
* Not Found (404)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| organizations | array | List of organizations with access to the workspace. |
| updated | string | Date of the last update. |
| name | string | Workspace name. |
| created | string | Creation date. |
| uri | string | Workspace uri. |
| members | array | List of users with access to the workspace. |
| group_dns | array | List of fully qualified names of LDAP groups to which a user’s personal workspace belongs. You can’t update this field. |
| ldap_groups | array | List of fully qualified names of LDAP groups that are members of a team workspace. |
| owner | string | User that owns the workspace. |
| icon | string | Workspace icon uri. |
| id | string | List of users with access to the workspace. |
| schema | string | Workspace schema uri. |

**Request Body**

```
{
   "organizations":[
       "public"
   ],
   "updated":"2014-03-20 21:58:36.109138",
   "name":"--workspace name--",
   "created":"2014-03-20 21:58:36.109138",
   "uri":"/services/workspaces/--workspace name--",
   "members":[
                {
                        "role": "collaborator",
                        "workspace": "david"
                },
                {
                        "role": "collaborator",
                        "workspace": "oscar"
                }
   ],
   "owner":"--owner name--",
   "icon":"--url icon--",
   "id":"--id--",
   "schema":"http://elasticbox.net/schemas/workspaces/team"
}
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| organizations | array | List of organizations with access to the workspace. |
| updated	 | string | Date of the last update. |
| name | string | Workspace name. |
| created | string | Creation date. |
| uri | string | Workspace uri. |
| members | array | List of users with access to the workspace. |
| group_dns | array | List of fully qualified names of LDAP groups to which a user’s personal workspace belongs. You can’t update this field. |
| ldap_groups | array | List of fully qualified names of LDAP groups that are members of a team workspace. |
| owner | string | User that owns the workspace. |
| icon | string | Workspace icon uri. |
| id | string | List of users with access to the workspace. |
| schema | string | Workspace schema uri. |

**Response Body**

```
{
  "organizations": [
    "public"
  ],
  "updated": "2015-07-02 14:48:33.527673",
  "name": "Project Elastic",
  "created": "2015-07-02 14:38:42.107981",
  "deleted": null,
  "uri": "/services/workspaces/project",
  "members": [
    {
      "role": "collaborator",
      "workspace": "david"
    },
    {
      "role": "collaborator",
      "workspace": "operations"
    }
  ],
  "owner": "--owner name--",
  "id":"--id--",
  "icon":"--url icon--",
  "ldap_groups": [],
  "schema": "http://elasticbox.net/schemas/workspaces/team"
}
```

### DELETE /services/workspaces/{workspace_id}

Deletes an existing workspace, requires the specified id workspace_id.

**Normal Response Codes**

* 204

**Common Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

### GET /services/workspaces/{workspace_id}/providers

Gets a list of workspace providers, requires the specified id workspace_id.There are two types of providers: Amazon Web Services and VMware vShpere.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Bad Request (400)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| updated | string | Date of the last update. |
| description | string | Provider description. |
| created | string | Creation date. |
| uri | string | Provider uri. |
| name | string | Provider name. |
| state | string | Provider state, there are five possible states: initializing, processing, ready, deleting or unavailable. |
| members | array | List of members with access to the provider. |
| owner | string | Provider owner. |
| type | string | Provider type. Check the Provider page in the API for more info. |
| id | string | Provider unique identificator. |
| icon | string | Provider Icon uri. |

```

   {
      "updated":"2014-03-21 17:27:18.731525",
      "description":"Manage EC2, ECS and Cloudformation instances",
      "created":"2014-03-21 17:27:06.848858",
      "uri":"--Provider uri--",
      "name":"Amazon",
      "services":[
         {
            "name":"Linux Compute"
         },
         {
            "name":"Windows Compute"
         }
      ],
      "state":"ready",
      "members":[
                 {
                    "role": "collaborator",
                    "workspace": "david"
                  },
                  {
                    "role": "collaborator",
                    "workspace": "operations"
                  }
      ],
      "owner":"workspace1",
      "type":"Amazon Web Services",
      "id":"--Provider id--",
      "icon":"images/platform/aws.png"
   }
]
```

### GET /services/workspaces/{workspace_id}/boxes

Gets a list of workspace boxes, requires the specified id workspace_id.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Bad Request (400)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| organizations | array | List of organizations with access to the box. |
| updated | string | Date of the last update. |
| description | string | Box description. |
| tags | array | Box tags. |
| variables | array | List of box variables, each variable object contains the parameters: type, name and value. |
| created | string | Creation date. |
| uri | string | Box uri. |
| id | array | Box unique identificator. |
| schema | string | Box schema uri. |
| members | array | List of Box members. |
| group_dns | array | List of fully qualified names of LDAP groups to which a user’s personal workspace belongs. You can’t update this field. |
| ldap_groups | array | List of fully qualified names of LDAP groups that are members of a team workspace. |
| owner | string | Box owner. |
| icon | string | Box icon uri. |
| events | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | object | Event contained in one of the event lists, each event object contains the parameters: url, upload_date, length and destination_path. |
| name | string | Box name. |

**Response Body**

```
[
   {
      "organization": "public",
      "updated":"2014-03-08 00:01:57.792623",
      "description":"Cookbook with a simple recipe",
      "service":"Linux Compute",
      "tags":[
         "Chef"
      ],
      "variables":[
         {
            "type":"Text",
            "name":"CHEF_COOKBOOK_NAME",
            "value":"elasticbox"
         },
         {
            "type":"File",
            "name":"CHEF_DEFAULT_RB",
            "value":"/services/blobs/download/52fe31c349bbcc830f342f7f/default.rb"
         },
         {
            "scope":"chef_solo",
            "type":"File",
            "name":"CHEF_METADATA_RB",
            "value":"/services/blobs/download/52fe31c449bbcc830f342f81/metadata.rb"
         },
         {
            "scope":"chef_solo",
            "type":"File",
            "name":"CHEF_SOLO_JSON",
            "value":"/services/blobs/download/52fe31c549bbcc830f342f83/solo.json"
         },
         {
            "type":"Box",
            "name":"chef_solo",
            "value":"05b76b08-5238-4e05-ae5f-8ea8afe00378"
         }
      ],
      "created":"2014-02-14 15:10:36.368716",
      "uri":"/services/boxes/c149114d-8298-4c36-be8a-1fb02e6ec975",
      "id":"c149114d-8298-4c36-be8a-1fb02e6ec975",
      "schema":"http://elasticbox.net/schemas/box",
      "members":[
         "member1","member2"
      ],
      "owner":"public",
      "bindings":[
         {
            "box":"05b76b08-5238-4e05-ae5f-8ea8afe00378",
            "name":"chef_solo"
         },
         {
            "box":"b9abd0d9-0e9c-4c2c-928a-2896e35d854d",
            "name":"git_repository"
         }
      ],
      "icon":"images/platform/chef-cookbook.png",
      "events":{
         "pre_install":{
            "url":"/services/blobs/download/52fe31c249bbcc830f342f7d/pre_install",
            "upload_date":"2014-02-14 15:09:55.095819",
            "length":262,
            "destination_path":"scripts"
         }
      },
      "name":"Chef Cookbook"
   },
   {
      "organization": "public",
      "updated":"2014-03-08 00:01:57.844612",
      "description":"Opscode Chef client",
      "service":"Linux Compute",
      "tags":[
         "Chef",
         "Ruby"
      ],
      "variables":[
         {
            "type":"File",
            "name":"CHEF_SOLO_JSON",
            "value":"/services/blobs/download/52fe31c849bbcc830f342f89/solo.json"
         },
         {
            "type":"File",
            "name":"CHEF_SOLO_RB",
            "value":"/services/blobs/download/52fe31c949bbcc830f342f8b/solo.rb"
         },
         {
            "type":"File",
            "name":"CHEF_METADATA_RB",
            "value":"/services/blobs/download/52fe31ca49bbcc830f342f8d/metadata.rb"
         },
         {
            "type":"File",
            "name":"BERKSFILE",
            "value":"/services/blobs/download/52fe31cc49bbcc830f342f8f/Berksfile"
         },
         {
            "type":"Box",
            "name":"Ruby",
            "value":"a27e3cdf-4d32-4972-aec1-32ebc4e37e1b"
         }
      ],
      "created":"2014-02-14 15:10:36.368716",
      "uri":"/services/boxes/05b76b08-5238-4e05-ae5f-8ea8afe00378",
      "id":"05b76b08-5238-4e05-ae5f-8ea8afe00378",
      "schema":"http://elasticbox.net/schemas/box",
      "members":[
                 "member1","member2"
      ],
      "owner":"public",
      "bindings":[
         {
            "box":"05b76b08-5238-4e05-ae5f-8ea8afe00378",
            "name":"chef_solo"
         },
         {
            "box":"b9abd0d9-0e9c-4c2c-928a-2896e35d854d",
            "name":"git_repository"
         }
      ],
      "icon":"images/platform/chef.png",
      "events":{
         "configure":{
            "url":"/services/blobs/download/52fe31c749bbcc830f342f87/configure",
            "upload_date":"2014-02-14 15:10:00.517413",
            "length":251,
            "destination_path":"scripts"
         },
         "pre_install":{
            "url":"/services/blobs/download/52fe31c649bbcc830f342f85/pre_install",
            "upload_date":"2014-02-14 15:09:59.289119",
            "length":378,
            "destination_path":"scripts"
         }
      },
      "name":"Chef Solo"
   }
]
```

### GET /services/workspaces/{workspace_id}/instances

Gets a list of workspace instances, requires the specified id workspace_id.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Bad Request (400)

**Request Headers**

```
Headers:

        Content-Type: application/json
        Elasticbox-Token: your_authentication_token
        ElasticBox-Release: 4.0
```

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| (optional) service | string | Unique identifier of a deployed service, allows to filter instance by service type. |

**Response Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| updated | string | Date of the last update. |
| operation | string | Last operation, there are seven types of operations: deploy, shutdown, poweron, reinstall, reconfigure, terminate and terminate_service. |
| name | string | Instance name. |
| service | Object | Instance service. |
| service.type | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| service.id | string | Service type. |
| service.machines | array | List of service machines. |
| machine | object | Machine contained in the service machines list. |
| machine.state | string | Machine state, there are three possible states: processing, done and unavailable. |
| machine.name | string | Machine name. |
| machine.workflow | List | List of workflow actions, each workflow action object contains three parameters: box, event and script. |
| workflow.box | string | Workflow action box. |
| workflow.event | string | Workflow action event. |
| workflow.script | string | Workflow action script uri. |
| tags | array | Instance tags. |
| boxes | array | List of boxes where each box object contains a service parameter. The service parameter can have one of these values: Linux Compute, Windows Compute and CloudFormation Service. |
| uri | string | Instance uri. |
| environment | string | Environment name. |
| state | string | Instance state, there are three possible states: processing, done and unavailable. |
| bindings | array | List of instance bindings. |
| binding | object | Binding contained in the bindings list, each binding object contains the parameters: instance and name. |
| id | array | Instance unique identifier. |
| icon | string | Instance icon uri. |
| schema | string | Instance schema uri. |

**Response Body**

```

   {
      "updated":"2014-03-23 16:12:25.219301",
      "operation":"poweron",
      "name":"PHP",
      "service":{
         "type":"Linux Compute",
         "id":"--service id--",
         "machines":[
            {
               "state":"done",
               "name":"--machine name--",
               "workflow":[

               ]
            }
         ]
      },
      "tags":[
         "Git",
         "Puppet",
         "GitHub",
         "environmentapache",
         "Web Framework"
      ],
      "boxes":[
         {
            "service":"Linux Compute"
         },
         {
            "service":"Linux Compute"
         },
         {
            "service":"Linux Compute"
         },
         {
            "service":"Linux Compute"
         }
      ],
      "uri":"/services/instances/i-rf79pl",
      "environment":"environmentapache",
      "state":"done",
      "id":"i-rf79pl",
      "icon":"images/platform/php.png"
   },
   {
      "updated":"2014-03-21 18:22:47.054005",
      "operation":"deploy",
      "name":"Wordpress",
      "service":{
         "type":"Linux Compute",
         "id":"--service id--",
         "machines":[
            {
               "state":"processing",
               "name":"--machine name--",
               "workflow":[
                  {
                     "box":"chef_cookbook.chef_solo.Ruby",
                     "event":"install",
                     "script":"/services/blobs/download/52fe31e649bbcc830f342fc1/install"
                  },
                  {
                     "box":"chef_cookbook.chef_solo",
                     "event":"pre_install",
                     "script":"/services/blobs/download/52fe31c649bbcc830f342f85/pre_install"
                  },
                  {
                     "box":"chef_cookbook",
                     "event":"pre_install",
                     "script":"/services/blobs/download/52fe31c249bbcc830f342f7d/pre_install"
                  },
                  {
                     "box":"chef_cookbook.chef_solo",
                     "event":"configure",
                     "script":"/services/blobs/download/52fe31c749bbcc830f342f87/configure"
                  }
               ]
            }
         ]
      },
      "tags":[
         "environment",
         "Chef",
         "Featured",
         "CMS",
         "Ruby"
      ],
      "boxes":[
         {
            "service":"Linux Compute"
         },
         {
            "service":"Linux Compute"
         },
         {
            "service":"Linux Compute"
         },
         {
            "service":"Linux Compute"
         }
      ],
      "uri":"--instance uri--",
      "environment":"environment",
      "state":"processing",
      "id":"--instance id--",
      "icon":"images/platform/wordpress.png"
   }
]
```

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
