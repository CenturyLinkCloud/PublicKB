{{{
  "title": "Creating a Server",
  "date": "7-12-2021",
  "author": "John Grant",
  "keywords": ["cpc", "cloud", "vm", "server", "ssl", "vapp", "vpn", "vcf"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we demonstrate how to provision a new virtual server in Lumen Private Cloud on VMware Cloud Foundation™.

Once you've gone through this KB article and created a new virtual server, you can follow the  [Configure SSL VPN-Plus](../Security/configuring-sslvpn-plus.md) guide to configure the Lumen Private Cloud on VMware Cloud Foundation environment.

Note: This KB assumes you have followed the KB article on [Adding to your Catalog](../Catalog/add-to-catalog.md) in Lumen Private Cloud on VMware Cloud Foundation.

### Steps
* Log in to your Lumen Private Cloud on VMware Cloud Foundation (LPC on VCF) environment.

  ![Login to Lumen Private Cloud on VMware Cloud Foundation](../../images/dccf/login-html5.png)

* Once logged in, select __Data Centers__ from the menu at the top of the screen, and then click the Data Centers summary box. 

![Data Centers Summary](../../images/dccf/data-centers-summary.png)

* You will then land on a page showing all your VMs. In the left side panel, select __vApps__ below Compute. 

![Select vApps](../../images/dccf/new-vapp.png)

* Select __NEW VAPP__. A popup window will appear. Enter a name for the new vApp you are creating — in the context of VMware Cloud Director, a vApp is simply a container for the objects you create. Once you enter a Name, click __ADD VIRTUAL MACHINE__. 

  ![Quick Access](../../images/dccf/creating-a-server3-html5.png)

* In the New VM popup window, type a name for your Virtual Machine &mdash; this is the friendly name that will be displayed inside of VMware Cloud Director. Enter your __Computer Name__ &mdash; the Computer Name will default to the same as the Name but can be edited as needed. For __Type__ of VM, select __New__ or __From Template__. If choosing __From Template__, the Compute details can be updated in later steps. Click __OK__.

  ![Select Name and Location](../../images/dccf/creating-a-server4-html5.png)

* On the New vApp window, you can add additional Virtual Machines to your vApp, or you can click __CREATE__.

  ![Configure Networking](../../images/dccf/creating-a-server5-html5.png)

* After clicking __CREATE__ you will be navigated back to the vApps screen. If you would like to update details within your vApp or VM, and add a Network, locate your vApp and click __DETAILS__.

  ![Configure Networking](../../images/dccf/creating-a-server6-html5.png)

### Configure a Network

* Select __Data Centers__ in the top menu.

* Click __Networks__. Then click __NEW__.

  ![Configure Networking](../../images/dccf/creating-a-server7-html5.png)

* In the New Organization VDC Network wizard, click Scope, and then select Current Organization Virtual Data Center.

* Click __NEXT__. 

  ![Configure Networking](../../images/dccf/new-org-vdc-network-scope.png)

* Select the Network Type (__Isolated__ or __Routed__). Click __NEXT__.

  ![Configure Networking](../../images/dccf/new-org-vdc-network-type.png)

* Select the Edge Connection (for Routed networks). Click __NEXT__.

  ![Configure Networking](../../images/dccf/new-org-vdc-edge-connection.png)

* For General, type the Name and Gateway CIDR (Classless Inter-Domain Routing). Click __NEXT__.

  ![Configure Networking](../../images/dccf/new-org-vdc-network-general.png)

* For Static IP Pools, type the Gateway CIDR and the Static IP Pools range. Click __NEXT__.

  ![Configure Networking](../../images/dccf/new-org-vdc-network-ip-pools.png)

* For DNS, type the Primary and Secondary DNS, and the DNS suffix. Click __NEXT__.

  ![Configure Networking](../../images/dccf/new-org-vdc-network-dns.png)

* For Ready to Complete, review the settings and click __FINISH__.

  ![Configure Networking](../../images/dccf/new-org-vdc-network-ready-to-complete.png)

* If you would like to update the Compute details on your VM, click __Data Centers__ in the top menu, click the Data Centers summary box, and then click the __Name__ of your VM. You will then be able to edit General fields, Hardware, Guest OS Customization, Guest Properties, Monitoring, and Metadata. 

  ![Configure Networking](../../images/dccf/creating-a-server9-html5.png)

* To navigate back to your vApps page, click __Data Centers__ at the top of the screen, then click the Data Centers summary box, and then click __DETAILS__ for your vAPP.

  ![Configure Networking](../../images/dccf/creating-a-server6-html5.png)

* Click __POWER ON__.

  ![Configure Networking](../../images/dccf/creating-a-server11-html5.png)
