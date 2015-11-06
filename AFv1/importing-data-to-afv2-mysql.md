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
MIIDgTCCAmmgAwIBAgIJAMubOSUqSIZOMA0GCSqGSIb3DQEBCwUAMFcxGTAXBgNV
BAoMEENlbnR1cnlMaW5rREJhYVMxHTAbBgNVBAsMFENlcnRpZmljYXRlQXV0aG9y
aXR5MRswGQYDVQQDDBJDZW50dXJ5TGlua0RCYWFTQ0EwHhcNMTUwNjEyMDExMzIx
WhcNMjUwNjA5MDExMzIxWjBXMRkwFwYDVQQKDBBDZW50dXJ5TGlua0RCYWFTMR0w
GwYDVQQLDBRDZXJ0aWZpY2F0ZUF1dGhvcml0eTEbMBkGA1UEAwwSQ2VudHVyeUxp
bmtEQmFhU0NBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzN5bNNjV
GLZzq1vpGzgIDBdKzZtl625QSCVXu5vOGKZxsQDdMcflDylOPlOyJmg6t9KEkduQ
KJvZhAoR03/ftqsYTNvzsbzyTraZb3fK7NZhbPLml9JLGrCeN0F3XmmYCKy+hoDA
IegCOk4QazHu2XvVp/ATFc+w9jzEb6uHRrfvXtBPoGV3Td5tqfLEx+ZC9JAm6Ri3
/eT8D+ys+sKYUyPPqJD12QN/ceWjvBrlCpyca2QoBb7OfZOZR8Q/xhxznYLsqBda
4gWov23bGOVj9vSD/2kr9eSO+Ap739Awlso/hOjB/abDumsW9t1NPYSdscjxTD+t
2EVcdGrvT5CT+QIDAQABo1AwTjAdBgNVHQ4EFgQULNhBKIj12kTdxWrg/hwMbtSk
ND4wHwYDVR0jBBgwFoAULNhBKIj12kTdxWrg/hwMbtSkND4wDAYDVR0TBAUwAwEB
/zANBgkqhkiG9w0BAQsFAAOCAQEAbuEg3VquJxgg5exRtdgff9tWTozM0OozJc6d
oYgV11oH8NtvKLkwbChgGHKL1bXmMxTfW4vUk3FhuiO5S85oi0vvDGPq5gqM6oxr
tbhaml7Nd0OoNCvRsGJiINKS3G8JRKmZ3+WA55wQEjZC5KuPlgB5XO418byYYDnc
/k08pmEr8ztymAjVvc6rzlK0ZmUJqQnIEk+cDTHNYbALQwJ7+QZMbOGj1v/9w05M
xFpTIBmySTP2+leCTP2qnJUiFc9yzfcMPQs6wS1KOOTwWS5LAqEUicZ17hCOMUi+
1J1oVss1KdfPYfhSmbCbPg1ELwEHvnE7Bo4ildRlPGeSSb+gZw==
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
     "host": "25dd22ae-0065-454b-8uw3-14c09814cec2.il1.dbaas.ctl.io",
     "password": "GKQY0qbxn7i24Ftt",
     "port": 49340,
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
  mysql -h 25dd22ae-0065-454b-8uw3-14c09814cec2.il1.dbaas.ctl.io -u admin -p -P 49340
  ```
  * At the prompt enter the password `GKQY0qbxn7i24Ftt`.
  * To import a MySQL dump file the the default database:
  
  ```
  mysql -h 25dd22ae-0065-454b-8uw3-14c09814cec2.il1.dbaas.ctl.io default -u admin -p --ssl-ca=/path/to/file/ca-cert.pem -P 49340 < /path/to/file/db_dump.sql
  ```
