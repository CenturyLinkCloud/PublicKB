{{{
  "title": "Example Migration Walkthrough",
  "date": "11-10-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in the CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once applications and services are deleted it is **permanent**. We will not be able to provide a backup.

### Overview
In this article we will walk through an example migration from AppFog v1 to AppFog v2. The example is based on the following factors:

1. Utilization of the "Teams" feature on AppFog v1
2. A PHP 5.3 applicaiton named **example-app**, with a memory reservation of 128M
3. A PHP 5.6 application named **test-app**, with a memory reservation of 256M
4. A MySQL service named **example-db**
5. A single Add-On: IronMQ
6. Two custom domains in use
7. An SSL endpoint for application **example-app**
8. Deploying in the AppFog v2 US West region


### Establish AppFog v2 Account

First we need to create an account on the CenturyLink platform, submit the discount form, and install the `cf` CLI tool. The Knowledge Base articles on these subjects can be found in the [AppFog Section](../AppFog/)

1. Create an account at: https://www.ctl.io by selecting "Free Trial" from the upper corner
2. Once an account is created, complete the [Discount Request Form](https://www.ctl.io/appfog/v1-discount-request/). This will discount AppFog v2 for one year for AppFog v1 users.
3. Follow this article to [Enable AppFog](../AppFog/getting-started-with-appfog.md).
4. [Install the Cloud Foundry](../AppFog/login-using-cf-cli.md) `cf` tool.

### Manage AppFog Membership

AppFog v2 has a variety of options to manage and create spaces, invite users, and enable user permissions. This replaces the "Teams" feature on AppFog v1.

1. To add "team" members, first [Create a User](../Accounts & Users/creating-users.md) from the Control Portal.
2. Next follow the steps in our [Manage AppFog Membership](../AppFog/manage-appfog-membership.md) article to select the regions, spaces, and permissions for users. Keep in mind, users must have the Space Developer role enabled to deploy and manage applications and service instances in a space.
3. Once you login via the command line you will be prompted to select a space. The defaults are Dev, Prod, and QA.

### Migrate an Application

Now the account is established on AppFog v2 and the CLI tool is installed. Next we'll migrate the applications. More information can be found in our [Migrating an Application](how-to-migrate-an-application.md) and [Migrating a PHP Application](migrating-php-to-afv2.md) articles. The application will be pushed to the current space logged into. Use `cf push` whether it is the initial push or an update, there is no equivalent to AppFog v1's `af update` command.

1. PHP 5.3 and 5.4 are deprecated and no longer [officially supported](http://php.net/eol.php). We recommend updating applications to at least PHP 5.5. If updating is not possible at this time we have provided a custom buildpack to support PHP 5.3 and 5.4.
2. Download a copy of the application from AppFog v1 using `af pull <appname>`.
3. Modify your applications to replace any AppFog v1 URLs in the application's code. For instance, replace calls to `example-app.aws.af.cm` with a new application URL of `example-app.uswest.appfog.ctl.io`.
4. Modify how the VCAP_SERVICES environment variable is called. The fields are slightly different on AppFog v2. On AppFog v1 the database and host fields were "name" and "hostname". They are defined as "dbname" and "host" on AppFog v2, respectively. Follow these links for examples of the VCAP_SERVICES environment variable for [AppFog v1](mysql.md) and [AppFog v2](importing-data-to-afv2-mysql.md). Here is an example using the VCAP_SERVICES variable with PHP:

 ```
$services = json_decode($_ENV['VCAP_SERVICES'], true);
$service = $services['ctl_mysql'][0];
define('DB_NAME', $service['credentials']['dbname']);
define('DB_USER', $service['credentials']['username']);
define('DB_PASSWORD', $service['credentials']['password']);
define('DB_HOST', $service['credentials']['host'] . ':' . $service['credentials']['port']);
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '')
 ```
5. AppFog v1 had several PHP extensions and modules enabled by default. AppFog v2 allow users to specify necessary extensions and modules. The following steps outline the process:
 * Create a new `.bp-config` directory in your application's root directory.
 * Within the new `.bp-config` directory add a filed named `options.json`.
 * Enable extensions by adding the PHP_EXTENSIONS or PHP_MODULES setting in the `options.json` file. The following example enables several PHP extensions that were available on AppFog v1:
 ```
{
"PHP_EXTENSIONS": ["pdo", "pdo_mysql", "mysqli", "mysql", "mbstring", "mcrypt", "gd", "zip", "curl", "openssl", "sockets", "pdo_pgsql", "pdo_sqlite", "pgsql", "mongo"]
}
 ```
6. Users were able to modify some php.ini settings on AppFog v1 within their .htaccess file. On AppFog v2 users will need to create a `user.ini` file in their root directory and include their settings. The following are examples of settings which may be modified:

 ```
memory_limit = 256M
upload_max_filesize = 4M
max_input_time = 90
  ```
7. The default application memory reservation is 1GB and the default buildpack will support PHP 5.5 and 5.6. Specify the PHP custom buildpack when deploying PHP 5.3 and 5.4 applications, if necessary also specify the memory allocation:
 
 ```
cf push <appname> -m <memory> -b https://github.com/CenturyLinkCloud/php-buildpack.git#af_custom_php
 ```
 
8. For this example we would use the following commands to push the example-app and test-app applications to AppFog v2:
```
cf push example-app -m -128M -b https://github.com/CenturyLinkCloud/php-buildpack.git#af_custom_php
cf push test-app -m 256M
```

### Migrate Services

More information can be found in our [Migrating a Service](export-services-and-third-party-alternatives.md) and [Importing Data Into AppFog v2 MySQL](importing-data-to-afv2-mysql.md) articles. Our MySQL DBaaS is currently in Beta. It is due to release from Beta in December.

1. First we need to export the data from AppFog v1. There are several options available. In this example we'll use the `af export-service <service_name>` command. The [Migrating a Service](export-services-and-third-party-alternatives.md) article provides information on other options.
 * From the CLI on AppFog v1:
 ```
af export-service example-db
 ```
 * This proivdes a URL to download your database. Use the wget command to download the database:
 ```
wget -c -O <example-db>.zip <URL_provided_by_export-service_command>
 ```
 * Decompress the downloaded file:
 ```
 unzip <example-db>.zip
 ```
 * Naviagte to the "content" directory. Then decompress the SQL file and rename it to your service name:
 ```
gunzip <example-db>.sql <file_name>.gz
 ```
 
2. Next, create a service on AppFog v2. You can view the available first-party service options using `cf marketplace`:

 ```
service       plans                         description   
ctl_mysql     micro, small, medium, large   CenturyLink's BETA MySQL DBaaS.  For development use only; not subject to SLAs.   
orchestrate   free                          Orchestrate DBaaS
 ```

3. The syntax to create a service is `cf create-service <service-type> <plan> <service-name>`. For this example, `cf create-service ctl_mysql micro example-db`.
4. Next bind the service to the application: `cf bind-service example-app example-db`.
5. You can then view the VCAP_SERVICES environment variable using `cf env example-app`:

 ```
$ cf env example-app
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

6. Use the VCAP_SERVICES credentials to connect to the database and import the `example-db.sql` file:

```
mysql -h <HOST_ADDRESS> default -u admin -p -P <PORT_NUMBER> < /path/to/file/example-db.sql
```
You will be prompted for the password. You can also use SSL when connecting to the database. To do so copy the ca.cert to a file and specify the location as described in the [Importing Data Into AppFog v2 MySQL](importing-data-to-afv2-mysql.md) article.

### Set up Custom Domains

Here is our Knowledge Base article on AppFog v2 [Custom Domains](../AppFog/setup-custom-domain-for-appfog-app.md). Additional information can be found in the Cloud Foundry Docs at: https://docs.cloudfoundry.org/devguide/deploy-apps/domains-routes.html

1. Create the domain on AppFog v2 using `cf create-domain <organization> <domain>`:

 ```
cf create-domain <organization> example-app.com
cf create-domain <organization> www.example-app.com
cf create-domain <organization> test-app.com
 ```

2. Next create a custom route and map it to your application using `cf map-route <appname> <domain>`:

 ```
cf map-route example-app example-app.com
cf map-route example-app www.example-app.com
cf map-route test-app    test-app.com
 ```

3. At your DNS provider create a CNAME record routing traffic to AppFog with a CNAME record pointing to `hello-node.uswest.appfog.ctl.io` or `hello-node.useast.appfog.ctl.io`, depending on the region. If the DNS service provider does not offer the option of a CNAME for the root domain, we recommend creating a 302 redirect from your root domain pointing to `www.<yourdomain>.com`. For example, the domain example-app.com would have a 302 redirect pointing to www.example-app.com. Then create a CNAME record such as:
```
CNAME www 1 min hello-node.uswest.appfog.ctl.io
```
More detail is described in the next section if using CloudFlare for SSL support.

### SSL Support on AppFog v2

AppFog v2 does not currently support SSL endpoints for a custom domain. We recommend using a service such as CloudFlare to enable SSL support. You can read our Knowledge Base artilce [Migrating SSL Support to AppFog v2](how-to-migrate-ssl-certs.md).

1. Visit [CloudFlare](https://www.cloudflare.com/) and create an account. Note, when you set up SSL for a domain the name servers are transferred from your current provider to CloudFlare.
2. Enable SSL support from the "Crypto" tab at the top of the page. Select the "Full SSL" option. "Flexible" will only provide SSL support from the user to the CloudFlare server, not from CloudFlare to AppFog. The "Full Strict" option is not supported by AppFog.
3. If you would like to use your own SSL certificate you will need to upgrade from the free plan.
4. One of the benefits of CloudFlare is they support [CNAME Flattening](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/). This means you can create a CNAME record for your root domain and do not have to use an A record. For example, the DNS settings for **example-app** would be:

```
CNAME example-app.com  is an alias of example-app.uswest.appfog.ctl.io
CNAME www is an alias of example-app.uswest.appfog.ctl.io
```

### Migrate an Add-On

For more information visit our [Add-On Migration](migrating-environment-variables.md) article.

1. Obtain the IronMQ credentials on AppFog v1 by using `af env example-app`, or view the variables from the application's Mission Control page of the web console.
2. Set the variable on AppFog v2 using `cf set-env <appname> <variable> <value>`
3. Here are the commands to migrate the IronMQ configs to AppFog v2:

```
cf set-env example-app IRON_MQ_TOKEN <YOUR_IRON_MQ_TOKEN>
cf set-env example-app IRON_MQ_PROJECT_ID <YOUR_IRON_MQ_PROJECT_ID>
```
