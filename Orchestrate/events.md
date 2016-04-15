{{{
  "title": "Events",
  "date": "04-07-2016",
  "author": "Daniel Morton",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

`Events` associate time-ordered data with key/value objects. They power audit trails, logs, and timelines.

`Events` are a perfect fit for time-ordered data that needs to be associated with a specific item in a collection. Audit history and activity trails are great examples of `Events` data in action, because `Events` are always associated with a specific item in a collection, and are always ordered by a timestamp.

### Storing Events
As an example, we can store a timeline of activity for our user. Specify a collection (users) and key (kates-user-id), and then the event type. Orchestrate supports the storage of multiple types of events for a key/value object. For example, we could store events for the user's timeline, as well as for a history of logins.

### Request
```
curl -i "https://api.orchestrate.io/v0/users/kates-user-id/events/timeline" \
-XPUT \
-H "Content-Type: application/json" \
-u '12345678-1234-1234-1234-123456789012:' \
-d '{"type": "liked", "page_title": "Photos from my trip"}'
```

### Response
```
HTTP/1.1 204 No Content
```

### Retrieving Events
Retrieve all events for Kate to display her timeline.

### Request
```
curl -i "https://api.orchestrate.io/v0/users/kates-user-id/events/timeline" \
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
        "kind": "event",
        "key" : "kates-user-id",
        "type" : "timeline",
        "timestamp": 1425398999671,
        "ordinal": 618485351434448900,
        "ref": "f8a86a25029a907b",
        "reftime": 1425398999671,
        "ordinal_str": "08954d2677087000"
      },
      "value" : {
        "type" : "liked",
        "page_title" : "Photos from my trip"
      },
      "timestamp": 1425398999671,
      "ordinal": 618485351434448900,
      "reftime": 1425398999671
    }
  ]
}
```
Optionally, we can specify the start and end times, if we only want events from a certain time span.

### Request
```
curl -i "https://api.orchestrate.io/v0/users/kates-user-id/events/timeline?startEvent=1384534722568&endEvent=1403206439244" \
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
        "kind": "event",
        "key" : "kates-user-id",
        "type" : "timeline",
        "timestamp": 1425398999671,
        "ordinal": 618485351434448900,
        "ref": "f8a86a25029a907b",
        "reftime": 1425398999671,
        "ordinal_str": "08954d2677087000"
      },
      "value" : {
        "type" : "liked",
        "page_title" : "Photos from my trip"
      },
      "timestamp": 1425398999671,
      "ordinal": 618485351434448900,
      "reftime": 1425398999671
    }
  ]
}
```

### Searching Events
Retrieve all events mentioning 'trip'.

### Request
```
curl -i "https://api.orchestrate.io/v0/users?query=%40path.kind%3Aevent%20AND%20trip" \
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
        "kind": "event",
        "key" : "kates-user-id",
        "type" : "timeline",
        "timestamp": 1425398999671,
        "ordinal": 618485351434448900,
        "ref": "f8a86a25029a907b",
        "reftime": 1425398999671,
        "ordinal_str": "08954d2677087000"
      },
      "value" : {
        "type" : "liked",
        "page_title" : "Photos from my trip"
      },
      "score": 10.33141040802002,
      "reftime": 1406572291885
    }
  ]
}
```

[Next: Clients](https://orchestrate.io/docs/clients)
