{{{
  "title": "Importing Data Into AppFog v2 MySQL",
  "date": "02-08-2016",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

When migration is complete your billing subscription can be canceled from the [Account](https://console.appfog.com/#account) page of the web console. Please be sure to cancel your subscription as we are not aware when individual user migration is complete. The billing system will not automatically prorate the subscription and issue a refund. If applicable, please open a [Support Ticket](https://support.appfog.com/tickets/new) or email support@appfog.com to receive a prorated refund of your subscription.


### Importing Data Into CenturyLink MySQL Relational DB Service
* To learn how to create, bind, and determine connection credentials review our Knowledge Base article on [Using CenturyLink MySQL with AppFog Applications](../AppFog/using-ctl-mysql-with-appfog-apps.md).
* You can access your database from the command line or a third-party tool using the credentials provided by the VCAP_SERVICES environment variable. The VCAP_SERVICES variable can be viewed using `cf env <APP_NAME>` from the CLI, or by navigating to your application in the web control portal by selecting the AppFog icon, choosing the application, then selecting Environment. You can also [Connect to MySQL Relational DB over SSL on AppFogv2](../Database/connecting-to-mysql-rdbs-over-ssl-on-appfog.md). The certificate needs to be in proper .pem format:

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
