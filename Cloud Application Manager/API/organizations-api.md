{{{
"title": "Organizations API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Manage an Organization

| Resource | Description |
|----------|-------------|
| GET /services/organizations/{organization_name} | Gets the schema of the given organization. |
| PUT /services/organizations/{organization_name} | Updates an existing organization. |
| PUT /organizations/{organization_name}/sync_groups | Queues a request to sync LDAP groups. |

### GET /services/organizations/{organization_name}

Gets the schema of a given organization.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* User doesn’t belong to the organization (403)
* Not Found (404)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| schema |  string| Organization schema URI: **//elasticbox.net/schemas/organization** |
| name |    string   |  Organization name |
| icon | string |   Organization icon URI |
| updated | string | Date of the last update |
| created | string | Creation date |
| setup | boolean | This is read-only. It indicates that the Cloud Application Manager appliance is set up and ready for use. |
| administrators | array | List of users who can administer the organization |
| domains | string | Domains that are a part of the organization |
| authentication | object | List of the authentication methods to allow single sign-on in the organization. Contains the following properties:<li>github: Boolean. If enabled, it is true, else false.</li><li>google: Boolean. If enabled, it is true, else false.</li><li>password: Boolean. If enabled, it is true, else false.</li><li>ldap: Boolean. If enabled, it is true, else false.</li><li>ldap_config: Object that contains the LDAP service settings:</li><ul><li>ldap_group_sync: Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>sources: Array of [LDAP sources](../Administering Your Organization/user-authentication.md). Each source has the following properties:</li><ul><li>host: Required. String identifies the hostname or IP address of the LDAP service.</li><li>groups_dn: String specifies a fully qualified group name.</li><li>group_dn_filter: String defines an entity on the LDAP server. All groups are synchronised as children of this entity.</li><li>email_field: String specifies the email field name by which to look up users. Typically, this field is called email.</li><li>ldap_search_password: String specifies the password for the LDAP service account to look up users who try to log in</li><li>ldap_search_user: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul></ul> |
| ldap_last_sync_completed | string | Timestamp of the last successful LDAP group sync, for example, 2015-04-06 14:28:12.874910. Value is null if ldap_group_sync is set to false. |
| ldap_groups | array | List of objects, each of which is an LDAP group. Each group has two properties:<li>dn: String identifier for the group.</li><li>name: String name shown in the workspace web interface.</li> |
| providers | array | List of cloud providers the organization can enable to register and deploy. Each provider type has the following properties enabled:<li>Boolean value of true if enabled, else false.</li><li>type: String values of the supported cloud providers: Amazon Web Services, Openstack, VMWare vSphere, Google Compute, Microsoft Azure, Cloudstack, SoftLayer, VMware vCloud Director, Amazon Web Services GovCloud, Rackspace.</li><li>description: String that briefly enumerates the services from the cloud provider.</li><li>pricing: Array of pricing information for Linux and Windows compute instance types. Only available for Amazon Web Services.</li> |
| tags | array | List of [tags](../Administering Your Organization/resource-tags.md) applied on instances deployed to cloud providers from the organization. Each tag has three properties:<li>name: String you apply as a tag.</li><li>type: String identifies the type of tag whether an Cloud Application Manager object or a custom one. Allowed values are Box, Workspace, Provider, Environment, Email, User ID, Service Instance ID, Service ID, Workspace ID, Instance ID, Custom.</li><li>value: String value of null for Cloud Application Manager objects. For custom tags, set its value using this property.</li> |
| webhooks | array | List of webhooks that integrate with the organization. |
| cost_centers | array | List of cost centers. Each cost center contains the following properties:<li>enforce: Boolean. If true, an instance cannot be deployed if it is over the quota.</li><li>name: String. Name of the cost center</li><li>workspaces: Array. List of the names that belongs to the cost center.</li><li>quotas: List of quotas. Each quota contains an object with the following properties:</li><ul><li>cost: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>provider: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>allocated: Array. List of instances which are contributing to the current quota. Each allocated instance has these properties:</li> <ul><li>instance_id: Required. String. Id of the instance.</li><li>instances: Required. Int. Number of instances.</li><li>started: Required. String. Date when this instance was deployed.</li><li>flavor: Required. String. Type of instance.</li><li>region: Required. String. Region where it was deployed.</li><li>service_type: Required. String. Type of the service.</li><li>terminated: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul><li>resources: Object. Resources of the quota.</li><ul><li>cpu: Required. Int. Number of cpu units.</li><li>disk: Required. Object. A disk with these properties:</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb, Gb or Tb.</li></ul><li>ram: Required. String. Ram of the quota.</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb or Gb.</li> </ul>|

### Response Body

```
{
   {
   "schema":"http://elasticbox.net/schemas/organization",
   "name":"elasticbox",
   "icon":"/services/blobs/download/5452705c3bbd224ef9541c41/elasticbox.png",
   "theme":null,
   "updated":"2015-04-06 14:28:12.874910",
   "created":"2014-02-14 15:12:21.526672",
   "setup":true,
   "administrators":[
      "x",
      "a",
      "bc",
      "ca",
      "ce",
      "di",
      "el",
      "ig",
      "la",
      "ma",
      "mas",
      "mr",
      "os",
      "ra",
      "ri",
      "ri",
      "ys",
      "lu"
   ],
   "domains":[
      "cam.ctl.io"
   ],
   "authentication":{
      "github":false,
      "google":true,
      "ldap":true,
      "password":false,
      "ldap_config":{
         "sources":[
            {
               "host":"ldap://ldap.cam.ctl.io",
               "email_field":"mail"
            }
         ]
      }
   },
   "features":{
      "admin_boxes":true,
      "cost_center":true,
      "custom_pricing":false,
      "onboard_checklist":false,
      "provider_sharing":true,
      "reporting":true
   },
   "providers":[
      {
         "enabled":true,
         "type":"Amazon Web Services",
         "description":"Manage EC2, ECS and Cloudformation instances",
         "pricing":[
            {
               "platform":"Linux Compute",
               "price":7000,
               "region":"ap-southeast-2",
               "flavor":"i2.8xlarge",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            },
            {
               "platform":"Linux Compute",
               "price":5,
               "region":"us-east-1",
               "flavor":"t2.micro",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            },
            {
               "platform":"Windows Compute",
               "price":10,
               "region":"us-east-1",
               "flavor":"t2.micro",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            }
         ]
      },
      {
         "enabled":true,
         "type":"Openstack",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vSphere",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Google Compute",
         "description":"Manage cloud hosting and Linux machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Microsoft Azure",
         "description":"Manage compute services for Windows and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Cloudstack",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"SoftLayer",
         "description":"Manage compute services for Windows and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vCloud Director",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Amazon Web Services GovCloud",
         "description":"Manage compute services in an isolated ITAR compliant AWS region.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Rackspace",
         "description":"Manage cloud hosting and Linux machines.",
         "pricing":[

         ]
      }
   ],
   "tags":[
      {
         "name":"workspace",
         "type":"Workspace",
         "value":null
      },
      {
         "name":"box",
         "type":"Box",
         "value":null
      },
      {
         "name":"environment",
         "type":"Environment",
         "value":null
      },
      {
         "name":"email",
         "type":"Email",
         "value":null
      },
      {
         "name":"user",
         "type":"User ID",
         "value":null
      },
      {
         "name":"Name",
         "type":"Service Instance ID",
         "value":null
      }
   ],
   "cost_centers":[
      {
         "name":"test",
         "enforce":false,
         "quotas":[
            {
               "allocated":[

               ],
               "cost":0,
               "provider":"2bf1bd2c-b03d-460f-80da-647d26bdbcfe"
            },
            {
               "cost":3000,
               "provider":"5908ee9b-0c0a-4af6-8eef-2dc9f95d033a"
            }
         ],
         "workspaces":[
            "operations"
         ]
      }
   ],
   "webhooks":[

   ]
}
```

### PUT /services/organizations/{organization_name}

Updates an existing organization given its name. Only the organization administrator can update.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* User doesn’t belong to the organization (403)
* Not Found (404)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Request Body**

```
{
   "schema":"http://elasticbox.net/schemas/organization",
   "name":"elasticbox",
   "icon":"/services/blobs/download/5452705c3bbd224ef9541c41/elasticbox.png",
   "theme":null,
   "updated":"2015-04-06 14:28:12.874910",
   "created":"2014-02-14 15:12:21.526672",
   "setup":true,
   "administrators":[
      "ad",
      "al",
      "ar",
      "ca",
      "ce",
      "di",
      "el",
      "ig",
      "la",
      "ma",
      "mas",
      "mr",
      "os",
      "ra",
      "ri",
      "ric",
      "ys",
      "lu"
   ],
   "domains":[
      "cam.ctl.io"
   ],
   "authentication":{
      "github":false,
      "google":true,
      "ldap":true,
      "password":false,
      "username":null,
      "ldap_config":{
         "sources":[
            {
               "host":"ldap://ldap.cam.ctl.io",
               "email_field":"mail"
            }
         ]
      }
   },
   "features":{
      "admin_boxes":true,
      "cost_center":true,
      "custom_pricing":false,
      "onboard_checklist":false,
      "provider_sharing":true,
      "reporting":true
   },
   "providers":[
      {
         "enabled":true,
         "type":"Amazon Web Services",
         "description":"Manage EC2, ECS and Cloudformation instances",
         "pricing":[
            {
               "platform":"Linux Compute",
               "price":7000,
               "region":"ap-southeast-2",
               "flavor":"i2.8xlarge",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            },
            {
               "platform":"Linux Compute",
               "price":5,
               "region":"us-east-1",
               "flavor":"t2.micro",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            },
            {
               "platform":"Windows Compute",
               "price":10,
               "region":"us-east-1",
               "flavor":"t2.micro",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            }
         ]
      },
      {
         "enabled":true,
         "type":"Openstack",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vSphere",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Google Compute",
         "description":"Manage cloud hosting and Linux machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Microsoft Azure",
         "description":"Manage compute services for Windows and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Cloudstack",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"SoftLayer",
         "description":"Manage compute services for Windows and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vCloud Director",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Amazon Web Services GovCloud",
         "description":"Manage compute services in an isolated ITAR compliant AWS region.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Rackspace",
         "description":"Manage cloud hosting and Linux machines.",
         "pricing":[

         ]
      }
   ],
   "tags":[
      {
         "name":"workspace",
         "type":"Workspace",
         "value":null
      },
      {
         "name":"box",
         "type":"Box",
         "value":null
      },
      {
         "name":"environment",
         "type":"Environment",
         "value":null
      },
      {
         "name":"email",
         "type":"Email",
         "value":null
      },
      {
         "name":"user",
         "type":"User ID",
         "value":null
      },
      {
         "name":"Name",
         "type":"Service Instance ID",
         "value":null
      },
      {
         "name":"Testing",
         "type":"Custom",
         "value":"test"
      }
   ],
   "cost_centers":[
      {
         "name":"test",
         "enforce":false,
         "quotas":[
            {
               "allocated":[

               ],
               "cost":0,
               "provider":"2bf1bd2c-b03d-460f-80da-647d26bdbcfe"
            },
            {
               "cost":3000,
               "provider":"5908ee9b-0c0a-4af6-8eef-2dc9f95d033a"
            }
         ],
         "workspaces":[
            "operations"
         ]
      }
   ],
   "webhooks":[

   ]
}
```

**Request Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| schema |  string| Organization schema URI: **//elasticbox.net/schemas/organization** |
| name |    string   |  Organization name |
| icon | string |   Organization icon URI |
| updated | string | Date of the last update |
| created | string | Creation date |
| setup | boolean | This is read-only. It indicates that the Cloud Application Manager appliance is set up and ready for use. |
| administrators | array | List of users who can administer the organization |
| domains | string | Domains that are a part of the organization |
| authentication | object | List of the authentication methods to allow single sign-on in the organization. Contains the following properties:<li>github: Boolean. If enabled, it is true, else false.</li><li>google: Boolean. If enabled, it is true, else false.</li><li>password: Boolean. If enabled, it is true, else false.</li><li>ldap: Boolean. If enabled, it is true, else false.</li><li>ldap_config: Object that contains the LDAP service settings:</li><ul><li>ldap_group_sync: Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>sources: Array of [LDAP](../Administering Your Organization/user-authentication.md) sources. Each source has the following properties:</li><ul><li>host: Required. String identifies the hostname or IP address of the LDAP service.</li><li>groups_dn: String specifies a fully qualified group name.</li><li>group_dn_filter: String defines an entity on the LDAP server. All groups are synchronized as children of this entity.</li><li>email_field: String specifies the email field name by which to look up users. Typically, this field is called email.</li><li>ldap_search_password: String specifies the password for the LDAP service account to look up users who try to log in</li><li>ldap_search_user: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul></ul> |
| ldap_last_sync_completed | string | Timestamp of the last successful LDAP group sync, for example, 2015-04-06 14:28:12.874910. Value is null if ldap_group_sync is set to false. |
| ldap_groups | array | List of objects, each of which is an LDAP group. Each group has two properties:<li>dn: String identifier for the group.</li><li>name: String name shown in the workspace web interface.</li> |
| providers | array | List of cloud providers the organization can enable to register and deploy. Each provider type has the following properties:<li>enabled: Boolean value of true if enabled, else false.</li><li>type: String values of the supported cloud providers: Amazon Web Services, Openstack, VMWare vSphere, Google Compute, Microsoft Azure, Cloudstack, SoftLayer, VMware vCloud Director, Amazon Web Services GovCloud, Rackspace.</li><li>description: String that briefly enumerates the services from the cloud provider.</li><li>pricing: Array of pricing information for Linux and Windows compute instance types. Only available for Amazon Web Services.</li> |
| tags | array | List of [tags](../Administering Your Organization/resource-tags.md) applied on instances deployed to cloud providers from the organization. Each tag has three properties:<li>name: String you apply as a tag.</li><li>type: String identifies the type of tag whether an Cloud Application Manager object or a custom one. Allowed values are Box, Workspace, Provider, Environment, Email, User ID, Service Instance ID, Service ID, Workspace ID, Instance ID, Custom.</li><li>value: String value of null for Cloud Application Manager objects. For custom tags, set its value using this property.</li> |
| webhooks | array | List of webhooks that integrate with the organization. |
| cost_centers | array | List of cost centers. Each cost center contains the following properties:<li>enforce: Boolean. If true, an instance cannot be deployed if it is over the quota.</li><li>name: String. Name of the cost center</li><li>workspaces: Array. List of the names that belongs to the cost center.</li><li>quotas: List of quotas. Each quota contains an object with the following properties:</li><ul><li>cost: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>provider: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>allocated: Array. List of instances which are contributing to the current quota. Each allocated instance has these properties:</li><ul><li>instance_id: Required. String. Id of the instance.</li><li>instances: Required. Int. Number of instances.</li><li>started: Required. String. Date when this instance was deployed.</li><li>flavor: Required. String. Type of instance.</li><li>region: Required. String. Region where it was deployed.</li><li>service_type: Required. String. Type of the service.</li><li>terminated: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul><li>resources: Object. Resources of the quota.</li><ul><li>cpu: Required. Int. Number of cpu units.</li><li>disk: Required. Object. A disk with these properties:</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb, Gb or Tb.</li></ul><li>ram: Required. String. Ram of the quota.</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb or Gb.</li> </ul>|

**Response Parameters**

|  Parameter  |     Type      |	Description |
|----------|:-------------|-----|
| schema |  string| Organization schema URI: **http://elasticbox.net/schemas/organization** |
| name |    string   |  Organization name |
| icon | string |   Organization icon URI |
| updated | string | Date of the last update |
| created | string | Creation date |
| setup | boolean | This is read-only. It indicates that the Cloud Application Manager appliance is set up and ready for use. |
| administrators | array | List of users who can administer the organization |
| domains | string | Domains that are a part of the organization |
| authentication | object | List of the authentication methods to allow single sign-on in the organization. Contains the following properties:<li>github: Boolean. If enabled, it is true, else false.</li><li>google: Boolean. If enabled, it is true, else false.</li><li>password: Boolean. If enabled, it is true, else false.</li><li>ldap: Boolean. If enabled, it is true, else false.</li><li>ldap_config: Object that contains the LDAP service settings:</li><ul><li>ldap_group_sync: Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>sources: Array of [LDAP sources](../Administering Your Organization/user-authentication.md). Each source has the following properties:</li><ul><li>host: Required. String identifies the hostname or IP address of the LDAP service.</li><li>groups_dn: String specifies a fully qualified group name.</li><li>group_dn_filter: String defines an entity on the LDAP server. All groups are synchronized as children of this entity.</li><li>email_field: String specifies the email field name by which to look up users. Typically, this field is called email.</li><li>ldap_search_password: String specifies the password for the LDAP service account to look up users who try to log in</li><li>ldap_search_user: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul></ul> |
| ldap_last_sync_completed | string | Timestamp of the last successful LDAP group sync, for example, 2015-04-06 14:28:12.874910. Value is null if ldap_group_sync is set to false. |
| ldap_groups | array | List of objects, each of which is an LDAP group. Each group has two properties:<li>dn: String identifier for the group.</li><li>name: String name shown in the workspace web interface.</li> |
| providers | array | List of cloud providers the organization can enable to register and deploy. Each provider type has the following properties enabled:<li>Boolean value of true if enabled, else false.</li><li>type: String values of the supported cloud providers: Amazon Web Services, Openstack, VMWare vSphere, Google Compute, Microsoft Azure, Cloudstack, SoftLayer, VMware vCloud Director, Amazon Web Services GovCloud, Rackspace.</li><li>description: String that briefly enumerates the services from the cloud provider.</li><li>pricing: Array of pricing information for Linux and Windows compute instance types. Only available for Amazon Web Services.</li> |
| tags | array | List of [tags](../Administering Your Organization/resource-tags.md) applied on instances deployed to cloud providers from the organization. Each tag has three properties:<li>name: String you apply as a tag.</li><li>type: String identifies the type of tag whether an Cloud Application Manager object or a custom one. Allowed values are Box, Workspace, Provider, Environment, Email, User ID, Service Instance ID, Service ID, Workspace ID, Instance ID, Custom.</li><li>value: String value of null for Cloud Application Manager objects. For custom tags, set its value using this property.</li> |
| webhooks | array | List of webhooks that integrate with the organization. |
| cost_centers | array | List of cost centers. Each cost center contains the following properties:<li>enforce: Boolean. If true, an instance cannot be deployed if it is over the quota.</li><li>name: String. Name of the cost center</li><li>workspaces: Array. List of the names that belongs to the cost center.</li><li>quotas: List of quotas. Each quota contains an object with the following properties:</li><ul><li>cost: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>provider: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>allocated: Array. List of instances which are contributing to the current quota. Each allocated instance has these properties:</li><ul><li>instance_id: Required. String. Id of the instance.</li><li>instances: Required. Int. Number of instances.</li><li>started: Required. String. Date when this instance was deployed.</li><li>flavor: Required. String. Type of instance.</li><li>region: Required. String. Region where it was deployed.</li><li>service_type: Required. String. Type of the service.</li><li>terminated: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul><li>resources: Object. Resources of the quota.</li><ul><li>cpu: Required. Int. Number of cpu units.</li><li>disk: Required. Object. A disk with these properties:</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb, Gb or Tb.</li></ul><li>ram: Required. String. Ram of the quota.</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb or Gb.</li> </ul>|

**Response Body**

```
{
   "schema":"http://elasticbox.net/schemas/organization",
   "name":"elasticbox",
   "icon":"/services/blobs/download/5452705c3bbd224ef9541c41/elasticbox.png",
   "theme":null,
   "updated":"2015-04-06 20:38:46.060399",
   "created":"2014-02-14 15:12:21.526672",
   "setup":true,
   "administrators":[
      "ad",
      "al",
      "ar",
      "ca",
      "ce",
      "di",
      "el",
      "ig",
      "la",
      "ma",
      "mas",
      "mr",
      "os",
      "ra",
      "ri",
      "ric",
      "ys",
      "lu"
   ],
   "domains":[
      "cam.ctl.io"
   ],
   "authentication":{
      "github":false,
      "google":true,
      "ldap":true,
      "password":false,
      "username":null,
      "ldap_config":{
         "sources":[
            {
               "host":"ldap://ldap.cam.ctl.io",
               "email_field":"mail"
            }
         ]
      }
   },
   "features":{
      "admin_boxes":true,
      "cost_center":true,
      "custom_pricing":false,
      "onboard_checklist":false,
      "provider_sharing":true,
      "reporting":true
   },
   "providers":[
      {
         "enabled":true,
         "type":"Amazon Web Services",
         "description":"Manage EC2, ECS and Cloudformation instances",
         "pricing":[
            {
               "platform":"Linux Compute",
               "price":7000,
               "region":"ap-southeast-2",
               "flavor":"i2.8xlarge",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            },
            {
               "platform":"Linux Compute",
               "price":5,
               "region":"us-east-1",
               "flavor":"t2.micro",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            },
            {
               "platform":"Windows Compute",
               "price":10,
               "region":"us-east-1",
               "flavor":"t2.micro",
               "schema":"http://elasticbox.net/schemas/aws/compute/pricing"
            }
         ]
      },
      {
         "enabled":true,
         "type":"Openstack",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vSphere",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Google Compute",
         "description":"Manage cloud hosting and Linux machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Microsoft Azure",
         "description":"Manage compute services for Windows and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Cloudstack",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"SoftLayer",
         "description":"Manage compute services for Windows and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vCloud Director",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Amazon Web Services GovCloud",
         "description":"Manage compute services in an isolated ITAR compliant AWS region.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Rackspace",
         "description":"Manage cloud hosting and Linux machines.",
         "pricing":[

         ]
      }
   ],
   "tags":[
      {
         "name":"workspace",
         "type":"Workspace",
         "value":null
      },
      {
         "name":"box",
         "type":"Box",
         "value":null
      },
      {
         "name":"environment",
         "type":"Environment",
         "value":null
      },
      {
         "name":"email",
         "type":"Email",
         "value":null
      },
      {
         "name":"user",
         "type":"User ID",
         "value":null
      },
      {
         "name":"Name",
         "type":"Service Instance ID",
         "value":null
      },
      {
         "name":"Testing",
         "type":"Custom",
         "value":"test"
      }
   ],
   "cost_centers":[
      {
         "name":"test",
         "enforce":false,
         "quotas":[
            {
               "allocated":[

               ],
               "cost":0,
               "provider":"2bf1bd2c-b03d-460f-80da-647d26bdbcfe"
            },
            {
               "cost":3000,
               "provider":"5908ee9b-0c0a-4af6-8eef-2dc9f95d033a"
            }
         ],
         "workspaces":[
            "operations"
         ]
      }
   ],
   "webhooks":[

   ]
}
```

### PUT /organizations/{organization_name}/sync_groups

Queues a request to sync LDAP groups. The sync request, depending on the amount of data from the LDAP service, can take a few minutes. The ldap_last_sync_completed property updates when the request finishes successfully.

**Normal Response Codes**

* 200

**Error Response Codes**

* Not Found (404)

**Request Headers**

```
Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| schema |  string| Organization schema URI: **//elasticbox.net/schemas/organization** |
| name |    string   |  Organization name |
| icon | string |   Organization icon URI |
| updated | string | Date of the last update |
| created | string | Creation date |
| setup | boolean | This is read-only. It indicates that the Cloud Application Manager appliance is set up and ready for use. |
| administrators | array | List of users who can administer the organization |
| domains | string | Domains that are a part of the organization |
| authentication | object | List of the authentication methods to allow single sign-on in the organization. Contains the following properties:<li>github: Boolean. If enabled, it is true, else false.</li><li>google: Boolean. If enabled, it is true, else false.</li><li>password: Boolean. If enabled, it is true, else false.</li><li>ldap: Boolean. If enabled, it is true, else false.</li><li>ldap_config: Object that contains the LDAP service settings:</li><ul><li>ldap_group_sync: Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>sources: Array of [LDAP sources](../Administering Your Organization/user-authentication.md). Each source has the following properties:</li><ul><li>host: Required. String identifies the hostname or IP address of the LDAP service.</li><li>groups_dn: String specifies a fully qualified group name.</li><li>group_dn_filter: String defines an entity on the LDAP server. All groups are synchronised as children of this entity.</li><li>email_field: String specifies the email field name by which to look up users. Typically, this field is called email.</li><li>ldap_search_password: String specifies the password for the LDAP service account to look up users who try to log in</li><li>ldap_search_user: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul></ul> |
| ldap_last_sync_completed | string | Timestamp of the last successful LDAP group sync, for example, 2015-04-06 14:28:12.874910. Value is null if ldap_group_sync is set to false. |
| ldap_groups | array | List of objects, each of which is an LDAP group. Each group has two properties:<li>dn: String identifier for the group.</li><li>name: String name shown in the workspace web interface.</li> |
| providers | array | List of cloud providers the organization can enable to register and deploy. Each provider type has the following properties enabled:<li>Boolean value of true if enabled, else false.</li><li>type: String values of the supported cloud providers: Amazon Web Services, Openstack, VMWare vSphere, Google Compute, Microsoft Azure, Cloudstack, SoftLayer, VMware vCloud Director, Amazon Web Services GovCloud, Rackspace.</li><li>description: String that briefly enumerates the services from the cloud provider.</li><li>pricing: Array of pricing information for Linux and Windows compute instance types. Only available for Amazon Web Services.</li> |
| tags | array | List of [tags](../Administering Your Organization/resource-tags.md) applied on instances deployed to cloud providers from the organization. Each tag has three properties:<li>name: String you apply as a tag.</li><li>type: String identifies the type of tag whether an Cloud Application Manager object or a custom one. Allowed values are Box, Workspace, Provider, Environment, Email, User ID, Service Instance ID, Service ID, Workspace ID, Instance ID, Custom.</li><li>value: String value of null for Cloud Application Manager objects. For custom tags, set its value using this property.</li> |
| webhooks | array | List of webhooks that integrate with the organization. |
| cost_centers | array | List of cost centers. Each cost center contains the following properties:<li>enforce: Boolean. If true, an instance cannot be deployed if it is over the quota.</li><li>name: String. Name of the cost center</li><li>workspaces: Array. List of the names that belongs to the cost center.</li><li>quotas: List of quotas. Each quota contains an object with the following properties:</li><ul><li>cost: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>provider: Required. Boolean. By default it’s false. Specify as true to enable synchronizing with LDAP groups.</li><li>allocated: Array. List of instances which are contributing to the current quota. Each allocated instance has these properties:</li><ul><li>instance_id: Required. String. Id of the instance.</li><li>instances: Required. Int. Number of instances.</li><li>started: Required. String. Date when this instance was deployed.</li><li>flavor: Required. String. Type of instance.</li><li>region: Required. String. Region where it was deployed.</li><li>service_type: Required. String. Type of the service.</li><li>terminated: String specifies the username of the LDAP service account to look up users who try to log in.</li></ul><li>resources: Object. Resources of the quota.</li><ul><li>cpu: Required. Int. Number of cpu units.</li><li>disk: Required. Object. A disk with these properties:</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb, Gb or Tb.</li></ul><li>ram: Required. String. Ram of the quota.</li><ul><li>quantity: Required. String. Amount of storage.</li><li>unit: Required. String. Mb or Gb.</li></ul> |

**Response Body**

```
{
   "schema":"http://elasticbox.net/schemas/organization",
   "name":"organization_name",
   "icon":null,
   "theme":null,
   "updated":"2015-04-06 16:59:02.486606",
   "created":"2015-03-25 10:41:15.098256",
   "setup":true,
   "administrators":[
      "operations"
   ],
   "domains":[
      "cam.ctl.io"
   ],
   "authentication":{
      "ldap_config":{
         "ldap_group_sync":false,
         "sources":[
            {
               "host":"ldap://test_ldap"
            }
         ]
      },
      "github":true,
      "google":true,
      "ldap":true,
      "password":true,
   },
   "ldap_groups":[

   ],
   "providers":[
      {
         "enabled":true,
         "type":"Amazon Web Services",
         "description":"Manage EC2, ECS and Cloudformation instances",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Google Compute",
         "description":"Manage cloud hosting and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Openstack",
         "description":"Manage cloud hosting, Linux and Windows machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vSphere",
         "description":"Manage cloud hosting, Linux and Windows machines",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Microsoft Azure",
         "description":"Manage compute services for Windows and Linux machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Cloudstack",
         "description":"Manage cloud hosting, Linux and Windows machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"VMware vCloud Director",
         "description":"Manage cloud hosting, Linux and Windows machines.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Amazon Web Services GovCloud",
         "description":"Manage compute services in an isolated ITAR compliant AWS region.",
         "pricing":[

         ]
      },
      {
         "enabled":true,
         "type":"Rackspace",
         "description":"Manage cloud hosting and Linux machines.",
         "pricing":[

         ]
      }
   ],
   "ldap_last_sync_completed":null,
   "tags":[
      {
         "name":"box",
         "type":"Box name",
         "value":null
      },
      {
         "name":"environment",
         "type":"Environment",
         "value":null
      },
      {
         "name":"devenv",
         "type":"Custom",
         "value":"Cloud Application Manager Dev Environment"
      }
   ],
   "cost_centers":[
      {
         "name":"test",
         "enforce":false,
         "quotas":[
            {
               "allocated":[

               ],
               "cost":0,
               "provider":"2bf1bd2c-b03d-460f-80da-647d26bdbcfe"
            },
            {
               "cost":3000,
               "provider":"5908ee9b-0c0a-4af6-8eef-2dc9f95d033a"
            }
         ],
         "workspaces":[
            "operations"
         ]
      }
   ],
   "webhooks":[

   ]
}
```

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
