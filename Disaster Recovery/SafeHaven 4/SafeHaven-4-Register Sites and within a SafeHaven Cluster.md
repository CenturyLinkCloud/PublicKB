{{{
  "title": "SafeHaven-4-Register Sites and SRN within a SafeHaven Cluster",
  "date": "05-03-2016",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false
}}}

## Article Overview

### Requirements


### Register the production and recovery data centers

Within the SafeHaven Console, right-click on the CMS in the Navigation Tree and select Register Data Center from the drop-down menu. First, we will register the recovery data center.

![Upgrade](../../images/SH4.0/Cluster/07.png)

Enter a name for the data center and the data center type. In this case, we assume you will recover in the CenturyLink Cloud so the data center type is CenturyLink Cloud. Select Register.

![Upgrade](../../images/SH4.0/Cluster/08.png)

Next register the production data center by following a similar procedure. If your production data center is at your premises or at co-location facility and managed directly through VMware vCenter Server, select VMware vSphere as the data center type. If your private data center does not have access to VMware vCenter Server, select Manual as the data center type.

Now select the recovery data center in the Navigation Tree and select Change Credentials in the main data panel.

![Upgrade](../../images/SH4.0/Cluster/09.png)

A pop-up panel appears. Enter your user name and password for CenturyLink Cloud administration.

![Upgrade](../../images/SH4.0/Cluster/10.png)

Enter your account alias, identify the data center with one of the CenturyLink data centers and select Finish.

![Upgrade](../../images/SH4.0/Cluster/11.png)

Now perform the same tasks for the production data center. You have now registered the production and recovery data center with the SafeHaven Cluster.

### Register the SRNs

Right-click on the recovery data center within the Navigation Tree and select Register SRN from the drop-down menu.

![Upgrade](../../images/SH4.0/Cluster/12.png)

A pop-up panel appears. Provide a name for the SRN. You may want to match the name already provided for the SRN by the CenturyLink Cloud. Next provide the root password, the Service IP, WAN Replication IP, and local iSCSI IP along with the service ports for TCP and UDP (both have default values of 20082). Select Register.

![Upgrade](../../images/SH4.0/Cluster/13.png)

If you need additional SRNs in the recovery data center, use a similar procedure to register them as well.

Using a similar procedure, register the SRNs in the production data center.

### Establish peering between SRNs and claim storage

Next we must establish peering relationships between SRNs in the production and recovery data centers. Select an SRN in the recovery data center. Select the Peers tab in the main data panel, then select Add peer.

![Upgrade](../../images/SH4.0/Cluster/14.png)

A pop-up panel appears. Provide the root password for the recovery SRN. Next, identify the SRN in the production data center which needs to act as a peer. Provide its root password as well. Select Register.

![Upgrade](../../images/SH4.0/Cluster/15.png)

Finally, you need to claim storage pools for each SRN. In the Navigation Tree, select an SRN in the recovery data center. In the main data panel under the Properties tab, select Claim Storage Pool.

![Upgrade](../../images/SH4.0/Cluster/16.png)

A pop-up panel appears. Select the radio button to Claim a New Storage Pool. Provide the new pool a name. Select Claim.

![Upgrade](../../images/SH4.0/Cluster/17.png)

Perform a similar task for all other SRNs in the recovery data center and also for the SRNs in the production data center. 
