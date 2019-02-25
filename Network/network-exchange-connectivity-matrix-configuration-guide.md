{{{
  "title": "Network Exchange Availability Matrix and Configuration Guide",
  "date": "2-25-2019",
  "author": "Jason Holland",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Availability Matrix

The table, below, documents the metropolitan areas where Network Exchange is offered and the type and identity of Endpoints that are available there for inclusion into an Exchange. Please note any constraints in the following section.

Region|Metro Area|Colo/<br>DA|Managed<br>Hosting|CLC|CPC|AWS|IQ+|
--------|---------|---------------------------|---------------|-----------------|----------------|----------------|----------------
North<br>America|Chicago, IL|CH3|CH3|IL1|CH3|CH3|CH3
North<br>America|Santa Clara, CA|SC8<br>SC9|SC8<br>SC9|UC1|SC9|SC8<br>SC9|SC8<br>SC9
North<br>America|Seattle, WA|SE2|SE2|WA1||SE2
North<br>America|Sterling, VA|DC2<br>DC3<br>DC4|DC2<br>DC3<br>DC4|VA1|DC3<br>DC4|DC2<br>DC3<br>DC4|DC2<br>DC3<br>DC4
North<br>America|Toronto, CA|TR1|TR1|CA3|||TR1
North<br>America|Weehawken, NJ|NJ2<br>NJ2X|NJ2<br>NJ2X|NY1|NJ2|NJ2<br>NJ2X|NJ2<br>NJ2X
Europe|Frankfurt, DE|FR6|FR6|DE1<br>DE3|||FR6
Europe|London, UK (Reading)|LO6|LO6|GB1|LO6||L06
Europoe|London, UK (Slough)|LO1|LO1|GB3|LO1|L01|L01
Asia<br>Pacific|Singapore, SG|SG2|SG2|SG1|SG2||SG2
Asia<br>Pacific|Sydney, AU|SY7|SY7|AU1|||SY7

### Endpoint Abbreviations
Colo / DA: Colocation / Dedicated Access
CLC: CenturyLink Cloud
CPC: CenturyLink Private Cloud on VMWare Cloud Foundation
AWS: AWS Direct Connect
IQ+: IQ+ in Cyxtera Data Centers

### Configuration Guide

* Only Endpoints in the same metro are allowed within an Exchange.
* There may be multiple instances of an Endpoint type per Exchange except for CenturyLink Cloud. A user may have multiple Exchanges in the same location.
* There can only be one CenturyLink Cloud (CLC) Endpoint per account alias, per data center, no matter the number of Exchanges.
* Once bandwidth for the physical connections (cross connects) between Network Exchange and the end user network for a Colocation/Dedicated Access Endpoint has been established, it cannot be modified without a scheduled service change. Bandwidth over connections is not determined by Network Exchange, but rather, by the physical medium chosen.

For more information, please see the [Network Exchange Product page](https://www.ctl.io/network-exchange/) or the [Network Exchange FAQ](../Network/network-exchange-faqs.md) page. For guidance on creating your first Exchange, see the [Network Exchange Getting Started Guide](../Network/network-exchange-getting-started-guide.md).

Please monitor Network Exchange release notes on ctl.io for news on additional features and site expansion. 