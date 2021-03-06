{{{
  "title": "Introducing Object Storage",
  "date": "6-15-2021",
  "author": "Daniel Stephan, updated by Randy Roten",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}
### Description

Lumen Edge Private Cloud now has a robust, geo-based Object Storage service capable of storing any type of digital content. Perfect for data backups, media distribution, and file transfers, the Lumen Edge Private Cloud Object Storage is Amazon S3-compatible and accessible from the Lumen Edge Private Cloud Control Portal or via API calls. 

### Audience

- Lumen Edge Private Cloud Users
### FAQ

#### Q: Is this software home-grown or is this based on a commercial product?

A: Lumen Edge Private Cloud Object Storage is based on a popular software package with targeted extensions to optimize it for Lumen Edge Private Cloud.

#### Q: What are the key vocabulary terms for Object Storage?

A: Object Storage is deployed in a series of "regions" which include data centers for each Lumen Edge Private Cloud geography (a full list of available regions is [here](https://www.ctl.io/knowledge-base/edge-computing-solutions/getting-started/lumen-cloud-data-center-locations/). Object Storage uses "buckets" to hold "objects." Buckets are flat (no hierarchy) and can contain an unlimited number of objects and unlimited amount of storage. "Access Control Lists" (ACLs) describe permissions to a bucket and the objects within it. Object Storage "users" have an "access key ID" and "secret access key" which act as the user's username and password for accessing storage.

#### Q: How do Object Storage users relate to Lumen Edge Private Cloud users?

A: Object Storage users are distinct from Lumen Edge Private Cloud users, but all reside under Lumen Edge Private Cloud accounts. A Lumen Edge Private Cloud user may create multiple Object Storage users that have different access to their buckets. For example, you can create "application users" that a web application uses to retrieve objects from buckets.
#### Q: What kind of data belongs in Object Storage?

A: Object Storage is for key-value data. It is a schema-less repository that can store large objects (up to 5 TB) and is perfect for archive data, Microsoft Office documents, and more.

#### Q: How available is my data?

A: Data stored in an Object Storage region is stored in a highly available, fault-tolerant way. When data is stored, it is written to a data center where it is stored in an industry standard, highly redundant method. Data is also replicated to an additional data center in the same region where it is again stored using the same redundant method. This combination of redundancy and replication yields a robust, always-on Object Storage solution.

#### Q: How do I interact with Object Storage?

A: Bucket Administrators can use the Lumen Edge Private Cloud Control Portal to create users, create buckets, and secure buckets. Object users and developers have their choice of numerous best-of-breed tools for interfacing with objects.

#### Q: What can I do in the Control Portal vs. 3rd party tools?

A: The following breakdown explains what is available in the Control Portal and what you should use 3rd party tools for:

##### CONTROL PORTAL ONLY
- Create user 

##### BOTH CONTROL PORTAL AND 3RD PARTY TOOLS
- List all buckets for user
- Create a bucket
- Delete a bucket 
- View bucket ACLs (permissions) 
- Set bucket ACLs (permissions) 
- See bucket region
- See bucket owner name|

##### 3RD PARTY TOOLS ONLY
- Add object to bucket
- Delete object in bucket
- View object ACLs (permissions)
- Set object ACLs (permissions)
- Perform multi-part upload for large objects

#### Q: Can I list all the buckets that I have access to, even if I'm not the owner?

A: No. The Object Storage API for retrieving bucket lists only returns buckets where the user is the owner. Users can use the Control Portal to view buckets across all users in an account.

#### Q: What are those built-in role types (All Users, Authenticated Users) for?

A: Built-in Access Control Lists (ACLs) make it easy to share access with a broad population. While you can add individual users to your bucket (and those users can then interface with that bucket via the API) you also may want to make a bucket (or object) public by giving "All Users" a "Read" permission. This would let public Internet users list the contents of a bucket or view an individual object. The "Authenticated Users" ACL lets any user with a valid Object Storage access key ID interact with the selected object.