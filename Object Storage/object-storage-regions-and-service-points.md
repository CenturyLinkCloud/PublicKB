{{{
  "title": "Object Storage Regions and Service Points",
  "date": "07-05-2016",
  "author": "Daniel Stephan",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description
The CenturyLink Cloud Object Storage service is available in multiple regions. A region consists of two data centers, a primary and a secondary. You can only read and write to the primary. You cannot directly interact with the secondary. Under certain circumstances, the service promotes the secondary to primary. Once you create a bucket in a specific region, you need to use the appropriate service point to interact with that bucket.  

Here is a list of the different regions, the individual data centers that comprise the region, and the region service points.  

### Service Points
|Region|Primary Data Center|Secondary Data Center|Service Point|
|---|---|---|---:|
|Canada|CA1|CA3|canada.os.ctl.io|
|US-East|VA1|NY1|useast.os.ctl.io|
