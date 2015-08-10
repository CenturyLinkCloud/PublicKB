{{{
 "title": "Bucket List Operations Timing Out",
 "date": "8-10-2015",
 "author": "Daniel Stephan",
 "attachments": [],
 "contentIsHTML": false
}}}

### Problem Description

Some buckets in CA3 are experiencing intermittent performance degradation
with the list command.  This causes certain buckets to timeout when listing.

### Ways to mitigate the issue

 * If you have a client side timeout setting, try increasing it.
 * You can try using a smaller page size in your list bucket operations.  
 By default, many clients use a page size of 1000.
 * By the design of Object Storage, bucket listing is an expensive
 operation that should be used only when you do not have the object keys.
 Generally, you should have the key of the object you wish to interact with
 and perform an action based on that key.
 * If the design of your implementation requires bucket listing, consider
 using many smaller buckets instead of one large bucket.

### Why is this happening?

We are working with our vendor to resolve the issue and are also taking
multiple steps to improve the performance of the cluster.  We will have
this issue resolved in the near future.
