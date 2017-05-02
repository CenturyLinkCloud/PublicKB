{{{
  "title": "Network Exchange Connectivity Matrix and Configuration Guide",
  "date": "04-27-2017",
  "author": "Rob Lesieur",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Availability Matrix

The table, below, documents the metropolitan areas where Network Exchange is offered and the type and identity of endpoints that are available there for inclusion into an Exchange. Please note any constraints in the following section.

Metro Area|Colocation/<br>Dedicated Cloud Compute|Managed Hosting|CenturyLink Cloud
----------|------------------------------------|---------------|-----------------
Ashburn, VA|DC2|DC2<br>DC3<br>DC4|VA1<br>VA2
Santa Clara, CA|SC8|SC8<br>SC9|UC1
Chicago, IL|CH3|CH3|IL1
New Jersey|NJ2|NJ2<br>NJ2X|NY1
London, UK|LO1|LO1|GB3
Toronto, Canada|TR1|TR1|CA3

Please monitor Network Exchange release notes on ctl.io for additional site availability.

### Configuration Guide

* Only endpoints in the same metro are allowed within an Exchange.
* There may be only a single instance of an endpoint type per exchange. Barring other constraints, the same type of endpoint may appear in multiple exchanges for a single end user.
* There can only be one CenturyLink Cloud (CLC) endpoint per account alias no matter the number of exchanges.
* Once bandwidth for the physical connections (cross connects) between Network Exchange and the end user network for a colocation/direct connect endpoint has been established, it cannot be modified without a scheduled service change. Bandwidth over connections is not determined by Network Exchange, but rather, by the physical medium chosen.

Please monitor Network Exchange release notes on ctl.io for additional capabilities and constraint relief.
