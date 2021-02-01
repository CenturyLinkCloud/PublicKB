{{{
"title": "Lumen Network Storage Glossary of Terms",
"date": "12-02-2020",
"author": "Dave Schwent",
"keywords": ["cns", "lns", "glossary", "network", "portal", "storage"],
"attachments": [],
"contentIsHTML": false
}}}

**Access Protocol:** The access method used to establish a connection between an operating system and a Storage Volume and falls into categories of block, file and object protocols. Lumen Network Storage access protocols include NFS v3 and CIFS for File access and iSCSI for Block access. Object access is via an industry-standard S3-compatible API.

**LNS Node:** A Virtual Storage Machine (VSM) providing access to purchased storage volumes via iSCSI, CIFS or NFS for a desired location.

**IOP:** Input/Output operation. Within Lumen Network Storage, IOPs are used to meter consumption of performance units measured from the software-defined storage controller. Does not include endpoint (server) effective IOPs.

**Portal:** Within Lumen Network Storage, the portal is associated with the Lumen Network Storage Service.

**Replication:** Lumen Network Storage provides asynchronous replication of data between Storage Nodes as configured on a volume basis.

**Snapshot:** A local, point-in-time copy of a Storage Volume that resides on the same Storage Node as the parent Storage Volume.

**Storage Node:** A Storage Node is a software-defined storage array co-located with the workloads that are consuming the Service. Each Storage Node is dedicated to a single customer.

**Service Pod:** A Service Pod is the hardware and software upon which the Service is delivered, including physical servers, storage and network devices and associated software. Service Pods are installed in all Service locations except third party cloud providers, where only software is installed on the provider’s underlying infrastructure. Hardware may be owned by Lumen, an affiliate or its vendors.

**Storage Volume:** A Storage Volume refers to the logical container that holds data being stored. Storage Volumes provide multi-protocol access to servers.
