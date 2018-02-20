{{{
  "title": "Object Storage Error Code: 503 Slow Down",
  "date": "2-8-2018",
  "author": "Daniel Stephan",
  "attachments": [],
  "contentIsHTML": false
}}}

### Symptom
You send a request to Object Storage and receive the following error message in return:
   ```
   503 Slow Down
   ```

### Cause
The error is generated when the request limit has been exceeded.

### Resolution
Review our [request rate and performance considerations article](../Object Storage/request-rate-and-performance-considerations.md) to look over design patterns you can implement to eliminate these errors and scale more efficiently. We recommend that you ensure your application properly handles this response and automatically scales the request rate back.
