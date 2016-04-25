{{{
  "title": "Geospacial Search",
  "date": "04-07-2016",
  "author": "Daniel Morton",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

Orchestrate provides a Geospatial Search API to make working with geolocation data easier.

With Geospatial Search you can query items by their distance from a point, find items in a specified area using bounding boxes, and sort results by distance.

Any object with fields that Orchestrate recognizes as representing a latitude and longitude can be queried. For example, consider this Key/Value item:
```
{
    "name": "Eiffel Tower",
    "location": {
        "latitude": 48.8582,
        "longitude": 2.2945
    }
}
```

Orchestrate understands the `location` field contains geographic data because the `latitude` and `longitude` fields contain numbers representing [decimal degrees](https://en.wikipedia.org/wiki/Decimal_degrees). That field can be named anything, not just `location`. Orchestrate will also understand `lat` as short for `latitude`, and `lon`, `long`, and `lng` as short for `longitude`. The values of these fields must be numbers, so Orchestrate can use them as decimal degrees.

### Geo Distance Queries
We can do a search for all items within a certain distance of a point using `NEAR` in the search's query string:

### Request
```
curl -i "https://api.orchestrate.io/v0/places?query=value.location:NEAR:%7blat:12.3%20lon:56.7%20dist:100km%20%7d" \
  -u "$api_key:"
```

### Syntax
Geo Distance queries uses `NEAR:{location}` to specify the latitude and longitude for a geographic point and how far from it to search for items. For example:
`value.location:NEAR:{latitude:12.3 longitude:56.7 radius:100km}`

Each argument accepts various aliases:

* latitude: lat
* longitude: lon, long, lng
* radius: distance, dist, dst, rad

`radius` and its aliases require some measure of units, like kilometers or miles. Orchestrate understands various units across multiple systems of measurement:

|**Unit**|**Definition**|**System**|
|:------:|:------------:|:--------:|
|   km   |   kilometer  |  metric  |
|    m   |     meter    |  metric  |
|   cm   |  centimeter  |  metric  |
|   mm   |  millimeter  |  metric  |
|   mi   |     mile     | imperial |
|   yd   |     yard     | imperial |
|   ft   |     foot     | imperial |
|   in   |     inch     | imperial |
|  nmi   | nautical mile| nautical |

### Sorting by Distance
When you're retrieving items by their proximity to a point, you can sort results by distance from that point:
```
curl -i "https://api.orchestrate.io/v0/places?query=value.location:NEAR:%7blat:12.3%20lon:56.7%20dist:100km%20%7d&sort=value.location:distance:asc" \
  -u "$api_key:"
```

### Syntax
The syntax for sorting by distance uses `distance` in the `sort` query parameter, like this:
`?sort=value.location:distance:asc`

Sorting by distance can either be done in ascending (`asc`) or descending (`desc`, `dsc`) order.

Distance sorting requires your query includes a `NEAR` clause.

To retrieve all items and sort them by distance, set your `radius` value to at least 20,037.5 km (or `20037.5km`). That's half the distance around the world, and thus the furthest distance two points could be from one another.

### Response
```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Tue, 07 Oct 2014 21:32:53 GMT
Vary: Accept-Encoding
X-ORCHESTRATE-REQ-ID: 7eada7c0-4e69-11e4-acec-12313d2f7cdc
transfer-encoding: chunked
Connection: keep-alive
```

```
{
  "results": [
    {
      "distance": 24.90598414714105,
      "value": {
        "lon": 56.87,
        "lat": 12.45,
        "id": "abc"
      },
      "path": {
        "ref": "d0d884bbeaa236cf",
        "key": "abc",
        "collection": "places"
      }
    },
    {
      "distance": 65.77211629374432,
      "value": {
        "lon": 56.32,
        "lat": 12.76,
        "id": "xyz"
      },
      "path": {
        "ref": "492acb11bc54cd6d",
        "key": "xyz",
        "collection": "places"
      }
    }
  ],
  "total_count": 2,
  "count": 2
}
```

Each item in the result set contains a `distance` value that indicates how far the item is from the geographic point specified in the query. This distance is in the same units as the query itself.

### Geo Bounding Box Queries
To retrieve all items within a particular area, you can specify a bounding box and return all items within it. For example:
```
curl -i "https://api.orchestrate.io/v0/places?query=value:IN:%7bnorth:12.5%20east:57%20south:12%20west:56%20%7d" \
  -u "$api_key:"
```

### Syntax
Unlike Geo Distance queries, Geo Bounding Box queries use `IN:{location}` to specify the geometry of the bounding box. For example:

`value.location:IN:{north:12.5 east:57 south:12 west:56}`

`north` and `south` represent latitudinal bounds, while east and west represent longitudinal bounds.

Each argument can take various aliases:

* north: n
* south: s
* east: e
* west: w

### Response
```
HTTP/1.1 200 OK
Content-Type: application/json
Date: Tue, 07 Oct 2014 21:32:52 GMT
Vary: Accept-Encoding
X-ORCHESTRATE-REQ-ID: 7e5834c0-4e69-11e4-acec-12313d2f7cdc
transfer-encoding: chunked
Connection: keep-alive
```

```
{
  "results": [
    {
      "score": 1,
      "value": {
        "lon": 56.87,
        "lat": 12.45,
        "id": "abc"
      },
      "path": {
        "ref": "d0d884bbeaa236cf",
        "key": "abc",
        "collection": "places"
      }
    }
  ],
  "total_count": 1,
  "count": 1
}
```

[Next: Graph](https://www.ctl.io/knowledge-base/orchestrate/graph/)
