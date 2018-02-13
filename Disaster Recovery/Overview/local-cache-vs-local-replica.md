{{{
  "title": "Local Cache V/S Local Replica",
  "date": "01-09-2018",
  "author": "Anshul Arora",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
Local Cache and Local Replica are two types of protection groups supported in CLC/VMware to CLC deployments. This article explains the key differences between the two approaches.

### Assumptions
This article assumes that the user has basic understanding of working of SafeHaven.

### Difference between Local Cache and Local Replica
Local Replica maintains a full copy of the Production VMs disk on both the production and the DR SRN. On the other hand, Local Cache stores the full copy on the DR SRN, and keeps a cache or buffer on the Production SRN.

### Storage Requirements
#### Local Cache Protection type
* 10% of provisioned production storage on the Production SRN.
* 125% of the provisioned storage on the DR SRN.
* About 6GB on the DR SRN for Test Failover.
* For example, a 100GB Virtual Machine requires a storage of 10GB on Production SRN and 131GB (125GB + 6GB) on the DR SRN

#### Local Replica Protection type
* 125% of provisioned production storage on the Production SRN.
* 125% of the provisioned storage on the DR SRN.
* About 6GB on both Production and DR SRNs for Test Failover.
* For example, a 100GB Virtual Machine requires a storage of 131GB on Production SRN and 131GB on the DR SRN

### Cost
Local Replica is more expensive of the two solutions, since it maintains a full copy of the provisioned storage on the production SRN in comparison to Local Cache, which requires just 10% of the provisioned storage.

### Failover and Failback
Failover time is same for both approaches.   
Failback resync time is reduced significantly in Local Replica because there is already a local copy present on the production SRN and only the changes are synced from the DR side. Local Cache, on the other hand, does not have a local copy at the production SRN, therefore full disk from the DR side needs to be synced back to the Production side. 

### Performance
Local Cache provides better performance in comparison to Local Replica.
