{{{
  "title": "Deploying a PHP Application",
  "date": "01-29-2016",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

Application developers

### Overview

AppFog includes the [Cloud Foundry PHP buildpack](https://github.com/cloudfoundry/php-buildpack) by default. This enables the deployment of PHP applications with a limited amount of configuration changes to an existing application.

The buildpack includes a customizable Apache (by deafult) or nginx server.

### Deploying a Simple Example

Run the following in a Bash shell to generate the simplest working example.

```
mkdir hello-php
cd hello-php
printf "<?php\n  phpinfo();\n?>"> index.php
cf push -m 128M --random-route hello-php
```

The `-m 128M` on `cf push` tells AppFog that it should allocate 128 MB of memory to run this website. Once it is deployed AppFog will return a URL where you can access the website in your browser:

```
➜  hello-php cf push -m 128M --random-route hello-php
...
Finished: [2015-07-07 16:33:37.539588]
-----> Uploading droplet (16M)

1 of 1 instances running

App started


OK

App hello-php was started using this command `$HOME/.bp/bin/start`

Showing health and status for app hello-php in org testOrg / space Dev as admin...
OK

requested state: started
instances: 1/1
usage: 128M x 1 instances
urls: hello-php-unsaved-focalization.uswest.appfog.ctl.io
last uploaded: Tue Jul 7 16:33:31 UTC 2015
stack: cflinuxfs2

     state     since                    cpu    memory          disk          details   
#0   running   2015-07-07 09:33:44 AM   0.0%   33.7M of 128M   37.4M of 1G      
```

Once the application has successfully started then you can go to the given URL route provided as the value for `urls` in the console log. The example URL route above is `hello-php-unsaved-focalization.uswest.appfog.ctl.io`. Take this URL and go to a browser to see the running application.

### Buildpack Options

The buildpack has several configuration options that a developer might want to customize. For example, to change the PHP version to the latest PHP 5.5, create a file `.bp-config/options.json` with the following contents:

```
{
    "PHP_VERSION": ["PHP_55_LATEST"]
}
```

For a complete list of options, see: https://github.com/cloudfoundry/php-buildpack/blob/master/docs/config.md

### php.ini

Many buildpack default php.ini settings may be modified by including a `.user.ini` file in your application's root directory. Additionally, a `.user.ini` file can be placed in any directory to limit modifications to a specific directory as described in the [PHP Documentation](http://php.net/manual/en/configuration.file.per-user.php). This PHP Manual page describes [where a configuration setting may be set](http://php.net/manual/en/ini.list.php). A `.user.ini` file will work for php.ini settings that do not have a [Changeable mode value](http://php.net/manual/en/ini.list.php) of PHP_INI_SYSTEM. Here you can find the default  [PHP 5.5 php.ini](https://github.com/cloudfoundry/php-buildpack/blob/master/defaults/config/php/5.5.x/php.ini) and [PHP 5.6 php.ini](https://github.com/cloudfoundry/php-buildpack/blob/master/defaults/config/php/5.6.x/php.ini) settings.

For example, a script that takes a long time to execute may need the following modifications within a `.user.ini` file:

```
max_execution_time = 300
max_input_time = 180
```

To modify php.ini settings marked PHP_INI_SYSTEM, create the directory `.bp-config/php/conf.d` in the root of your application. Next add a file with any name using the `.ini` extension in the directory, such as `php-settings.ini`. Then set the environment variable `PHP_INI_SCAN_DIR` to `.bp-config/php/conf.d`. This will instruct PHP to look for additional INI configuration in the directory you just created:

```
cf set-env <YOUR_APPNAME> PHP_INI_SCAN_DIR .bp-config/php/conf.d
```


### Configuring Apache

Developers have complete control over the buildpack's Apache server. For example, to change the modules and enable mod_alias to add Redirect support in .htaccess (which is off by default), add `httpd-modules.conf` the following to `.bp-config/httpd/extra/` with contents:

```
LoadModule authz_core_module modules/mod_authz_core.so
LoadModule authz_host_module modules/mod_authz_host.so
LoadModule log_config_module modules/mod_log_config.so
LoadModule env_module modules/mod_env.so
LoadModule setenvif_module modules/mod_setenvif.so
LoadModule dir_module modules/mod_dir.so
LoadModule mime_module modules/mod_mime.so
LoadModule reqtimeout_module modules/mod_reqtimeout.so
LoadModule unixd_module modules/mod_unixd.so
LoadModule mpm_event_module modules/mod_mpm_event.so
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_fcgi_module modules/mod_proxy_fcgi.so
LoadModule remoteip_module modules/mod_remoteip.so
LoadModule rewrite_module modules/mod_rewrite.so
LoadModule alias_module modules/mod_alias.so
```

This is the same as the default, with the added line `LoadModule alias_module modules/mod_alias.so`

Some users have reported issues with timeouts beyond the PHP configuration and have needed to modify the Apache timeout settings. This can be done by creating a `httpd-default.conf` file located within the `.bp-config/httpd/extra/` directory. The default can be found here: https://github.com/cloudfoundry/php-buildpack/blob/master/defaults/config/httpd/extra/httpd-default.conf. In the example below note the only change is updating the Timeout value from the default of 60 seconds to 300 seconds:

```
Timeout 300
KeepAlive On
MaxKeepAliveRequests 100
KeepAliveTimeout 5
UseCanonicalName Off
UseCanonicalPhysicalPort Off
AccessFileName .htaccess
ServerTokens Prod
ServerSignature Off
HostnameLookups Off
EnableMMAP Off
EnableSendfile On
RequestReadTimeout header=20-40,MinRate=500 body=20,MinRate=500
```

Here are the [default Apache configuration files](https://github.com/cloudfoundry/php-buildpack/tree/master/defaults/config/httpd). To override any file, simply provide a file of the same name and path in `.bp-config/httpd/`

##### Note

It's important to specify a specific buildpack with this level of customization. As we upgrade the platform, the default PHP buildpack version will increase and it could be incompatible with any customizations you've made. To lock the buildpack to a specific version so you can control buildpack upgrades, include the buildpack directive in your manifest.yml. Example manifest specifying buildpack version 3.3.0:

```
---
applications:
  - name: my-php-app
    host: chk-my-php-app
    memory: 128M
    buildpack: https://github.com/cloudfoundry/php-buildpack.git#v3.3.0
```

### Using nginx

To use nginx, instead of the default Apache, create a file `.bp-config/options.json`, with the following contents:

```
{
    "WEB_SERVER": ["nginx"]
}
```

The server can be cusomtized in the same way as that described in the "Configuring Apache" section. Here are the
[default nginx configuration files](https://github.com/cloudfoundry/php-buildpack/tree/master/defaults/config/nginx)

### Troubleshooting

To enable the buildpack debug mode you can set the BP_DEBUG environment variable to true using the following command. This will instruct the buildpack to set it's log level to DEBUG and write to stdout:

```
cf se <YOUR_APPNAME> BP_DEBUG true
```
<b>NOTE</b>: If you enable debug logging it might include sensitive information like usernames, passwords, tokens, service info and file names from your application. Be careful where you post those logs and if necessary, redact any sensitive information first.
### Additional Information

More information on deploying PHP applicatinos can be found in the [Cloud Foundry Documentation](https://docs.cloudfoundry.org/buildpacks/php/index.html).
