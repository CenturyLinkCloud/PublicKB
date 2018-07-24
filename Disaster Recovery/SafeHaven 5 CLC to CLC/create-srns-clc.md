{{{
  "title": "Create SRNs in CenturyLink Cloud",
  "date": "12-27-2017",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to deploy a SafeHaven Replication Node(SRN) in CenturyLink Cloud.
SRN resides in both production and DR datacenters and work in pairs. A single SafeHaven Cluster can have upto 64 SRN's registered. This article explains how to deploy SRN in CenturyLink Cloud Production Datacenter.

### Requirements
1. Login access to the CenturyLink Cloud Portal at https://control.ctl.io.
2. Internet access on the Production and Recovery SRN in CenturyLink Cloud once it is deployed.

### Assumptions
This article assumes that the user has login access to the CenturyLink Cloud Portal.

### Create SRN in CenturyLink Cloud
1. Login to the **CenturyLink Control Portal** with your credentials.

2. Select the appropriate **DataCenter** and the appropriate **Server Group** to deploy the SRN. Click on **Create Server** from the drop-down menu.

3. Under the **Create Server** section, select the **Standard** server type. Select **Ubuntu 16 | 64 bit** as the **Operating System** type. Provide a **Name** and **Description** for the SRN. Provide a **root password** and confirm it.

4. Configure the SRN with **2 vCPU** and **4GB of memory**(bare minimum requirements).

5. Under the **Network** section, select a **network** (VLAN) that will have connectivity to the peer SRN, CMS and the appropriate recovery / production servers(depending on the environemnt) and enter the appropriate **Primary and Secondary DNS**. Click on **Create Server**. Wait for the server to get deployed.

You have now completed the deployment of SRN in CenturyLink Cloud.

### Video Tutorial
<p>
<iframe width="560" height="315" src="https://www.youtube.com/embed/GN8EhOBatIE" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
</p>

**Next Step** is to [Create CMS in AWS](Create CMS in AWS.md)
