{{{

  "title": "Add SRN Peer",

  "date": "07-30-2018",

  "author": "Weiran Wang",

  "attachments": [],

  "contentIsHTML": false

}}}



### Article Overview

This article focusses on how to pair two SRNs together to set up Protection Groups.



### Requirements

SRNs should already be registered within the SafeHaven Console.



### Assumptions

SafeHaven Cluster already installed with proper network connectivity between CMS-SRNs and SRN-SRN.



### Add SRN Peer

Once all the production and recovery SRN(s) have been registered, then we must establish peering relationships between SRNs (ssh key exchange) in the production and recovery datacenters.



1. Select an SRN in the production Data Center, navigate to the **Peers** tab and click on **Add Peer**.



2. Select the **SRN 2** (peer SRN on Recovery DataCenter) and provide the **Root Password** for both the SRN's. Click **Register**.



**NOTE**: A single production SRN can be paired with multiple recovery SRNs and vice-versa(many-to-many mapping is allowed and not limited to one-to-one mapping).
