{{{
  "title": "Key/Value Data",
  "date": "04-07-2016",
  "author": "Daniel Morton",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

Key/Values in Orchestrate are how you store most data. At it's basic level, it's a JSON object store. You specify a unique key and then the JSON value to store. Keys are unique to a collection and are used to store and retrieve an object.

### Storing Data
Let's store some data for a new user in our app. For our key we will assign the user a unique user ID, and for the value we will save a JSON object with the user's data. We use the user ID rather than the email because we want to use a key that won't ever change.

### Request
```
curl https://api.orchestrate.io/v0/users/kates-user-id \
-X PUT \
-H 'Content-Type:application/json' \
-u '12345678-1234-1234-1234-123456789012:' \
-d '{"name": "Kate Robbins", "hometown": "Portland, OR", "twitter": "@katesfaketwitter"}'
```

### Response
```
HTTP/1.1 201 Created
```

### Retrieving Data
Now let's get the user data. We just specify the key and are returned the JSON object for that user.

### Request
```
curl https://api.orchestrate.io/v0/users/kates-user-id \
-X GET \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "name": "Kate Robbins",
  "hometown": "Portland, OR",
  "twitter": "@katesfaketwitter"
}
```

### Updating Data
Let's add a new field to our user data. One of the ways we can accomplish this is through a `PATCH` request. Using this method, we only need the key of our user to manipulate the data, rather than retrieving the entire user item.

### Request
```
curl -i "https://api.orchestrate.io/v0/users/kates-user-id" \
  -XPATCH \
  -H "Content-Type: application/json-patch+json" \
  -u "$api_key" \
  -d '[{ "op": "add", "path": "favorite_food", "value": "Pizza" }]'
```

### Response
```
HTTP/1.1 201 Created
```

For more about patch requests, see the [Patch API Reference](https://orchestrate.io/docs/apiref#keyvalue-patch).

[Next: Search](https://www.ctl.io/knowledge-base/orchestrate/search/)
