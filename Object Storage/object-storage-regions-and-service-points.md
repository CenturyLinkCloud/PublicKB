{{{
  "title": "Object Storage Regions and Service Points",
  "date": "5-12-2016",
  "author": "Daniel Stephan",
  "attachments": [],
  "contentIsHTML": false
}}}
### Description
The CenturyLink Cloud Object Storage service is available in multiple regions.  A region consists of two data centers, a primary and secondary.  You can only read and write to the primary.  You cannot directly interact with the secondary.  Under certain circumstances, the service will promote the secondary to primary.  Once you create a bucket in a specific region, you will need to use the appropriate service point to interact with that bucket.  Below we have listed the different regions, the individual data centers that make up a region, and the service points of that region.  

### Service Points
|Region|Data Centers|Service Point|
|---|---|---:|
|Canada|CA3[P], CA1[S]|canada.os.ctl.io|
|US-East|VA1[P], NY1[S]|useast.os.ctl.io|

[P] - Primary data centers  
[S] - Secondary data centers
