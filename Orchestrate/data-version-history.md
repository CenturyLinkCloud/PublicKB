{{{
  "title": "Data Version History",
  "date": "4-20-2015",
  "author": "Adam DuVander",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

All Key/Value items in Orchestrate have a version history, a list of all the changes to the item over time.

[Data in Orchestrate is immutable](//www.ctl.io/developers/blog/post/immutability) and the majority of operations are non-destructive. When updating a Key/Value item, Orchestrate creates a new version (instead of overwriting the original), and adds it to the version history.

This non-destructive behavior enables you to track changes, retrieve previous values of a Key/Value item, restore deleted values, or manage state when multiple actors are changing values in parallel.

### What's in a Version?

A version comprises:

* **Ref** - a content-based hash of the Key/Value item's value.
* **Reftime** - the timestamp (as milliseconds since epoch) that the update occurred.

Even if a Key/Value item is updated to the same value (i.e. same ref) multiple times, each update will have a different timestamp, thus creating distinct versions.

### Using Refs

When an item is retrieved by key, the current version of that item is returned. When you specify a ref for an item, you’ll get the value of that item at a particular point in time.

Every ref can be retrieved via its fully-qualified path:

```
GET https://api.orchestrate.io/v0/$collection/$key/refs/$ref
```

```
{
  "path": {
      "collection": "collection",
      "key": "some-key",
      "ref": "c4c3fc3bca065572"
  },
  "value": {
      "field_name": "some_value"
  },
  "reftime": 1400085119216
}
```

The version history of a Key/Value item is also available via the uri path:

```
GET https://api.orchestrate.io/v0/$collection/$key/refs
```

```
{
  "count": 3,
  "results": [
    {
      "path": {
        "collection": "collection",
        "key": "key",
        "ref": "cbb48f9464612f20"
      },
      "reftime": 1400085119216
    },
    {
      "path": {
        "collection": "collection",
        "key": "key",
        "ref": "1c5df46404b6db87"
      },
      "reftime": 1400085117084
    },
    {
      "path": {
        "collection": "collection",
        "key": "key",
        "ref": "61691089abf12e18"
      },
      "reftime": 1400085084739
    }
  ]
}
```

Each version in the resulting list will have a `ref` and `reftime`. By default, the Key/Value item's value for each version is not included. To include each version’s value, you can add a `values=true` parameter to the request:

```
GET https://api.orchestrate.io/v0/$collection/$key/refs/?values=true
```

```
{
  "count": 3,
  "results": [
    {
      "path": {
        "collection": "collection",
        "key": "key",
        "ref": "cbb48f9464612f20"
      },
      "value": {
        "field_name": "some_value"
      },
      "reftime": 1400085119216
    },
    {
      "path": {
        "collection": "collection",
        "key": "key",
        "ref": "1c5df46404b6db87"
      },
      "value": {
        "field_name": "some_value"
      },      
      "reftime": 1400085117084
    },
    {
      "path": {
        "collection": "collection",
        "key": "key",
        "ref": "61691089abf12e18"
      },
      "value": {
        "field_name": "some_value"
      },
      "reftime": 1400085084739
    }
  ]
}
```

> See the [Refs](//orchestrate.io/docs/apiref#refs) in the [API Reference](//orchestrate.io/docs/apiref) for language specific usage and further information.

### Dangling Refs

A Key/Value item's version history may contain "dangling” or orphaned refs. This is because the `reftime` only supports millisecond precision.

Updating a Key/Value item's values many times in the same millisecond will create distinct refs. These refs are always retrievable by their ref path. But, when fetching a Key/Value item's version history, only one version per millisecond will be on the list. Which leaves the other refs dangling.
