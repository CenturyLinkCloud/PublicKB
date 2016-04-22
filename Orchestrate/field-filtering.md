{{{
  "title": "Field Filtering",
  "date": "04-07-2016",
  "author": "Daniel Morton",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

The Orchestrate API provides a convenient mechanism for filtering result JSON objects to include only the field values you actually need from each query. This is conceptually similar to the way a relational database lets you select individual fields from a record (`SELECT id, first_name, last_name FROM USERS`) instead of selecting the entire record every time (`SELECT * FROM USERS`).

Field-filtering in the Orchestrate API is controlled by two query string parameters, which you can send to any API endpoint that returns JSON bodies:

|**Parameter**|**Description**|
|-------------|---------------|
|`with_fields`|A list of fully-qualified field names to include in the filtered JSON body|
|`without_fields`|A list of fully-qualified field names to exclude from the filtered JSON body|

For example, consider this JSON record:
```
{
  "a" : 1,
  "b" : [{
    "c" : 1,
    "d" : 2
  },{
    "c" : 3,
    "d" : 4
  }]
}
```

An application dependent upon this data might only need to retrieve the value of the `"a"` field in some cases, and we could omit the value of the `"b"` field entirely. It should come as no surprise then that are two different ways to filter the fields:
```
curl -XGET http://api.orchestrate.io/v0/my_collection/my_key
   ?with_fields=value.a

curl -XGET http://api.orchestrate.io/v0/my_collection/my_key
   ?without_fields=value.b
```

With either query the resultant filtered JSON would look like this:
```
{ "a" : 1 }
```

The `with_fields` and `without_fields` parameters can also be used together to achieve more advanced filtering operations. The `with_fields` predicate is always applied first, causing all the designated field values to be cloned into a new object. If the `with_fields` predicate is empty, all field values are copied by default. Then, the `without_fields` predicate is applied to the resultant JSON and all the designated field values are subtracted from the cloned subset.

When used in concert, the two operations are most useful when blacklisting a subordinate field of an object whose values we've already whitelisted. So, given our previous example, we could combine a `with_fields=value.b` clause with a `without_fields=value.b.d` to create the following result:
```
{
  "b" : [{
    "c" : 1
  },{
    "c" : 3
  }]
}
```

By designating the deeply-nested field name `value.b.d` as a blacklist field, we erase that value from all the deeply-nested children, even within arrays. You can use this functionality to optimize payload sizes, or to avoid retrieving sensitive data when it's not absolutely necessary.

Field filtering is available everywhere in the API where JSON results are served: from simple `HTTP GET` requests to key-ordered listings and search queries, across all of our data types: key-value items, time-series events, and graph relationships.
