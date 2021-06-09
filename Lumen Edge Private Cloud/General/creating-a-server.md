{{{
  "title": "Creating a Server",
  "date": "06-09-2021",
  "author": "Hannah Melvin",
  "keywords": ["cpc", "cloud", "vm", "server", "ssl", "vapp", "vpn", "vcf"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we demonstrate how to provision a new virtual server in Lumen Private Cloud on VMware Cloud Foundation™.

Once you've gone through this KB article and created a new virtual server, you can follow these guides to learn how to [Configure SSL VPN-Plus](../Security/configuring-sslvpn-plus.md) and [How to Securely Connect](../Security/how-to-securely-connect.md) to your Lumen Private Cloud on VMware Cloud Foundation environment.

Note: This KB assumes you have followed the KB article on [Adding to your Catalog](../Catalog/add-to-catalog.md) in Lumen Private Cloud on VMware Cloud Foundation (LPC on VCF).

### Steps
* Login to your Lumen Private Cloud on VMware Cloud Foundation environment.

  ![Login to Lumen Private Cloud on VMware Cloud Foundation](../../images/dccf/login-html5.png)

* Once logged in, select __Datacenters__ from the menu at the top of the screen. Then select the datacenter for the server.

  ![Quick Access](../../images/dccf/creating-a-server1-html5.png)

* You will then land on a page showing all your VMs. In the left side panel, select __vApps__ below __Compute__.

  ![Select vApp Template](../../images/dccf/creating-a-server2-html5.png)

* Click __NEW__, and select __New vAPP__. A popup window will appear. Enter a name for the new vApp you are creating &mdash; in the context of LPC on VCF, a vApp is simply a container for the objects you create. Once you enter a Name, click __Add Virtual Machine__.

  ![Select Name and Location](../../images/dccf/creating-a-server3-html5.png)

* In the New VM popup window, enter a name for your Virtual Machine &mdash; this is the friendly name that will be displayed inside of LPC on VCF. Enter your __Computer Name__ &mdash; the Computer Name will default to the same as the Name but can be edited as needed. For __Type__ of VM, select New or From Template. If choosing __From Template__, the Compute details can be updated in later steps. Click __OK__.

  ![Select Name and Location](../../images/dccf/creating-a-server4-html5.png)

* On the New vApp window, you can add additional Virtual Machines to your vApp, or you can click __CREATE__.

  ![Configure Networking](../../images/dccf/creating-a-server5-html5.png)

* After clicking __CREATE__ you will be navigated back to the vApps screen. If you would like to update details within your vApp or VM and to add a Network, locate your vApp and click __Details__.

  ![Configure Networking](../../images/dccf/creating-a-server6-html5.png)

* Click the __Networks__ tab to configure a network. Then click __New__.

  ![Configure Networking](../../images/dccf/creating-a-server7-html5.png)

* Select the Network Type. If choosing __OrgVDC Network__ select the network and click __Add__. If choosing __vApp Network__ complete the fields that appear, then click __Add__.

  ![Configure Networking](../../images/dccf/creating-a-server8-html5.png)

* If you would like to update the Compute details on your VM, select the Details link in your VM. You will then be able to edit General fields, Hardware, Guest OS Customization, Guest Properties, Monitoring, and Metadata. Click __Save__ when finished.

  ![Configure Networking](../../images/dccf/creating-a-server9-html5.png)

  ![Configure Networking](../../images/dccf/creating-a-server10-html5.png)

* Navigate back to your vApps page by clicking __vApps__ in the sidebar on the left of the navigation at the top of the screen.

  ![Configure Networking](../../images/dccf/creating-a-server11-html5.png)

* To power on your vApp, click __Actions__, then __Power On__.

  ![Configure Networking](../../images/dccf/creating-a-server12-html5.png)
