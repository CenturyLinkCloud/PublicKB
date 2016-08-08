{{{
 "title": "Temporary Request Redirection",
 "date": "08-25-2015",
 "author": "Daniel Stephan",
 "attachments": [],
 "contentIsHTML": false
}}}

### Temporary Request Redirection
The S3 protocol supports a feature called Temporary Request Redirection.
This feature is used by S3 to indicate that the requested resource should
be retrieved from a different location. Every S3 compliant client is required to support this redirection. When a client makes a request to S3, S3 can return HTTP 307 with a location indicating where the object is available. The client can then make the request to the new location.

### Why would this happen?
This redirect will happen whenever the region specified for the bucket is
incorrect and the bucket exists in another region. This can occur because
of user error or if your bucket has moved.

As long as you are using a S3 compliant client, these redirects happen seamlessly with no changes needed on your end.

For more information, [see the S3 documentation](//docs.aws.amazon.com/AmazonS3/latest/dev/Redirects.html#TemporaryRedirection).
