{{{
  "title": "Network Exchange Connectivity Matrix and Configuration Guide",
  "date": "05-08-2018",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Availability Matrix

The table, below, documents the metropolitan areas where Network Exchange is offered and the type and identity of Endpoints that are available there for inclusion into an Exchange. Please note any constraints in the following section.

Metro Area|Colocation/<br>Dedicated Cloud Compute|Managed Hosting|CenturyLink Cloud
----------|------------------------------------|---------------|-----------------
Ashburn, VA|DC2|DC2<br>DC3<br>DC4|VA1
Santa Clara, CA|SC8|SC8<br>SC9|UC1
Chicago, IL|CH3|CH3|IL1
New Jersey, NJ|NJ2|NJ2<br>NJ2X|NY1
London, UK|LO1|LO1|GB3
London, UK|LO6|LO6|GB1
Frankfurt, DE|FR6|FR6|DE3
Toronto, Canada|TR1|TR1|CA3
Sydney, AU|SY7|SY7|AU1
Singapore, SG|SG2|SG2|SG1


### Configuration Guide

* Only Endpoints in the same metro are allowed within an Exchange.
* There may be multiple instances of an Endpoint type per Exchange except for CenturyLink Cloud, further explained in the next bullet. Barring other constraints, a single user may have multiple Exchanges in the same location.
* There can only be one CenturyLink Cloud (CLC) Endpoint per account alias, per data center, no matter the number of Exchanges.
* Once bandwidth for the physical connections (cross connects) between Network Exchange and the end user network for a Colocation/Dedicated Access Endpoint has been established, it cannot be modified without a scheduled service change. Bandwidth over connections is not determined by Network Exchange, but rather, by the physical medium chosen.

For more information, please see the [Network Exchange Product page](https://www.ctl.io/network-exchange/) or the [Network Exchange FAQ](../Network/network-exchange-faqs.md) page. For guidance on creating your first Exchange, see the [Network Exchange Getting Started Guide](../Network/network-exchange-getting-started-guide.md).

Please monitor Network Exchange release notes on ctl.io for news on additional features and site expansion. 
