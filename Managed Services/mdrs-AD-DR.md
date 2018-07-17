{{{
  "title": "AD DR Replication FAQ",
  "date": "06-14-2018",
  "author": "Shasha Zhu",
  "attachments": [],
 "contentIsHTML": false
}}}

### Overview
Managed Disaster Recovery Services (MDRS) are ideal for customers who lack Disaster Recovery (DR) expertise or do not have the staff needed to maintain a DR solution. CenturyLink takes over these responsibilities and delivers end-to-end services. Unlike other DRaaS solutions, CenturyLink MDRS carries out regular audits, tests, and at-time-of-disaster (ATOD) failover services to ensure the reliability, accuracy, and efficiency of your DR solution. MDRS services including:

* White-glove on boarding
* 24x7 monitoring and maintenance
* Semi-annual testing
* Quarterly audits
* ATOD failover services
* Runbook automation and maintenance
* Application recovery services

### Why do we provide DR replication for AD within Managed Disaster Recovery Package? 
Majority of the customer’s IT environment has Active Directory servers. MDRS leverages Microsoft native disaster recovery replication to protect AD servers and uses SafeHaven technology to protect other business-critical servers. Customer benefits from the cohesive and thorough protection. 

MDRS provides unified and consistent DR services for both AD servers and other business-critical servers in terms of audit, test and at-time-of-disaster events. MDRS takes the DR burden off customer’s shoulder and allow customer to focus on the business-core applications. 

### What is DR replication for AD?
DR replication for AD leverages Microsoft Active Directory Replication technology to replicate the primary AD servers into the recovery site. MDRS monitors the replication process and provide audit and maintenance services. MDRS also provides test and at-time-of-disaster services for AD servers. Please refer to the following table for DR replication for AD service scope. 

Responsible - People who are expected to actively participate in the activity and contribute to the best of their abilities 
Accountable - Person who is ultimately responsible for the results 
Consulted -	 People who either have a particular expertise they can contribute to specific decisions (i.e., their advice will be sought) or who must be consulted for some other reason before a final decision is made 
Informed - 	People who are affected by the activity/decision and therefore need to be kept informed, but do not participate in the effort

| Activities | Tasks                                                   							|Operations | DR Manager | Customer |
|---------|---------|---------|---------|--------|
| Installation | Create and distribute the active directory inventory list | I 				| R 					| I 					|
|					|Customer grant CTL operations full access to the domain | I | I | R |
|					| Create secondary AD servers on the recovery site and add them to the existing domain, ensure full and continuous AD database replication| R | I | I |
|					|Set up monitoring on the secondary Ad server to monitor the replication status and AD status| R | I | I |
| Maintenance | Monitoring of AD servers and replication health. Maintain AD server replication health between sites| R | I | I |
|Audit			|Collect the changes made on primary AD servers including OS update, AD application changes and deliver the changes to CTL operations team | I | R | I |
|					| Reflect the changes on secondary AD servers|		R| I	| I	|
| Test			| Validate and test AD replication prior to network connectivity isolation  1) Validate successful site to site replication 2) Create test object on AD server in primary site, validate successful replication on AD server in secondary/DR site | R | I | I |
|					| Verify connectivity and AD domain resolution of Safehaven servers in all sites | R | C | I |
|					| Validate and remediate any AD domain issues during network isolation/test failover, assist with domain related troubleshooting as failover servers brought online | R | C | I |
|					| Move/sieze AD FSMO roles to secondary/DR site, only if deemed necessary for successful failover operations| R | C | I |
|					| POST TEST - Move/sieze AD FSMO roles to primary site, only if moved during test step 4 | R | C | I |
|					| Validate and test successful AD Replication after test completed and network connectivity is restored 	1) Validate successful site to site replication 2) Create test object on AD server in primary site, validate successful replication on AD server in secondary/DR site | R | I | I |
| ATOD service | Assess state of AD site replication and connectivity 1) 	Full connectivity outage between AD servers/sites 2) Restore of primary site possible? ETA until restore of primary 3) Make note of replication state and last good replication between primary/secondary sites | R | C | I |
|				| Move/seize AD FSMO roles to secondary/DR site 1) Required if primary site is hard down with no ETA for restore, and/or application servers in secondary site require roles resident for successful operations 2) Optional if primary site restore expected within 24 hours, and/or application servers in secondary site DO NOT require roles resident for successful operations | R | C | I |
|				| Verify connectivity and AD domain resolution of Safehaven servers in secondary/DR site | C | R | I |
| 				| Validate and remediate any AD domain issues, assist with domain related troubleshooting as failover servers brought online| R | C | I |
|				| Validate successful monitoring of AD domain and server health for secondary/DR site | R | I | I |


 
### How is DR Replication for AD services different from Managed AD services?

Managed AD focuses on the primary Active Directory application services and ensure the application is running properly. MDRS DR Replication for AD servers focuses on replication, test and recovery of the AD services after a disaster. DR Replication for AD is an add-on service of MDRS and cannot be purchased separately. 