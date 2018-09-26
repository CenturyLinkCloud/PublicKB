{{{
  "title": "Azure to CenturyLink Cloud VPN Guide",
  "date": "01-17-2018",
  "author": "Taufique Noorani",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview
You can connect your Azure VNET to CenturyLink Cloud networks by using a VPN connection. The following steps guide you on how to use the Azure portal to configure Azure VNET.

### Steps
If you would like to use IKEv1, you can follow the guide below to configure site-to-site VPN between Azure and CenturyLink Cloud using self-service.
1.	You can follow Azure VPN documentation to configure VPN on their end.
2.	Once you configure Azure VPN from the documentation stated in step 1, you can follow this guide to setup VPN from CenturyLink side. 

As IKEv2 VPN cannot be configured via Control, it would have to be done as [Service Task](https://www.ctl.io/service-tasks/#vpn-tunnels-deployment). 
1.	You can follow Azure VPN documentation to configure VPN on their end.
2.	We will need the following information to configure VPN tunnel on our end.
    ###### Phase 1
      *	Device Type
      *	VPN Peer IPv4 address
      *	Tunnel Encrypted Subnet
      *	Protocol Mode
      *	Authentication Type
      *	Encryption Algorithm
      *	Hashing Algorithm
      *	Diffie-Helman Group
      *	Lifetime Value
      *	DPD State
      *	NAT-T State
      *	Peer Identity Type
    ###### Phase 2
      *	IPSEC Protocol
      *	Encryption Algorithm
      *	Hashing Algorithm
      *	PFS Enabled/Disabled
      *	PFS Group (if enabled)
      *	Lifetime Value

Send this information with the VPN request to help@ctl.io
