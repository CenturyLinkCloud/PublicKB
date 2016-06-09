{{{
  "title": "Managed Pivotal Cloud Foundry - Cluster Bill of Materials",
  "date": "11-16-2015",
  "author": "Bob Jackson & Jared Ruckle",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the reader should know what's included in the Managed PivotalCF cluster that is deployed by CenturyLink Managed Services.

### Cluster Bill of Materials

This table lists what is included in a Managed Pivotal Cloud Foundry cluster.

| Server | CPU Count | RAM | Disk | Purpose |
| --- | --- | --- | --- | --- |
| NATS | 1 | 2 | 20 | Messaging bus for all user applications and internal services
| consul | 1 | 2 | 20 | |
| etcd | 1 | 2 | 20 | Key-value store; source of truth for cluster coordination/state management |
| NFS Server | 1 | 2 | 20 | Blobstore (stores apps in predeployment) |
| Cloud Controller Database | 1 | 2 | 20 | Stores info regarding all apps & services deployed (active or not) |
| UAA Database | 1 | 2 | 20 | User account storage |
| Apps Manager Database | 1 | 2 | 20 | Backend for the Apps Manager UI |
| Cloud Controller | 2 | 4 | 40 | Controls all aspects of deployment to the DEAs; handles Orgs, Spaces, and so on |
| HAProxy | 1 | 2 | 20 | High availability for lab/test environments |
| Router | 1 | 2 | 20 | Routing |
| Health Manager | 1 | 2 | 20 | Monitors all apps and restarts/redeploys as needed |
| Clock Global | 1 | 2 | 20 | NTP manager for the cluster |
| Cloud Controller Worker | 1 | 2 | 20 | Supports the Cloud Controller |
| Collector | 1 | 2 | 20 | Metrics collector for all hosts in the cluster |
| UAA | 1 | 2 | 20 | OAUTH Authentication provider |
| MySQL Proxy | 1 | 2 | 20 | Service broker for MySQL instance(s) |
| MySQL Server | 4 | 8 | 80 | Service node |
| DEA | 8 | 16 | 160 | Workhorse; actual application deployment |
| DEA | 8 | 16 | 160 | Workhorse; actual application deployment |
| Doppler Server | 1 | 2 | 20 | Gathers logs from MetronAgents, forwards to Loggregator Trafficcontroller |
| Loggregator Trafficcontroller | 1 | 2 |  20 | User application log aggregation |
| JMX Provider (Collector) | 2 | 4 | 40 |Provides JMX nozzle for ingestion by Nagios
| OMDistro | 1 | 2 | 17 | Nagios monitoring |
| Ops Manager | 4 | 16 | 50 | Elastic Runtime, Ops Metrics deployment |
| Total | 46 | 100 | 887 |
