{{{
  "title": "FAQ - Load Balancer as a Service",
  "date": "2-1-2017",
  "author": "Matthew Farrell",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

Audience
--

This article is to support customers of both Shared Load Balancer and
Load Balancer as a Service (LBaaS). The responses in this FAQ document
aim to provide additional clarity and expectations to both existing
Shared Load Balancer customers as well as to new prospective LBaaS
customers while we work to introduce LBaaS.

**Q:** What is Load Balancer as a Service (LBaaS)?

**A:** Lumen Load Balancer as a Service (LBaaS) helps you build
highly scalable and highly available applications by providing
application-level (HTTP & TCP) load balancing. It also offers various
persistence methods to ensure that a user, once connected, continues to
be connected to the same application instance.

LBaaS is a load balancing solution that is meant to provide both server
load balancing and high availability in an industry standard.

**Q:** What’s the difference between Lumen Cloud’s existing Shared
Load Balancer service and Lumen Cloud’s new Load Balancer as a
Service (LBaaS)?

**A:** LBaaS provides for all of the existing functionality or our
Shared Load Balancer Service. Every feature that existed previously for
SLB will be present inside of LBaaS. LBaaS however provides additional
features such as:

-   TCP load Balancing

-   Load balance on any port

-   Configurable health checks

**Q:** What Data Center(s) is Load Balancer as a Service (LBaaS) available
in?

**A:** Please review the [Feature Availability Matrix](https://www.ctl.io/knowledge-base/general/hybrid-it/hybrid-it-availability-matrix/) for a list of LBaaS Locations.

**Q:** What if I require a Load Balancer but I don’t have a presence in
a LBaaS enabled Data Center?

**A:** Our Shared Load Balancer service is still available for use in
all non-LBaaS enabled Data Centers. Unfortunately, customers will not
immediately get the benefit of the advanced features provided by LBaaS
such as TCP Load Balancing, Load Balance on any port, and configurable
health checks. Rest assured, our goal is to quickly and seamlessly
integrate LBaaS into all of our Data Centers in short order!

**Q:** What do I do if I have an existing Shared Load Balancer in a LBaaS Service Location?

**A:** This is an easy one! You don’t have to do anything! However, there is a catch (there’s always a catch!). All existing Shared Load
Balancer instances created prior to LBaaS availability will remain in tact and operation just as they are today. Unfortunately, this means that those previous instances will not be LBaaS enabled. We’re working on a feature that will allow for uninterrupted upgrade from the existing Shared Load Balancer to LBaaS. Until that feature is completed, customers can remain on SLB should they choose or create a new VIP using LBaaS and migrate their services.


Any new instances of the new LBaaS service after service availability will be priced according to our [pricing catalog](//www.ctl.io/pricing).

**Q:** Can I add public IP addresses to my load balancer pools?

**A:** No, this is not possible. Using private server IPs is the most efficient way of balancing traffic and is the only option.
