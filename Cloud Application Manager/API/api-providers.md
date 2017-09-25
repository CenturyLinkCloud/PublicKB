{{{ "title": "Providers API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

Manage and perform provider actions.

### Manage Providers

|  Resource  |  Description |
|------------|--------------|
| POST /services/providers | Creates a new provider account in Cloud Application Manager and gets the status of the provider. |
| GET /services/providers | Gets the list of providers. |
| GET /services/providers/{provider_id} | Fetches an existing provider. |
| PUT /services/providers/{provider_id} | Updates an existing provider. |
| DELETE /services/providers/{provider_id}| Deletes an existing provider.|

### Provider Operations

|  Resource  |  Description |
|------------|--------------|
| PUT /services/providers/{provider_id}/sync |Syncs an existing provider.|
| GET /services/providers/{provider_id}/logs | Gets the logs of a provider. |
| GET /services/providers/{provider_id}/unregisted-instances | Gets the unregistered instances of a provider. |
| POST /services/providers/{provider_id}/images | Adds a new machine image to a provider. |
| DELETE /services/providers/{provider_id}/images/{machine_image_id} | Updates an existing provider. |


### POST /services/providers

Creates a new provider account in Cloud Application Manager and gets the status of the provider.

**Normal Code**

* 202 accepted

**Error Codes**

**Request Headers**

```
content-type:application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```
**Request parameters for all providers**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| icon | string | Specify an icon URI for the provider account. |
| type | string | Required. Specify the account type as one of the following: Amazon Web Services, Rackspace, Openstack, VMware vSphere, Google Compute, Microsoft Azure, Cloudstack, SoftLayer. |
| description | string | Describe the services from the provider. |
| schema | string | Required. Provide the schema for the request. |
| name | string | Required. Give the provider account a name in Cloud Application Manager. |
| owner | string | Specify the user in Cloud Application Manager who owns the provider account. |

**Amazon Web Services request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| credentials | object | Required. Contains the credential object, which is either the AWS role ARN name if using Cloud Application Manager as a SaaS or the key and secret if using Cloud Application Manager as an appliance. |

**Amazon Web Services request body**

```
{
   "icon": "images/platform/aws.png",
   "type": "Amazon Web Services",
   "description": "Manage EC2, ECS and Cloudformation instances",
   "schema": "http://elasticbox.net/schemas/aws/provider",
   "name": "example account",
   "credentials": {
      "role": "role_ARN_that_gives_Cloud_Application_Manager_access"
   },
   "owner": "mrina"
}
```

**Amazon Web Services Gov request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| credentials | object | Required. Contains the credential object, which is either the [AWS role ARN name](../Deploying Anywhere/using-your-aws-account.md) if using Cloud Application Manager as a SaaS or the key and secret if using Cloud Application Manager as an appliance. |

**Amazon Web Services Gov request body**

```
{
  "icon": "images/platform/govcloud.png",
  "type": "Amazon Web Services GovCloud",
  "description": "Manage compute services in an isolated ITAR compliant AWS region",
  "schema": "http://elasticbox.net/schemas/aws/provider",
  "name": "AWSGovCloud",
  "credentials": {
    "key": "_the_key",
    "secret": "_the_secret"
  },
  "owner": "operations"
}
```

**Rackspace and OpenStack request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| identity_url | string |Required. Specify the identity service endpoint.|
| project | string | Required. Specify the project ID for Rackspace or the tenant for OpenStack. |
| username | string | Required. Specify the username. |
| password | string | Required. Specify the password. |

**Rackspace request body**

```
{
   "icon": "images/platform/rackspace.png",
   "type": "Rackspace",
   "description": "Manage cloud hosting and Linux machines",
   "schema": "http://elasticbox.net/schemas/openstack/provider",
   "identity_url": "https://identity.api.rackspacecloud.com/v2.0",
   "name": "example rackspace",
   "project": "your_project_ID",
   "username": "your_Rackspace_username",
   "password": "your_Rackspace_password",
   "owner": "mrina"
}
```

**OpenStack request body**

```
{
   "icon": "images/platform/openstack.png",
   "type": "Openstack",
   "description": "Manage cloud hosting, Linux and Windows machines",
   "schema": "http://elasticbox.net/schemas/openstack/provider",
   "name": "example openstack",
   "identity_url": "http://openstack-26.cam.ctl.io:5000/v2.0",
   "project": "your_OpenStack_tenant",
   "username": "your_OpenStack_username",
   "password": "your_OpenStack_password",
   "owner": "mrina"
}
```

**VSphere request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| username | string | Required. Specify a vCenter username. |
| secret | string | Required. Specify the user’s password. |
| endpoint | string | Required. Specify the vCenter server URL. |

**VSphere request body**

```
{
   "icon": "images/platform/vsphere.png",
   "type": "VMware vSphere",
   "description": "Manage cloud hosting, Linux and Windows machines",
   "schema": "http://elasticbox.net/schemas/vsphere/provider",
   "name": "example vcenter",
   "username": "your_Vspherer_username",
   "secret": "your_Vsphere_user_password",
   "endpoint": "your_vCenter_server_URL",
   "owner": "mrina"
}
```

**VCloud request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| username | string | Required. Specify a vCenter username. |
| password | string | Required. Specify the user’s password. |
| url | string | Required. Specify the vCenter server URL. |
| organization | string | Required. Organization. |

**VCloud request body**

```
{
  "icon": "images/platform/vcloud.png",
  "type": "VMware vCloud Director",
  "description": "Manage cloud hosting, Linux and Windows machines",
  "schema": "http://elasticbox.net/schemas/vcloud/provider",
  "name": "VMwareVCloudProvider",
  "url": "https://v-cloud.cam.ctl.io",
  "vorg": "system",
  "username": "_the_username",
  "password": "_the_password",
  "owner": "operations"
}
```

**Google Cloud request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| project_id | string | Required. Specify a project ID in Google Cloud that has billing and the Google Compute Engine API enabled. |
| email | string | Required. Specify your Gmail account associated with Google Cloud. |
| credentials | object | Required. Specify either the refresh_token object or the key. You can get the refresh_token from Google OAuth 2.0 to allow Cloud Application Manager to make API requests on your behalf. Or you can provide the JSON key for the project service account. |

**Google Cloud request body**

```
{
   "icon": "images/platform/google.png",
   "type": "Google Compute",
   "description": "Manage cloud hosting and Linux machines",
   "name": "example google cloud account",
   "project_id": "your_GoogleCloud_projectID",
   "email": "your_gmailaccount_for_GoogleCloud",
   "credentials": {
      "refresh_token": "Google_OAuth_2.0_refresh_token"
   },
   "schema": "http://elasticbox.net/schemas/gce/provider",
   "owner": "mrina"
}
```

**Azure request parameter**

To add an Azure subscription in Cloud Application Manager, you first have to upload the Cloud Application Manager management certificate to your subscription in Azure.

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| subscription | string | Required. Specify the Azure subscription ID.|

**Azure request body**

```
{
   "icon": "images/platform/azure-storage.png",
   "type": "Microsoft Azure",
   "description": "Manage compute services for Windows and Linux machines.",
   "schema": "http://elasticbox.net/schemas/azure/provider",
   "name": "example azure",
   "subscription_id": "your_Azure_subscription_ID",
   "owner": "mrina"
}
```

**CloudStack request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| url | string | Required. Specify the API endpoint to the CloudStack management server. |
| api_key | string | Required. Specify the API key for the CloudStack user account. |
| secret_key | string | Required. Specify the API secret for the CloudStack user account. |

**CloudStack request body**

```
{
   "icon": "images/platform/cloudstack.png",
   "type": "Cloudstack",
   "description": "Manage cloud hosting, Linux and Windows machines",
   "schema": "http://elasticbox.net/schemas/cloudstack/provider",
   "name": "example CloudStack",
   "url": "CloudStack_management_server_endpoint",
   "api_key": "CloudStack_API_key",
   "secret_key": "CloudStack_secret_key",
   "owner": "mrina"
}
```

**SoftLayer request parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| username | string | Required. Specify a SoftLayer account username. |
| api_key | string | Required. Specify the API key for the SoftLayer user. |

**SoftLayer request body**

```
{
   "icon": "images/platform/softlayer.png",
   "type": "SoftLayer",
   "description": "Manage compute services for Windows and Linux machines.",
   "schema": "http://elasticbox.net/schemas/softlayer/provider",
   "name": "example softlayer",
   "username": "your_SoftLayer_username",
   "api_key": "SoftLayer_API_key_for_username",
   "owner": "mrina"
}
```

**Response parameters for all providers**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| updated | string | Returns the date the provider was updated. |
| description | string | Returns the description for the provider. |
| deleted | object | Identifies whether the provider is deleted. |
| services | array | Returns the available services from the provider.|
| members | array | Returns users with whom the provider is shared. |
| owner | string | Returns the provider account owner in Cloud Application Manager. |
| id | string | Returns the ID of the provider account in Cloud Application Manager. |
| icon | string | Returns the icon used for the provider account. |
| name | string | Returns the name used to identify the provider account in Cloud Application Manager. |
| created | string | Returns the date that the provider was added. |
| uri | string | Returns the unique resource identifier path to the provider account. |
| admin_boxes | string | Lists the admin boxes attached to the provider. |
| organization | string | Identifies the name of the organization. |
| type | string | Identifies the provider as one of the following: Amazon Web Services, Rackspace, Openstack, VMware vSphere, Google Compute, Microsoft Azure, Cloudstack, SoftLayer. |
| schema | string | Returns the schema URL. |

**AWS response parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| credentials | object | Returns the Amazon Web Services role ARN if using Cloud Application Manager as a SaaS or identifies the key and secret if using Cloud Application Manager as an appliance. |

**AWS response body**

```
{
   "updated": "2015-01-05 18:36:26.227970",
   "description": "Manage EC2, ECS and Cloudformation instances",
   "deleted": null,
   "services": [],
   "members": [],
   "owner": "mrina",
   "credentials": {
      "role": "your_ARN_role_that_allows_Cloud_Application_Manager_access"
   },
   "id": "aefc3f24-74af-414d-98ae-d6ee05997610",
   "icon": "images/platform/aws.png",
   "name": "example account",
   "created": "2015-01-05 18:36:26.227970",
   "uri": "/services/providers/aefc3f24-74af-414d-98ae-d6ee05997610",
   "state": "initializing",
   "admin_boxes": [],
   "organization": "elasticbox",
   "type": "Amazon Web Services",
   "schema": "http://elasticbox.net/schemas/aws/provider"
}
```

**Rackspace and OpenStack response parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| username | string | Returns the username. |
| password | string | Masks the password for the provider account. |
| project | string | Returns the Rackspace project ID or the OpenStack tenant. |
| identity_url | string | Returns the OpenStack identity service endpoint. |

**Rackspace response example**

```
{
  "username": "_the_username",
  "updated": "2015-10-30 12:16:30.836398",
  "password": "_the_password",
  "description": "Manage cloud hosting and Linux machines",
  "created": "2015-10-30 12:16:30.836398",
  "deleted": null,
  "type": "Rackspace",
  "uri": "/services/providers/c6ade25c-cc46-4271-934d-55c75dba821a",
  "name": "RackSpace",
  "project": "937535",
  "services": [

  ],
  "state": "initializing",
  "admin_boxes": [

  ],
  "members": [

  ],
  "owner": "operations",
  "organization": "elasticbox",
  "icon": "images/platform/rackspace.png",
  "identity_url": "https://identity.api.rackspacecloud.com/v2.0",
  "id": "c6ade25c-cc46-4271-934d-55c75dba821a",
  "schema": "http://elasticbox.net/schemas/openstack/provider"
}
```

**Openstack response example**

```
{
  "username": "_the_username",
  "updated": "2015-10-30 12:26:14.331420",
  "password": "_the_password",
  "description": "Manage cloud hosting, Linux and Windows machines",
  "created": "2015-10-30 12:26:14.331420",
  "deleted": null,
  "identity_url": "http://openstack-36.cam.ctl.io:5000/v2.0",
  "uri": "/services/providers/57106d2a-ab5d-486a-988f-31a729a0c29d",
  "name": "OpenStackProvider",
  "project": "admin",
  "services": [

  ],
  "state": "initializing",
  "admin_boxes": [

  ],
  "members": [

  ],
  "owner": "operations",
  "organization": "elasticbox",
  "icon": "images/platform/openstack.png",
  "type": "Openstack",
  "id": "57106d2a-ab5d-486a-988f-31a729a0c29d",
  "schema": "http://elasticbox.net/schemas/openstack/provider"
}
```

**VSphere response parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| username | string | Returns the vCenter username. |
| secret | string | Masks the user’s password. |
| endpoint | string | Returns the vCenter server URL. |

**VSphere response example**

```
{
  "username": "_the_username",
  "updated": "2015-10-30 12:51:53.729679",
  "endpoint": "https://10.0.128.2",
  "description": "Manage cloud hosting, Linux and Windows machines",
  "state": "initializing",
  "deleted": null,
  "created": "2015-10-30 12:51:53.729679",
  "uri": "/services/providers/3afc1c99-dd66-436a-ace4-33979dd5f5ca",
  "name": "VMWareVSphereProvider",
  "services": [

  ],
  "secret": "_the_secret",
  "admin_boxes": [

  ],
  "members": [

  ],
  "owner": "operations",
  "organization": "elasticbox",
  "icon": "images/platform/vsphere.png",
  "type": "VMware vSphere",
  "id": "3afc1c99-dd66-436a-ace4-33979dd5f5ca",
  "schema": "http://elasticbox.net/schemas/vsphere/provider"
}
```

**Google Cloud response parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| project_id | string | Returns the project ID in Google Cloud that the provider account uses. |
| email | string | Returns the Gmail account associated with Google Cloud for the provider account. |
| credentials | object | Returns either the access_token and refresh_token objects or the key. Returns a key if you provided a JSON key for the project service account. |

**Google Cloud response example**

```
{
  "updated": "2015-10-30 12:34:09.062710",
  "description": "Manage cloud hosting and Linux machines",
  "icon": "images/platform/google.png",
  "created": "2015-10-30 12:34:09.062710",
  "deleted": null,
  "id": "d86e3bfe-1edc-45b4-a03b-28d1e2b7eee2",
  "uri": "/services/providers/d86e3bfe-1edc-45b4-a03b-28d1e2b7eee2",
  "name": "GoogleComputeProvider",
  "services": [

  ],
  "state": "initializing",
  "admin_boxes": [

  ],
  "members": [

  ],
  "organization": "elasticbox",
  "owner": "operations",
  "credentials": {
    "key": "_the_key"
  },
  "project_id": "_project_id",
  "type": "Google Compute",
  "email": "email@company.com",
  "schema": "http://elasticbox.net/schemas/gce/provider"
}
```

**Azure response parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| subscription_id | string | Returns the Azure subscription ID that the provider account uses. |

**Azure response example**

```
{
  "updated": "2015-10-30 12:49:38.014690",
  "description": "Manage compute services for Windows and Linux machines",
  "created": "2015-10-30 12:49:38.014690",
  "deleted": null,
  "uri": "/services/providers/57b41251-43fd-4a18-9182-c71db30f9035",
  "name": "MicrosoftAzureServiceProvider",
  "services": [

  ],
  "state": "initializing",
  "admin_boxes": [

  ],
  "members": [

  ],
  "owner": "operations",
  "organization": "elasticbox",
  "subscription_id": "_the_subscription_id",
  "icon": "images/platform/azure-storage.png",
  "type": "Microsoft Azure",
  "id": "57b41251-43fd-4a18-9182-c71db30f9035",
  "schema": "http://elasticbox.net/schemas/azure/provider"
}
```

**CloudStack response parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| url | string | Returns the API endpoint to the CloudStack management server. |
| api_key | string | Returns the API key for the CloudStack user account. |
| secret_key | string | Returns the API secret for the CloudStack user account. |

**CloudStack response example**

```
{
  "updated": "2015-10-30 12:28:22.315749",
  "api_key": "the_api_key",
  "description": "Manage cloud hosting, Linux and Windows machines",
  "created": "2015-10-30 12:28:22.315749",
  "url": "http://10.0.128.21:8080/client/api",
  "uri": "/services/providers/e50e4612-74a5-40b9-8aa0-b82631782c10",
  "name": "CloudStack",
  "deleted": null,
  "state": "initializing",
  "admin_boxes": [

  ],
  "members": [

  ],
  "organization": "elasticbox",
  "owner": "operations",
  "services": [

  ],
  "secret_key": "_the_secret_key",
  "icon": "images/platform/cloudstack.png",
  "type": "Cloudstack",
  "id": "e50e4612-74a5-40b9-8aa0-b82631782c10",
  "schema": "http://elasticbox.net/schemas/cloudstack/provider"
}
```

**SoftLayer response parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| username | string | Returns the SoftLayer username the provider account uses. |
| api_key | string | Returns the API key for the SoftLayer user. |

**SoftLayer response example**

```
{
  "username": "_the_username",
  "updated": "2015-10-30 12:22:57.519720",
  "api_key": "_the_apikey",
  "description": "Manage compute services for Windows and Linux machines",
  "created": "2015-10-30 12:22:57.519720",
  "deleted": null,
  "uri": "/services/providers/8a820dc5-c21e-434f-9ca7-03434d066bd6",
  "name": "SoftlayerProvider",
  "services": [

  ],
  "state": "initializing",
  "admin_boxes": [

  ],
  "members": [

  ],
  "owner": "operations",
  "organization": "elasticbox",
  "icon": "images/platform/softlayer.png",
  "type": "SoftLayer",
  "id": "8a820dc5-c21e-434f-9ca7-03434d066bd6",
  "schema": "http://elasticbox.net/schemas/softlayer/provider"
}
```

### GET /services/providers

Gets available providers from the personal workspace of the authenticated user.

**GET /services/providers**

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

**Response parameters**

|Parameter | Type | Description |
|----------|------|-------------|
|updated | string | Date of the last update.|
|description | string | Provider description.|
|created | string | Creation date.|
|uri | string | Provider uri.|
|name | string | Provider name.|
|services | array | List of services associated to the provider, each service has a name.|
|state | string | Provider state, there are five possible states: initializing , processing , ready , deleting or unavailable.|
|members | array | List of members with access to the provider.|
|owner | string | Provider owner.|
|type | string | Provider type, there are the available providers: Amazon Web Services (AWS), VShpere, VCloud, RackSpace, Openstack, Google Compute, Azure, CloudStack, Softlayer, AWS Gov.|
|id | string | Provider unique identificator.|
|icon | string | Provider Icon uri.|
|schema | string | The uri schema of the right provider.|

```
[
    {
        "updated": "2015-10-30 12:28:38.312157",
        "description": "Manage cloud hosting, Linux and Windows machines",
        "icon": "images/platform/cloudstack.png",
        "created": "2015-10-30 12:28:22.315749",
        "uri": "/services/providers/e50e4612-74a5-40b9-8aa0-b82631782c10",
        "name": "CloudStack",
        "services": [],
        "state": "unavailable",
        "members": [],
        "owner": "operations",
        "type": "Cloudstack",
        "id": "e50e4612-74a5-40b9-8aa0-b82631782c10",
        "schema": "http://elasticbox.net/schemas/cloudstack/provider"
    },
    {
        "schema": "http://elasticbox.net/schemas/vsphere/provider",
        "updated": "2015-10-30 12:25:42.135998",
        "description": "Manage cloud hosting, Linux and Windows machines",
        "created": "2015-10-09 07:35:00.273473",
        "uri": "/services/providers/cac26e4c-16f8-46ad-83ae-52a2b1ba4fca",
        "name": "vSphere",
        "owner": "operations",
        "state": "ready",
        "members": [],
        "services": [
            {
                "name": "Linux Compute"
            },
            {
                "name": "Windows Compute"
            }
        ],
        "type": "VMware vSphere",
        "id": "cac26e4c-16f8-46ad-83ae-52a2b1ba4fca",
        "icon": "images/platform/vsphere.png"
    },
    {
        "updated": "2015-10-30 12:18:45.899110",
        "description": "Manage cloud hosting and Linux machines",
        "icon": "images/platform/rackspace.png",
        "created": "2015-10-30 12:16:30.836398",
        "uri": "/services/providers/c6ade25c-cc46-4271-934d-55c75dba821a",
        "name": "RackSpace",
        "services": [
            {
                "locations": [
                    {},
                    {},
                    {},
                    {}
                ],
                "name": "Linux Compute"
            }
        ],
        "state": "ready",
        "members": [],
        "owner": "operations",
        "type": "Rackspace",
        "id": "c6ade25c-cc46-4271-934d-55c75dba821a",
        "schema": "http://elasticbox.net/schemas/openstack/provider"
    },
    {
        "schema": "http://elasticbox.net/schemas/softlayer/provider",
        "updated": "2015-10-30 12:23:01.133330",
        "description": "Manage compute services for Windows and Linux machines",
        "created": "2015-10-30 12:22:57.519720",
        "uri": "/services/providers/8a820dc5-c21e-434f-9ca7-03434d066bd6",
        "name": "SoftlayerProvider",
        "services": [
            {
                "name": "Linux Compute"
            },
            {
                "name": "Windows Compute"
            }
        ],
        "state": "ready",
        "members": [],
        "owner": "operations",
        "type": "SoftLayer",
        "id": "8a820dc5-c21e-434f-9ca7-03434d066bd6",
        "icon": "images/platform/softlayer.png"
    },
    {
        "updated": "2015-10-30 12:26:23.841387",
        "description": "Manage cloud hosting, Linux and Windows machines",
        "icon": "images/platform/openstack.png",
        "created": "2015-10-30 12:26:14.331420",
        "uri": "/services/providers/57106d2a-ab5d-486a-988f-31a729a0c29d",
        "name": "OpenStackProvider",
        "services": [
            {
                "locations": [
                    {}
                ],
                "name": "Linux Compute"
            },
            {
                "locations": [
                    {}
                ],
                "name": "Windows Compute"
            }
        ],
        "state": "ready",
        "members": [],
        "owner": "operations",
        "type": "Openstack",
        "id": "57106d2a-ab5d-486a-988f-31a729a0c29d",
        "schema": "http://elasticbox.net/schemas/openstack/provider"
    },
    {
        "schema": "http://elasticbox.net/schemas/dimension-data/provider",
        "updated": "2015-10-30 12:58:20.228258",
        "description": "Manage compute services in DD",
        "created": "2015-10-30 12:58:19.078758",
        "uri": "/services/providers/052211ae-096a-44e7-b88c-27d8dcac3971",
        "name": "DimensionDataProvider",
        "services": [
            {
                "locations": [],
                "name": "Linux Compute"
            },
            {
                "locations": [],
                "name": "Windows Compute"
            }
        ],
        "state": "unavailable",
        "members": [],
        "owner": "operations",
        "type": "Dimension Data",
        "id": "052211ae-096a-44e7-b88c-27d8dcac3971",
        "icon": "images/platform/dimension-data.png"
    },
    {
        "schema": "http://elasticbox.net/schemas/gce/provider",
        "updated": "2015-10-30 12:39:06.518493",
        "description": "Manage cloud hosting and Linux machines",
        "created": "2015-10-30 12:34:09.062710",
        "uri": "/services/providers/d86e3bfe-1edc-45b4-a03b-28d1e2b7eee2",
        "name": "GoogleComputeProvider",
        "owner": "operations",
        "state": "ready",
        "members": [],
        "services": [
            {
                "name": "Linux Compute"
            }
        ],
        "type": "Google Compute",
        "id": "d86e3bfe-1edc-45b4-a03b-28d1e2b7eee2",
        "icon": "images/platform/google.png"
    },
    {
        "schema": "http://elasticbox.net/schemas/vsphere/provider",
        "updated": "2015-10-30 12:52:48.017525",
        "description": "Manage cloud hosting, Linux and Windows machines",
        "created": "2015-10-30 12:51:53.729679",
        "uri": "/services/providers/3afc1c99-dd66-436a-ace4-33979dd5f5ca",
        "name": "VMWareVSphereProvider",
        "services": [
            {
                "name": "Linux Compute"
            },
            {
                "name": "Windows Compute"
            }
        ],
        "state": "ready",
        "members": [],
        "owner": "operations",
        "type": "VMware vSphere",
        "id": "3afc1c99-dd66-436a-ace4-33979dd5f5ca",
        "icon": "images/platform/vsphere.png"
    },
    {
        "updated": "2015-10-27 20:54:28.739422",
        "description": "Manage EC2, ECS and Cloudformation instances",
        "icon": "images/platform/aws.png",
        "created": "2015-10-27 16:25:58.448390",
        "uri": "/services/providers/7e841966-1dec-4460-a981-1db4e1eec10c",
        "name": "AWSProvider",
        "owner": "operations",
        "state": "ready",
        "members": [],
        "services": [
            {
                "locations": [
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {}
                ],
                "name": "CloudFormation Service"
            },
            {
                "name": "ECS Service",
                "locations": [
                    {
                        "clusters": []
                    },
                    {},
                    {
                        "clusters": []
                    },
                    {},
                    {
                        "clusters": []
                    },
                    {},
                    {
                        "clusters": [
                            {
                                "name": "scenarios-cluster",
                                "arn": "arn:aws:ecs:us-east-1:729190825118:cluster/scenarios-cluster"
                            }
                        ]
                    },
                    {
                        "clusters": []
                    },
                    {
                        "clusters": []
                    }
                ]
            },
            {
                "name": "Linux Compute",
                "locations": [
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {}
                ]
            },
            {
                "name": "Windows Compute",
                "locations": [
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {},
                    {}
                ]
            }
        ],
        "type": "Amazon Web Services",
        "id": "7e841966-1dec-4460-a981-1db4e1eec10c",
        "schema": "http://elasticbox.net/schemas/aws/provider"
    },
    {
        "schema": "http://elasticbox.net/schemas/azure/provider",
        "updated": "2015-10-30 12:49:46.850182",
        "description": "Manage compute services for Windows and Linux machines",
        "created": "2015-10-30 12:49:38.014690",
        "uri": "/services/providers/57b41251-43fd-4a18-9182-c71db30f9035",
        "name": "MicrosoftAzureServiceProvider",
        "services": [
            {
                "name": "Linux Compute"
            },
            {
                "name": "Windows Compute"
            }
        ],
        "state": "ready",
        "members": [],
        "owner": "operations",
        "type": "Microsoft Azure",
        "id": "57b41251-43fd-4a18-9182-c71db30f9035",
        "icon": "images/platform/azure-storage.png"
    },
    {
        "updated": "2015-10-30 12:54:50.566266",
        "description": "Manage cloud hosting, Linux and Windows machines",
        "icon": "images/platform/vcloud.png",
        "created": "2015-10-30 12:53:55.767875",
        "uri": "/services/providers/51cf6ea7-1edc-42b7-ae96-f7a304060188",
        "name": "VMwareVCloudProvider",
        "services": [
            {
                "name": "Linux Compute"
            },
            {
                "name": "Windows Compute"
            }
        ],
        "state": "ready",
        "members": [],
        "owner": "operations",
        "type": "VMware vCloud Director",
        "id": "51cf6ea7-1edc-42b7-ae96-f7a304060188",
        "schema": "http://elasticbox.net/schemas/vcloud/provider"
    },
    {
        "schema": "http://elasticbox.net/schemas/aws/provider",
        "updated": "2015-10-30 13:00:29.227885",
        "description": "Manage compute services in an isolated ITAR compliant AWS region",
        "created": "2015-10-30 13:00:24.039492",
        "uri": "/services/providers/b975319b-d5c5-4f8b-8077-0e78a0240efa",
        "name": "AWSGovCloud",
        "services": [
            {
                "locations": [
                    {}
                ],
                "name": "CloudFormation Service"
            },
            {
                "name": "Linux Compute",
                "locations": [
                    {}
                ]
            },
            {
                "name": "Windows Compute",
                "locations": [
                    {}
                ]
            }
        ],
        "state": "ready",
        "members": [],
        "owner": "operations",
        "type": "Amazon Web Services GovCloud",
        "id": "b975319b-d5c5-4f8b-8077-0e78a0240efa",
        "icon": "images/platform/govcloud.png"
    }
]
```

**GET /services/providers/{provider_id}**

Fetches an existing provider when you give the provider ID.

**Normal Response Codes**

* 202

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

**Response parameters**

| Parameter | Type | Description |
|----------------|--------|-----------------|
| updated | string | Date of the last update. |
| description | string | Provider description. |
| created | string | Creation date. |
| uri | string | Provider uri. |
| name | string | Provider name. |
| services | array | List of services associated to the provider, each service has a name. |
| state | string | Provider state, there are five possible states: initializing , processing , ready , deleting or unavailable. |
| members | array | List of members with access to the provider. |
| owner | string | Provider owner. |
| type | string | Provider type, there are the available providers: Amazon Web Services (AWS), VShpere, VCloud, RackSpace, Openstack, Google Compute, Azure, CloudStack, Softlayer, AWS Gov. |
| id | string | Provider unique identificator. |
| schema | string | The provider type schema uri. |
| icon | string | Provider Icon uri. |

```
{
   "updated":"2014-03-26 14:03:41.783045",
   "description":"Manage EC2, ECS and Cloudformation instances",
   "created":"2014-03-26 14:03:30.192871",
   "uri":"/services/providers/8c501fe3-54d7-49eb-b5d3-05016becabe3",
   "state":"ready",
   "name":"MyAmazon",
   "members":[

   ],
   "services":[
      {
         "flavors":[
            {
               "name":"t1.micro"
            },
            {
               "name":"m1.small"
            },
            {
               "name":"m1.medium"
            },
            {
               "name":"m1.large"
            },
            {
               "name":"m1.xlarge"
            },
            {
               "name":"m2.xlarge"
            },
            {
               "name":"m2.2xlarge"
            },
            {
               "name":"m2.4xlarge"
            },
            {
               "name":"c1.medium"
            },
            {
               "name":"c1.xlarge"
            },
            {
               "name":"c3.4xlarge"
            },
            {
               "name":"cr1.8xlarge"
            },
            {
               "name":"m3.medium"
            },
            {
               "name":"m3.large"
            },
            {
               "name":"m3.xlarge"
            },
            {
               "name":"m3.2xlarge"
            }
         ],
         "schema":"http://elasticbox.net/schemas/aws/compute/linux",
         "locations":[
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"us-east-1b"
                        },
                        {
                           "name":"us-east-1c"
                        },
                        {
                           "name":"us-east-1d"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-53556515"
                        },
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-002b3c74"
                        },
                        {
                           "description":"172.31.32.0/20",
                           "name":"subnet-425b0b6a"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"Elasticbox:a0215ef6-dd9e-49c3-bcbf-77f1567c630c - SG for eb-aknf5",
                           "name":"sg-babf1cdf"
                        },
                        {
                           "description":"default VPC security group",
                           "name":"sg-77b71412"
                        },
                        {
                           "description":"Elasticbox:a0215ef6-dd9e-49c3-bcbf-77f1567c630c - SG for eb-u3yyi",
                           "name":"sg-12c26077"
                        }
                     ],
                     "name":"vpc-f6f10e93"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"us-east-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"us-west-1a"
                        },
                        {
                           "name":"us-west-1b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-68e4c32e"
                        },
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-75846010"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-14e80c71"
                        }
                     ],
                     "name":"vpc-4cf4e82e"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"us-west-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"us-west-2a"
                        },
                        {
                           "name":"us-west-2b"
                        },
                        {
                           "name":"us-west-2c"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-b1353dc5"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-63e2c925"
                        },
                        {
                           "description":"172.31.32.0/20",
                           "name":"subnet-97d43cf2"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-0d659d68"
                        }
                     ],
                     "name":"vpc-efa1418a"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"us-west-2"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"eu-west-1a"
                        },
                        {
                           "name":"eu-west-1b"
                        },
                        {
                           "name":"eu-west-1c"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-b50ae6d0"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-76d1f830"
                        },
                        {
                           "description":"172.31.32.0/20",
                           "name":"subnet-c75f57b3"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-91d831f4"
                        }
                     ],
                     "name":"vpc-b9c2dadb"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"eu-west-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"ap-northeast-1a"
                        },
                        {
                           "name":"ap-northeast-1c"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-2c27046a"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-1b4e4c6f"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-0995726c"
                        }
                     ],
                     "name":"vpc-3997885b"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"ap-northeast-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"ap-southeast-1a"
                        },
                        {
                           "name":"ap-southeast-1b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-ea12149e"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-35618750"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-3c668359"
                        }
                     ],
                     "name":"vpc-95435cf7"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"ap-southeast-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"ap-southeast-2a"
                        },
                        {
                           "name":"ap-southeast-2b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-cb595abf"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-95fd1af0"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-9ffa1dfa"
                        }
                     ],
                     "name":"vpc-c3e6f9a1"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"ap-southeast-2"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Linux AMI",
                     "name":"Linux Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"sa-east-1a"
                        },
                        {
                           "name":"sa-east-1b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-04eff766"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-24281050"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-27263d45"
                        }
                     ],
                     "name":"vpc-058e2960"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"sa-east-1"
            }
         ],
         "name":"Linux Compute",
         "icon":"images/platform/large/linux.png"
      },
      {
         "flavors":[
            {
               "name":"t1.micro"
            },
            {
               "name":"m1.small"
            },
            {
               "name":"m1.medium"
            },
            {
               "name":"m1.large"
            },
            {
               "name":"m1.xlarge"
            },
            {
               "name":"m2.xlarge"
            },
            {
               "name":"m2.2xlarge"
            },
            {
               "name":"m2.4xlarge"
            },
            {
               "name":"c1.medium"
            },
            {
               "name":"c1.xlarge"
            },
            {
               "name":"c3.4xlarge"
            },
            {
               "name":"cr1.8xlarge"
            },
            {
               "name":"m3.medium"
            },
            {
               "name":"m3.large"
            },
            {
               "name":"m3.xlarge"
            },
            {
               "name":"m3.2xlarge"
            }
         ],
         "schema":"http://elasticbox.net/schemas/aws/compute/windows",
         "locations":[
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"us-east-1b"
                        },
                        {
                           "name":"us-east-1c"
                        },
                        {
                           "name":"us-east-1d"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-53556515"
                        },
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-002b3c74"
                        },
                        {
                           "description":"172.31.32.0/20",
                           "name":"subnet-425b0b6a"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"Elasticbox:a0215ef6-dd9e-49c3-bcbf-77f1567c630c - SG for eb-aknf5",
                           "name":"sg-babf1cdf"
                        },
                        {
                           "description":"default VPC security group",
                           "name":"sg-77b71412"
                        },
                        {
                           "description":"Elasticbox:a0215ef6-dd9e-49c3-bcbf-77f1567c630c - SG for eb-u3yyi",
                           "name":"sg-12c26077"
                        }
                     ],
                     "name":"vpc-f6f10e93"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"us-east-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"us-west-1a"
                        },
                        {
                           "name":"us-west-1b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-68e4c32e"
                        },
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-75846010"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-14e80c71"
                        }
                     ],
                     "name":"vpc-4cf4e82e"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"us-west-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"us-west-2a"
                        },
                        {
                           "name":"us-west-2b"
                        },
                        {
                           "name":"us-west-2c"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-b1353dc5"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-63e2c925"
                        },
                        {
                           "description":"172.31.32.0/20",
                           "name":"subnet-97d43cf2"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-0d659d68"
                        }
                     ],
                     "name":"vpc-efa1418a"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"us-west-2"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"eu-west-1a"
                        },
                        {
                           "name":"eu-west-1b"
                        },
                        {
                           "name":"eu-west-1c"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-b50ae6d0"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-76d1f830"
                        },
                        {
                           "description":"172.31.32.0/20",
                           "name":"subnet-c75f57b3"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-91d831f4"
                        }
                     ],
                     "name":"vpc-b9c2dadb"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"eu-west-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"ap-northeast-1a"
                        },
                        {
                           "name":"ap-northeast-1c"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-2c27046a"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-1b4e4c6f"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-0995726c"
                        }
                     ],
                     "name":"vpc-3997885b"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"ap-northeast-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"ap-southeast-1a"
                        },
                        {
                           "name":"ap-southeast-1b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-ea12149e"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-35618750"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-3c668359"
                        }
                     ],
                     "name":"vpc-95435cf7"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"ap-southeast-1"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"ap-southeast-2a"
                        },
                        {
                           "name":"ap-southeast-2b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-cb595abf"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-95fd1af0"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-9ffa1dfa"
                        }
                     ],
                     "name":"vpc-c3e6f9a1"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"ap-southeast-2"
            },
            {
               "images":[
                  {
                     "description":"Latest AWS Windows AMI",
                     "name":"Windows Compute"
                  }
               ],
               "clouds":[
                  {
                     "subnets":[
                        {
                           "name":"sa-east-1a"
                        },
                        {
                           "name":"sa-east-1b"
                        }
                     ],
                     "name":"EC2",
                     "security_groups":[
                        {
                           "name":"Automatic"
                        }
                     ]
                  },
                  {
                     "subnets":[
                        {
                           "description":"172.31.16.0/20",
                           "name":"subnet-04eff766"
                        },
                        {
                           "description":"172.31.0.0/20",
                           "name":"subnet-24281050"
                        }
                     ],
                     "description":"172.31.0.0/16",
                     "security_groups":[
                        {
                           "description":"default VPC security group",
                           "name":"sg-27263d45"
                        }
                     ],
                     "name":"vpc-058e2960"
                  }
               ],
               "keypairs":[
                  {
                     "name":"None"
                  }
               ],
               "name":"sa-east-1"
            }
         ],
         "name":"Windows Compute",
         "icon":"images/platform/large/windows.png"
      }
   ],
   "key":"AKIAJPKHHGHLEAOTKQ6A",
   "owner":"--owner--",
   "icon":"images/platform/aws.png",
   "type":"Amazon Web Services",
   "id":"8c501fe3-54d7-49eb-b5d3-05016becabe3",
   "schema":"http://elasticbox.net/schemas/aws/provider"
}
```

**PUT /services/providers/{provider_id}**

Updates an existing provider when you give the provider ID. Pass the provider object in the request body to update these fields: name, description, and members.

For AWS, you can also update the key and secret. For VMware vShpere, you can also update the username, secret, and endpoint.

**Normal Response Codes**

* 200

**Error Response Codes**

* Invalid Data (400)
* Conflict (409)

**Request parameters**

|Parameter | Type | Description |
|----------|------|-------------|
|updated | string | Date of the last update.|
|description | string | Provider description.|
|created | string | Creation date.|
|uri | string | Provider uri.|
|name | string | Provider name.|
|services | array | List of services associated to the provider, each service has a name.|
|state | string | Provider state, there are five possible states: initializing , processing , ready , deleting or unavailable .|
|members | array | List of members with access to the provider.|
|owner | string | Provider owner.|
|type | string | Provider type, there are two possible providers: Amazon Web Services or VMware vShpere. |
|id | string | Provider unique identificator.|
|icon | string | Provider Icon uri.|

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

    "schema": "http://elasticbox.net/schemas/gce/provider",
    "updated": "2015-10-30 12:39:06.518493",
    "project_id": "the_project_id",
    "description": "Manage cloud hosting and Linux machines, description has been updated",
    "created": "2015-10-30 12:34:09.062710",
    "deleted": null,
    "uri": "/services/providers/d86e3bfe-1edc-45b4-a03b-28d1e2b7eee2",
    "name": "GoogleComputeProvider",
    "owner": "operations",
    "state": "ready",
    "email": "therightemail@company.com",
    "admin_boxes": [],
    "members": [],
    "credentials": {},
    "services": [
        {
            "name": "Linux Compute",
            "zones": [
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "asia-east1-b"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "asia-east1-a"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "asia-east1-c"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "europe-west1-b"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "europe-west1-c"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "europe-west1-d"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "us-central1-f"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "us-central1-a"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "us-central1-b"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "us-central1-c"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "us-east1-c"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "us-east1-d"
                },
                {
                    "machineTypes": [
                        {
                            "description": "1 vCPU (shared physical core) and 0.6 GB RAM",
                            "name": "f1-micro"
                        },
                        {
                            "description": "1 vCPU (shared physical core) and 1.7 GB RAM",
                            "name": "g1-small"
                        },
                        {
                            "description": "16 vCPUs, 14.4 GB RAM",
                            "name": "n1-highcpu-16"
                        },
                        {
                            "description": "2 vCPUs, 1.8 GB RAM",
                            "name": "n1-highcpu-2"
                        },
                        {
                            "description": "32 vCPUs, 28.8 GB RAM",
                            "name": "n1-highcpu-32"
                        },
                        {
                            "description": "4 vCPUs, 3.6 GB RAM",
                            "name": "n1-highcpu-4"
                        },
                        {
                            "description": "8 vCPUs, 7.2 GB RAM",
                            "name": "n1-highcpu-8"
                        },
                        {
                            "description": "16 vCPUs, 104 GB RAM",
                            "name": "n1-highmem-16"
                        },
                        {
                            "description": "2 vCPUs, 13 GB RAM",
                            "name": "n1-highmem-2"
                        },
                        {
                            "description": "32 vCPUs, 208 GB RAM",
                            "name": "n1-highmem-32"
                        },
                        {
                            "description": "4 vCPUs, 26 GB RAM",
                            "name": "n1-highmem-4"
                        },
                        {
                            "description": "8 vCPUs, 52 GB RAM",
                            "name": "n1-highmem-8"
                        },
                        {
                            "description": "1 vCPU, 3.75 GB RAM",
                            "name": "n1-standard-1"
                        },
                        {
                            "description": "16 vCPUs, 60 GB RAM",
                            "name": "n1-standard-16"
                        },
                        {
                            "description": "2 vCPUs, 7.5 GB RAM",
                            "name": "n1-standard-2"
                        },
                        {
                            "description": "32 vCPUs, 120 GB RAM",
                            "name": "n1-standard-32"
                        },
                        {
                            "description": "4 vCPUs, 15 GB RAM",
                            "name": "n1-standard-4"
                        },
                        {
                            "name": "n1-standard-8"
                        }
                    ],
                    "name": "us-east1-b"
                }
            ],
            "images": [
                {
                    "description": "",
                    "name": "ubuntu-14-04-lts-v20140709"
                },
                {
                    "description": "CentOS, CentOS, 6.7, x86_64 built on 2015-09-29",
                    "name": "centos-6-v20150929"
                },
                {
                    "description": "CentOS, CentOS, 7.1.1503, x86_64 built on 2015-09-29",
                    "name": "centos-7-v20150929"
                },
                {
                    "description": "Debian, Debian GNU/Linux, 7.9 (wheezy), amd64 with backports kernel and SSH packages built on 2015-09-29",
                    "name": "backports-debian-7-wheezy-v20150929"
                },
                {
                    "description": "Accounts Beta Debian GNU/Linux, 7.9 (wheezy), amd64 with backports kernel and SSH packages and beta accounts packages built on 2015-09-30",
                    "name": "beta-accounts-backports-debian-7-wheezy-v20150930"
                },
                {
                    "description": "Accounts Beta Debian GNU/Linux, 8.1 (jessie), amd64 with beta accounts package built on 2015-09-30",
                    "name": "beta-accounts-debian-8-jessie-v20150930"
                },
                {
                    "description": "Debian, Debian GNU/Linux, 7.9 (wheezy), amd64 built on 2015-09-29",
                    "name": "debian-7-wheezy-v20150929"
                },
                {
                    "description": "Debian, Debian GNU/Linux, 8.1 (jessie), amd64 built on 2015-09-29",
                    "name": "debian-8-jessie-v20150929"
                },
                {
                    "description": "Red Hat, Red Hat Enterprise Linux, 6.7, x86_64 built on 2015-09-29",
                    "name": "rhel-6-v20150929"
                },
                {
                    "description": "Red Hat, Red Hat Enterprise Linux, 7.1, x86_64 built on 2015-09-29",
                    "name": "rhel-7-v20150929"
                },
                {
                    "description": "SLES, SUSE Linux Enterprise Server, 11 SP4, x86_64 built on 2015-07-14",
                    "name": "sles-11-sp4-v20150714"
                },
                {
                    "description": "SUSE, SUSE Linux Enterprise Server, 12, x86_64 built on 2015-05-11",
                    "name": "sles-12-v20150511"
                },
                {
                    "description": "Canonical, Ubuntu, 12.04 LTS, amd64 precise image built on 2015-09-10",
                    "name": "ubuntu-1204-precise-v20150910"
                },
                {
                    "description": "Canonical, Ubuntu, 14.04 LTS, amd64 trusty image built on 2015-09-09",
                    "name": "ubuntu-1404-trusty-v20150909a"
                },
                {
                    "description": "Canonical, Ubuntu, 15.04, amd64 vivid image built on 2015-09-11",
                    "name": "ubuntu-1504-vivid-v20150911"
                },
                {
                    "description": "Canonical, Ubuntu, 15.10, amd64 wily image built on 2015-10-26",
                    "name": "ubuntu-1510-wily-v20151026"
                }
            ],
            "icon": "images/platform/linux.png",
            "networks": [
                {
                    "routes": [],
                    "firewalls": [
                        {
                            "target_tags": [
                                "couchbase"
                            ],
                            "description": "",
                            "name": "couchbase"
                        },
                        {
                            "target_tags": [
                                "http-server"
                            ],
                            "description": "",
                            "name": "default-allow-http"
                        },
                        {
                            "target_tags": [
                                "https-server"
                            ],
                            "description": "",
                            "name": "default-allow-https"
                        },
                        {
                            "target_tags": [
                                "allow-internal"
                            ],
                            "description": "Internal traffic from default allowed",
                            "name": "default-allow-internal"
                        },
                        {
                            "target_tags": [
                                "jboss"
                            ],
                            "description": "",
                            "name": "jboss"
                        },
                        {
                            "target_tags": [
                                "jbossmgmt"
                            ],
                            "description": "",
                            "name": "jbossmgmt"
                        },
                        {
                            "target_tags": [
                                "jenkins"
                            ],
                            "description": "",
                            "name": "jenkins"
                        },
                        {
                            "target_tags": [
                                "mongo"
                            ],
                            "description": "Firewall rule for MongoDB server",
                            "description": "8 vCPUs, 30 GB RAM",
                            "name": "mongodb"
                        },
                        {
                            "target_tags": [
                                "mysql"
                            ],
                            "description": "",
                            "name": "mysql"
                        },
                        {
                            "target_tags": [
                                "rabbitmq"
                            ],
                            "description": "Firewall rule for RabbitMQ server",
                            "name": "rabbitmq"
                        },
                        {
                            "target_tags": [
                                "redis"
                            ],
                            "description": "rule used for testing redis in gce",
                            "name": "redis"
                        },
                        {
                            "target_tags": [
                                "test-firewall"
                            ],
                            "description": "Don't Delete. Use by scenario tests",
                            "name": "test-firewall"
                        },
                        {
                            "target_tags": [
                                "web"
                            ],
                            "description": "Firewall rule for Web Server",
                            "name": "web"
                        }
                    ],
                    "description": "Default network for the project",
                    "name": "default"
                }
            ],
            "schema": "http://elasticbox.net/schemas/gce/compute/linux"
        }
    ],
    "organization": "elasticbox",
    "type": "Google Compute",
    "id": "d86e3bfe-1edc-45b4-a03b-28d1e2b7eee2",
    "icon": "images/platform/google.png"
}
```

**DELETE /services/providers/{provider_id}**

Deletes an existing provider when you give the provider ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Invalid Data (400)
* Forbidden (403)
* Active service using the provider (400)

**Request**

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
DELETE /services/providers/{provider_id}
```

**PUT /services/providers/{provider_id}/sync**

Syncs an existing provider when you give the provider ID.

**Normal Response Codes**

* 202

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

**GET /services/providers/{provider_id}/logs**

Retrieves the logs of a provider when you give the provider ID.

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

**Response parameters**

|Parameter | Type | Description |
|----------|------|-------------|
|workspace | string | Id of the workspace who perform the action.|
|provider_id | string | Provider unique identifier.|
|created | string | Creation date.|
|text | string | Profiver-log action description.|
|level | integer | Provider-log action level.|
|updated | array | Date of the update.|
|id | string | Provider unique identifier.|
|schema | string | Provider-log schema url.|

```
[
   {
      "workspace":"--workspace name--",
      "provider_id":"8c501fe3-54d7-49eb-b5d3-05016becabe3",
      "created":"2014-03-28 12:18:02.455710",
      "text":"Provider 'MyAmazon' synchronized",
      "level":40,
      "updated":"2014-03-28 12:18:02.456441",
      "id":"6303cd2f-3c73-4b8e-9aa3-12cdacc15093",
      "schema":"http://elasticbox.net/schemas/provider-log"
   },
   {
      "workspace":"--workspace name--",
      "provider_id":"8c501fe3-54d7-49eb-b5d3-05016becabe3",
      "created":"2014-03-26 14:03:41.863572",
      "text":"Provider 'MyAmazon' synchronized",
      "level":40,
      "updated":"2014-03-26 14:03:41.864242",
      "id":"3fa58165-2af8-47eb-99e9-98f68e76c9b2",
      "schema":"http://elasticbox.net/schemas/provider-log"
   }
]
```

**GET /services/providers/{provider_id}/unregisted-instances**

Retrieves a list of unregistered instances found in a provider when you give the provider ID.

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

**Response parameters**

|Parameter | Type | Description |
|----------|------|-------------|
|profile | object | Instance profile. |
| profile.subnet | string | Instance subnet. |
| profile.image | string | Instance image. |
| profile.keypair | string | Instance keypair. |
| profile.location | string| Instance location. |
| profile.security_groups | string | Instance security groups. |
| profile.flavor | string | Instance flavor. |
| profile.manageos | boolean | Instance Manage. |
| profile.autoscalable | boolean | Instance autoscalable. |
| profile.cloud | boolean | Cloud type. |
| profile.schema | string | Instance schema uri. |
|provider_id | string | Instance provider unique identifier. |
|name | string | Instance name. |
|created | string | Creation date.|
|deleted | string | Logical deletion date. |
|type | string | Can be one of these types: Linux Compute, Windows Compute and CloudFormation Service. |
|server_info | object | Instance public and private ips and public dns.|
|updated | array | Date of the update.|
|power_state | string | Can be running or stopped.|
|organization | string | Organization to which instance belongs.|
|external_id | string | Instance external id. |
|id | string | Instance unique identifier.|
|schema | string | Unregistered-instance schema url.|

```
[
  {
    "profile": {
      "subnet": "ca-central-1a",
      "cloud": "vpc-083cc961",
      "image": "ami-bf5ee2db",
      "ebs_optimized": false,
      "instances": 1,
      "keypair": "Operations",
      "security_groups": [],
      "volumes": [],
      "flavor": "t2.micro",
      "schema": "http://elasticbox.net/schemas/aws/ec2/profile",
      "managed_os": false,
      "location": "ca-central-1"
    },
    "provider_id": "8c501fe3-54d7-49eb-b5d3-05016becabe3",
    "name": "AWS LDAP Windows",
    "created": "2017-06-15 11:40:00.243971",
    "deleted": null,
    "type": "Windows Compute",
    "server_info": {
      "public_ip": "52.62.222.233",
      "private_ip": "172.33.22.199",
      "public_dns": "ec2-52-62-222-233.ca-central-1.compute.amazonaws.com"
    },
    "updated": "2017-06-15 11:40:00.243971",
    "power_state": "running",
    "organization": "centurylink",
    "external_id": "i-06bee885e4e806ca0",
    "id": "957625f1-3c6f-423c-a8ac-430983c369f7",
    "schema": "http://elasticbox.net/schemas/unregistered-instance"
  },
  {...},
  {...}
]
```

**POST /services/providers/{provider_id}/images**

Adds a new machine image to a provider when you give the provider ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Invalid Data (400)
* Forbidden (403)
* Not Found (404)

**Request Parameters**

|Parameter | Type | Description|
|----------|------|------------|
|location | string | Image location. |
|name | string | Image name. |
|description | string | Image description. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

{
   "location":"us-east-1",
   "name":"ami-3275ee5b",
   "description":"New Image Description"
}
```

**DELETE /services/providers/{provider_id}/images/{machine_image_id}**

Deletes an existing machine image when you give the provider ID and the machine image ID.

**Normal Response Codes**

* 202

**Error Response Codes**

* Location query parameter is missing (400)
* Forbidden (403)
* Not Found (404)

**Request Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
|location | string | Location of the machine image to be deleted. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

```
Body:

DELETE /services/providers/{provider_id}/images/{machine_image_id}?location=us-east-1
```

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
