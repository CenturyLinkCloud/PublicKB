{{{
  "title": "Search",
  "date": "04-07-2016",
  "author": "Daniel Morton",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

Orchestrate automatically creates a full-text search index for every object you store. With just a single call to the REST API, you can perform complex searches.

Search queries allow the retrieval of key/value objects based on their contents. When an object is put into Orchestrate, the document is analyzed and its contents are indexed. Orchestrate does not require schemas. Instead, the first time it sees a field in an object it determines the type based on the contents of the field. Each collection will have its own implicit schema based on the contents of its object.

### Find a User
We can do a simple search on any field. The following will search for any occurrence of "Portland".

### Request
```
curl -i "https://api.orchestrate.io/v0/users?query=Portland" \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "count" : 2,
  "total_count" : 2,
  "results" : [
    {
      "path" : {
        "collection" : "users",
        "key" : "kates-user-id",
        "ref" : "c1c04f3cdfafa321"
      },
      "value" : {
        "name" : "Kate Robbins",
        "hometown" : "Portland, OR",
        "twitter" : "@katesfaketwitter"
      },
      "score" : 0.09589150547981262
    },
    {
      "path" : {
        "collection" : "users",
        "key" : "robs-user-id",
        "ref" : "8b184d87be5b0163"
      },
      "value" : {
        "name" : "Rob Miller",
        "bio" : "Developer from Portland, OR",
        "twitter" : "@robthesnob",
        "hometown" : "Portland, OR"
      },
      "score" : 0.09589150547981262
    }
  ]
}
```

### More Refined Search
But what if we want to find only the users who's home town is "Portland, OR". We can tell Orchestrate to only match a specific field by searching for `value.hometown: "Portland, OR"`.

### Request
```
curl -i "https://api.orchestrate.io/v0/users?query=value.hometown%3A%20%22Portland%2C%20OR%22" \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "count" : 1,
  "total_count" : 1,
  "results" : [
    {
      "path" : {
        "collection" : "users",
        "key" : "kates-user-id",
        "ref" : "c1c04f3cdfafa321"
      },
      "value" : {
        "name" : "Kate Robbins",
        "hometown" : "Portland, OR",
        "twitter" : "@katesfaketwitter"
      },
      "score" : 0.3835660219192505
    }
  ]
}
```

### Pagination and Limits
We can also have Orchestrate use an offset and limit so we can page through the results.

### Request
```
curl -i "https://api.orchestrate.io/v0/users?query=value.hometown%3A%22Portland%2C%20OR%22&limit=1&offset=1" \
-u '12345678-1234-1234-1234-123456789012:'
```

### Response
```
{
  "count" : 1,
  "total_count" : 2,
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
        "twitter" : "@robthesnob",
        "hometown" : "Portland, OR"
      },
      "score" : 0.0767132043838501
    }
  ],
  "prev" : "/v0/users?limit=1&amp;query=Portland&amp;offset=0"
}
```

### Complex Queries
Orchestrate harnesses the power of [Lucene](http://lucene.apache.org/core/4_5_1/queryparser/org/apache/lucene/queryparser/classic/package-summary.html#Overview) for full text search.

### Boolean Operators
You can use `AND`, `OR`, and `NOT`.

`value.name: "Portland" AND NOT "Maine"`

### Grouping
Grouping allows for complex boolean statements to be made.

`(node.js AND developer) OR (engineer AND full-stack)`

### Field Grouping
Statements can be grouped, such that a boolean statement can apply to a specific field. This will search an array of tags and match any that contain both "node.js" and "developer" OR "engineer" and "full-stack".

`value.tags: (node.js AND developer) OR (engineer AND full-stack)`

### Wildcards
Orchestrate offers two wildcards `?` and `*`.

`?` matches any single character. `*` matches any number of characters.

For example: `value.tags: ruby*` will match the tags "Ruby" as well as "Ruby on Rails".

[Read more about Orchestrate's Search Syntax](https://orchestrate.io/docs/apiref#search-syntax)

[Read more about Lucene](https://www.ctl.io/developers/blog/post/querying-the-enron-email-trove-with-lucene)

### Searching Items, Events, and Graph Relationships
So far, we've only considered searching the key-value Items you've stored in your Orchestrate database. But Orchestrate also supports timestamped Event objects, and Graph objects representing the relationships between Items. Event and Graph objects can have their own JSON properties, and Orchestrate lets you search those objects using exactly the same Lucene syntax you use to search for Items.

By default, Orchestrate only returns Items from search queries. But you can enable Event and Graph results by adding a clause to your query filtering the `@path.kind` field. For example, this query would return only Event objects with the phrase "mountain biking" in the description.

`@path.kind:event AND value.description:"mountain biking"`

Likewise, this query would return only the Graph Relationship objects having a "coworker" relation, with the word "orchestrate" in the company name field.

`@path.kind:relationship AND @path.relation:coworker AND value.company:orchestrate`

You can even search for multiple object kinds simultaneously like this:

`@path.kind:(item OR event) AND value.foo:bar`

Or like this:

`@path.kind:* AND value.foo:bar`

[Read more about Event Search](https://orchestrate.io/docs/apiref#search-events)

[Read more about Graph Relationship Search](https://orchestrate.io/docs/apiref#search-graph-relationships)

### Sorting
Orchestrate also supports sorting search results by field value. By default, search queries return results in order of decreasing relevance: items with more matches get a higher score than items with fewer matches. By adding a sort parameter along with the field name and order we want to sort by, we can customize the sorting behavior.

We can sort users with the hometown "Portland, OR" in ascending order by name like this:

```
curl -i "https://api.orchestrate.io/v0/users?query=value.hometown%3A%20%22Portland%2C%20OR%22&sort=value.name:asc" \
  -u '12345678-1234-1234-1234-123456789012:'
```

Or, you can sort in descending order like this:

```
curl -i "https://api.orchestrate.io/v0/users?query=value.hometown%3A%20%22Portland%2C%20OR%22&sort=value.name:desc" \
  -u '12345678-1234-1234-1234-123456789012:'
```

### Multiple Field Sorting
What if we updated our user object by adding fields for first and last names?
```
{
  "name" : {
    "first": "Kate",
    "last": "Robbins"
  },
  "hometown" : "Portland, OR",
  "twitter" : "@katesfaketwitter"
}
```

It's not uncommon to encounter multiple items with identical field values (e.g., many users with the same surname). With Orchestrate, we can sort search results by multiple field names.

Let's sort our users primarily by last name. Whenever two users have the same last name, we'll tell Orchestrate to sort by first name as well:
```
curl -i "https://api.orchestrate.io/v0/users?query=value.hometown%3A%20%22Portland%2C%20OR%22&sort=value.name.last:asc,value.name.first:asc" \
  -u "$api_key:"
```

[Read more about Sorting](https://orchestrate.io/docs/apiref#sorting)


[Next: Geospacial](https://www.ctl.io/knowledge-base/orchestrate/geospacial/)
