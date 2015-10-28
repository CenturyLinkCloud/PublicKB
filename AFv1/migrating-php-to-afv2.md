{{{
  "title": "Migrating a PHP Application to AppFog v2",
  "date": "10-28-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

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
`cf push <appname> -b https://github.com/CenturyLinkCloud/php-buildpack#af_custom_php`

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
### VCAP_SERVICES
The VCAP_SERVICES environment varialbe is available on AppFog v2. Some of the fields are slightly different than AppFog v1. Here is an example to connect to a MySQL instance:
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
