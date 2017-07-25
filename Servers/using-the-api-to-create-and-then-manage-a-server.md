{{{
  "title": "Using the API to Create and Configure a Server",
  "date": "4-15-2015",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

The CenturyLink Cloud API can be used to perform the same actions programmatically as you can from within the Control Portal. Oftentimes multiple API calls are required to perform a particular task, and this may include waiting for asynchronous jobs to complete. Particularly in these cases, it's important to make sure to use a very prescriptive sequence for the calls to ensure success. The below example shows one such sequence for authenticating, creating a server, updating the server information, and restarting it.

For more details about the specific API functions used below, you may reference the complete [API documentation](https://www.ctl.io/api-docs/v2).

### Steps

We will use ALIAS as the account alias for all the calls below and will build our server in the WA1 data center. As shown below, all HTTP requests must include the `Content-Type` header set to `application/json`.

#### 1. Authentication

To authenticate against the API, we use the following request:

    POST https://api.ctl.io/v2/authentication/login
    Content-Type: application/json

    {
      "username":"demouser1",
      "password":"mypassword"
    }

We get a response that includes the `bearerToken`:

    200 OK

    {
      "userName": "demouser1",
      "accountAlias": "ALIAS",
      "locationAlias": "WA1",
      "roles": [
        "AccountAdmin"
      ],
      "bearerToken": "VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe"
    }

As shown below, all subsequent HTTP requests must also include this token in the `Authorization` header as follows:

    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

More information can be found in the [Authentication Overview API Documentation](https://www.ctl.io/api-docs/v2/#getting-started-api-v20-authentication-overview) as needed.

#### 2. Get Deployment Capabilities

We first need to gather some details that will be required to create a new server. Most of this information is available via the deployment capabilities API call which can be retrieved using the following request:

    GET https://api.ctl.io/v2/datacenters/ALIAS/WA1/deploymentCapabilities
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

The response should be similar to the following (but may also include additional information). We are particularly interested right now in the `networkId` listed in the `deployableNetworks` section as well as the `name` attribute of each item in the list of `templates`. These represent the network we wish to deploy our server to and the template we wish to be used on the server. We will use these values in a subsequent to create the server.

    200 OK

    {
      "dataCenterEnabled": true,
      "importVMEnabled": true,
      "supportsPremiumStorage": true,
      "supportsSharedLoadBalancer": true,
      "deployableNetworks": [
        {
          "name": "My Network",
          "networkId": "a933432bd1234e84b6c4fa329e48cb8b",
          "type": "private",
          "accountID": "ALIAS"
        }
      ],
      "templates": [
        {
          "name": "RHEL-6-64-TEMPLATE",
          "osType": "redHat6_64Bit",
          "description": "RedHat Enterprise Linux 6 | 64-bit",
          "storageSizeGB": 17,
          "capabilities": [...],
          "reservedDrivePaths": [...]
        },
        {
          "name": "WIN2012R2DTC-64",
          "osType": "windows2012R2DataCenter_64Bit",
          "description": "Windows 2012 R2 Datacenter Edition | 64-bit",
          "storageSizeGB": 60,
          "capabilities": [...],
          "reservedDrivePaths": [...]
        }
      ]
    }

#### 3. Get Available Groups

Next we need to decide which group to create our server in and retrieve the UUID to pass to the create server method. To get a list of available groups, we first retrieve the root group for the given account and data center using the following request (note the `groupLinks=true` query parameter that is required in this case):

    GET https://api.ctl.io/v2/datacenters/ALIAS/WA1?groupLinks=true
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

We get back a number of links to other resources related to this data center (not all shown below). Notice the `deploymentCapabilities` endpoint that we've already used as well as the link to create a server. Most importantly, though, we see the link and identifier for the root data center group for this account.

    200 OK

    {
      "id": "wa1",
      "name": "WA1 - US West (Seattle)",
      "links": [
      {
        "rel": "self",
        "href": "/v2/datacenters/ALIAS/wa1"
      },
      {
        "rel": "deploymentCapabilities",
        "href": "/v2/datacenters/ALIAS/wa1/deploymentCapabilities"
      },
      {
        "rel": "group",
        "href": "/v2/groups/ALIAS/890312348ddfe311b05f00505682315a",
        "id": "890312348ddfe311b05f00505682315a",
        "name": "WA1 Hardware"
      },
      {
        "rel": "createServer",
        "href": "/v2/servers/ALIAS",
        "verbs": [
          "POST"
        ]
      }
    }

Now we can use this UUID to get the list of groups for this account in this data center. The request is as follows:

    GET https://api.ctl.io/v2/groups/ALIAS/890312348ddfe311b05f00505682315a
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

We get back the complete list of groups. (Some of the details of the response have been stripped out for readability.)

    200 OK

    {
      "id": "8903fcae8ddfe311b05f00505682315a",
      "name": "WA1 Hardware",
      "description": "WA1 Hardware",
      "locationId": "WA1",
      "type": "default",
      "status": "active",
      "serversCount": 7,
      "groups": [
        {
          "id": "8b03fcae8ddfe311b05f005056812345",
          "name": "Archive",
          "description": "Pay only for the storage consumed by the archived server. No compute or licensing costs are incurred.",
          "locationId": "WA1",
          "type": "archive",
          "status": "active",
          "serversCount": 0,
          "groups": [],
          "changeInfo": {...},
          "links": [...],
          "customFields": []
        },
        {
          "id": "8a03fcae8ddfe311b05f005056812345",
          "name": "Default Group",
          "description": "The default location for new servers created in your account.",
          "locationId": "WA1",
          "type": "default",
          "status": "active",
          "serversCount": 0,
          "groups": [...],
          "changeInfo": {...},
          "links": [...],
          "customFields": []
        },  
        {
          "id": "8d03fcae8ddfe311b05f005056812345",
          "name": "Templates",
          "description": "Custom templates provide a set of hardware/software settings that can be used repeatedly to create servers configured with the same settings.",
          "locationId": "WA1",
          "type": "templates",
          "status": "active",
          "groups": [...],
          "changeInfo": {...},
          "links": [...],
          "customFields": []
        }
      ]
      "links": [...],
      "changeInfo": {...},
      "customFields": []

We will use the UUID for the Default Group (`8a03fcae8ddfe311b05f005056812345`) to create our server below.

For more details about the links referenced above and other link types, see the [Links Framework API Documentation](https://www.ctl.io/api-docs/v2/#getting-started-api-v20-links-framework) as well as the [Link Definitions API Documentation](https://www.ctl.io/api-docs/v2/#link-definitions) for each resource type.

#### 4. Create a Server

To create a server we use the following request. Notice in the JSON payload we are using the `groupId` from our previous call to the groups endpoint as well as the `sourceServerId` (the desired template name) and `networkId` we chose from the deployment capabilities call above. We also include all of the other required parameters as outlined in the [Create Server API Documentation](https://www.ctl.io/api-docs/v2/#servers-create-server).

    POST https://api.ctl.io/v2/servers/ALIAS
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

    {
      "name": "web",
      "description": "My web server",
      "groupId": "890312348ddfe311b05f00505682315a",
      "sourceServerId": "RHEL-6-64-TEMPLATE",
      "isManagedOS": false,
      "networkId": "a933432bd1234e84b6c4fa329e48cb8b",
      "password": "P@ssw0rd1",
      "cpu": 2,
      "memoryGB": 4,
      "type": "standard",
      "storageType": "standard"
    }

We get back the following response. Notice the HTTP status is a `202 ACCEPTED`. Also in this message we get two important links that we will use to call in our subsequent steps. The first one is the `status` of the asyncronous job that runs to build the server. The second `self` link is used to query the server itself. (The server name will generated based on the provided name and other parameters like account alias and data center code. Because the name is generated during the server build process and it is not yet built, this URL uses the UUID rather than the name of the server and thus requires the `uuid=True` query parameter.)

    202 ACCEPTED

    {
      "server": "web",
      "isQueued": true,
      "links": [
        {
          "rel": "status",
          "href": "/v2/operations/ALIAS/status/wa1-123456",
          "id": "wa1-123456"
        },
        {
          "rel": "self",
          "href": "/v2/servers/ALIAS/43f5f0becea84694b1d340d399571234?uuid=True",
          "id": "43f5f0becea84694b1d340d399571234",
          "verbs": [
            "GET"
          ]
        }
      ]
    }

#### Get Build Status

Since the server build is an asynchronous process, we use the status link from the response above to query the status of the job.

    GET https://api.ctl.io/v2/operations/ALIAS/status/wa1-123456
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

Before the server build job starts the status will be `notStarted` and while it is still running, the status will be `executing`. Once it is completed it should show `succeeded`.

    200 OK

    { "status":"executing" }

In most cases, the status should continue to be polled until the `succeeded` status is reached before performing any additional action on the server.

#### Get Server

Regardless of the build status, we can query the server directly using the server link returned in the create server response above. Make sure to include the `uuid=True` query parameter to let the API know we are referencing the server using the UUID instead of the alias.

    GET https://api.ctl.io/v2/servers/ALIAS/43f5f0becea84694b1d340d399571234?uuid=True
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

The response provides the details of the server in its current state. Notice the `status` field is set to `underConstruction`, meaning the server is not ready for use yet. (For [managed servers](../Managed Services/managed-operating-system-frequently-asked-questions.md), even after the job status has been set to `succeeded`, the server status will remain `underConstruction` until the server has been completely set up with the necessary services when it will be set to `active`.)

    200 OK

    {
        "id": "wa1ALIASweb01",
        "name": "WA1ALIASWEB01",
        "description": "My web server",
        "groupId": "890312348ddfe311b05f00505682315a",
        "isTemplate": false,
        "locationId": "WA1",
        "osType": "RedHat Enterprise Linux 6 64-bit",
        "os": "redHat6_64Bit",
        "status": "underConstruction",
        "type": "standard",
        "storageType": "standard",
        "changeInfo": {...},
        "links": [...]
    }

A few minutes later (after the job status is `succeeded`) we call the same method and see the server status is now `active` and there is additional information about the server including the name, IP address, and disk information.

    200 OK

    {
        "id": "wa1ALIASweb01",
        "name": "WA1ALIASWEB01",
        "description": "My web server",
        "groupId": "890312348ddfe311b05f00505682315a",
        "isTemplate": false,
        "locationId": "WA1",
        "osType": "RedHat Enterprise Linux 6 64-bit",
        "os": "redHat6_64Bit",
        "status": "active",
        "details": {
            "ipAddresses": [
                {
                    "internal": "10.20.30.40"
                }
            ],
            "alertPolicies": [],
            "cpu": 2,
            "diskCount": 3,
            "hostName": "",
            "inMaintenanceMode": false,
            "memoryMB": 4096,
            "powerState": "started",
            "storageGB": 17,
            "disks": [
                {
                    "id": "0:0",
                    "sizeGB": 1,
                    "partitionPaths": []
                },
                {
                    "id": "0:1",
                    "sizeGB": 2,
                    "partitionPaths": []
                },
                {
                    "id": "0:2",
                    "sizeGB": 14,
                    "partitionPaths": []
                }
            ],
            "partitions": [],
            "snapshots": [],
            "customFields": []
        },
        "type": "standard",
        "storageType": "standard",
        "changeInfo": {...},
        "links": [...]
    }

Now we are ready to interact with the server as needed.

#### Update Server Description

First, we will update the server description using the following request. (We are using the server name in the URI now since it is known from the previous call, but we could continue to use the UUID if we wanted to however we would have to add the `uuid=True` query parameter as we did above.)

    PATCH https://api.ctl.io/v2/servers/ALIAS/wa1ALIASweb01
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

    [
      {
        "op":"set",
        "member":"description",
        "value":"A very important server"
      }
    ]

We receive a `204 NO CONTENT` status meaning the update was successful. (We could use the GET request if we wanted to see the server details with the new description.)

For more information on updating properties of a server, see the [API Documentation](https://www.ctl.io/api-docs/v2/#servers).

#### Restart Server

Finally, we will restart the server using this request:

    POST https://api.ctl.io/v2/operations/ALIAS/servers/reboot
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

    [ "wa1ALIASweb01" ]

Once again, this is an asynchronous job so we get back a link to the status endpoint:

    200 OK

    [
        {
            "server": "wa1bryfweb04",
            "isQueued": true,
            "links": [
                {
                    "rel": "status",
                    "href": "/v2/operations/ALIAS/status/wa1-123458",
                    "id": "wa1-146517"
                }
            ]
        }
    ]

We query the status using the link provided:

    GET https://api.ctl.io/v2/operations/ALIAS/status/wa1-123458
    Content-Type: application/json
    Authorization: Bearer VGCVlA1JK5WLEXicGVujiJblEIApnIJhicZcNZG1MjvJI5IQXJime3tzQYOYHjLuX2NiZLiJvTRi2JOXdcbkX46UWzmIZnJIzpM6JjpmJDB.iX91ML6IzhdX62cekloAB6uJUOjjoi1xClUOBXZmXJxciUzdje2MJM96VM1Mk4NOXubYIXbbiwf06E1YQbeEsKIy1HdizndJWyJVs4XCGiwpTdlyiRXkGrikopi0I5pI.6RYzOrI2lj4bYZsJzeWXGCRNpyXjIbbJLcJL3ckH4CjbisZnZJYMiiIYgD1plIa9JUXuFUG4iymCQV2JXiJluZiziRJYk0b1VJhIRc3M13ihOe

When the server has been restarted successfully, the status will appear as `succeeded`.

    200 OK

    { "status":"succeeded" }
