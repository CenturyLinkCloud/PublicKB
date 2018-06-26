{{{
  "title": "Connecting to MySQL Relational DB over SSL on AppFogv2",
  "date": "01-25-2016",
  "author": "Lane Maxwell",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service was retired on June 29, 2018. The AppFog Platform-as-a-Service is no longer available, including all source code, env vars, and database information. More information is available [here](../../appfog/appfog-retirement-guide.md).</strong>

### Audience
This article is to support AppFog customers using the ctl_mysql service through the AppFog AddOn Engine. The ctl_mysql service is Centurylink's MySQL-compatible Relational Database Service. For instructions on how to use your cert after purchasing through the Relational DB UI, see our Knowledge Base article titled [Connecting to MySQL Relational DB Over SSL](rdbs-mysql-connecting-over-ssl.md).

### Connecting over SSL-enabled Connection
Provisioning the Relational DB MySQL instance through the AddOn Engine returns a collection of variables as defined below.

```
{
  "config": {
    "password": "mZOyJ5Bf6Pfk6K38",
    "url": "mysql://10.0.0.1:3306",
    "username": "admin",
    "certificate": "-----BEGIN CERTIFICATE----- MIIDgTCCAmmgAwIBAgIJAMubOSUqSIZOMA0GCSqGSIb3DQEBCwUAMFcxGTAXBgNV BAoMEENlbnR1cnlMaW5rREJhYVMxHTAbBgNVBAsMFENlcnRpZmljYXRlQXV0aG9y aXR5MRswGQYDVQQDDBJDZW50dXJ5TGlua0RCYWFTQ0EwHhcNMTUwNjEyMDExMzIx WhcNMjUwNjA5MDExMzIxWjBXMRkwFwYDVQQKDBBDZW50dXJ5TGlua0RCYWFTMR0w GwYDVQQLDBRDZXJ0aWZpY2F0ZUF1dGhvcml0eTEbMBkGA1UEAwwSQ2VudHVyeUxp bmtEQmFhU0NBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzN5bNNjV GLZzq1vpGzgIDBdKzZtl625QSCVXu5vOGKZxsQDdMcflDylOPlOyJmg6t9KEkduQ KJvZhAoR03/ftqsYTNvzsbzyTraZb3fK7NZhbPLml9JLGrCeN0F3XmmYCKy+hoDA IegCOk4QazHu2XvVp/ATFc+w9jzEb6uHRrfvXtBPoGV3Td5tqfLEx+ZC9JAm6Ri3 /eT8D+ys+sKYUyPPqJD12QN/ceWjvBrlCpyca2QoBb7OfZOZR8Q/xhxznYLsqBda 4gWov23bGOVj9vSD/2kr9eSO+Ap739Awlso/hOjB/abDumsW9t1NPYSdscjxTD+t 2EVcdGrvT5CT+QIDAQABo1AwTjAdBgNVHQ4EFgQULNhBKIj12kTdxWrg/hwMbtSk ND4wHwYDVR0jBBgwFoAULNhBKIj12kTdxWrg/hwMbtSkND4wDAYDVR0TBAUwAwEB /zANBgkqhkiG9w0BAQsFAAOCAQEAbuEg3VquJxgg5exRtdgff9tWTozM0OozJc6d oYgV11oH8NtvKLkwbChgGHKL1bXmMxTfW4vUk3FhuiO5S85oi0vvDGPq5gqM6oxr tbhaml7Nd0OoNCvRsGJiINKS3G8JRKmZ3+WA55wQEjZC5KuPlgB5XO418byYYDnc /k08pmEr8ztymAjVvc6rzlK0ZmUJqQnIEk+cDTHNYbALQwJ7+QZMbOGj1v/9w05M xFpTIBmySTP2+leCTP2qnJUiFc9yzfcMPQs6wS1KOOTwWS5LAqEUicZ17hCOMUi+ 1J1oVss1KdfPYfhSmbCbPg1ELwEHvnE7Bo4ildRlPGeSSb+gZw== -----END CERTIFICATE-----"
  },
  "id": "lane"
}
```
1. Begin by creating a file from the contents of the certificate variable.
   Example: dbaas_instance.pem

2. Connect specifying the `--ssl-ca` parameter and pass in the newly created certificate.
   `mysql -h 10.0.0.1 -u admin -p ---ssl-ca=dbaas_instance.pem`

3. Once logged in, validate the SSL connection by using the show command.
   `mysql> show status like 'Ssl_cipher';`

   ```
   +---------------+--------------------+
   | Variable_name | Value              |
   +---------------+--------------------+
   | Ssl_cipher    | DHE-RSA-AES256-SHA |
   +---------------+--------------------+
   1 row in set (0.07 sec)

   mysql>
   ```

4. If you have questions or feedback, please submit them to our team by emailing <a href="mailto:rdbs-help@ctl.io">rdbs-help@ctl.io</a>.
