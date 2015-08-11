{{{
  "title": "Connecting to MySQL DBaaS over SSL-enabled Connection",
  "date": "08-14-2015",
  "author": "Lane Maxwell",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}


#### IMPORTANT NOTE

CenturyLink Cloud’s MySQL-compatible Database-as-a-Service product is currently in a Limited Beta with specific customers by invitation only and is not intended for production usage.
During the Limited Beta there is no production Service Level Agreement.

#### Audience

Currently, this article is to support customers in the Limited Beta program.  Additionally, the steps below are for customers using the DBaaS service through our Beta UI.  For instructions on how to use your cert in AppFog, please see "Connecting to MySQL DBaaS over SSL-enabled Connection - AppFog"

## Connecting over SSL-enabled Connection

1.  Navigate to the "Database Instances" screen.  For provisioned instances of MySQL, you will see a "Download Certificate" button.  When you click this button, you will download a file called ca-cert.pem. This is the certificate that will enable the SSL connection.  ![DownloadCert](../images/dbaas-cert-beta.png)

2.  Once the certificate is downloaded, you can connect specifying the ![ssl-ca](../images/dbaas--ssl-ca-beta.png) parameter and pass in the certificate.
![SSL Command](../images/dbaas-sslcommand-beta.png)

3.  Once logged in, validate the SSL connection by using the show command. ![Validate SSL](../images/dbaas-validatessl-beta.png)
