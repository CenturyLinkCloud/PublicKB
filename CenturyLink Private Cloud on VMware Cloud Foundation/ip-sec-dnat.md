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

1. Login to your CenturyLink Private Cloud on VMware Cloud Foundation environment with an Org Admin Account

  ![Login to CenturyLink Private Cloud on VMware Cloud Foundation](../images/dccf/login-to-dcc-f.png)

2. Once logged in, click __Administration__ at the top.

  ![IPSec VPN](../images/dccf/configuring-sslvpn-plus1.png)

3. Double-click your Org VDC to open.

  ![IPSec VPN](../images/dccf/configuring-sslvpn-plus2.png)

4. In the __org001-vdc__ page, click on the __Edge Gateways__ tab, then right-click your __org001-edge__, then select __Properties...__

  ![IPSec VPN](../images/dccf/edge-gws1.png)

5. Select the Configure IP Settings tab, and take note of the (Public) IP Address for the Edge Gateway.

  ![IPSec VPN](../images/dccf/edge-gws2.png)

6. Right-click your __org001-edge__, then select __Edge Gateway Services...__ A new tab will open.

  ![IPSec VPN](../images/dccf/edge-gws3.png)

7. Select the VPN tab, then __IPSec VPN Sites__, Click __+__ sign to add IPsec VPN Sites (this is a prerequisite to enable IPsec VPN Services).

  ![IPSec VPN](../images/dccf/edge-gws4.png)

8.	Add IPsec VPN:
  a. Enabled: Click slider to enable
  b. Enable perfect forward secrecy (PFS): default
  c. Name: Name your IPSec VPN
  d. Local Id: Your Local Id
  e. Local Endpoint: IP address of Edge Gateway
  f. Local Subnets: Your Local Subnets
  g. Peer Id: Your Peer Id
  h. Peer Endpoint: IP address of Peer
	i. Peer Subnets: Your Peer Subnets
  j. Encryption Algorithm: Must match with peer
  k. Authentication: Must match with peer
  l. Change Shared Key:
  m. Pre-Shared Key: Shared Key
  n. Display Shared Key:
  o. Diffie-Hellman Group: Must match with peer
  p. Extension:

  ![IPSec VPN](../images/dccf/edge-gws5.png)

9.	Click Keep
10.	In the __IPSec VPN Configuration__ page, select the __Activation Status__ tab, and enable __IPsec VPN Service Status__

  ![IPSec VPN](../images/dccf/edge-gws6.png)

11.	Configure the Peer/Remote Site.
