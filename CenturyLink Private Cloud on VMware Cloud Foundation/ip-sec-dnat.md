{{{
  "title": "Enable IPSec VPN on Edge Gateway Services",
  "date": "9-11-2018",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we walk through how to enable an IPSec VPN on Edge Gateway Services within the vCloud Director (vCD) Web Console environment for CenturyLink Private Cloud on VMware Cloud Foundation™.

### Prerequisites
You must configure at least one IPSec VPN site on the NSX Edge before enabling the IPSec VPN service.

* Login to your CenturyLink Private Cloud on VMware Cloud Foundation environment with an Org Admin Account

  ![Login to CenturyLink Private Cloud on VMware Cloud Foundation](../images/dccf/login-to-dcc-f.png)

* Once logged in, click __Administration__ at the top.

  ![IPSec VPN](../images/dccf/configuring-sslvpn-plus1.png)

* Double-click your Org VDC to open.

  ![IPSec VPN](../images/dccf/configuring-sslvpn-plus2.png)

* In the __org001-vdc__ page, click on the __Edge Gateways__ tab, then right-click your __org001-edge__, then select __Properties...__

  ![IPSec VPN](../images/dccf/edge-gws1.png)

* Select the Configure IP Settings tab, and take note of the (Public) IP Address for the Edge Gateway.

  ![IPSec VPN](../images/dccf/edge-gws2.png)

* Right-click your __org001-edge__, then select __Edge Gateway Services...__ A new tab will open.

  ![IPSec VPN](../images/dccf/edge-gws3.png)

* Select the VPN tab, then __IPSec VPN Sites__, Click __+__ sign to add IPsec VPN Sites (this is a prerequisite to enable IPsec VPN Services).

  ![IPSec VPN](../images/dccf/edge-gws4.png)

*	Add IPsec VPN:
  * Enabled: Click slider to enable
  * Enable perfect forward secrecy (PFS): default
  * Name: Name your IPSec VPN
  * Local Id: Your Local Id
  * Local Endpoint: IP address of Edge Gateway
  * Local Subnets: Your Local Subnets
  * Peer Id: Your Peer Id
  * Peer Endpoint: IP address of Peer
	* Peer Subnets: Your Peer Subnets
  * Encryption Algorithm: Must match with peer
  * Authentication: Must match with peer
  * Change Shared Key:
  * Pre-Shared Key: Shared Key
  * Display Shared Key:
  * Diffie-Hellman Group: Must match with peer
  * Extension:

  ![IPSec VPN](../images/dccf/edge-gws5.png)

*	Click Keep
*	In the __IPSec VPN Configuration__ page, select the __Activation Status__ tab, and enable __IPsec VPN Service Status__

  ![IPSec VPN](../images/dccf/edge-gws6.png)

*	Configure the Peer/Remote Site.
