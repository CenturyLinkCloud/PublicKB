{{{
  "title": "Object Storage Error Code: 503 Slow Down",
  "date": "5-11-2016",
  "author": "Daniel Stephan",
  "attachments": [],
  "contentIsHTML": false
}}}
### Symptom
You send a request to Object Storage and receive the following error message:
```
503 Slow Down
```
### Cause
This is caused when the request limit has been exceeded.

### Resolution
In order to avoid receiving this message, you must reduce your request rate.  This request limit changes based on several factors such as the current load of the service.  We recommend that you ensure your application properly handles this response and automatically scales the request rate back.
