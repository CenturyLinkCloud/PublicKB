{{{
  "title": "Deploying a PHP Laravel Application",
  "date": "02-26-2016",
  "author": "AppFog Team",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

Application developers

### Overview

AppFog includes the [Cloud Foundry PHP buildpack](https://github.com/cloudfoundry/php-buildpack) by default. This enables the deployment of PHP applications and PHP [Laravel](https://www.laravel.com/) applications.

The Laravel framework is a PHP framework that can be succesfully deployed in AppFog with a few additional steps.  These steps have been tested with a basic Laravel application.  Other modifications may be necessary if you are using specific PHP extensions or are conneting to specific database services.

### Add an `options.json` file

The `options.json` file allows for customization of the PHP Buildpack, and for Laravel it's explictly used to enable necessary PHP extensions and specify the appropriate web directory.  Create an `options.json` file in a `.bp-config` folder with the following content:

```
 {
   "PHP_VERSION": "PHP_55_LATEST",
   "COMPOSER_VENDOR_DIR": "vendor",
   "WEBDIR": "public",
   "PHP_EXTENSIONS": [ "bz2", "zlib", "openssl", "curl", "mcrypt", "mbstring", "pdo"]
 }
```

### Ignore the vendor folder
You can avoid uploading the vendor folder by creating or update a `.cfignore` file in your apps root folder that includes the following line:

```
vendor/
```

### Optionally, add a manifest.yml file
Add a manifest file in your apps root folder.  The contents will be application-specific and should look similar to:

```
---
 applications:
 - name: <yourappname>
   memory: 128M
   instances: 2
   buildpack: https://github.com/cloudfoundry/php-buildpack
   env:
     CF_STAGING_TIMEOUT: 15
     CF_STARTUP_TIMEOUT: 15
```

### Troubleshooting

To enable the buildpack debug mode you can set the BP_DEBUG environment variable to true using the following command. This will instruct the buildpack to set its log level to DEBUG and write to stdout:

```
cf se <YOUR_APPNAME> BP_DEBUG true
```
<b>NOTE</b>: If you enable debug logging it might include sensitive information like usernames, passwords, tokens, service info and file names from your application. Be careful where you post those logs and if necessary, redact any sensitive information first.
### Additional Information

More information on deploying PHP applications can be found in the [Cloud Foundry Documentation](http://http://docs.cloudfoundry.org/buildpacks/php/index.html)
