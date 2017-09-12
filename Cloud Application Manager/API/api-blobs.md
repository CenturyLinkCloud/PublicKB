{{{
"title": "Blobs API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

**Manage Blobs**

| Resource | Description |
|----------|-------------|
| POST /services/blobs/upload | Uploads a file using multi-part form data. |
| POST /services/blobs/upload/{file_name} | Creates a blob from submitted data. |
| GET /services/blobs/download/{file_id}/{file_name} | Downloads a file uploaded previously. |

### POST /services/blobs/upload

Uploads a file using multi-part form data when you give these parameters in the request body: url, length, upload_date, and content_type.

**Normal Response Codes**

* 200

**Error Response Codes**

* Bad Request (400)

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| url | string | The URL of the uploaded file. |
| length | integer | The file length in bytes. |
| upload_date | string | The upload date. |
| content_type | string | The content type of the file. |

```
{
   "url":"/services/blobs/download/533577cb7d0083310b7c9600/arrow.png",
   "upload_date":"2014-03-28 13:23:23.462060",
   "length":1287,
   "content_type":"image/png"
}
```

### POST /services/blobs/upload/{file_name}

Creates a blob from submitted data when you give the file name.

**Normal Response Codes**
* 200

**Error Response Codes**
* Bad request (400)

**Request Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| tags | string | Box tags. |
| bindings | string | List of Box bindings. |
| binding | object | Binding contained in the bindings list, each binding have a box and a name. |
| owner | string | Box owner, the user name for a personal workspace and the workspace name for a team workspace. |
| name | string | Box name. |
| description | string | Box description. |
| service | string | Required. Can be one of these types: Linux Compute, Windows Compute, CloudFormation Service. |
| icon | string | Icon url. |
| schema | string | Box schema. |

```
Headers:

Content-Type: application/json
Elasticbox-Token: your_authentication_token
ElasticBox-Release: 4.0
```

**Response Parameters**

| Parameter | Type | Description |
|-----------|------|-------------|
| url | string | The URL of the uploaded file. |
| length | integer | The file length in bytes. |
| upload_date | string | The upload date. |
| content_type | string | The content type of the file. |

```
{
   "url":"/services/blobs/download/53357ac57d0083310b7c960b/miblob",
   "upload_date":"2014-03-28 13:36:05.227905",
   "length":143951,
   "content_type":"multipart/form-data"
}
```

### GET /services/blobs/download/{file_id}/{file_name}

Downloads a file uploaded previously when you give the file_id and the file_name. You can get the full download URL from the response body of the file upload request.

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

| Parameter | Type | Description |
|-----------|------|-------------|
| url | string | The URL of the uploaded file. |
| length | integer | The file length in bytes. |
| upload_date | string | The upload date. |
| content_type | string | The content type of the file. |

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
