{{{
  "title": "Importing Data Into AppFog v2 MySQL",
  "date": "10-21-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

### Importing Data Into CenturyLink MySQL DBaaS
* To learn how to create, bind, and determine connection credentials review our Knowledge Base article on [Using CenturyLink MySQL with AppFog Applications](../AppFog/using-ctl-mysql-with-appfog-apps.md).
* You can access your database from the command line using the credentials provided by the VCAP_SERVICES environment variable. You can also [Connect to MySQL DBaaS over SSL on AppFogv2](../Database/connecting-to-mysql-dbaas-over-ssl-on-appfog.md). The certificate needs to be in proper .pem format:

```
-----BEGIN CERTIFICATE-----
...
<CERTIFICATE>
...
-----END CERTIFICATE-----
```

#### Example VCAP_SERVICES environment variables:
```
$ cf env myapp
...
System-Provided:
{
 "VCAP_SERVICES": {
  "ctl_mysql": [
   {
    "credentials": {
     "certificate": "-----BEGIN CERTIFICATE-----\n{...}\n-----END CERTIFICATE-----",
     "dbname": "default",
     "host": "<HOST_ADDRESS>",
     "password": "<PASSWORD>",
     "port": <PORT_NUMBER>,
     "username": "admin"
    },
    "label": "ctl_mysql",
    "name": "example-db",
    "plan": "small",
    "tags": []
   }
  ],
  ```
  
#### Example Connection:
  
  ```
  mysql -h <HOST_ADDRESS> -u admin -p -P <PORT_NUMBER>
  ```
  * At the prompt enter the password `<PASSWORD>`.
  * To import a MySQL dump file the the default database:
  
  ```
  mysql -h <HOST_ADDRESS> default -u admin -p --ssl-ca=/path/to/file/ca-cert.pem -P <PORT_NUMBER> < /path/to/file/db_dump.sql
  ```
