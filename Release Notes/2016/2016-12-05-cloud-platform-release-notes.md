{{{
"title": "Cloud Platform - Release Notes: December 5, 2016",
"date": "12-05-2016",
"author": "Anthony Vetter",
"attachments": [],
"contentIsHTML": false
}}}


### New Features (1)

* __NetX Multi-Endpoint__

Instances of Network Exchange were previously referred to as "Virtual Circuits" consisting of two endpoints. In this release, "Exchanges" replace "Virtual Circuits" as the instances of Network Exchange. Each instance must contain two endpoints, but may contain more. Only one HAN-connected endpoint may be included in an Exchange.


### Enhancements (1)

* __NetX Any to any connectivity__

Network Exchange previously assumed Lumen Cloud to be a default endpoint of a Virtual Circuit. In this release, there is no assumption CLC is an endpoint.


### Announcements (2)

* __MSSQL Relational DB Beta Program__

We are still accepting beta customer requests for our MSSQL Relational DB Beta. The beta service is currently limited to IL1 and includes a single instance of MSSQL with private routing, daily backups held for 7 days and configurable backup time. Keep watching release notes for announcements on when new beta features and locations are added. If you are interested in joining the beta program, please visit https://www.ctl.io/relational-database/#MSSQLbeta.

* __SMTP Relay - EOL Update__

Previously, Lumen announced that we will be deactivating the SMTP Relay Service on December 1st, 2016. To give some customers more time to migrate off of the service we are going to push back the deactivation of the SMTP Relay Service to January 15th, 2017.


### Bug Fixes (1)

* __NetX Santa Clara datacenter options__

Selecting HAN as an endpoint for the UC1 CLC datacenter incorrectly offered Lumen SC4 & Lumen SC5 as datacenter options. This has been corrected to reflect the two valid options of SC8 and SC9.
