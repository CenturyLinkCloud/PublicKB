{{{
  "title": "Create Internet Accessible Network",
  "date": "06-03-2021",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we walk through how to create a new software-defined network in Lumen Private Cloud on VMware Cloud Foundation (LPC on VCF). In this particular use case, we would like to allow this network to have Outbound Internet, and will do the following:

1. Create the Network
2. Create a Firewall Rule to allow Outbound Internet Access for the Network
3. Create a Source NAT Rule to allow Outbound Internet Access for the Network

### Steps

#### Create the Network

Log in to your LPC on VCF environment.

Click __Datacenters__ from the top menu. Select your Datacenter. Select __Networks__ in the left side-panel. On the Networks page, click __NEW__

  ![Network](../../images/dccf/network1.png)

In the __New Organization VDC Network__ page:

__Network Type:__ Select Routed and click __NEXT__

  ![Network](../../images/dccf/network2.png)

__General:__
  * __Name:__ Enter your network name
  * __Gateway CIDR:__ (i.e. 10.20.30.1/24)
  * __Description:__ Optional
  * __Shared:__ Default setting
  * Click __NEXT__

  ![Network](../../images/dccf/network3.png)

__Edge Connection:__
  * Select your Edge
  * __Interface Type:__ Select Distributed
  * __Guest VLAN Allowed:__ Keep default selection
  * Click __NEXT__

  ![Network](../../images/dccf/network4.png)

__Static IP Pools:__
  * Enter an IP range (i.e. 10.20.30.50-10.20.30.200)
  * Click __ADD__
  * Click __NEXT__

  ![Network](../../images/dccf/network5.png)

__DNS:__
  * __Primary DNS:__ (i.e. 8.8.8.8)
  * __Secondary DNS:__ (i.e. 8.8.4.4)
  * __DNS suffix:__ As needed
  * Click __NEXT__

  ![Network](../../images/dccf/network6.png)

__Ready to Complete:__
  * Review your selections and click __FINISH__

  ![Network](../../images/dccf/network7.png)

##### Create the Firewall Rule to allow Outbound Internet Access for the Network

In vCloud Director, under __Networking__, click __Edges__, select your Edge (siteID-edge-0) and click __CONFIGURE SERVICES__

  ![Network](../../images/dccf/network8.png)

In the Edge Gateway - siteID-edge-0 page, ensure __Firewall__ is selected, then click + to add a New Rule

  ![Network](../../images/dccf/network9.png)

Enter the following for the New Rule:

  * __Name:__ Outbound 10.20.30.0 network
  * __Type:__ User (by default)
  * __Source:__ Click IP, enter 10.20.30.0/24 and click KEEP

  ![Network](../../images/dccf/network10.png)

  * __Destination:__ Any (by default) - varies by requirements
  * __Service:__ Any (by default) - varies by requirements
  * __Action:__ Accept
  * __Enable logging:__ Unchecked (by default) - varies by requirements
  * Click __Save changes__

  ![Network](../../images/dccf/network11.png)

##### Create a Source NAT Rule to allow Outbound Internet Access for the Network

In the Edge Gateway - siteID-edge-0 page, click __NAT__, then click __+ SNAT RULE__ (under NAT 44 Rules)

  __Note:__ You will need to make a note of the Public IP that is listed under Translated in order to create this SNAT rule.

  ![Network](../../images/dccf/network12.png)

Enter the following for the New Rule:

  * __Applied On:__ Public-1
  * __Original Source IP/Range:__ 10.20.30.0/24
  * __Translated Source IP/Range:__ This is the Public IP you recorded from the note above
  * Click __KEEP__

  ![Network](../../images/dccf/network13.png)
