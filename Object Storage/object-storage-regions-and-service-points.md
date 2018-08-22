{{{
  "title": "Object Storage Regions and Service Points",
  "date": "07-10-2017",
  "author": "Daniel Stephan",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description
The CenturyLink Cloud Object Storage service is available in multiple regions. A region consists of two data centers, a primary and a secondary. You can only read and write to the primary. You cannot directly interact with the secondary. Under certain circumstances, the service promotes the secondary to primary. Once you create a bucket in a specific region, you need to use the appropriate service point to interact with that bucket.  

Here is a list of the different regions, the individual data centers that comprise the region, and the region service points.  Please note, too, that our service endpoints leverage wildcard (SSL) certificates for the respective region, as shown in the table below.

### Service Points
Region|Primary Data Center|Secondary Data Center|Service Point|SSL Certificate
---|---|---|---|---:|
Canada|CA1|CA3|canada.os.ctl.io|*.canada.os.ctl.io|
US-West|WA1|UC1|uswest.os.ctl.io|*.uswest.os.ctl.io|
US-East|VA1|NY1|useast.os.ctl.io|*.useast.os.ctl.io|
Germany|DE1|DE3|germany.os.ctl.io|*.germany.os.ctl.io
