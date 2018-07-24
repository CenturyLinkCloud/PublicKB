{{{

  "title": "Add SRN Peer",

  "date": "12-27-2017",

  "author": "Juan Aristizabal",

  "attachments": [],

  "contentIsHTML": false

}}}



### Article Overview

This article focusses on how to pair two SRNs together to set up Protection Groups.



### Requirements

SRNs should already be registered within the SafeHaven Console.



### Assumptions

SafeHaven Cluster already installed with proper network connectivity between CMS-SRN and SRN-SRN.



### Add SRN Peer

Once all the production and recovery SRN(s) have been registered, then we must establish peering relationships between SRNs (ssh key exchange) in the production and recovery datacenters.



1. Select an SRN in the production Data Center, navigate to the **Peers** tab and click on **Add Peer**.



2. Select the **SRN 2** (peer SRN on Recovery DataCenter) and provide the **Root Password** for both the SRN's. Click **Register**.



**NOTE**: A single production SRN can be paired with multiple recovery SRNs and vice-versa(many-to-many mapping is allowed and not limited to one-to-one mapping).



**NOTE**: Please follow the same procedure for CLC/VMWare/Manual sites as source datacenters. 



### Video Tutorial

<p>

<iframe width="560" height="315" src="https://www.youtube.com/embed/wtTgkhxLNGw" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>

</p>



**Next Step** is to [Add and Claim Storage on Production SRN in CenturyLink Cloud](Add and Claim Storage on Production SRN in CenturyLink Cloud.md)

