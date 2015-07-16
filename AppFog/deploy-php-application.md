{{{
  "title": "Deploying a PHP Application",
  "date": "07-07-2015",
  "author": "Matt Cholick",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

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
