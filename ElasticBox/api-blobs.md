{{{
"title": "API Blobs",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}
**Manage Blobs**

**Resource**|**Description**
------------|----------
[POST /services/blobs/upload](./api-blobs.md) | Uploads a file using multi-part form data.
[POST /services/blobs/upload/{file_name}](./api-blobs.md) | Creates a blob from submitted data.
[GET /services/blobs/download/{file_id}/{file_name}](./api-blobs.md) | Downloads a file uploaded previously.

**POST /services/blobs/upload**

Uploads a file using multi-part form data when you give these parameters in the request body: url, length, upload_date, and content_type.

**Normal Response Codes**

* 200

**Error Response Codes**

* Bad Request (400)

![Screen Shot 2016-12-12 at 12.04.37 PM.png](https://ucarecdn.com/1272ead4-14b1-46dd-b33f-0e132623b7ba/)

**Response Parameters**

![blob2.png](https://ucarecdn.com/e8bd2430-9e54-4a78-9d78-7024b5807d1e/)

```
{
   "url":"/services/blobs/download/533577cb7d0083310b7c9600/arrow.png",
   "upload_date":"2014-03-28 13:23:23.462060",
   "length":1287,
   "content_type":"image/png"
}
```
**POST /services/blobs/upload/{file_name}**

Creates a blob from submitted data when you give the file name.

**Normal Response Codes**
* 200

**Error Response Codes**
* Bad request (400)

**Request Parameters**

![blob3.png](https://ucarecdn.com/934e0206-5487-4a14-82f5-72459a2e203f/)

![blobs4.png](https://ucarecdn.com/05930ed5-5609-453b-a538-b45192fe16ef/)

**Response Parameters**

![blob5.png](https://ucarecdn.com/0fb1ac32-a54b-49c8-b3b0-9f6f7c9533b3/)
