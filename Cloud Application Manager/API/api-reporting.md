{{{ "title": "Reporting API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

Get the cost report of your organization.

### Manage an Organization

|  Resource  |  Description |
|------------|--------------|
| GET /services/organizations/{organization}/report/{start}/{end} | Gets the report of the amount spent per instance and day of a period of time. |
| GET /services/organizations/{organization}/csv/{start}/{end} | Gets the report of the amount spent per instance and day of a period of time in CSV format. |

### GET /services/organizations/{organization}/report/{start}/{end}

Gets the report of the amount spent per instance and day of a period of time.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Wrong date format (400)
* User not authorized to get the reports (403)
* Organization not found (404)

**URL parameters**

* organization: name of the organization
* start: day of the start date in format ‘YYYY-MM-DD’
* end: day of the end date in format ‘YYYY-MM-DD’

**Request Headers**

```
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```
**Response Parameters**

|  Parameter  |      Type     |   Description   |
|-------------|---------------|-----------------|
| Cost |  Array | List of cost per instance. Contains the following properties:<ul><li>cost: Array of ints. Each number in the list represents the amount of fraction of dollar cents spent that day in the specific instance.</li><li>service: Service associated with the instance, contains among other properties:</li><ul><li>state_history: List of changes in the state of the instance. Each state contains the following properties:</li><ul><li>started: Required. String that represents the date in UTC when it changed its state.</li><li>state: Required. “up” or “down”. Tells whether the instance was up or down.</li><li>completed: String that represents the date in UTC when it finished the current state.</li></ul></ul></ul> |

**Response Body**

```
{
   "cost":[
      {
         "cost":[
            0,
            0,
            0,
            0,
            0,
            1300,
            3000,
         ],
         "service":{
            "profile":{
               "subnet":"us-west-1a",
               "cloud":"EC2",
               "image":"ami-a8d3d4ed",
               "elastic_ip":true,
               "instances":1,
               "keypair":"None",
               "role":"None",
               "location":"us-west-1",
               "volumes":[

               ],
               "flavor":"t1.micro",
               "security_groups":[

               ],
               "schema":"http://elasticbox.net/schemas/aws/ec2/profile"
            },
            "schema":"http://elasticbox.net/schemas/service",
            "provider_id":"5908ee9b-0c0a-4af6-8eef-2dc9f95d033a",
            "tags":[

            ],
            "deleted":"2015-11-16 10:40:11.484485",
            "variables":[

            ],
            "created":"2015-11-12 16:45:05.246651",
            "state_history":[
               {
                  "started":"2015-11-12 16:47:02.399111",
                  "state":"up",
                  "completed":"2015-11-13 09:29:20.728718"
               }
            ],
            "updated":"2015-11-13 09:29:20.730134",
            "token":"e327e9fb-b6c8-43fe-af94-b2f339e3d6a8",
            "state":"done",
            "organization":"elasticbox",
            "operation":"terminate",
            "type":"Linux Compute",
            "id":"eb-zwm7u",
            "machines":[
               {
                  "name":"eb-zwm7u-1",
                  "token":"cfa24ede-172f-4427-b55e-4d134cce3252",
                  "state":"processing",
                  "address":{
                     "public":"54.241.36.174",
                     "private":"10.251.133.133"
                  },
                  "external_id":"i-76dad8b6",
                  "schema":"http://elasticbox.net/schemas/aws/service-machine"
               }
            ],
            "icon":"images/platform/linux.png"
         }
      }
   ]
}
```

### GET /services/organizations/{organization}/csv/{start}/{end}

Gets the report of the amount spent per instance and day of a period of time in CSV format.

**Normal Response Codes**

* 200

**Common Error Response Codes**

* Wrong date format (400)
* User not authorized to get the reports (403)
* Organization not found (404)

**URL Parameters**

* Organization_name: name of the organization
* start: day of the start date in format ‘YYYY-MM-DD’
* end: day of the end date in format ‘YYYY-MM-DD’

**Request Headers**

```
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Body**

```
SERVICE_ID,DAY (in Date Range),SIZE,REGION,PROVIDER_TYPE,PROVIDER_ID,PROFILE_SCHEMA,CREATED (UTC),TYPE,COST (cents of $),EVENT_TYPE,INSTANCES,SIZE.CPU,SIZE.MEMORY,SIZE.DISK,CPU UNIT,MEMORY UNIT,DISK UNIT,ALLOCATED.CPU (Max.),ALLOCATED.MEMORY (Max.),ALLOCATED.DISK (Max.)
  eb-o125v,2015-10-18,m1.small,us-east-1,Amazon Web Services,5908ee9b-0c0a-4af6-8eef-2dc9f95d033a,http://elasticbox.net/schemas/aws/ec2/profile,2015-11-12 16:29:31.993282,Linux Compute,0
  eb-o125v,2015-10-19,m1.small,us-east-1,Amazon Web Services,5908ee9b-0c0a-4af6-8eef-2dc9f95d033a,http://elasticbox.net/schemas/aws/ec2/profile,2015-11-12 16:29:31.993282,Linux Compute,0
```

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
