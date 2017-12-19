{{{
  "title": "Network Exchange Getting Started Guide",
  "date": "06-16-2017",
  "author": "Rob Lesieur",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Product Overview

[Network Exchange](//www.ctl.io/network-exchange/) provides secure, reliable, automated interconnectivity between service networks offered by Network Exchange Providers, including managed hosting, colocation and cloud environments. A Network Exchange Provider is any service provider who has integrated their networking domain for interconnect provisioning by Network Exchange. A Network Exchange User is any credentialed user of Network Exchange who has provider-defined access privileges to two or more Network Exchange Providers. This is the party who ultimately consumes Network Exchange, regardless of the Provider with which they have a direct contractual relationship. An instance of Network Exchange is itself referred to as an Exchange. It is an interconnect between two or more Network Exchange Providers. A Network Exchange User may have one or more Exchanges. A connectivity point for a Network Exchange Provider for a given Exchange is referred to as an Exchange Port. For example, "Colocation" is a type of Exchange Port.

Network Exchange is offered in a pay-as-you-go billing model in which the Network Exchange User pays only for the bandwidth they consume for billable Exchange Port types. Please refer to the Knowledge Base article [Network Exchange Billing Guide ](network-exchange-billing-guide.md) for details on how billing is calculated.

**Note:** All equipment and connectivity is redundant in Network Exchange, including cross connects to colocation and direct connect endpoint types. Non-redundant connectivity is not supported.

### Glossary

* **Network Exchange:** Provides secure, reliable, automated interconnectivity between service networks within a metro-area computing environment.
  * **Network Exchange Provider:** Any service provider who has integrated their networking domain for interconnect Network Exchange.  
This integration comes in two common sub-types:
    * **Software Defined Integration:** Dynamic allocation of networks, IPs and routing by an API-driven resource model
    * **Configured Integration:** Automated allocation of networks, IPs and routing by Provider-defined manual entry for which the Provider is responsible
  * **Network Exchange User:** Any credentialed users of Network Exchange who has Provider-defined access privileges to two or more Network Exchange Providers.  This is the party who ultimately consumes Network Exchange, regardless of the Provider with which they have a direct contractual relationship.
    * **Exchange:** An interconnect between two or more Network Exchange Providers. A Network Exchange User may have one or more Exchanges.
    * **Exchange Port:** The connectivity point for a Network Exchange Provider for a given Exchange.

* Common Provider business models include:
  * **Hosted Service Provider:** Primarily provides SaaS or managed services on infrastructure hosted by CenturyLink o External Managed Service Provider: Primarily provides services to others on infrastructure not operated by CTL, i.e. IaaS clouds, SaaS platforms, Colocation providers.
  * **External Network Service Provider:** Primarily provides WAN services, e.g. Level3, Comcast.
  * **CenturyLink Managed Service Provider:** Any CTL-provided service, e.g. CLC, DCC, Managed Hosting, Network Exchange or CenturyLink Managed Network Provider: Any CTL-provided network, e.g. IQ, CTL-SDWAN
* **On-Net Provider:** A service provider, fitting any of the above sub-models, who is directly or indirectly reachable via Network Exchange
* **On-Net Traffic:** Network traffic that leaves Network Exchange to a CenturyLink Managed Service Provider, CenturyLink Managed Network Provider or Hosted Service Provider
* **Egress Traffic:** Network traffic that leaves Network Exchange to an External Managed Service Provider or External Network Service Provider
* **Network Exchange Reseller:** A Provider who also offers white-labeled Network Exchange interconnectivity, providing their customers access to all On-Net Providers.

### Prerequisites

* You must be logged in to perform the functions outlined in this guide.
* The desired Exchange Port type should be verified as supported at the desired data center(s). Please refer to the Knowledge Base article [Network Exchange Availability Matrix](network-exchange-connectivity-matrix-configuration-guide.md).
* The desired Exchange Ports / data center combination(s) per Exchange should be validated as a supported configuration in the Knowledge Base article [Network Exchange Configuration Guide](network-exchange-connectivity-matrix-configuration-guide.md) once Exchange Port availability has been validated, per the previous step.
* Each Exchange Port type has certain prerequisites, capabilities and caveats that should be understood before setting up an Exchange. Please see the following Knowledge Base documents for details:
	* [Network Exchange CenturyLink Cloud Exchange Ports](network-exchange-clc-endpoint-guide.md)
	* [Network Exchange Managed Hosting Exchange Ports](network-exchange-clc-managed-hosting-endpoint-guide.md)
	* [Network Exchange Colocation Exchange Ports](network-exchange-clc-colocation-endpoint-guide.md)
	* [Network Exchange Dedicated Access Exchange Ports](network-exchange-clc-dedicated-access-endpoint-guide.md)

### Exceptions

Network Exchange is designed to enable connectivity between any supported Exchange Port type in any supported data center. Under certain circumstances, not all supported Exchange Port types will be available at every supported data center. Any exceptions to this general rule will be noted in the Knowledge Base article [Network Exchange Configuration Guide](network-exchange-connectivity-matrix-configuration-guide.md) in the addendum. Retirement of known exceptions will be published in the [CenturyLink Cloud release notes](//www.ctl.io/knowledge-base/release-notes/2017/#1).

### Log-in to Network Exchange

1. Log-in to [Control Portal](https://control.ctl.io/auth/Login?ReturnUrl=%2f) using your ctl.io username and password.

2. From the left side navigation menu, click on **Products > Network Exchange**.
  
   ![Network Exchange Portal](../images/netx-getting-started-guide-1-v2.png)

### Creating An Exchange

   ![Network Exchange Portal](../images/netx-getting-started-guide-2-v2.png)

Click on the "Create an Exchange" button.

   ![Network Exchange Portal](../images/netx-getting-started-guide-3-v2.png)

In the top-left corner of the screen, select the (sub)account to be used for this Exchange.

In the **Name Your Exchange** dialogue box:

1. Enter the **Exchange Name**. This name will be appended with a randomly generated
number to create a unique identifier for this Exchange. Note that this field may not contain spaces.

2. Enter the **Description**. This free form text is used to describe the Exchange you are
creating. This field should be utilized to differentiate amongst Exchanges.

43. Only usage-based billing is available at this time and therefore no selection is required for **Billing Type**.

    **Note:** “Account Alias” is a four character ID that will be auto-populated after the first step, and thus does not need to be manually entered.

    **Note:** CenturyLink Service Delivery teams acting on behalf of a customer should enter the customer’s Account Alias here.

4. Click **Next**.

   ![Network Exchange Portal](../images/netx-getting-started-guide-3a-v2.png)

On the Network Exchange **Select Feature 1** screen:

1. Select the endpoint from the drop down menu for **Select Feature Type** from the options of **Cloud**, **Colocation**, **Managed Hosting**. Endpoints may be added in any order.

2. Click **Next**.

Follow the instructions for the selected endpoint type from the options, below. You may add endpoints in any order and in any combination per supported configurations. The desired Exchange Ports / data center combination(s) per Exchange should be validated as a supported configuration in the Knowledge Base article [Network Exchange Configuration Guide](network-exchange-connectivity-matrix-configuration-guide.md).

### Create a Cloud Endpoint

   ![Network Exchange Portal](../images/netx-getting-started-guide-4-v2.png)

1. Select **Cloud** from the **Select Feature Type** drop down menu.

2. Click **Next**.

    **Note:** You may cancel this operation by clicking the red X on the screen, or, by selecting the **Back** button. 

      ![Network Exchange Portal](../images/netx-getting-started-guide-5-v2.png)

1. Select the provider from the **Select Provider** drop down menu. 

2. Click **Next**.

    **Note:** You may cancel this operation by clicking the red X on the screen, or, by selecting the **Back** button. 
    
     ![Network Exchange Portal](../images/netx-getting-started-guide-6-v2.png)

1. Select a data center from the **Datacenter** drop down menu.

2. Click **Next**.

**Notes**

* You may cancel this operation by clicking the red X on the screen, or, by selecting
the "Back" button.
* If this is your first endpoint, you will be prompted to enter a second endpoint. If you have entered an endpoint previously, you will be navigated to the **Review Your Request** flyout. See instructions below on how to proceed.

### Create a Colocation or “Dedicated Access" Endpoint

   ![Network Exchange Portal](../images/netx-getting-started-guide-7-v2.png)

1. Select **Colocation** or **Dedicated Access** from the **Select Feature Type** drop down menu.

2. Click **Next**. You may cancel this operation by clicking the red X on the screen, or, by selecting the **Back** button.

    **Note:** "Dedicated access" refers to a dedicated connection between Network Exchange and a CenturyLink Managed Service, that bypasses HAN.

     ![Network Exchange Portal](../images/netx-getting-started-guide-8-v2.png)

1. Select the provider from the **Select Provider** drop down menu.

2. Click **Next**.

    **Note:** You may cancel this operation by clicking the red X on the screen, or, by selecting the **Back** button.
  
     ![Network Exchange Portal](../images/netx-getting-started-guide-9-v2.png)

1. Select a colocation data center from the **Datacenter** drop down menu.

2. Select the Routing Type: Static or BGP.

3. Click "**Next**"

     ![Network Exchange Portal](../images/netx-getting-started-guide-10-v2.png)

**For static endpoints**

1. Select the static route to be applied to the connection. 

2. Select the CIDR for the route.

3. Click **Next**.

**Notes**

* You may cancel this operation by clicking the red X on the screen, or, by selecting the "Back" button.
* If this is your first endpoint, you will be prompted to enter a second endpoint. If you have entered an endpoint previously, you will be navigated to the **Review Your Request** flyout. See instructions below on how to proceed.

     ![Network Exchange Portal](../images/netx-getting-started-guide-11-v2.png)


**For BGP endpoints**

1. Enter the private ASN for your network.

2. Click **Next**.

**Notes:**

* You may cancel this operation by clicking the red X on the screen, or, by selecting
the **Back** button.
* If this is your first endpoint, you will be prompted to enter a second endpoint. If you
have entered an endpoint previously, you will be navigated to the **Review Your Request** flyout. See instructions below on how to proceed.


### Create a Managed Hosting Endpoint

   ![Network Exchange Portal](../images/netx-getting-started-guide-12-v2.png)

1. Select **Managed Hosting** from the **Select Feature Type** drop down menu.

2. Click **Next**. You may cancel this operation by clicking the red X on the screen, or, by selecting the **Back** button.

   ![Network Exchange Portal](../images/netx-getting-started-guide-13-v2.png)
   
Select the **Provider** from the drop down list.

   ![Network Exchange Portal](../images/netx-getting-started-guide-14-v2.png)

1. Select the **Datacenter** from the drop down list.

2. Enter the **VLAN A** value.

3. Enter the **VLAN B** value.

4. Click **Next**.

**Notes:**

* VLAN "A" and VLAN "B" are provided by a CenturyLink account manager and are based on the VLANs that are set up in the in the CenturyLink data center’s managed hosting network. Please see [Network Exchange Managed Hosting Exchange Ports](network-exchange-clc-managed-hosting-endpoint-guide.md) for details on how to obtain these.
* You may cancel this operation by clicking the red X on the screen, or, by selecting the "Back" button.
* If this is your first endpoint, you will be prompted to enter a second endpoint. If you have entered an endpoint previously, you will be navigated to the **Review Your Request** flyout. See instructions below on how to proceed.

### Completing Your Request

   ![Network Exchange Portal](../images/netx-getting-started-guide-15-v2.png)

Upon selecting two endpoints, you will reach the “Review Your Request” flyout.

1. Review your request to ensure the specifications for the Exchange you have configured.

2. Click on “Submit”. You will be navigated to the main Network Exchange screen which will display the Exchange you have just created and the status of the build. During creation the status will display “BUILDING” and that Exchange will not be accessible. Upon completion, the status will change to “ACTIVE”.

Note: The values displayed will reflect user selections. The image provided is for reference only.

### Adding an Endpoint to an Exchange

   ![Network Exchange Portal](../images/netx-getting-started-guide-16-v2.png)

1. Select the desired Exchange, which must have an “ACTIVE” status.

2. Select **Add Additional Endpoint**.

   ![Network Exchange Portal](../images/netx-getting-started-guide-17-v2.png)

* Click **Next**.

6. Follow the instructions for the particular endpoint type, above. Note that instead of displaying a “BUILDING” status as in the Completing Your Request section above, this action displays a “UPDATING” status.

   ![Network Exchange Portal](../images/netx-getting-started-guide-18-v2.png)

### Removing an Endpoint from an Exchange

   ![Network Exchange Portal](../images/netx-getting-started-guide-19-v2.png)

**Note:** Endpoints may not be deleted from an Exchange if there are less than three endpoints.

1. Select the Exchange containing the endpoint you wish to delete.

2. Select the endpoint you wish to delete.

3. Click **Delete Endpoint**.

4. Click **Yes** or **No** when prompted. The status will indicate “UPDATING” during the deletion process.


### Deleting an Exchange

   ![Network Exchange Portal](../images/netx-getting-started-guide-20-v2.png) 
   
1. Select the Exchange you wish to delete.

2. Click **Delete Exchange**.

3. Click **Yes** or **No** when prompted. The status will indicate “DELETING” during the deletion process.

### Q & A

**Q: How many Exchanges may an End User have?**

**A:** There are currently no limitations on the number of Exchanges per End User. See the Knowledge Base article [Network Exchange Configuration Guide](network-exchange-connectivity-matrix-configuration-guide.md) for more details.

**Q: How many endpoints may be in an Exchange?**

**A:** An Exchange may include a number of endpoints up to the maximum Exchange Port
types available in a metro area served by Network Exchange. See the Knowledge Base article [Network Exchange Configuration Guide](network-exchange-connectivity-matrix-configuration-guide.md) for more details.

**Q: How do I convert from Cloud Network Service to Network Exchange?**

**A:** A Knowledge Base article Migrating from Cloud Network Service to Network Exchange will be provided in the future that will discuss this in detail.

**Q: Can I change the name of an Exchange once it’s created.**

**A:** No. You will have to delete and recreate the Exchange with the name of your choice.

**Q: How do I know when I can use an Exchange?**

**A:** Exchanges will pass traffic any time it has an “ACTIVE” status. Note that for
colocation and direct connect endpoints, cross connects must be in place and the destination networks including the connectivity endpoints must be configured correctly
for traffic to pass.

**Q: Who should I contact for Support?**

**A:** Support requests should be emailed to [help@ctl.io](mailto:help@ctl.io).
