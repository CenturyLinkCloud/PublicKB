{{{
"title": "Instances API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

Manage and perform actions on instances.

**Create or List Instances**

| Resource | Description |
|----------|-------------|
| GET /services/instances | Gets the list of instances. |
| POST /services/instances | Creates a new instance, imports an unregistered instance or instances based on schema. |


**Perform Instance Operations**

| Resource | Description |
|----------|-------------|
| GET /services/instances/{instance_id}| Fetches an existing instance.|
| PUT /services/instances/{instance_id} | Updates an existing instance. |
| DELETE /services/instances/{instance_id} | Terminates, force-terminates, or deletes an existing instance.|
| GET /services/instances/{instance_id}/service | Gets the instance service. |
| GET /services/instances/{instance_id}/activity | Gets all activity logs from the executed operations of an instance. |
| GET /services/instances/{instance_id}/machine_logs | Gets the logs of all machines of a deployed instance. |
| GET /services/instances/{instance_id}/binding_instances | Gets the binding of a instance. |
| GET /services/instances/{instance_id}/operations | Gets all operations of an instance. |
| PUT /services/instances/{instance_id}/deploy | Re-deploy an existing instance. |
| PUT /services/instances/{instance_id}/poweron | Power-on an existing instance. |
| PUT /services/instances/{instance_id}/shutdown | 	Shutdown an existing instance. |
| PUT /services/instances/{instance_id}/reinstall | Re-install an existing instance. |
| PUT /services/instances/{instance_id}/reconfigure | Re-configure an existing instance. |
| PUT /services/instances/{instance_id}/import | Retry to import an unregistered instance. |
| PUT /services/instances/{instance_id}/cancel_import | Cancel a failed import of an unregistered instance. |


### GET /services/instances

Gets instances that are accessible in the personal workspace of the authenticated user.

**Normal Response Codes**

* 200

**Error Response Codes**

* Bad Request (400)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
|created | string | Creation date. |
| updated |  string | Date of the last update. |
| members | array | List of members whom you shared the instance. |
| owner | string | Instance owner. |
| operation | string | Last operation, there are seven types of operations: deploy , shutdown , poweron , reinstall , reconfigure , terminate and terminate_service |
| name | string | Instance name. |
| service | object | Instance service. |
| service.type | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| service.id | string | Service unique identifier. |
| service.machines | array | List of service machines |
| machine | object | Machine contained in the service machines list. |
| machine.state | string | Machine state, there are three possible states: processing , done and unavailable. |
| machine.name | string | Machine name. |
| machine.workflow | array | List of workflow actions, where each workflow action object contains three parameters: box, event, and script. |
| workflow.box | string | Workflow action box. |
| workflow.event | string | Workflow action event. |
| workflow.script | string | Workflow action script uri. |
| tags | array | Instance tags. |
| boxes | array | List of boxes where each box object contains a service parameter. The service parameter can have one of these values: Linux Compute, Windows Compute and CloudFormation Service. |
| uri |  string | Instance uri. |
| state | string | Instance state, there are three possible states: processing , done and unavailable |
| bindings | array | List of instance bindings. |
| binding | object | Binding contained in the bindings list, each binding object contains the parameters: instance and name. |
| id | array | Instance unique identifier |
| icon | string | Instance icon uri. |
| schema | string | Instance schema uri. |

```
[{
   "box": "691df09c-7588-4310-9e9a-a7993f3670b0",
   "updated": "2015-10-27 16:17:42.237233",
   "automatic_updates": "off",
   "name": "TestVSphere",
   "service": {
       "type": "Linux Compute",
       "id": "eb-ay43t",
       "machines": [
           {
               "state": "done",
               "name": "eb-ay43t-1",
               "workflow": []
           }
       ]
   },
   "tags": [],
   "policy_box": {
       "profile": {
           "resource_pool": "pullrequest",
           "datacenter": "ElasticBox - Development",
           "network": "Cluster Network",
           "disks": [
               {
                   "datastore": "Development Storage",
                   "name": "Hard disk 1",
                   "template": true,
                   "size": 97
               }
           ],
           "customization_spec": "None",
           "network_mor": "network-15",
           "instances": 1,
           "template": "debian-7-8-x86-64",
           "datastore": "Development Storage",
           "flavor": "Tiny",
           "schema": "http://elasticbox.net/schemas/vsphere/compute/profile"
       },
       "provider_id": "cac26e4c-16f8-46ad-83ae-52a2b1ba4fca",
       "automatic_updates": "off",
       "name": "TestVSphere",
       "created": "2015-10-09 08:25:02.378295",
       "deleted": null,
       "variables": [],
       "updated": "2015-10-09 08:25:02.378295",
       "lifespan": {
           "operation": "none"
       },
       "visibility": "workspace",
       "members": [],
       "organization": "elasticbox",
       "owner": "operations",
       "claims": [
           "linux"
       ],
       "id": "691df09c-7588-4310-9e9a-a7993f3670b0",
       "schema": "http://elasticbox.net/schemas/boxes/policy"
   },
   "created": "2015-10-09 08:25:36.025086",
   "uri": "/services/instances/i-6bdwwm",
   "id": "i-6bdwwm",
   "state": "done",
   "boxes": [
       {
           "profile": {
               "resource_pool": "pullrequest",
               "datacenter": "ElasticBox - Development",
               "network": "Cluster Network",
               "disks": [
                   {
                       "datastore": "Development Storage",
                       "name": "Hard disk 1",
                       "template": true,
                       "size": 97
                   }
               ],
               "customization_spec": "None",
               "network_mor": "network-15",
               "instances": 1,
               "template": "debian-7-8-x86-64",
               "datastore": "Development Storage",
               "flavor": "Tiny",
               "schema": "http://elasticbox.net/schemas/vsphere/compute/profile"
           },
           "provider_id": "cac26e4c-16f8-46ad-83ae-52a2b1ba4fca",
           "automatic_updates": "off",
           "name": "TestVSphere",
           "created": "2015-10-09 08:25:02.378295",
           "deleted": null,
           "variables": [],
           "updated": "2015-10-09 08:25:02.378295",
           "lifespan": {
               "operation": "none"
           },
           "visibility": "workspace",
           "members": [],
           "organization": "elasticbox",
           "owner": "operations",
           "claims": [
               "linux"
           ],
           "id": "691df09c-7588-4310-9e9a-a7993f3670b0",
           "schema": "http://elasticbox.net/schemas/boxes/policy"
       }
   ],
   "members": [],
   "owner": "operations",
   "icon": null,
   "operation": {
       "event": "terminate_service",
       "workspace": "operations",
       "created": "2015-10-27 16:17:36.268988"
   },
   "variables": [],
   "schema": "http://elasticbox.net/schemas/instance"
},
{
   "box": "15b5bc28-5ac5-4897-bd72-d4f2101da47a",
   "updated": "2015-10-09 10:00:07.434386",
   "automatic_updates": "off",
   "name": "Test2",
   "service": {
       "type": "Linux Compute",
       "id": "eb-l8gqr",
       "machines": []
   },
   "tags": [],
   "policy_box": {
       "profile": {
           "resource_pool": "pullrequest",
           "datacenter": "ElasticBox - Development",
           "network": "Cluster Network",
           "disks": [],
           "customization_spec": "None",
           "compute_resource": null,
           "instances": 1,
           "network_mor": "network-15",
           "template": "ebx-no-disks",
           "folder": "Templates",
           "flavor": "Tiny",
           "datastore": "Development Storage",
           "schema": "http://elasticbox.net/schemas/vsphere/compute/profile"
       },
       "provider_id": "cac26e4c-16f8-46ad-83ae-52a2b1ba4fca",
       "automatic_updates": "off",
       "name": "Test2",
       "created": "2015-10-09 08:30:52.736712",
       "deleted": null,
       "variables": [],
       "updated": "2015-10-09 08:31:10.338900",
       "lifespan": {
           "operation": "none"
       },
       "visibility": "workspace",
       "members": [],
       "claims": [
           "linux"
       ],
       "owner": "operations",
       "organization": "elasticbox",
       "id": "15b5bc28-5ac5-4897-bd72-d4f2101da47a",
       "schema": "http://elasticbox.net/schemas/boxes/policy"
   },
   "created": "2015-10-09 08:31:16.536012",
   "uri": "/services/instances/i-jt8p5d",
   "id": "i-jt8p5d",
   "state": "done",
   "boxes": [
       {
           "profile": {
               "resource_pool": "pullrequest",
               "datacenter": "ElasticBox - Development",
               "network": "Cluster Network",
               "disks": [],
               "customization_spec": "None",
               "compute_resource": null,
               "instances": 1,
               "network_mor": "network-15",
               "template": "ebx-no-disks",
               "folder": "Templates",
               "flavor": "Tiny",
               "datastore": "Development Storage",
               "schema": "http://elasticbox.net/schemas/vsphere/compute/profile"
           },
           "provider_id": "cac26e4c-16f8-46ad-83ae-52a2b1ba4fca",
           "automatic_updates": "off",
           "name": "Test2",
           "created": "2015-10-09 08:30:52.736712",
           "deleted": null,
           "variables": [],
           "updated": "2015-10-09 08:31:10.338900",
           "lifespan": {
               "operation": "none"
           },
           "visibility": "workspace",
           "members": [],
           "claims": [
               "linux"
           ],
           "owner": "operations",
           "organization": "elasticbox",
           "id": "15b5bc28-5ac5-4897-bd72-d4f2101da47a",
           "schema": "http://elasticbox.net/schemas/boxes/policy"
       }
   ],
   "members": [],
   "owner": "operations",
   "icon": null,
   "operation": {
       "event": "terminate_service",
       "workspace": "operations",
       "created": "2015-10-09 09:59:37.618930"
   },
   "variables": [],
   "schema": "http://elasticbox.net/schemas/instance"
}]
  ```

### POST /services/instances
Creates a new instance and gets the created instance.

**Normal Response Codes**

* 202

**Error Response Codes**

* Invalid Data (400)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| schema | string | Required. Instance schema URI. |
| owner | string | ID of the workspace where the instance is posted. |
| box | Object | Box object with its id and a list of overridden variable objects at deployment time |
| policy_box | Object | Box object with its id and a list of overridden variable objects at deployment time |
| automatic_updates | string | One of the: major, minor, patch, off. Default off. |
| lease | array | Schedules an instance with two parameters:<li>expire. Specifies in UTC format YYYY-MM-DD HH:MM:SS.SSSSSS, the time and date for stopping an instance. It’s required only when an instance is set to terminate or shut down.</li><li>operation. Specifies an instance to stop with **shutdown** or **terminate**. When not scheduled, the instance is set to **alwayson**.</li> |
| name | string | Instance name. |
| instance_tags | array | List of tags defined at deployment time. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body: notice that the request schedules the instance to shut down in five hours.
{
   "schema": "http://elasticbox.net/schemas/deploy-instance-request",
   "owner": "operations",
   "name": "ScriptBoxSample",
   "box": {
       "id": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
       "variables": [{
           "name": "variable_name",
           "type": "Text",
           "value": "overridden variable value at deployment time",
           "required": true,
           "visibility": "public"
       }]
   },
   "instance_tags": [

   ],
   "automatic_updates": "off",
   "policy_box": {
       "id": "e57466ee-7094-4bd4-9121-a6df4395d493",
       "variables": [

       ]
    },
   "lease": {
       "expire": "2014-11-17 23:00:00.000000",
       "operation": "shutdown"
   }
}
```

### POST /services/instances
Register an unregistered instance: notice that it's the same endpoint to create a new instance.

**Normal Response Codes**

* 202

**Error Response Codes**

* Invalid Data (400)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| schema | string | Required. Register Instance Request schema URI. |
| owner | string | ID of the workspace where the instance is imported. |
| name | string | Instance name to register. |
| description | string | Instance description to register. |
| unregistered_id | string | Instance unique identifier |
| linux_username | string | Linux user to install agent |
| private_key | string | Linux key to install agent  |
| windows_username | string | Windows username to install agent |
| windows_password | string | Windows password to install agent |
| instance_tags | array | List of tags defined at deployment time. |
| automatic_updates | string | One of the: major, minor, patch, off. Default off. |
| lease | array | Schedules an instance with two parameters:<li>expire. Specifies in UTC format YYYY-MM-DD HH:MM:SS.SSSSSS, the time and date for stopping an instance. It’s required only when an instance is set to terminate or shut down.</li><li>operation. Specifies an instance to stop with **shutdown** or **terminate**. When not scheduled, the instance is set to **alwayson**.</li> |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:
{
   "schema": "http://elasticbox.net/schemas/register-instance-request",
   "owner": "operations",
   "name": "LDAP Box",
   "unregistered_id": "7a99f95c-30e6-4986-9059-f6999d1jhgf9",
   "description": "Ldap server registered",
   "linux_username": "root",
   "private_key": "-----BEGIN RSA PRIVATE KEY-----
..................................................
-----END RSA PRIVATE KEY-----",
   "instance_tags": [],
   "automatic_updates": "off",
   "lease": {
       "expire": "2017-11-11 23:00:00.000000",
       "operation": "shutdown"
   }
}
```

For use bulk import, the request must have bulk import request schema, and a list of
unregistered instances:

```
Body:
{
  "schema": "http://elasticbox.net/schemas/bulk-import-request",
  "owner": "operations",
  "unregistered_instances": [
    {
      "schema": "http://elasticbox.net/schemas/register-instance-request",
      "name": "msql-a",
      "unregistered_id": "5eed8408-3ece-45d9-8e78-3f3472bea165",
      "instance_tags": [
        "zoneA"
      ]
    },
    {
      "schema": "http://elasticbox.net/schemas/register-instance-request",
      "name": "msql-b",
      "unregistered_id": "6b9b9ecc-f22d-4101-991c-c55f8de80439",
      "instance_tags": [
        "zoneB"
      ]
    }
  ],
  "instance_tags": [
    "registered"
  ]
}
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| lease | array | If scheduled, this object displays these parameters for the instance:<li>released. Is a true or false boolean value. False means that the operation scheduled on the instance is not executed yet.</li><li>expire. Specifies in UTC format YYYY-MM-DD HH:MM:SS.SSSSSS, the time and date for stopping an instance. It applies only when an instance is set to terminate or shut down.</li><li>operation. Specifies the stop operation scheduled as either **shutdown** or **terminate**. When not scheduled, the instance is set to **alwayson**.</li> |
| bindings | array | List of instance bindings. |
| binding | object | Binding contained in the bindings list, each binding object contains the parameters: instance and name. |
| updated | string | Date of the last update. |
|name | string | Instance name. |
| service | Object | Instance service. |
| service.type | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| service.id | string | Service type. |
| service.machines | array | List of service machines. |
| machine | object | Machine contained in the service machines list. |
| machine.state | string | Machine state, there are three possible states: processing , done and unavailable. |
| machine.name | string | Machine name. |
| machine.workflow | array | 	List of workflow actions, where each workflow action object contains three parameters: box, event, and script. |
| workflow.box | string | Workflow action box. |
| workflow.event | string |	Workflow action event.|
| workflow.script | string | Workflow action script uri. |
| tags | array | Instance tags. |
| variables | array | 	List of instance variables, each variable object contains the parameters: type , name and value. |
| created | string | Creation date. |
| boxes | array | List of boxes |
| box.visibility | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values:<li>public: Visible to Cloud Application Manager users across all organizations.</li><li>organization: Visible to all users in the organization where the box was created.</li><li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| box.organization | string | Organization to which the box belongs. |
| box.updated | string | Date of the last update. |
| box.description | string | Box description. |
| box.service | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| box.tags | array | Box tags. |
| box.variables | array | 	List of box variables, each variable object contains the parameters: type , name and value. |
| box.created | string | Creation date. |
| box.uri | string | Box uri. |
| box.id | array | Box unique identifier. |
| box.schema | string | Box schema uri. |
| box.members | array | List of Box members. |
| box.owner | string | Box owner. |
| box.bindings | array | List of Box bindings. |
| box.binding | object | Binding contained in the bindings list, each binding have a box and a name. |
| box.icon | string | Box icon uri. |
| box.events | array | 	List of Box events, there may be nine event lists: configure, dispose, install, post_configure, post_dispose, post_install, post_start, post_stop, start, and stop. |
| box.event | object | Event contained in one of the event lists, each event object contains the parameters: url , upload_date , length and destination_path. |
| box.name | string | Box name. |
| uri | string | instance uri. |
| state | string | Instance state, there are three possible states: processing , done and unavailable |
| members | array | Instance members. |
| owner | string | Instance owner. |
| operation | string | Last operation, there are seven types of operations: deploy , shutdown , poweron , reinstall , reconfigure , terminate and terminate_service |
| icon | string | Instance icon uri. |
| id | array | Instance unique identifier. |
| schema | string | Instance schema uri. |
| policy_box | object | specific deployment policy for a provider |
| policy_box.provider_id | string | provider id |
| policy_box.automatic_updates | string | One of them: mayor, minor, patch, off |
| policy_box.name | string | Policy box name |
| policy_box.variables | array | List of deployment box policy variables |
| policy_box.claims | array | List of deployment box policy claims |
| policy_box.id | string | Deployment box policy id |
| policy_box.schema | string | Deployment box policy schema |
| policy_box.members | array | 	List of members sharing the deployment policy box |
| policy_box.owner | string | Deployment box policy owner |
| policy_box.readme | object | Readme file for the Deployment policy box |

```
Response:
{
 "box": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
 "policy_box": {
   "profile": {
     "image": "test",
     "instances": 1,
     "keypair": "test_keypair",
     "location": "Simulated Location",
     "flavor": "test.micro",
     "schema": "http://elasticbox.net/schemas/test/compute/profile"
   },
   "provider_id": "0476718d-2b00-45ce-8a1c-30b10a16cfc7",
   "automatic_updates": "off",
   "name": "Linux Compute",
   "created": "2015-10-21 08:35:50.165822",
   "deleted": null,
   "variables": [
     {
       "automatic_updates": "off",
       "name": "policy_box_variable",
       "required": false,
       "visibility": "public",
       "value": "381d0fd8-b59e-4be6-afc7-3ee1a0a2db1c",
       "type": "Box"
     }
   ],
   "updated": "2015-10-29 12:05:39.065397",
   "visibility": "workspace",
   "owner": "operations",
   "members": [

   ],
   "claims": [
     "linux"
   ],
   "readme": {
     "url": "/resources/default_box_overview.md",
     "upload_date": "2015-10-21 08:35:50.164926",
     "length": 1302,
     "content_type": "text/x-markdown"
   },
   "organization": "elasticbox",
   "id": "e57466ee-7094-4bd4-9121-a6df4395d493",
   "schema": "http://elasticbox.net/schemas/boxes/policy"
 },
 "updated": "2015-10-29 12:26:20.377029",
 "automatic_updates": "off",
 "name": "ScriptBoxSample",
 "service": {
   "type": "Linux Compute",
   "id": "eb-bbhzh",
   "machines": [

   ]
 },
 "tags": [

 ],
 "deleted": null,
 "variables": [
   {
     "required": true,
     "type": "Text",
     "name": "variable_name",
     "value": "variable_value_overridden",
     "visibility": "public"
   }
 ],
 "created": "2015-10-29 12:26:20.377029",
 "state": "processing",
 "uri": "/services/instances/i-3e43qa",
 "boxes": [
   {
     "updated": "2015-10-29 11:55:23.842461",
     "automatic_updates": "off",
     "requirements": [

     ],
     "description": "sample box",
     "name": "ScriptBoxSample",
     "created": "2015-10-29 10:52:08.446868",
     "deleted": null,
     "variables": [
       {
         "required": true,
         "type": "Text",
         "name": "variable_name",
         "value": "variable_value",
         "visibility": "public"
       }
     ],
     "visibility": "workspace",
     "id": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
     "members": [

     ],
     "owner": "operations",
     "organization": "elasticbox",
     "events": {
       "configure": {
         "url": "/services/blobs/download/5631fa7614841250525226cc/configure",
         "length": 5,
         "destination_path": "scripts",
         "content_type": "text/x-shellscript"
       },
       "install": {
         "url": "/services/blobs/download/5631fa6614841250525226ca/install",
         "length": 5,
         "destination_path": "scripts",
         "content_type": "text/x-shellscript"
       }
     },
     "schema": "http://elasticbox.net/schemas/boxes/script"
   }
 ],
 "members": [

 ],
 "bindings": [

 ],
 "owner": "operations",
 "operation": {
   "event": "deploy",
   "workspace": "operations",
   "created": "2015-10-29 12:26:20.375582"
 },
 "schema": "http://elasticbox.net/schemas/instance",
 "id": "i-3e43qa",
 "icon": null
}
```

### GET /services/instances/{instance_id}

Fetches an existing instance given its ID.

**Normal Response Codes**

* 200

**Error Response Codes**

* Invalid Data (400)
* Forbidden (403)
* Not Found (404)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| bindings | array | List of instance bindings. |
| binding | object | Binding contained in the bindings list, each binding object contains the parameters: instance and name. |
| updated |  string | Date of the last update. |
| name | string | Instance name. |
| service | object | Instance service. |
| service.type | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| service.id | string | Service type. |
| service.machines | array | List of service machines |
| machine | object | Machine contained in the service machines list. |
| machine.state | string | Machine state, there are three possible states: processing , done and unavailable. |
| machine.name | string | Machine name. |
| machine.workflow | array | List of workflow actions, where each workflow action object contains three parameters: box, event, and script. |
| workflow.box | string | Workflow action box. |
| workflow.event | string | Workflow action event. |
| workflow.script | string | Workflow action script uri. |
| tags | array | Instance tags. |
| variables | array | List of instance variables, each variable object contains the parameters: type , name and value. |
| created | string | Creation date. |
| boxes | array | List of boxes |
| box.visibility | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values:<li>public: Visible to Cloud Application Manager users across all organizations.</li><li>organization: Visible to all users in the organization where the box was created.</li><li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| box.organization | string | Organization to which the box belongs. |
| box.updated | string | Date of the last update. |
| box.description | string | Box description. |
| box.service | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| box.tags | array | Box tags. |
| box.variables | array | 	List of box variables, each variable object contains the parameters: type , name and value. |
| box.created | string | Creation date. |
| box.uri | string | Box uri. |
| box.id | array | Box unique identifier. |
| box.schema | string | Box schema uri. |
| box.members | array | List of Box members. |
| box.owner | string | Box owner. |
| box.bindings | array | List of Box bindings. |
| box.binding | object | Binding contained in the bindings list, each binding have a box and a name. |
| box.icon | string | Box icon uri. |
| box.events | array | 	List of Box events, there may be nine event lists: configure, dispose, install, post_configure, post_dispose, post_install, post_start, post_stop, start, and stop. |
| box.event | object | Event contained in one of the event lists, each event object contains the parameters: url , upload_date , length and destination_path. |
| box.name | string | Box name. |
| policy_box | object | specific deployment policy for a provider |
| policy_box.provider_id | string | provider id |
| policy_box.automatic_updates | string | One of them: mayor, minor, patch, off |
| policy_box.name | string | Policy box name |
| policy_box.variables | array | List of deployment box policy variables |
| policy_box.claims | array | List of deployment box policy claims |
| policy_box.id | string | Deployment box policy id |
| policy_box.schema | string | Deployment box policy schema |
| policy_box.members | array | 	List of members sharing the deployment policy box |
| policy_box.owner | string | Deployment box policy owner |
| policy_box.readme | object | Readme file for the Deployment policy box |
| uri | string | instance uri. |
| state | string | Instance state, there are three possible states: processing , done and unavailable |
| members | array | Instance members. |
| owner | string | Instance owner. |
| operation | string | Last operation, there are seven types of operations: deploy , shutdown , poweron , reinstall , reconfigure , terminate and terminate_service |
| icon | string | Instance icon uri. |
| id | array | Instance unique identifier. |
| schema | string | Instance schema uri. |

```
{
 "box": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
 "bindings": [

 ],
 "updated": "2015-10-29 12:26:24.446893",
 "automatic_updates": "off",
 "name": "ScriptBoxSample",
 "service": {
   "type": "Linux Compute",
   "id": "eb-bbhzh",
   "machines": [
     {
       "state": "done",
       "name": "eb-bbhzh-1",
       "workflow": [

       ]
     }
   ]
 },
 "tags": [

 ],
 "deleted": null,
 "policy_box": {
   "profile": {
     "image": "test",
     "instances": 1,
     "keypair": "test_keypair",
     "location": "Simulated Location",
     "flavor": "test.micro",
     "schema": "http://elasticbox.net/schemas/test/compute/profile"
   },
   "provider_id": "0476718d-2b00-45ce-8a1c-30b10a16cfc7",
   "automatic_updates": "off",
   "name": "Linux Compute",
   "created": "2015-10-21 08:35:50.165822",
   "deleted": null,
   "variables": [
     {
       "automatic_updates": "off",
       "name": "policy_box_variable",
       "required": false,
       "visibility": "public",
       "value": "381d0fd8-b59e-4be6-afc7-3ee1a0a2db1c",
       "type": "Box"
     }
   ],
   "updated": "2015-10-29 12:05:39.065397",
   "visibility": "workspace",
   "owner": "operations",
   "members": [

   ],
   "claims": [
     "linux"
   ],
   "readme": {
     "url": "/resources/default_box_overview.md",
     "upload_date": "2015-10-21 08:35:50.164926",
     "length": 1302,
     "content_type": "text/x-markdown"
   },
   "organization": "elasticbox",
   "id": "e57466ee-7094-4bd4-9121-a6df4395d493",
   "schema": "http://elasticbox.net/schemas/boxes/policy"
 },
 "created": "2015-10-29 12:26:20.377029",
 "uri": "/services/instances/i-3e43qa",
 "state": "done",
 "boxes": [
   {
     "updated": "2015-10-29 11:55:23.842461",
     "automatic_updates": "off",
     "requirements": [

     ],
     "description": "sample box",
     "name": "ScriptBoxSample",
     "created": "2015-10-29 10:52:08.446868",
     "deleted": null,
     "variables": [
       {
         "required": true,
         "type": "Text",
         "name": "variable_name",
         "value": "variable_value",
         "visibility": "public"
       }
     ],
     "visibility": "workspace",
     "id": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
     "members": [

     ],
     "owner": "operations",
     "organization": "elasticbox",
     "events": {
       "configure": {
         "url": "/services/blobs/download/5631fa7614841250525226cc/configure",
         "length": 5,
         "destination_path": "scripts",
         "content_type": "text/x-shellscript"
       },
       "install": {
         "url": "/services/blobs/download/5631fa6614841250525226ca/install",
         "length": 5,
         "destination_path": "scripts",
         "content_type": "text/x-shellscript"
       }
     },
     "schema": "http://elasticbox.net/schemas/boxes/script"
   }
 ],
 "schema": "http://elasticbox.net/schemas/instance",
 "members": [

 ],
 "owner": "operations",
 "variables": [
   {
     "required": true,
     "type": "Text",
     "name": "variable_name",
     "value": "variable_value_overridden",
     "visibility": "public"
   }
 ],
 "operation": {
   "event": "deploy",
   "workspace": "operations",
   "created": "2015-10-29 12:26:20.504356"
 },
 "id": "i-3e43qa",
 "icon": null
}
```

### PUT /services/instances/{instance_id}

Given the instance ID, updates only these fields of an existing instance: boxes, tags, schedule, members, and variables. The request body should contain an instance object.

**Normal Response Codes**

* 200
* 202

**Error Response Codes**

* Invalid Data (400)
* Forbidden (403)
* Not Found (404)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| bindings | array | List of instance bindings. |
| binding | object | Binding contained in the bindings list, each binding object contains the parameters: instance and name. |
| updated |  string | Date of the last update. |
| name | string | Instance name. |
| service | object | Instance service. |
| service.type | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| service.id | string | Service type. |
| service.machines | array | List of service machines |
| machine | object | Machine contained in the service machines list. |
| machine.state | string | Machine state, there are three possible states: processing , done and unavailable. |
| machine.name | string | Machine name. |
| machine.workflow | array | List of workflow actions, where each workflow action object contains three parameters: box, event, and script. |
| workflow.box | string | Workflow action box. |
| workflow.event | string | Workflow action event. |
| workflow.script | string | Workflow action script uri. |
| tags | array | Instance tags. |
| variables | array | List of instance variables, each variable object contains the parameters: type , name and value. |
| created | string | Creation date. |
| boxes | array | List of boxes |
| box.visibility | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values:<li>public: Visible to Cloud Application Manager users across all organizations.</li><li>organization: Visible to all users in the organization where the box was created.</li><li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| box.organization | string | Organization to which the box belongs. |
| box.updated | string | Date of the last update. |
| box.description | string | Box description. |
| box.service | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| box.tags | array | Box tags. |
| box.variables | array | 	List of box variables, each variable object contains the parameters: type , name and value. |
| box.created | string | Creation date. |
| box.uri | string | Box uri. |
| box.id | array | Box unique identifier. |
| box.schema | string | Box schema uri. |
| box.members | array | List of Box members. |
| box.owner | string | Box owner. |
| box.bindings | array | List of Box bindings. |
| box.binding | object | Binding contained in the bindings list, each binding have a box and a name. |
| box.icon | string | Box icon uri. |
| box.events | array | 	List of Box events, there may be nine event lists: configure, dispose, install, post_configure, post_dispose, post_install, post_start, post_stop, start, and stop. |
| box.event | object | Event contained in one of the event lists, each event object contains the parameters: url , upload_date , length and destination_path. |
| box.name | string | Box name. |
| policy_box | object | specific deployment policy for a provider |
| policy_box.provider_id | string | provider id |
| policy_box.automatic_updates | string | One of them: mayor, minor, patch, off |
| policy_box.name | string | Policy box name |
| policy_box.variables | array | List of deployment box policy variables |
| policy_box.claims | array | List of deployment box policy claims |
| policy_box.id | string | Deployment box policy id |
| policy_box.schema | string | Deployment box policy schema |
| policy_box.members | array | 	List of members sharing the deployment policy box |
| policy_box.owner | string | Deployment box policy owner |
| policy_box.readme | object | Readme file for the Deployment policy box |
| uri | string | instance uri. |
| state | string | Instance state, there are three possible states: processing , done and unavailable |
| members | array | Instance members. |
| owner | string | Instance owner. |
| operation | string | Last operation, there are seven types of operations: deploy , shutdown , poweron , reinstall , reconfigure , terminate and terminate_service |
| icon | string | Instance icon uri. |
| id | array | Instance unique identifier. |
| schema | string | Instance schema uri. |
| lease | array | Schedules an instance with two parameters:<li>expire. Specifies in UTC format YYYY-MM-DD HH:MM:SS.SSSSSS, the time and date for stopping an instance. It’s required only when an instance is set to terminate or shut down.</li><li>operation. Specifies an instance to stop with **shutdown** or **terminate**. When not scheduled, the instance is set to **alwayson**.</li> |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```
```
Body:
In this sample request, the instance is tagged and scheduled to terminate at a given UTC time.


{
   "box": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
   "bindings": [

   ],
   "updated": "2015-10-29 12:26:24.446893",
   "automatic_updates": "off",
   "name": "ScriptBoxSample",
   "service": {
   "type": "Linux Compute",
   "id": "eb-bbhzh",
   "machines": [
     {
       "state": "done",
       "name": "eb-bbhzh-1",
       "workflow": [

       ]
     }
   ]
   },
   "tags": [

   ],
   "deleted": null,
   "policy_box": {
       "profile": {
         "image": "test",
         "instances": 1,
         "keypair": "test_keypair",
         "location": "Simulated Location",
         "flavor": "test.micro",
         "schema": "http://elasticbox.net/schemas/test/compute/profile"
       },
       "provider_id": "0476718d-2b00-45ce-8a1c-30b10a16cfc7",
       "automatic_updates": "off",
       "name": Linux Compute",
       "created": "2015-10-21 08:35:50.165822",
       "deleted": null,
       "variables": [
         {
           "automatic_updates": "off",
           "name": "policy_box_variable",
           "required": false,
           "visibility": "public",
           "value": "381d0fd8-b59e-4be6-afc7-3ee1a0a2db1c",
           "type": "Box"
         }
       ],
       "updated": "2015-10-29 12:05:39.065397",
       "visibility": "workspace",
       "owner": "operations",
       "members": [

       ],
       "claims": [
         "linux"
       ],
       "readme": {
         "url": "/resources/default_box_overview.md",
         "upload_date": "2015-10-21 08:35:50.164926",
         "length": 1302,
         "content_type": "text/x-markdown"
       },
       "organization": "elasticbox",
       "id": "e57466ee-7094-4bd4-9121-a6df4395d493",
       "schema": "http://elasticbox.net/schemas/boxes/policy"
   },
   "created": "2015-10-29 12:26:20.377029",
   "uri": "/services/instances/i-3e43qa",
   "state": "done",
   "boxes": [
       {
       "updated": "2015-10-29 11:55:23.842461",
       "automatic_updates": "off",
       "requirements": [

       ],
       "description": "sample box",
       "name": "ScriptBoxSample",
       "created": "2015-10-29 10:52:08.446868",
       "deleted": null,
       "variables": [
       {
         "required": true,
         "type": "Text",
         "name": "variable_name",
         "value": "variable_value",
         "visibility": "public"
       }
       ],
       "visibility": "workspace",
       "id": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
       "members": [

       ],
       "owner": "operations",
       "organization": "elasticbox",
       "events": {
           "configure": {
             "url": "/services/blobs/download/5631fa7614841250525226cc/configure",
             "length": 5,
             "destination_path": "scripts",
             "content_type": "text/x-shellscript"
           },
           "install": {
             "url": "/services/blobs/download/5631fa6614841250525226ca/install",
             "length": 5,
             "destination_path": "scripts",
             "content_type": "text/x-shellscript"
           }
       },
       "schema": "http://elasticbox.net/schemas/boxes/script"
       }
   ],
   "schema": "http://elasticbox.net/schemas/instance",
   "members": [

   ],
   "owner": "operations",
   "variables": [
       {
         "required": true,
         "type": "Text",
         "name": "variable_name",
         "value": "variable_value_overridden",
         "visibility": "public"
       }
   ],
   "operation": {
       "event": "deploy",
       "workspace": "operations",
       "created": "2015-10-29 12:26:20.504356"
   },
   "id": "i-3e43qa",
   "icon": null,
   "lease": {
       "expire": "2015-10-29 19:00:00.000000",
       "operation": "terminate"
   }
}
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| bindings | array | List of instance bindings. |
| binding | object | Binding contained in the bindings list, each binding object contains the parameters: instance and name. |
| updated | string | Date of the last update. |
|name | string | Instance name. |
| service | Object | Instance service. |
| service.type | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| service.id | string | Service type. |
| service.machines | array | List of service machines. |
| machine | object | Machine contained in the service machines list. |
| machine.state | string | Machine state, there are three possible states: processing , done and unavailable. |
| machine.name | string | Machine name. |
| machine.workflow | array | 	List of workflow actions, where each workflow action object contains three parameters: box, event, and script. |
| workflow.box | string | Workflow action box. |
| workflow.event | string |	Workflow action event.|
| workflow.script | string | Workflow action script uri. |
| tags | array | Instance tags. |
| variables | array | 	List of instance variables, each variable object contains the parameters: type , name and value. |
| created | string | Creation date. |
| boxes | array | List of boxes |
| box.visibility | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values:<li>public: Visible to Cloud Application Manager users across all organizations.</li><li>organization: Visible to all users in the organization where the box was created.</li><li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| box.organization | string | Organization to which the box belongs. |
| box.updated | string | Date of the last update. |
| box.description | string | Box description. |
| box.service | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| box.tags | array | Box tags. |
| box.variables | array | 	List of box variables, each variable object contains the parameters: type , name and value. |
| box.created | string | Creation date. |
| box.uri | string | Box uri. |
| box.id | array | Box unique identifier. |
| box.schema | string | Box schema uri. |
| box.members | array | List of Box members. |
| box.owner | string | Box owner. |
| box.bindings | array | List of Box bindings. |
| box.binding | object | Binding contained in the bindings list, each binding have a box and a name. |
| box.icon | string | Box icon uri. |
| box.events | array | 	List of Box events, there may be nine event lists: configure, dispose, install, post_configure, post_dispose, post_install, post_start, post_stop, start, and stop. |
| box.event | object | Event contained in one of the event lists, each event object contains the parameters: url , upload_date , length and destination_path. |
| box.name | string | Box name. |
| policy_box | object | specific deployment policy for a provider |
| policy_box.provider_id | string | provider id |
| policy_box.automatic_updates | string | One of them: mayor, minor, patch, off |
| policy_box.name | string | Policy box name |
| policy_box.variables | array | List of deployment box policy variables |
| policy_box.claims | array | List of deployment box policy claims |
| policy_box.id | string | Deployment box policy id |
| policy_box.schema | string | Deployment box policy schema |
| policy_box.members | array | 	List of members sharing the deployment policy box |
| policy_box.owner | string | Deployment box policy owner |
| policy_box.readme | object | Readme file for the Deployment policy box |
| uri | string | instance uri. |
| state | string | Instance state, there are three possible states: processing , done and unavailable |
| members | array | Instance members. |
| owner | string | Instance owner. |
| operation | string | Last operation, there are seven types of operations: deploy , shutdown , poweron , reinstall , reconfigure , terminate and terminate_service |
| icon | string | Instance icon uri. |
| id | array | Instance unique identifier. |
| schema | string | Instance schema uri. |
| lease | array | Schedules an instance with two parameters:<li>released. Is a true or false boolean value. False means that the operation scheduled on the instance is not executed yet.</li><li>expire. Specifies in UTC format YYYY-MM-DD HH:MM:SS.SSSSSS, the time and date for stopping an instance. It’s required only when an instance is set to terminate or shut down.</li><li>operation. Specifies an instance to stop with **shutdown** or **terminate**. When not scheduled, the instance is set to **alwayson**.</li> |

```
{
   "box": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
   "bindings": [],
   "updated": "2015-10-29 14:16:48.304153",
   "automatic_updates": "off",
   "name": "ScriptBoxSample",
   "service": {
       "type": "Linux Compute",
       "id": "eb-bbhzh",
       "machines": [
           {
               "state": "done",
               "name": "eb-bbhzh-1",
               "workflow": []
           }
       ]
   },
   "tags": [],
   "deleted": null,
   "policy_box": {
       "profile": {
           "image": "test",
           "instances": 1,
           "keypair": "test_keypair",
           "location": "Simulated Location",
           "flavor": "test.micro",
           "schema": "http://elasticbox.net/schemas/test/compute/profile"
       },
       "provider_id": "0476718d-2b00-45ce-8a1c-30b10a16cfc7",
       "automatic_updates": "off",
       "name": "Deploy Policy - Linux Compute",
       "created": "2015-10-21 08:35:50.165822",
       "deleted": null,
       "variables": [
           {
               "automatic_updates": "off",
               "name": "policy_box_variable",
               "required": false,
               "visibility": "public",
               "value": "381d0fd8-b59e-4be6-afc7-3ee1a0a2db1c",
               "type": "Box"
           }
       ],
       "updated": "2015-10-29 12:05:39.065397",
       "visibility": "workspace",
       "owner": "operations",
       "members": [],
       "claims": [
           "linux"
       ],
       "readme": {
           "url": "/resources/default_box_overview.md",
           "upload_date": "2015-10-21 08:35:50.164926",
           "length": 1302,
           "content_type": "text/x-markdown"
       },
       "organization": "elasticbox",
       "id": "e57466ee-7094-4bd4-9121-a6df4395d493",
       "schema": "http://elasticbox.net/schemas/boxes/policy"
   },
   "created": "2015-10-29 12:26:20.377029",
   "uri": "/services/instances/i-3e43qa",
   "state": "done",
   "boxes": [
       {
           "updated": "2015-10-29 11:55:23.842461",
           "automatic_updates": "off",
           "requirements": [],
           "description": "sample box",
           "name": "ScriptBoxSample",
           "created": "2015-10-29 10:52:08.446868",
           "deleted": null,
           "variables": [
               {
                   "required": true,
                   "type": "Text",
                   "name": "variable_name",
                   "value": "variable_value",
                   "visibility": "public"
               }
           ],
           "visibility": "workspace",
           "id": "7a99f75c-30e6-4986-9059-f6889d1ff5f9",
           "members": [],
           "owner": "operations",
           "organization": "elasticbox",
           "events": {
               "configure": {
                   "url": "/services/blobs/download/5631fa7614841250525226cc/configure",
                   "length": 5,
                   "destination_path": "scripts",
                   "content_type": "text/x-shellscript"
               },
               "install": {
                   "url": "/services/blobs/download/5631fa6614841250525226ca/install",
                   "length": 5,
                   "destination_path": "scripts",
                   "content_type": "text/x-shellscript"
               }
           },
           "schema": "http://elasticbox.net/schemas/boxes/script"
       }
   ],
   "schema": "http://elasticbox.net/schemas/instance",
   "members": [],
   "owner": "operations",
   "variables": [
       {
           "required": true,
           "type": "Text",
           "name": "variable_name",
           "value": "variable_value_overridden",
           "visibility": "public"
       }
   ],
   "operation": {
       "event": "deploy",
       "workspace": "operations",
       "created": "2015-10-29 12:26:20.504356"
   },
   "lease": {
       "released": false,
       "operation": "terminate",
       "expire": "2015-10-29 19:00:00.000000"
   },
   "id": "i-3e43qa",
   "icon": null
}
```

### DELETE /services/instances/{instance_id}
Terminates, force-terminates, or deletes an existing instance based on its instance ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Invalid Operation (400)
* Forbidden (403)
* Not Found (404)
* Operation Conflict (409)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| operation | string | Operation type must be one of the following values: terminate, force_terminate and delete |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```
```
Body:

DELETE /services/instances/{instance_id}?operation=force_terminate
```

### GET /services/instances/{instance_id}/service
Gets the service on the instance given its instance ID.

**Normal Response Codes**

* 200

**Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| profile | object | Service profile. |
| profile.subnet | string | Profile subnet. |
| profile.image | string | Profile image. |
| profile.keypair | string | Profile keypair. |
| profile.location | string| Profile location. |
| profile.security_group | string | Profile secruty group. |
| profile.flavor | string | Profile flavor. |
| profile.autoscalable | boolean | Profile autoscalable. |
| profile.cloud | boolean | Cloud type. |
| profile.schema | string | Profile schema uri. |
| provider_id | string | Profile provider unique identifier. |
|created | string | Creation date. |
| tags | array | Service tags. |
| state | string | Service state, there are three possible states: processing , done and unavailable |
| token | string | Service token. |
| operation | string | Service last operation, there are seven types of operations: deploy, shutdown, poweron, reinstall, reconfigure, terminate, and terminate_service. |
| icon | string | Service icon url. |
| type | string | Instance type. |
| id | string | Instance unique identifier. |
| machines | array | List of service machines. |
| machine.token | string | Machine token. |
| machine.name | string | Machine name. |
| machine.address | array | The array contains the public and private address. |
| machine.agent_version | array | Machine agent version. |
| machine.external_id | array | Machine external id. |
| machine.state | string | Machine state, there are three possible states: processing , done and unavailable. |
| machine.schema | array | Machine schema uri. |
| schema | string | Service schema uri. |
| organization | string | The name of the organization that owns this service. |
| deleted | string | Deleted. |

```
{
   "profile": {
       "image": "test",
       "instances": 1,
       "keypair": "test_keypair",
       "location": "Simulated Location",
       "flavor": "test.micro",
       "schema": "http://elasticbox.net/schemas/test/compute/profile"
   },
   "schema": "http://elasticbox.net/schemas/service",
   "provider_id": "0476718d-2b00-45ce-8a1c-30b10a16cfc7",
   "tags": [],
   "deleted": null,
   "variables": [],
   "created": "2015-10-29 12:26:20.384736",
   "state_history": [
       {
           "started": "2015-10-29 12:26:21.719034",
           "state": "up"
       }
   ],
   "updated": "2015-10-29 12:26:21.824949",
   "token": "8f4ca23f-5b01-44b8-810c-21b287e63098",
   "state": "done",
   "organization": "elasticbox",
   "operation": "deploy",
   "type": "Linux Compute",
   "id": "eb-bbhzh",
   "machines": [
       {
           "name": "eb-bbhzh-1",
           "token": "d58634c4-b8f0-4bef-b2f8-a2a83e8397da",
           "state": "done",
           "tmp_folder": "/tmp/eb-bbhzh-1TeAIPz",
           "address": {
               "public": "127.59.247.222",
               "private": "127.218.204.194"
           },
           "schema": "http://elasticbox.net/schemas/test/service-machine",
           "external_id": "eb-bbhzh-1TeAIPz",
           "agent_version": "6.2"
       }
   ],
   "icon": "images/platform/linux.png"
}
```

### GET /services/instances/{instance_id}/activity

Gets all activity logs from operations run on an instance given its instance ID.

**Normal Response Codes**

* 200

**Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| (Optional) operation | string | The specific operation id, there are seven types of operations: deploy, shutdown, poweron, reinstall, reconfigure, terminate and terminate_service. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

GET /services/instances/{instance_id}/activity?operation=deploy
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
|* box | string | Box name. |
| username | string | User who performed the activity. |
|* machine | string | Machine. |
| level | string | Activity type. |
| text | string | Activity description. |
| created | string | Activity creation date. |
|* event | string | Activity event. |

```
[
       {
           "text": "Deploying instance.",
           "created": "2015-10-29 12:26:20.510174",
           "level": "start"
       },
       {
           "text": "Creating machine eb-bbhzh-1.",
           "created": "2015-10-29 12:26:20.558906",
           "level": "add"
       },
       {
           "text": "Waiting to install ElasticBox agent in machine eb-bbhzh-1.",
           "created": "2015-10-29 12:26:21.717263",
           "level": "waiting"
       },
       {
           "box": "",
           "created": "2015-10-29 12:26:21.905717",
           "text": "Executing install:ScriptBoxSample in machine eb-bbhzh-1.",
           "level": "install",
           "machine": "eb-bbhzh-1",
           "event": "install"
       },
       {
           "box": "",
           "created": "2015-10-29 12:26:22.262111",
           "text": "Executing configure:ScriptBoxSample in machine eb-bbhzh-1.",
           "level": "configure",
           "machine": "eb-bbhzh-1",
           "event": "configure"
       },
       {
           "text": "Machine eb-bbhzh-1 successfully deployed.",
           "created": "2015-10-29 12:26:24.433644",
           "level": "success"
       },
       {
           "text": "Instance successfully deployed.",
           "created": "2015-10-29 12:26:24.437692",
           "level": "success"
       }
]
```

### GET /services/instances/{instance_id}/machine_logs

Gets the logs of one machine for a deployed instance given its instance ID.

**Normal Response Codes**

* 200

**Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| machine_name | string | 	The name of the machine you want to retrieve the log. You can get the name of the machine from the instance document. |
| (Optional) box | string | Box name. |
| (Optional) event | string | Event type, there may be nine event lists: configure, dispose, install, post_dispose, post_stop, pre_configure, pre_install, pre_start, start and stop. |
| (Optional) operation | string | The specific operation id, there are seven types of operations: deploy , shutdown , poweron , reinstall , reconfigure, terminate and terminate_service. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

GET /services/instances/{instance_id}/machine_logs?machine_name={machine_name}
```

**Response**

```
Executing pre_install-{instance_id} script
...
pre_install-{instance_id} successfully executed.
Executing install-{instance_id} script
...
install-{instance_id} successfully executed.
Executing configure-{instance_id} script
...
configure-{instance_id} successfully executed.
```

### GET /services/instances/{instance_id}/binding

Gets the binding of an instance when you give the instance ID.

**Normal Response Codes**

* 200

**Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| updated | string | Date of the last update. |
| operation | string | Last operation, there are seven types of operations: deploy , shutdown , poweron , reinstall , reconfigure , terminate and terminate_service |
| name | string | Instance name. |
| service| Object | Instance service. |
| service.type | string | Required. Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
| service.id | string | Service type. |
| service.machines | array | List of service machines |
| machine | object | Machine contained in the service machines list. |
| machine.state | string | Machine state, there are three possible states: processing , done and unavailable. |
| machine.name | string | Machine name. |
| machine.workflow | array | List of workflow actions, where each workflow action object contains three parameters: box, event, and script. |
| workflow.box | string | Workflow action box. |
| workflow.event | string | Workflow action event. |
| workflow.script | string | Workflow action script uri. |
| tags | array | Instance tags. |
| boxes | array | List of boxes where each box object contains a service parameter. The service parameter can have one of these values: Linux Compute, Windows Compute and CloudFormation Service. |
| uri |  string | Instance uri. |
| state | string | Instance state, there are three possible states: processing , done and unavailable |
| bindings | array | List of instance bindings. |
| binding | object | Binding contained in the bindings list, each binding object contains the parameters: instance and name. |
| id | array | Instance unique identifier |
| icon | string | Instance icon uri. |
| schema | string | Instance schema uri. |

```
[
  {
     "box":{
        "version":"1186ce20-96f2-458d-ae62-19496036b275",
        "name":"Wordpress"
     },
     "updated":"2014-03-21 18:20:04.921745",
     "name":"profile",
     "created":"2014-03-21 18:20:04.921745",
     "default_stamp":1395426004.921258,
     "uri":"--profile uri--",
     "instances":[
        {
           "box":{
              "version":"1186ce20-96f2-458d-ae62-19496036b275",
              "name":"Wordpress"
           },
           "profile":{
              "subnet":"us-east-1b",
              "image":"Linux Compute",
              "instances":1,
              "keypair":"None",
              "location":"us-east-1",
              "security_group":"Automatic",
              "flavor":"t1.micro",
              "autoscalable":false,
              "cloud":"EC2",
              "schema":"http://elasticbox.net/schemas/aws/ec2/profile"
           },
           "provider":"Amazon",
           "path":"/",
           "variables":[
              {
                 "type":"Port",
                 "name":"http",
                 "value":"80"
              }
           ],
           "bindings":[

           ]
        }
     ],
     "members":[
               "member1","member2"
     ],
     "owner":"workspace1",
     "id":"--profile id--",
     "schema":"http://elasticbox.net/schemas/deployment-profile"
  }
]
```

### GET /services/instances/{instance_id}/operations

Gets all operations run on an instance when you give the instance ID.

**Normal Response Codes**

* 200

**Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```
**Response Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| username | string | User name. |
| updated | string | Date of the last update. |
| created | string | Creation date. |
| instance | string | Instance unique identifier. |
| state | string | Instance state, there are three possible states: processing , done and unavailable |
| workspace | string | Workspace name. |
| activities | array | List of activities. |
| activity.username | string | User who performed the activity. |
| activity.text | string | Activity description. |
| activity.level | string | Activity type. |
| activity.created | string | Activity date. |
| operation | string | Last operation, there are seven types of operations: deploy, shutdown, poweron, reinstall, reconfigure, terminate and terminate_service. |
| id | string | Operation unique identifier. |
| deleted | string | Removal date. |
| schema | string | Operation schema uri. |

```
[
  {
     "username":"--user--",
     "updated":"2014-03-27 13:37:23.533241",
     "created":"2014-03-27 13:33:49.602291",
     "instance":"i-ndt46z",
     "state":"done",
     "workspace":"--workspace name--",
     "activity":[
        {
           "username":"--user--",
           "text":"Deploying instance.",
           "level":"start",
           "created":"2014-03-27 13:33:49.642654"
        },
        {
           "username":"--user--",
           "text":"Binding linux_compute is up and running.",
           "level":"info",
           "created":"2014-03-27 13:37:22.826035"
        },
     ],
     "operation":"deploy",
     "id":"3265826c-0d00-4619-9e8c-d1dc23d2c81c",
     "schema":"http://elasticbox.net/schemas/instance-operation"
  }
]
```

### PUT /services/instances/{instance_id}/deploy

Re-deploy an existing instance, requires the specified id instance_id.

**Normal Response Codes**

* 202

**Error Response Codes**

* Operation Conflict (409)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

### PUT /services/instances/{instance_id}/poweron

Powers on an existing instance when you give the instance ID.

**Normal Response Codes**
* 202

**Error Response Codes**
* Operation Conflict (409)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

### PUT /services/instances/{instance_id}/shutdown

Shuts down an existing instance when you give the instance ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Operation Conflict (409)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

### PUT /services/instances/{instance_id}/reinstall

Reinstalls an existing instance when you give its ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Operation Conflict (409)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

### PUT /services/instances/{instance_id}/reconfigure

Re-configures an existing instance when you give its ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Operation Conflict (409)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| id | string | Instance ID. |
| method | string | Operation on the instance. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
  "id":"i-4g166v",
  "method":"reconfigure"
}
```

### PUT /services/instances/{instance_id}/import

Retry to import an unregistered instance. when you give its ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| id | string | Instance ID. |
| method | string | Operation on the instance (import). |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
  "id":"i-eruumb",
  "method":"import"
}
```

### PUT /services/instances/{instance_id}/cancel_import

Cancel a failed import of an unregistered instance when you give its ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Forbidden (403)
* Not Found (404)

**Request Parameters**

| Parameter | Type |Description |
|-----------|------|------------|
| id | string | Instance ID. |
| method | string | Operation on the instance (cancel_import). |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
  "id":"i-eruumb",
  "method":"cancel_import"
}
```


### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
