{{{
"title": "Boxes API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

Manage and perform actions on boxes.

**Create or List Boxes**

| Resource | Description |
|----------|-------------|
| GET /services/boxes | Gets the list of boxes that are accessible in the personal workspace. |
| POST /services/boxes | Creates a new box. |

**Perform Box Operations**

| Resource | Description |
|----------|-------------|
| GET /services/boxes/{box_id} | Fetches an existing box. |
| PUT /services/boxes/{box_id} | Updates an existing box. |
| DELETE /services/box/{box_id} | Deletes an existing box. |
| GET /services/boxes/{box_id}/stack | Gets the box stack. |
| GET /services/boxes/{box_id}/bindings | Gets the box bindings. |
| GET /services/boxes/{box_id}/versions | Get the list of box versions. |
| PUT /services/boxes/{box_id}/diff  | Get the diff between two boxes. |

**CloudFormation Box**

The Cloud Application Manager CloudFormation box runs on the AWS CloudFormation service. It lets you create and customize templates that you can launch as a single stack of combined services in AWS. Manage CloudFormation configurations in Cloud Application Manager using these [API actions](./api-boxes.md).

### GET /services/boxes

Gets boxes that are accessible in the personal workspace of the authenticated user.

**Normal Response Codes:**

* 200

**Error Response Codes:**

* Bad Request (400)

**Request Headers**

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| ids (optional) | plain | string | Comma-separate list of boxes IDs |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

GET /services/boxes?ids=05b76b08-5238-4e05-ae5f-8ea8afe00378
```

**Response Parameters**

| Parameter | Style | Type | Description |
|--------------|-----------|----------|--------------|
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| organization | plain | string | Organization to which the box belongs. |
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| requirements | plain | array | Box requirements. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| id | plain | array | Box unique identificator. |
| schema | plain | string | Box schema uri. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| icon | plain | string | Box icon uri. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the  parameters: url, upload_date, length and destination_path. |
| name | plain | string | Box name. |

```
[
  {
    "schema": "http://elasticbox.net/schemas/boxes/script",
    "updated": "2015-05-27 08:25:49.363170",
    "automatic_updates": "off",
    "requirements": [
      "linux"
    ],
    "description": "An open source, BSD licensed, advanced key-value store",
    "created": "2015-04-30 14:09:40.247173",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "Port",
        "name": "redisport",
        "value": "6379",
        "visibility": "public"
      },
      {
        "name": "CHEF_DEFAULT_RB",
        "required": false,
        "value": "/services/blobs/download/554237a3da3116443909eb79/default.rb",
        "visibility": "public",
        "scope": "chef_cookbook",
        "type": "File"
      },
      {
        "name": "CHEF_METADATA_RB",
        "required": false,
        "value": "/services/blobs/download/554237a3da3116443909eb7b/metadata.rb",
        "visibility": "public",
        "scope": "chef_cookbook",
        "type": "File"
      },
      {
        "name": "COOKBOOK_LIST",
        "required": false,
        "value": "/services/blobs/download/554237a3da3116443909eb7d/Cookbooks.config",
        "visibility": "public",
        "scope": "chef_solo",
        "type": "File"
      },
      {
        "name": "CHEF_SOLO_JSON",
        "required": false,
        "value": "/services/blobs/download/554237a3da3116443909eb7f/solo.json",
        "visibility": "public",
        "scope": "chef_solo",
        "type": "File"
      },
      {
        "automatic_updates": "off",
        "name": "chef_cookbook",
        "required": false,
        "visibility": "public",
        "value": "391e2946-552d-47b3-8551-d414ed47a97f",
        "type": "Box"
      },
      {
        "automatic_updates": "off",
        "name": "chef_solo",
        "required": false,
        "visibility": "public",
        "value": "02d1c985-04fb-41a5-83c0-cff13f02a80b",
        "type": "Box"
      }
    ],
    "uri": "/services/boxes/7e846aa1-d490-4b8a-a2a1-555407a90105",
    "visibility": "public",
    "name": "Redis",
    "id": "7e846aa1-d490-4b8a-a2a1-555407a90105",
    "members": [],
    "owner": "public",
    "organization": "public",
    "events": {},
    "draft_from": "aa5a019a-5dd6-4669-a591-ec52783b123e",
    "icon": "images/platform/redis.png"
  },
  {
    "schema": "http://elasticbox.net/schemas/boxes/script",
    "updated": "2015-05-27 08:25:49.536624",
    "automatic_updates": "off",
    "requirements": [
      "linux"
    ],
    "description": "A semantic personal publishing platform with a focus on aesthetics, web standards, and usability",
    "created": "2015-04-30 14:09:40.247173",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "Port",
        "name": "http",
        "value": "80",
        "visibility": "public"
      },
      {
        "required": false,
        "type": "Port",
        "name": "https",
        "value": "443",
        "visibility": "public"
      },
      {
        "automatic_updates": "off",
        "name": "chef_cookbook",
        "required": false,
        "visibility": "public",
        "value": "391e2946-552d-47b3-8551-d414ed47a97f",
        "type": "Box"
      },
      {
        "name": "CHEF_DEFAULT_RB",
        "required": false,
        "value": "/services/blobs/download/554237a3da3116443909ebc7/default.rb",
        "visibility": "public",
        "scope": "chef_cookbook",
        "type": "File"
      },
      {
        "name": "CHEF_METADATA_RB",
        "required": false,
        "value": "/services/blobs/download/554237a3da3116443909ebc9/metadata.rb",
        "visibility": "public",
        "scope": "chef_cookbook",
        "type": "File"
      },
      {
        "name": "COOKBOOK_LIST",
        "required": false,
        "value": "/services/blobs/download/554237a4da3116443909ebcb/Cookbooks.config",
        "visibility": "public",
        "scope": "chef_solo",
        "type": "File"
      },
      {
        "name": "CHEF_SOLO_JSON",
        "required": false,
        "value": "/services/blobs/download/554237a4da3116443909ebcd/solo.json",
        "visibility": "public",
        "scope": "chef_solo",
        "type": "File"
      },
      {
        "automatic_updates": "off",
        "name": "chef_solo",
        "required": false,
        "visibility": "public",
        "value": "02d1c985-04fb-41a5-83c0-cff13f02a80b",
        "type": "Box"
      }
    ],
    "uri": "/services/boxes/74325e01-eefd-4108-abad-b42791960f7e",
    "visibility": "public",
    "name": "Wordpress",
    "id": "74325e01-eefd-4108-abad-b42791960f7e",
    "members": [],
    "owner": "public",
    "organization": "public",
    "events": {},
    "draft_from": "412f1e21-02cb-4c51-aafd-7e0b1eff6122",
    "icon": "images/platform/wordpress.png"
  }
]
```

### POST/services/boxes

Creates a new box in the personal workspace and gets the created box.

**Normal Response Codes**

* 200

**Error Response Codes**

* Invalid Data (400)
* Conflict (409)

**Request parameters**

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| requirements | plain | array | Box requirements. |
| owner | plain | string | Box owner, the user name for a personal workspace and the workspace name for a team workspace. |
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| name | plain | string | Box name. |
| description | plain | string | Box description. |
| icon | plain | string | Icon url. |
| schema | plain | string | Box schema. |

**Response parameters**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
    "owner": "project",
    "schema":"http://elasticbox.net/schemas/boxes/script",
    "requirements":["linux"],
    "automatic_updates":"off",
    "name":"Wordpress Starter Box",
    "description":"Wordpress Started for our showcase"
}
```

**Response parameters**

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| organization | plain | string | Organization to which the box belongs. |
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| requirements | plain | array | Box requirements. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| id | plain | array | Box unique identificator. |
| schema | plain | string | Box schema uri. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| icon | plain | string | Box icon uri. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the parameters: url, upload_date, length and destination_path. |
| name | plain | string | Box name. |

```
{
  "updated": "2015-07-02 16:20:35.534878",
  "automatic_updates": "off",
  "description": "Wordpress Started for our showcase",
  "deleted": null,
  "variables": [],
  "visibility": "workspace",
  "members": [],
  "owner": "project",
  "id": "60cef61c-73dc-41d9-a32f-70f49a509c66",
  "requirements": [
    "linux"
  ],
  "name": "Wordpress Starter Box",
  "created": "2015-07-02 16:20:35.534878",
  "uri": "/services/boxes/60cef61c-73dc-41d9-a32f-70f49a509c66",
  "organization": "elasticbox",
  "events": {},
  "schema": "http://elasticbox.net/schemas/boxes/script"
}
```

### GET /services/boxes/{box_id}

Fetches an existing box, requires the specified id box_id.

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

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| organization | plain | string | Organization to which the box belongs. |
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| requirements | plain | array | Box requirements. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| id | plain | array | Box unique identificator. |
| schema | plain | string | Box schema uri. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| icon | plain | string | Box icon uri. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the  parameters: url, upload_date, length and destination_path. |
| name | plain | string | Box name. |

```
{
  "schema": "http://elasticbox.net/schemas/boxes/script",
  "updated": "2015-07-02 16:20:35.534878",
  "automatic_updates": "off",
  "requirements": [
    "linux"
  ],
  "description": "Wordpress Started for our showcase",
  "created": "2015-07-02 16:20:35.534878",
  "deleted": null,
  "variables": [],
  "uri": "/services/boxes/60cef61c-73dc-41d9-a32f-70f49a509c66",
  "visibility": "workspace",
  "events": {},
  "members": [],
  "owner": "project",
  "organization": "elasticbox",
  "id": "60cef61c-73dc-41d9-a32f-70f49a509c66",
  "name": "Wordpress Starter Box"
}
```

### PUT /services/boxes/{box_id}

Requires the box ID to update an existing box. The request body must contain the box object and can only update the following fields: files, variables, ports, requirements, description, icon, name, events, and members.

**Normal Response Codes**
* 200

**Error Response Codes**
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

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| requirements | plain | array | Box requirements. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| id | plain | array | Box unique identificator. |
| schema | plain | string | Box schema uri. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| icon | plain | string | Box icon uri. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the  parameters: url, upload_date, length and destination_path. |
| name | plain | string | Box name. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
    "schema":"http://elasticbox.net/schemas/boxes/script",
    "updated":"2015-07-02 16:23:46.702968",
    "automatic_updates":"off",
    "requirements":[
        "linux"
    ],
    "description":"Wordpress Started box",
    "created":"2015-07-02 16:20:15.098554",
    "deleted":null,
    "variables":[
        {
            "required":false,
            "type":"Text",
            "name":"Text_var",
            "value":"Default value",
            "visibility":"public"

        },
        {
            "required":true,
            "type":"Port",
            "name":"Port_variable",
            "value":"80",
            "visibility":"public"

        },{
            "automatic_updates":"off",
            "name":"Wordpress_base",
            "required":false,
            "value":"412f1e21-02cb-4c51-aafd-7e0b1eff6122",
            "visibility":"internal",
            "type":"Box"

        },
        {
            "name":"Binding_db",
            "type":"Binding",
            "value":"2a7a5f6b-280d-47de-afaa-65db5dd85816",
            "visibility":"public"

        }
        ],
        "uri":"/services/boxes/9192cb3e-04e2-4c50-b8a5-a25c980479d4",
        "visibility":"workspace",
        "events":{},
        "members":[],
        "owner":"project",
        "organization":"elasticbox",
        "id":"60cef61c-73dc-41d9-a32f-70f49a509c66",
        "name":"Wordpress Starter Box"
}

```

**Response Parameters**

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| organization | plain | string | Organization to which the box belongs. |
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| requirements | plain | array | Box requirements. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| id | plain | array | Box unique identificator. |
| schema | plain | string | Box schema uri. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| icon | plain | string | Box icon uri. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the  parameters: url, upload_date, length and destination_path. |
| name | plain | string | Box name. |

```
{
  "updated": "2015-07-02 16:28:13.181040",
  "automatic_updates": "off",
  "requirements": [
    "linux"
  ],
  "description": "Wordpress Started box",
  "name": "Wordpress Starter Box",
  "created": "2015-07-02 16:20:35.534878",
  "deleted": null,
  "variables": [
    {
      "required": false,
      "type": "Text",
      "name": "Text_var",
      "value": "Default value",
      "visibility": "public"
    },
    {
      "required": true,
      "type": "Port",
      "name": "Port_variable",
      "value": "80",
      "visibility": "public"
    },
    {
      "value": "412f1e21-02cb-4c51-aafd-7e0b1eff6122",
      "automatic_updates": "off",
      "name": "Wordpress_base",
      "required": false,
      "type": "Box",
      "visibility": "internal"
    },
    {
      "value": "2a7a5f6b-280d-47de-afaa-65db5dd85816",
      "required": false,
      "type": "Binding",
      "name": "Binding_db",
      "visibility": "public"
    }
  ],
  "uri": "/services/boxes/60cef61c-73dc-41d9-a32f-70f49a509c66",
  "visibility": "workspace",
  "id": "60cef61c-73dc-41d9-a32f-70f49a509c66",
  "members": [],
  "owner": "project",
  "organization": "elasticbox",
  "events": {},
  "schema": "http://elasticbox.net/schemas/boxes/script"
}
```

### DELETE /services/boxes/{box_id}

Deletes an existing box, requires the specified id box_id.

**Normal Response Codes**
* 204

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

### GET /services/boxes/{box_id}/stack

Gets the box stack. The box stack is a list of boxes. All boxes that are a box variable of the given box are included. The first box is always the given box.

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

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| organization | plain | string | Organization to which the box belongs. |
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| tags | plain | array | Box tags. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| id | plain | array | Box unique identificator. |
| schema | plain | string | Box schema uri. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| icon | plain | string | Box icon uri. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the  parameters: url, upload_date, length and destination_path. |
| name | plain | string | Box name. |

```

[
  {
    "updated": "2015-05-27 08:25:49.655298",
    "automatic_updates": "off",
    "requirements": [
      "linux"
    ],
    "description": "Cookbook with a simple recipe",
    "icon": "images/platform/chef-cookbook.png",
    "created": "2015-04-30 14:09:40.247173",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "Text",
        "name": "CHEF_COOKBOOK_NAME",
        "value": "elasticbox",
        "visibility": "public"
      },
      {
        "required": false,
        "type": "File",
        "name": "CHEF_DEFAULT_RB",
        "value": "/services/blobs/download/554237a3da3116443909eb9f/default.rb",
        "visibility": "public"
      },
      {
        "required": false,
        "type": "File",
        "name": "CHEF_METADATA_RB",
        "value": "/services/blobs/download/554237a3da3116443909eba1/metadata.rb",
        "visibility": "public"
      }
    ],
    "uri": "/services/boxes/31689659-fed1-49f0-ac31-379d192751be",
    "visibility": "public",
    "name": "Chef Cookbook",
    "version": {
      "box": "391e2946-552d-47b3-8551-d414ed47a97f",
      "description": "Initial Cloud Application Manager Version",
      "workspace": "public",
      "number": {
        "major": 1,
        "minor": 0,
        "patch": 0
      }
    },
    "id": "31689659-fed1-49f0-ac31-379d192751be",
    "members": [],
    "owner": "public",
    "organization": "public",
    "events": {
      "pre_configure": {
        "url": "/services/blobs/download/554237a3da3116443909eb9d/pre_configure",
        "upload_date": "2015-04-30 14:09:39.701080",
        "length": 252,
        "destination_path": "scripts",
        "content_type": null
      }
    },
    "schema": "http://elasticbox.net/schemas/boxes/script"
  },
        ....
  {
    "updated": "2015-05-27 08:25:49.687260",
    "automatic_updates": "off",
    "requirements": [
      "linux"
    ],
    "description": "Opscode Chef client",
    "icon": "images/platform/chef.png",
    "created": "2015-04-30 14:09:40.247173",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "File",
        "name": "CHEF_SOLO_JSON",
        "value": "/services/blobs/download/554237a3da3116443909ebbb/solo.json",
        "visibility": "public"
      },
      {
        "required": false,
        "type": "File",
        "name": "CHEF_SOLO_RB",
        "value": "/services/blobs/download/554237a3da3116443909ebbd/solo.rb",
        "visibility": "public"
      },
      {
        "required": false,
        "type": "File",
        "name": "COOKBOOK_LIST",
        "value": "/services/blobs/download/554237a3da3116443909ebbf/Cookbooks.config",
        "visibility": "public"
      }
    ],
    "uri": "/services/boxes/860e943e-bb69-416c-ba6e-06099dd5f7ea",
    "visibility": "public",
    "name": "Chef Solo",
    "version": {
      "box": "02d1c985-04fb-41a5-83c0-cff13f02a80b",
      "description": "Initial Cloud Application Manager Version",
      "workspace": "public",
      "number": {
        "major": 1,
        "minor": 0,
        "patch": 0
      }
    },
    "id": "860e943e-bb69-416c-ba6e-06099dd5f7ea",
    "members": [],
    "owner": "public",
    "organization": "public",
    "events": {
      "pre_install": {
        "url": "/services/blobs/download/554237a3da3116443909ebb7/pre_install",
        "upload_date": "2015-04-30 14:09:39.904687",
        "length": 1033,
        "destination_path": "scripts",
        "content_type": null
      },
      "pre_configure": {
        "url": "/services/blobs/download/554237a3da3116443909ebb9/pre_configure",
        "upload_date": "2015-04-30 14:09:39.908203",
        "length": 182,
        "destination_path": "scripts",
        "content_type": null
      }
    },
    "schema": "http://elasticbox.net/schemas/boxes/script"
  }
]

```

### GET /services/boxes/{box_id}/bindings

Gets a list of box objects that are bindings of the request box, requires the specified id box_id.

**Normal Response Codes**
* 200

**Error Response Codes**
* Bad Request (400)
* Request

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| uri | plain | string | Box uri. |
| id | plain | array | Box unique identificator. |
| icon | plain | string | Box icon uri. |
| name | plain | string | Box name. |

```
[
  {
    "id": "2a7a5f6b-280d-47de-afaa-65db5dd85816",
    "uri": "/services/boxes/2a7a5f6b-280d-47de-afaa-65db5dd85816",
    "name": "MongoDB Server",
    "icon": "images/platform/mongodb.png"
  }
]
```

### GET /services/boxes/{box_id}/versions

Gets a list of box versions, requires the specified id box_id. If the box is unversioned is the empty list.

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

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| tags | plain | array | Box tags. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| id | plain | array | Box unique identificator. |
| icon | plain | string | Box icon uri. |
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| organization | plain | string | Organization to which the box belongs. |
| name | plain | string | Box name. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| version | plain | object | The box version object contains the parameters box, description and workspace. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the  parameters: url, upload_date, length and destination_path. |
| schema | plain | string | Box schema uri. |

```
[
  {
    "schema": "http://elasticbox.net/schemas/boxes/script",
    "updated": "2015-07-02 16:28:13.181040",
    "automatic_updates": "off",
    "requirements": [
      "linux"
    ],
    "description": "Wordpress Started box",
    "created": "2015-07-02 16:36:30.325064",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "Text",
        "name": "Text_var",
        "value": "Default value",
        "visibility": "public"
      },
      {
        "required": true,
        "type": "Port",
        "name": "Port_variable",
        "value": "80",
        "visibility": "public"
      },
      {
        "automatic_updates": "off",
        "name": "Wordpress_base",
        "required": false,
        "value": "412f1e21-02cb-4c51-aafd-7e0b1eff6122",
        "visibility": "internal",
        "type": "Box"
      },
      {
        "required": false,
        "type": "Binding",
        "name": "Binding_db",
        "value": "2a7a5f6b-280d-47de-afaa-65db5dd85816",
        "visibility": "public"
      }
    ],
    "uri": "/services/boxes/ca197de8-25e1-4e9b-9d45-c99a049249fc",
    "visibility": "workspace",
    "events": {},
    "version": {
      "box": "60cef61c-73dc-41d9-a32f-70f49a509c66",
      "number": {
        "major": 0,
        "minor": 1,
        "patch": 0
      },
      "workspace": "operations",
      "description": "Initial version"
    },
    "members": [],
    "owner": "project",
    "organization": "elasticbox",
    "id": "ca197de8-25e1-4e9b-9d45-c99a049249fc",
    "name": "Wordpress Starter Box"
  }
]
```

### PUT /services/boxes/{box_id}/diff

Compares a box to the submitted box, requires the specified id box_id.

**Normal Response Codes**
* 200

**Error Response Codes**
* Forbidden (403)
* Not Found (404)

**Request parameters**

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| updated | plain | string | Date of the last update. |
| description | plain | string | Box description. |
| tags | plain | array | Box tags. |
| variables | plain | array | List of box variables, each variable object contains the parameters: type, name and value. |
| members | plain | array | List of Box members. |
| owner | plain | string | Box owner. |
| id | plain | array | Box unique identificator. |
| icon | plain | string | Box icon uri. |
| visibility | plain | string | Indicates at what level the box is visible. By default, boxes are visible to the workspace they’re created in. Can have one of these values: <li>public: Visible to Cloud Application Manager users across all organizations.</li> <li>organization: Visible to all users in the organization where the box was created.</li> <li>workspace: By default, the box is visible only to members of the workspace where it was created.</li> |
| organization | plain | string | Organization to which the box belongs. |
| name | plain | string | Box name. |
| created | plain | string | Creation date. |
| uri | plain | string | Box uri. |
| version | plain | object | The box version object contains the parameters box, description and workspace. |
| events | plain | array | List of Box events, there may be nine event lists: configure, dispose, install, pre_configure, pre_dispose, pre_install, pre_start, pre_stop, start and stop. |
| event | plain | object | Event contained in one of the event lists, each event object contains the  parameters: url, upload_date, length and destination_path. |
| schema | plain | string | Box schema uri. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
  "updated": "2015-07-02 16:36:30.348041",
  "automatic_updates": "off",
  "requirements": [
    "linux",
    "new_requirement"
  ],
  "description": "Wordpress Started box proposal",
  "name": "Wordpress Starter Box",
  "created": "2015-07-02 16:20:35.534878",
  "deleted": null,
  "variables": [
    {
      "required": false,
      "type": "Text",
      "name": "Text_var",
      "value": "Default value",
      "visibility": "public"
    },
    {
      "required": true,
      "type": "Port",
      "name": "Port_variable_renamed",
      "value": "80",
      "visibility": "public"
    },
    {
      "automatic_updates": "off",
      "name": "Wordpress_base",
      "required": false,
      "value": "412f1e21-02cb-4c51-aafd-7e0b1eff6122",
      "visibility": "internal",
      "type": "Box"
    },
    {
      "required": false,
      "type": "Binding",
      "name": "Binding_db",
      "value": "2a7a5f6b-280d-47de-afaa-65db5dd85816",
      "visibility": "public"
    },
    {
      "required": false,
      "type": "Text",
      "name": "Text_var2",
      "value": "Default value",
      "visibility": "public"
    }
  ],
  "uri": "/services/boxes/60cef61c-73dc-41d9-a32f-70f49a509c66",
  "visibility": "workspace",
  "id": "60cef61c-73dc-41d9-a32f-70f49a509c66",
  "members": [],
  "owner": "project",
  "organization": "elasticbox",
  "events": {},
  "draft_from": "ca197de8-25e1-4e9b-9d45-c99a049249fc",
  "schema": "http://elasticbox.net/schemas/boxes/script"
}

```


**Response parameters**

| Parameter | Style | Type | Description |
|-----------|-------|------|-------------|
| box_variables | plain | object | Differences in the box variables, the object contains a title and three lists: removed, added and changed. |
| box_variables.removed | plain | array | List of box variables removed, each variable object contains the parameters: type, name and value. |
| box_variables.added | plain | array | List of box variables added, each variable object contains the parameters: type, name and value. |
| box_variables.changed | plain | array | List of box variables changed, each variable object contains the parameters: type, name and value. |
| box_details | plain | object | Differences in the box details, the object contains a title and three lists: removed, added and changed. |
| box_profile_properties | plain | object | Differences in the box profile properties, the object contains a title and three lists: removed, added and changed. Available for Policy boxes. |
| box_events | plain | array | List of box events. |
| changed | plain | boolean | There have been changes between versions. |


```
{
  "box_profile_properties": {
    "removed": [],
    "added": [],
    "changed": []
  },
  "box_details": {
    "title": "Modified Box Details",
    "removed": [],
    "added": [],
    "changed": [
      {
        "new": "Wordpress Started box proposal",
        "name": "Description",
        "previous": "Wordpress Started box"
      },
      {
        "new": "linux, new_requirement",
        "name": "Requirements",
        "previous": "linux"
      }
    ]
  },
  "box_events": [],
  "box_variables": {
    "title": "Modified Variables",
    "removed": [
      {
        "required": true,
        "type": "Port",
        "name": "Port_variable",
        "value": "80",
        "visibility": "public"
      }
    ],
    "files_diff": [],
    "added": [
      {
        "required": true,
        "type": "Port",
        "name": "Port_variable_renamed",
        "value": "80",
        "visibility": "public"
      },
      {
        "required": false,
        "type": "Text",
        "name": "Text_var2",
        "value": "Default value",
        "visibility": "public"
      }
    ],
    "changed": []
  },
  "box_readme": [],
  "changed": true
}
```

### Create and Launch a CloudFormation Box

**Create a CloudFormation box with template**

1. [POST /services/boxes](./api-boxes.md)
Creates a box of the CloudFormation service type. See example create a CloudFormation.

2. [GET /services/blobs/download/{file_id}/{file_name}](./api-blobs.md)
Fetches contents from a given file or URL. See example create a CloudFormation, part 2.
Submits a blank JSON template as a blob.

3. [POST /services/blobs/upload/{file_name}](./api-blobs.md)
Creates a blob from template data submitted through a file or URL. Here template data is in the request body. See example create a CloudFormation, part 3.

4. [PUT /services/boxes/{box_id}](./api-boxes.md)
Updates the CloudFormation box with the template. See example create a CloudFormation, part 4.

**Modify the CloudFormation Template**

1. [POST /services/blobs/upload/{file_name}](./api-blobs.md)
Creates a blob from modified template data. See example modify a CloudFormation.

2. [PUT /services/boxes/{box_id}](./api-boxes.md)
Updates the CloudFormation box. See example modify a CloudFormation, part 2.

**Delete a CloudFormation Box**

1. [DELETE /services/box/{box_id}](./api-blobs.md)
Removes the CloudFormation box from the boxes catalog.

**Launch a CloudFormation Box**

1. [POST /services/profiles](./api-blobs.md)
This step is optional. Passes deployment settings in a new deployment profile to launch the box in the provider’s infrastructure. See example launch a CloudFormation.

2. [POST /services/instances](./instances-api.md)
Creates a new instance of the CloudFormation box.

**Update a CloudFormation Stack in Real-Time**

1. [POST /services/blobs/upload](./api-blobs.md)
Uploads the modified template data. See example update a CloudFormation.

2. [PUT /services/instances/{instance_id}](./instances-api.md)
Updates the instance with the template changes. See example update a CloudFormation part 2.

3. [PUT /services/instances/{instance_id}/reconfigure](./instances-api.md)
Reconfigures the stack based on the changes. See example update a CloudFormation part 3.

### Example: Create a CloudFormation box with template

**1. POST https://cam.ctl.io/services/boxes/**

Creating a box of the CloudFormation service type.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:
{
    "owner": "operations",
    "schema":"http://elasticbox.net/schemas/boxes/cloudformation",
    "automatic_updates":"off",
    "name":"Wordpress Starter CF",
    "description":"Wordpress Started for our showcase"
}
```

**Response**

```
{
    "updated": "2015-10-28 11:24:01.854958",
    "automatic_updates": "off",
    "description": "Wordpress Started for our showcase",
    "deleted": null,
    "variables": [],
    "visibility": "workspace",
    "members": [],
    "owner": "operations",
    "id": "262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "requirements": [],
    "name": "Wordpress Starter CF",
    "created": "2015-10-28 11:24:01.854958",
    "uri": "/services/boxes/262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "organization": "elasticbox",
    "type": "CloudFormation Service",
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation"
}

```

**2. GET https://cam.ctl.io/services/blobs/download/{blob_id}/file_name**

Fetches contents from a given URL. Once we have checked that the template is the right one, we could assign it to the CloudFormation box.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response**

```
{
   "AWSTemplateFormatVersion":"2010-09-09",
   "Description":"AWS CloudFormation Sample Template WordPress_Single_Instance_With_RDS: WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using an Amazon RDS database instance for storage. It demonstrates using the AWS CloudFormation bootstrap scripts to install packages and files at instance launch time. **WARNING** This template creates an Amazon EC2 instance and an Amazon RDS database instance. You will be billed for the AWS resources used if you create a stack from this template.",
   "Parameters":{
      "KeyName":{
         "Description":"Name of an existing EC2 KeyPair to enable SSH access to the instances",
         "Type":"String",
         "MinLength":"1",
         "MaxLength":"255",
         "AllowedPattern":"[\\x20-\\x7E]*",
         "ConstraintDescription":"can contain only ASCII characters."
      },
    ...
   }
...
...

   "Outputs":{
      "WebsiteURL":{
         "Value":{
            "Fn::Join":[
               "",
               [
                  "http://",
                  {
                     "Fn::GetAtt":[
                        "WebServer",
                        "PublicDnsName"
                     ]
                  },
                  "/wordpress"
               ]
            ]
         },
         "Description":"WordPress Website"
      }
   }
}
```

**3. POST https://cam.ctl.io/services/blobs/upload/template.json**

Another option is to create the template from the data submitted through a URL.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
   "AWSTemplateFormatVersion":"2010-09-09",
   "Description":"AWS CloudFormation Sample Template WordPress_Single_Instance_With_RDS: WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using an Amazon RDS database instance for storage. It demonstrates using the AWS CloudFormation bootstrap scripts to install packages and files at instance launch time. **WARNING** This template creates an Amazon EC2 instance and an Amazon RDS database instance. You will be billed for the AWS resources used if you create a stack from this template.",
   "Parameters":{
      "KeyName":{
         "Description":"Name of an existing EC2 KeyPair to enable SSH access to the instances",
         "Type":"String",
         "MinLength":"1",
         "MaxLength":"255",
         "AllowedPattern":"[\\x20-\\x7E]*",
         "ConstraintDescription":"can contain only ASCII characters."
      },
    ...
   },
...
...
   "Outputs":{
      "WebsiteURL":{
         "Value":{
            "Fn::Join":[
               "",
               [
                  "http://",
                  {
                     "Fn::GetAtt":[
                        "WebServer",
                        "PublicDnsName"
                     ]
                  },
                  "/wordpress"
               ]
            ]
         },
         "Description":"WordPress Website"
      }
   }
}

```

**Response**

```
{
   "url":"/services/blobs/download/536a9e867d0083771808bacd/template.json",
   "upload_date":"2014-05-07 20:58:46.650140",
   "length":9739,
   "content_type":"text/x-shellscript"
}
```

**4. PUT https://cam.ctl.io/services/boxes/{box_id}**

Finally we are going to update the CloudFormation box with one of the templates we have obtained in the last two steps.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
    "automatic_updates": "off",
    "requirements": [],
    "description": "Wordpress Started for our showcase",
    "deleted": null,
    "variables": [],
    "uri": "/services/boxes/262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "visibility": "workspace",
    "members": [],
    "owner": "operations",
    "organization": "elasticbox",
    "type": "CloudFormation Service",
    "id": "262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "name": "Wordpress Starter CF",
    "template": {
        "url": "/services/blobs/download/536a9e867d0083771808bacd/template.json"
    }
}
```

**Response**

```
{
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
    "updated": "2015-10-28 12:03:32.661399",
    "automatic_updates": "off",
    "requirements": [],
    "description": "Wordpress Started for our showcase",
    "created": "2015-10-28 11:24:01.854958",
    "deleted": null,
    "variables": [
        {
            "value": "",
            "type": "Text",
            "name": "KeyName",
            "visibility": "public"
        },
        {
            "value": "",
            "type": "Text",
            "name": "SourceCidrForRDP",
            "visibility": "public"
        },
        {
            "value": "m1.large",
            "type": "Text",
            "name": "InstanceType",
            "visibility": "public"
        }
    ],
    "uri": "/services/boxes/262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "visibility": "workspace",
    "template": {
        "url": "/services/blobs/download/536a9e867d0083771808bacd/template.json"
    },
    "members": [],
    "owner": "operations",
    "organization": "elasticbox",
    "type": "CloudFormation Service",
    "id": "262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "name": "Wordpress Starter CF"
}
```

### Example: Modify the CloudFormation Template

**1. POST http://cam.ctl.io/services/blobs/upload/template.json**

Creates a blob from modified template data.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "AWS CloudFormation Sample Template WordPress_Single_Instance_With_RDS: WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using an Amazon RDS database instance for storage. It demonstrates using the AWS CloudFormation bootstrap scripts to install packages and files at instance launch time. **WARNING** This template creates an Amazon EC2 instance and an Amazon RDS database instance. You will be billed for the AWS resources used if you create a stack from this template.",
    "Parameters": {
        "KeyName": {
            "Description": "Name of an existing EC2 KeyPair to enable SSH access to the instances",
            "Type": "String",
            "MinLength": "1",
            "MaxLength": "255",
            "AllowedPattern": "[\\x20-\\x7E]*",
            "ConstraintDescription": "can contain only ASCII characters."
        },
       ...
    },
…
…
    "Outputs": {
        "WebsiteURL": {
            "Value": {
                "Fn::Join": [
                    "",
                    [
                        "http://",
                        {
                            "Fn::GetAtt": [
                                "WebServer",
                                "PublicDnsName"
                            ]
                        },
                        "/wordpress"
                    ]
                ]
            },
            "Description": "WordPress Website"
        }
    }
}
```

**Response**

```
{
   "url":"/services/blobs/download/536bd5619ac37b2f70318a87/template.json",
   "upload_date":"2014-05-08 19:05:05.761144",
   "length":15922,
   "content_type":"text/x-shellscript"
}
```

**2. PUT http://cam.ctl.io/services/boxes/{box_id}**

Updates the CloudFormation box.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
    "automatic_updates": "off",
    "requirements": [],
    "description": "Wordpress Started for our showcase",
    "deleted": null,
    "variables": [],
    "uri": "/services/boxes/262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "visibility": "workspace",
    "members": [],
    "owner": "operations",
    "organization": "elasticbox",
    "type": "CloudFormation Service",
    "id": "262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "name": "Wordpress Starter CF",
    "template": {
        "url": "//services/blobs/download/536bd5619ac37b2f70318a87/template.json"
    }
}
```

**Response**

```
{
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
    "updated": "2015-10-28 12:03:32.661399",
    "automatic_updates": "off",
    "requirements": [],
    "description": "Wordpress Started for our showcase",
    "created": "2015-10-28 11:24:01.854958",
    "deleted": null,
    "variables": [
        {
            "value": "",
            "type": "Text",
            "name": "KeyName",
            "visibility": "public"
        },
        {
            "value": "",
            "type": "Text",
            "name": "SourceCidrForRDP",
            "visibility": "public"
        },
        {
            "value": "m1.large",
            "type": "Text",
            "name": "InstanceType",
            "visibility": "public"
        }
    ],
    "uri": "/services/boxes/262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "visibility": "workspace",
    "template": {
        "url": "/services/blobs/download/536bd5619ac37b2f70318a87/template.json"
    },
    "members": [],
    "owner": "operations",
    "organization": "elasticbox",
    "type": "CloudFormation Service",
    "id": "262d4cbe-9ad9-4069-b6a8-76fda70a4d90",
    "name": "Wordpress Starter CF"
}
```

### Example: Launch a CloudFormation Box

**1. POST https://cam.ctl.io/services/instances**

Creates a new instance of the CloudFormation box.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
  "schema": "http://elasticbox.net/schemas/deploy-instance-request",
  "owner": "operations",
  "name": "CF WordPress 2",
  "box": {
    "id": "91645eed-173f-4aac-a713-69c6be7582fe",
    "variables": [

    ]
  },
  "instance_tags": [

  ],
  "automatic_updates": "off",
  "policy_box": {
    "id": "91645eed-173f-4aac-a713-69c6be7582fe",
    "variables": [
      {
        "name": "provider_id",
        "value": "7e841966-1dec-4460-a981-1db4e1eec10c",
        "type": "Text"
      },
      {
        "name": "location",
        "value": "ap-northeast-1",
        "type": "Text"
      }
    ]
  }
}
```

**Response**

```
{
  "box": "91645eed-173f-4aac-a713-69c6be7582fe",
  "policy_box": {
    "profile": {
      "location": "ap-northeast-1",
      "schema": "http://elasticbox.net/schemas/aws/cloudformation/profile"
    },
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
    "updated": "2015-10-28 13:46:55.247211",
    "automatic_updates": "off",
    "requirements": [

    ],
    "description": "CF test",
    "created": "2015-10-27 12:11:24.734064",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "Binding",
        "name": "Binding",
        "value": "5030fc49-773a-42fa-b569-c551e4f90d77",
        "visibility": "private"
      }
    ],
    "provider_id": "7e841966-1dec-4460-a981-1db4e1eec10c",
    "visibility": "workspace",
    "members": [

    ],
    "template": {
      "url": "/services/blobs/download/5630d1cf14841250525226a6/template.json",
      "upload_date": "2015-10-28 13:46:55.186875",
      "length": 104,
      "content_type": "text/x-shellscript"
    },
    "owner": "operations",
    "organization": "elasticbox",
    "type": "CloudFormation Service",
    "id": "91645eed-173f-4aac-a713-69c6be7582fe",
    "name": "CF WordPress 2"
  },
  "updated": "2015-10-28 13:47:15.567441",
  "automatic_updates": "off",
  "name": "CF WordPress 2",
  "service": {
    "type": "CloudFormation Service",
    "id": "eb-5cn45",
    "machines": [

    ]
  },
  "tags": [

  ],
  "deleted": null,
  "variables": [

  ],
  "created": "2015-10-28 13:47:15.567441",
  "state": "processing",
  "uri": "/services/instances/i-ywf1hu",
  "boxes": [
    {
      "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
      "updated": "2015-10-28 13:46:55.247211",
      "automatic_updates": "off",
      "requirements": [

      ],
      "description": "CF test",
      "created": "2015-10-27 12:11:24.734064",
      "deleted": null,
      "variables": [
        {
          "required": false,
          "type": "Binding",
          "name": "Binding",
          "value": "5030fc49-773a-42fa-b569-c551e4f90d77",
          "visibility": "private"
        }
      ],
      "visibility": "workspace",
      "members": [

      ],
      "template": {
        "url": "/services/blobs/download/5630d1cf14841250525226a6/template.json",
        "upload_date": "2015-10-28 13:46:55.186875",
        "length": 104,
        "content_type": "text/x-shellscript"
      },
      "owner": "operations",
      "organization": "elasticbox",
      "type": "CloudFormation Service",
      "id": "91645eed-173f-4aac-a713-69c6be7582fe",
      "name": "CF WordPress 2"
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
    "created": "2015-10-28 13:47:15.564698"
  },
  "schema": "http://elasticbox.net/schemas/instance",
  "id": "i-ywf1hu",
  "icon": null
}
```

### Example: Update a CloudFormation Stack in Real-Time

**1. POST http://cam.ctl.io/services/blobs/upload/simple_template.json**

Uploads the modified template data.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
    "Resources" : {
        "HelloBucket" : {
            "Type" : "AWS::S3::Bucket"
        }
    }
}

```

**Response**

```
{
    "url": "/services/blobs/download/5630d61d14841250525226aa/simple_template.json",
    "upload_date": "2015-10-28 14:05:17.752627",
    "length": 0,
    "content_type": "application/json"
}
```

**2. PUT http://cam.ctl.io/services/instances/{instance_id}**

Updates the instance with the template changes.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
{
  "box": "91645eed-173f-4aac-a713-69c6be7582fe",
  "bindings": [

  ],
  "updated": "2015-10-28 13:48:24.367626",
  "automatic_updates": "off",
  "name": "CF WordPress 2",
  "service": {
    "type": "CloudFormation Service",
    "id": "eb-5cn45",
    "machines": [

    ]
  },
  "tags": [

  ],
  "deleted": null,
  "policy_box": {
    "profile": {
      "location": "ap-northeast-1",
      "schema": "http://elasticbox.net/schemas/aws/cloudformation/profile"
    },
    "updated": "2015-10-28 13:46:55.247211",
    "automatic_updates": "off",
    "requirements": [

    ],
    "description": "CF test",
    "created": "2015-10-27 12:11:24.734064",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "Binding",
        "name": "Binding",
        "value": "5030fc49-773a-42fa-b569-c551e4f90d77",
        "visibility": "private"
      }
    ],
    "provider_id": "7e841966-1dec-4460-a981-1db4e1eec10c",
    "visibility": "workspace",
    "template": {
      "url": "/services/blobs/download/5630d1cf14841250525226a6/template.json",
      "upload_date": "2015-10-28 13:46:55.186875",
      "length": 104,
      "content_type": "text/x-shellscript"
    },
    "members": [

    ],
    "owner": "operations",
    "organization": "elasticbox",
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
    "type": "CloudFormation Service",
    "id": "91645eed-173f-4aac-a713-69c6be7582fe",
    "name": "CF WordPress 2"
  },
  "created": "2015-10-28 13:47:15.567441",
  "uri": "/services/instances/i-ywf1hu",
  "state": "done",
  "boxes": [
    {
      "updated": "2015-10-28 13:46:55.247211",
      "automatic_updates": "off",
      "requirements": [

      ],
      "description": "CF test",
      "created": "2015-10-27 12:11:24.734064",
      "deleted": null,
      "variables": [
        {
          "required": false,
          "type": "Binding",
          "name": "Binding",
          "value": "5030fc49-773a-42fa-b569-c551e4f90d77",
          "visibility": "private"
        }
      ],
      "visibility": "workspace",
      "template": {
        "url": "/services/blobs/download/5630d61d14841250525226aa/simple_template.json",
        "upload_date": "2015-10-28 13:46:55.186875",
        "length": 104,
        "content_type": "text/x-shellscript"
      },
      "members": [

      ],
      "owner": "operations",
      "organization": "elasticbox",
      "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
      "type": "CloudFormation Service",
      "id": "91645eed-173f-4aac-a713-69c6be7582fe",
      "name": "CF WordPress 2"
    }
  ],
  "schema": "http://elasticbox.net/schemas/instance",
  "members": [

  ],
  "owner": "operations",
  "variables": [

  ],
  "operation": {
    "event": "deploy",
    "workspace": "operations",
    "created": "2015-10-28 13:47:15.746398"
  },
  "id": "i-ywf1hu",
  "icon": null
}
```

**Response**

```
{
  "box": "91645eed-173f-4aac-a713-69c6be7582fe",
  "bindings": [

  ],
  "updated": "2015-10-28 14:44:49.999798",
  "automatic_updates": "off",
  "name": "CF WordPress 2",
  "service": {
    "type": "CloudFormation Service",
    "id": "eb-5cn45",
    "machines": [

    ]
  },
  "tags": [

  ],
  "deleted": null,
  "policy_box": {
    "profile": {
      "location": "ap-northeast-1",
      "schema": "http://elasticbox.net/schemas/aws/cloudformation/profile"
    },
    "updated": "2015-10-28 13:46:55.247211",
    "automatic_updates": "off",
    "requirements": [

    ],
    "description": "CF test",
    "created": "2015-10-27 12:11:24.734064",
    "deleted": null,
    "variables": [
      {
        "required": false,
        "type": "Binding",
        "name": "Binding",
        "value": "5030fc49-773a-42fa-b569-c551e4f90d77",
        "visibility": "private"
      }
    ],
    "provider_id": "7e841966-1dec-4460-a981-1db4e1eec10c",
    "visibility": "workspace",
    "template": {
      "url": "/services/blobs/download/5630d1cf14841250525226a6/template.json",
      "upload_date": "2015-10-28 13:46:55.186875",
      "length": 104,
      "content_type": "text/x-shellscript"
    },
    "members": [

    ],
    "owner": "operations",
    "organization": "elasticbox",
    "schema": "http://elasticbox.net/schemas/boxes/cloudformation",
    "type": "CloudFormation Service",
    "id": "91645eed-173f-4aac-a713-69c6be7582fe",
    "name": "CF WordPress 2"
  },
  "created": "2015-10-28 13:47:15.567441",
  "uri": "/services/instances/i-ywf1hu",
  "state": "done",
  "boxes": [
    {
      "updated": "2015-10-28 13:46:55.247211",
      "automatic_updates": "off",
      "description": "CF test",
      "deleted": null,
      "variables": [
        {
          "required": false,
          "type": "Binding",
          "name": "Binding",
          "value": "5030fc49-773a-42fa-b569-c551e4f90d77",
          "visibility": "private"
        }
      ],
      "visibility": "workspace",
      "members": [

      ],
      "owner": "operations",
      "id": "91645eed-173f-4aac-a713-69c6be7582fe",
      "requirements": [

      ],
      "name": "CF WordPress 2",
      "created": "2015-10-27 12:11:24.734064",
      "template": {
        "url": "/services/blobs/download/5630d61d14841250525226aa/simple_template.json",
        "upload_date": "2015-10-28 13:46:55.186875",
        "length": 104,
        "content_type": "text/x-shellscript"
      },
      "organization": "elasticbox",
      "type": "CloudFormation Service",
      "schema": "http://elasticbox.net/schemas/boxes/cloudformation"
    }
  ],
  "schema": "http://elasticbox.net/schemas/instance",
  "members": [

  ],
  "owner": "operations",
  "variables": [

  ],
  "operation": {
    "event": "deploy",
    "workspace": "operations",
    "created": "2015-10-28 13:47:15.746398"
  },
  "id": "i-ywf1hu",
  "icon": null
}
```

**3. PUT http://cam.ctl.io/services/instances/{instance_id}/reconfigure**

Reconfigures the stack based on the changes.

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
   "id":"i-ywf1hu",
   "method":"reconfigure"
}
```

**Response**

None.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
