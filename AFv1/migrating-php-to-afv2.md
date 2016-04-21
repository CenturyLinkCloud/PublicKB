{{{
  "title": "Migrating a PHP Application to AppFog v2",
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


### PHP Migration
The AppFog v2 PHP buildpack default differs from AppFog v1 configuration. This article provides some options for customizing the configuration.  More documentaion on modifying the PHP buildpack can be found at https://github.com/cloudfoundry/php-buildpack/blob/master/docs/config.md.

### PHP Version
The PHP buildpack defaults to version 5.5. To use a different version create a `.bp-config/options.json` file in the application's root directory and use the following variable: 
```
{
"PHP_VERSION" : "{PHP_56_LATEST}"
}
```
The default PHP buildpack does not support PHP 5.3, and soon will not support PHP 5.4. This is because both PHP versions are no longer supported. AppFog developers have created a custom buildpack to support PHP 5.3 and 5.4 on AppFog v2. To use PHP 5.3 or 5.4 specify the version as described above and include the custom buildpack when pushing your app:
`cf push <appname> -b https://github.com/CenturyLinkCloud/php-buildpack#af_custom_php`. When using the PHP custom buildpack only predefined environment variables can be utilized. This means user set environment variables will not be available to the deployed PHP application. The VCAP_SERVICES environment variable is available for use connecting to an AppFog marketplace service offering. This buildpack commit lists the [available environment variables](https://github.com/CenturyLinkCloud/php-buildpack/commit/6bd12f73bc68950856e67cae9a08c4d89c2dfefc) defined in the custom buildpack.

### .htaccess
* AppFog v2 allows for the use of an `.htaccess` file in the root of your application for URL rewriting: http://docs.cloudfoundry.org/buildpacks/php/gsg-php-usage.html.

### .user.ini
* Users can modify the default settings by adding a `.user.ini` file to their applicaiton root directory.
* The AppFog v2 PHP buildpack default is short_open_tag = Off. AppFog v1 set this value as "On". With the short_open_tag set to "Off" users will receive a 500 error and AppFog will read the code as plain text if their file reads as
```
<?
echo "Hello World";
?>
```
instead of
```
<?php
echo "Hello World";
?>
```
### PHP Extensions
* AppFog v1 made several PHP extensions available that are not enabled by default with the AppFog v2 PHP buildpack. To enable PHP extensions with the buildpack, create a `.bp-config/options.json` file in the application's root directory and include extensions to enable. This is not a complete list, but these are some common extensions enabled on AppFog v1 that you may want to enable on AppFog v2:
```
{
"PHP_EXTENSIONS": ["pdo", "pdo_mysql", "mysqli", "mysql", "mbstring", "mcrypt", "gd", "zip", "curl", "openssl", "sockets", "pdo_pgsql", "pdo_sqlite", "pgsql", "mongo"]
}
```
* The PHP extensions enabled by default on AppFog v1 can be found here: [PHP 5.3](http://php_info.aws.af.cm/), [PHP 5.4](http://php_info54.aws.af.cm/), [PHP 5.5](http://php_info55.aws.af.cm/), [PHP 5.6](http://php_info56.aws.af.cm/).

### VCAP_SERVICES
The VCAP_SERVICES environment varialbe is available on AppFog v2. Some of the fields are slightly different than AppFog v1. Also, the MySQL service is now named `ctl_mysql`. Here is an example to connect to a MySQL instance:
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

### Additional Information
Our [Deploying a PHP Application](../AppFog/deploy-php-application.md) article has more information about customizing PHP and Apache buildpack settings.
