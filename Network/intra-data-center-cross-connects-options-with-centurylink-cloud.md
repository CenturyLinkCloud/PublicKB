{{{
  "title": "Intra-Data Center Cross Connects Options with CenturyLink Cloud",
  "date": "1-26-2016",
  "author": "Dave Burkhardt",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This Knowledge Base provides an overview for customers who are considering deploying an intra-data center cross connect. The labor for this deployment is a [service task](//www.ctl.io/service-tasks/), performed by platform engineers to specifications provided by the customer.

### Cross Connects Description and Benefits
CenturyLink Cloud offers [multiple connectivity options](../Network/network-access-options-for-connecting-to-centurylink-clouds-platform.md) for its customers to leverage when deciding how they will connect to their resources deployed on CenturyLink Cloud’s platform (e.g., VPN tunnels, CNS, Cross Connects, etc). That said, as a point of clarity, this Knowledge Base article specifically pertains to the deployment of cross connects.

In summary, cross connects are directly connected redundant network circuits between two physically isolated organizations within a data center provider’s facility. Currently, CenturyLink Cloud has [presence within the data centers listed in our KB](../General/centurylink-cloud-data-center-locations.md). This direct connectivity allows for fast, low-latency secure connections – a perfect combination for enterprises who want to securely extend their network into the cloud. While this process may differ slightly in each data center, this article describes the general options and decisions that need to be considered.

Many of our data center providers are within in multiple building across their respective metropolitan areas, and therefore “campus cross connects” are also an option for customers to consider (e.g., Customer is in Equinix’s CH1 building and CenturyLink Cloud is in Equinix’s CH3 building). These connections are usually more costly, but are a feasible option to be considered.

### Planning Your Cross Connect
The first decision a customer needs to determine is how they want to purchase the cross connect. There are generally two options available to a customer:
  * Option 1 - The customer purchases the cross connect directly from the data center provider:
    * Pros: In the long run, this is cheaper for the customer as they are purchasing the cross connect directly from the data center provider.
    * Cons: The customer is responsible for the coordination of the cross connect implementation with the data center provider directly.</p>

  * Option 2 - The customer purchases the cross connect from CenturyLink Cloud:
    * Pros: CLC manages the implementation of the cross connect with the data center provider. The costs of the cross connect will come as part of the customer’s normal CLC monthly invoice.

Regardless, if a customer chooses to purchase the cross connect on their own, there still will be a fee that will include the following services:
  * Verify cross connect connectivity options with data center provider
  * Process Letter of Authorization (LOA) data center provider
  * Coordinate schedules to hold 30min "pre-turn-up" call and actual turn-up call
  * 1hr of time to work with customer to test and turn-up circuit

Note: additional fees may need to be authorized if customer requests CenturyLink Cloud (CLC) to:
  * Manage customer's 3rd party vendors
  * Design or document cross connect configurations
  * Setup a test environment
  * Turn-up calls last longer than 1hr
  * Provide recommendations/guidance on routing configurations (e.g., BGP, OSPF, etc)

Also, in addition to the Professional Services fee, a monthly port fee will be charged by CLC to cover cost for:
  * Parts associated to connect the data center provider’s cross connect to CLC’s router – this typically includes cabling and the Single Mode Fiber (SMF, 1310nm) 1Gbps (1000base-LX) and/or or 10gbps (10G-LR) transceiver optics.
  * Usage of the router port required for the cross connect
  * 24x7x365 monitoring and incident resolution of the connection/port

### Ordering Cross Connects
CenturyLink Cloud requires dual cross connects for redundancy.

Once a purchasing decision is made, the following will need to be ascertained/submitted:
  * All data center providers require a Letter of Authorization (LoA) to install a cross connect. In summary, LoAs provide data center authorization to provision the cross connects- although the responsibility to create the LoA is dependent on who is ordering the cross connect (e.g., CLC or our customer):
    * If the customer purchases the cross connect from the data center provider, CLC will supply a LoA to the customer, and then the customer will need to submit it to the data center.
    * If the customer buys the cross connect from CLC, the customer will need to give CLC a LoA and then the CenturyLink Cloud will submit the completed
  LoA the data center provider.
  * Determine the circuit requirements. CLC's currently only offers Single Mode Fiber (SMF, 1310nm) 1Gbps (1000base-LX) or 10gbps (10G-LR) fiber. We can also support 1 Gbps copper if the cross connect is less than 100m in length. Additionally, as a few points of clarity we do not offer support for:
    * Multi-Mode fiber (MMF, generally 850nm wavelength) is not supported (Note: 1 Gbps is 1000base-SX, 10 Gbps is 10G-SR)
    * Extended fiber distances (10G-ER, 10G-ZR, CWDM, DWDM etc).
    * Desktop initiated Internet access
  * Verify circuit hand-off will be native Ethernet hand-offs – e.g., no DS-3, SONET, OC3
  * Determine the preferred routing protocol (e.g., static, BGP, OSPF).
  * Will the cross connect be deployed within one of [the data centers/campuses.](../General/centurylink-cloud-data-center-locations.md)
  * Determine if any specific IP address ranges are required for CLC. Note, CLC can generally only provide /24 networks for customers, but if a specific requirement is needed CenturyLink Cloud will evaluate such requests.

Once the aforementioned is decided, the next steps are for CLC’s customers to complete the LoA (if CenturyLink Cloud is purchasing the cross connect on the customer’s behalf) and authorize an agreement for any associated costs. Customers should expect a minimum of two week lead time to provision most cross connect deployments once all of the paperwork has been finalized.
