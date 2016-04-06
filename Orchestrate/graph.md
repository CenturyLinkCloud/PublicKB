{{{
  "title": "Graph",
  "date": "04-07-2016",
  "author": "Daniel Morton",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

Graph queries create and retrieve relationships between items such as user profiles, accounts, or businesses. The Orchestrate Graph API puts no constraint on the number of relationships in your data set.

For example, use Graph to follow relationships between users, to query which products a user likes, or even to associate a set of photos with a specific user.

### Creating a Graph Relationship
Let's create a relationship between Kate and her friend Rob. Relationships are one-directional so Kate will follow Rob but Rob won't follow Kate (we can do bi-directional with two API calls).

### Request
```
curl -i "https://api.orchestrate.io/v0/users/kates-user-id/relation/follows/users/robs-user-id" \
-XPUT \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
HTTP/1.1 204 No Content
```

### Retrieving Graph Relationships
Let's now find all the users that Kate follows.

### Request
```
curl "https://api.orchestrate.io/v0/users/kates-user-id/relations/follows" \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "count" : 1,
  "results" : [
    {
      "path" : {
        "collection" : "users",
        "key" : "robs-user-id",
        "ref" : "7ba7b24ab0f7d85b"
      },
      "value" : {
        "name" : "Rob Miller",
        "bio" : "Developer from Portland, OR",
        "twitter" : "@robthesnob"
      },
      "reftime" : 1403202446328
    }
  ]
}
```

### Extended Graph Relationships
Let's take it a step further and find all likes for every user Kate follows. All we need to do is query the relationship follows/likes.

### Request
```
curl "https://api.orchestrate.io/v0/users/kates-user-id/relations/follows/likes" \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "count" : 2,
  "results" : [
    {
      "path" : {
        "collection" : "items",
        "key" : "motorcycles",
        "ref" : "2db214072d3cf000"
      },
      "value" : {
        "are" : "awesome",
        "name" : "Motorcycles"
      },
      "reftime" : 1403203471815
    },
    {
      "path" : {
        "collection" : "items",
        "key" : "pixels",
        "ref" : "b8a154d509710fe5"
      },
      "value" : {
        "name" : "Pixels"
      },
      "reftime" : 1403203471805
    }
  ]
}
```

### Removing a Graph Relationship
Removing relationships is simple. If Kate no longer wants to follow Asa, specify the relationship and call the appropriate method:

### Request
```
curl -i "https://api.orchestrate.io/v0/users/kates-user-id/relation/follows/users/robs-user-id?purge=true" \
-XDELETE \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
HTTP/1.1 204 No Content
```

### Other Uses
We could use Graph for other things as well. Let's say we have a `users` collection and a `photos` collection. When a user uploads a photo we create a new key/value object for it in our `photos` collection but we want to associate the photo with the user. We can create a Graph relationship between them.

### Request
```
curl -i "https://api.orchestrate.io/v0/users/kates-user-id/relation/posted/photos/the-photo-id" \
-XPUT \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
HTTP/1.1 204 No Content
```
Run a Graph search to get all photos Kate has posted.

### Request
```
curl "https://api.orchestrate.io/v0/users/kates-user-id/relations/posted" \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "count" : 2,
  "results" : [
    {
      "path" : {
        "collection" : "photos",
        "key" : "the-photo-id",
        "ref" : "7838eeddc1ff3700"
      },
      "value" : {
        "file" : "/photos/awesome.jpg",
        "name" : "Cool stuff"
      },
      "reftime" : 1403206042919
    },
    {
      "path" : {
        "collection" : "photos",
        "key" : "the-photo-id2",
        "ref" : "2ffe10d89e25baaa"
      },
      "value" : {
        "file" : "/photos/awesome.jpg",
        "name" : "Great stuff"
      },
      "reftime" : 1403206042894
    }
  ]
}
```

### Pagination and Limits
We can also have Orchestrate use an offset and limit so we can page through the relationships. If there are more results than the requested limit, the response will include a `next` field that will be a uri that can be used to fetch the next page of results. There will be a `prev` field to fetch the previous page. These links will also be included as Link headers in the HTTP response. The default limit is 10, and the maximum is 100.

### Request
```
curl "https://api.orchestrate.io/v0/users/kates-user-id/relations/posted?limit=1&offset=1" \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "count" : 1,
  "results" : [
    {
      "path" : {
        "collection" : "photos",
        "key" : "the-photo-id2",
        "ref" : "2ffe10d89e25baaa"
      },
      "value" : {
        "file" : "/photos/awesome.jpg",
        "name" : "Great stuff"
      },
      "reftime" : 1403206042894
    }
  ],
  "prev" : "/v0/users/kates-user-id/relations/posted?limit=1&offset=0"
}
```

[Next: Events](https://www.ctl.io/knowledge-base/orchestrate/events/)
