{{{
  "title": "Using Diego with AppFog",
  "date": "02-26-2016",
  "author": "Chris Selzo",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

Application developers

### What is Diego?

Diego is the next-generation runtime powering Cloud Foundry, on which AppFog is based.  Any apps that currently run on AppFog will run on Diego, and have some cool new features.  All app workloads on AppFog will eventually be transitioned to Diego.

### Enabling Diego

It's easy to enable Diego for your apps using the [Diego Enabler](https://github.com/cloudfoundry-incubator/Diego-Enabler) plugin for the `cf` cli.  Once installed, use the command:
```
$ cf has-diego-enabled hello-diego
false
```
to check the Diego status of your app.  To enable Diego, use:
```
$ cf enable-diego hello-diego
Setting hello-diego Diego support to true
Ok

Verifying hello-diego Diego support is set to true
Ok
```
If your app is currently running, this will restart it on Diego.  If you want to try out Diego with a new app, and only run it on Diego, you can push it with the `--no-start` flag, enable diego, and then start it:
```
$ cf push hello-diego --no-start -b nodejs_buildpack
Updating app hello-diego...
OK
...
$ cf enable-diego hello-diego
Setting hello-diego Diego support to true
Ok

Verifying hello-diego Diego support is set to true
Ok
$ cf start hello-diego
```

### SSH to app container

The most helpful feature in Diego is the ability to SSH into your running app containers.  Troubleshooting running apps is a whole lot easier when you can open an interactive shell to an app instance.  To SSH into an app, use the `cf ssh` command, and then use your standard suite of linux commands:
```
$ cf ssh hello-diego
vcap@dg1qg2t8dmi:~$ ls
app  logs  staging_info.yml  tmp
vcap@dg1qg2t8dmi:~$ cat staging_info.yml
detected_buildpack: ""
start_command: npm start
vcap@dg1qg2t8dmi:~$ exit
exit
$
```

Your app's file live in the `app` directory.

To SSH to a specific instance, use the `-i` flag:
```
$ cf ssh hello-diego -i 3
vcap@dg1qg2t8dmi:~$ echo $CF_INSTANCE_INDEX
3
```

To explore all of the capabilities, run `cf ssh --help`:
```
NAME:
   ssh - SSH to an application container instance

USAGE:
   cf ssh APP_NAME [-i app-instance-index] [-c command] [-L [bind_address:]port:host:hostport] [--skip-host-validation] [--skip-remote-execution] [--request-pseudo-tty] [--force-pseudo-tty] [--disable-pseudo-tty]

OPTIONS:
   --disable-pseudo-tty, -T      Disable pseudo-tty allocation
   -L                            Local port forward specification. This flag can be defined more than once.
   --command, -c                 Command to run. This flag can be defined more than once.
   --app-instance-index, -i      Application instance index
   --skip-host-validation, -k    Skip host key validation
   --skip-remote-execution, -N   Do not execute a remote command
   --request-pseudo-tty, -t      Request pseudo-tty allocation
   --force-pseudo-tty, -tt       Force pseudo-tty allocation
```

**Notes**
* Changes to app instance are not preserved after your app is restarted.  If you want your changes to be permanent, change your local copy and `cf push` again.
* `cf ssh` requires a `cf` [version](https://github.com/cloudfoundry/cli/releases) > 6.13
* For more information about all the capabilities of app SSH, see [this guide](https://docs.cloudfoundry.org/devguide/deploy-apps/ssh-apps.html)

### Diego differences

There are a few differences when running an app on Diego that you should be aware of

#### Port environment variable

Make sure to use `PORT` instead of `VCAP_APP_PORT` as the port for your app to listen on.  This change is backwards-compatible, so you can change your existing non-Diego apps to use this value.

#### Accessing app files

The `cf files` command no longer works in Diego

```
$ cf files hello-diego
FAILED
The app is running on the Diego backend, which does not support this command.
```

You should use the `cf ssh` command instead to access the files of your app.  To download app files using `scp`, see [this guide](https://docs.cloudfoundry.org/devguide/deploy-apps/ssh-apps.html#other-ssh-access)

#### Specifying a buildpack

It's always good practice to specify your buildpack when pushing an app to AppFog, but in Diego it's even more important.  Pushing without specifying a buildpack will take longer on Diego.  To specify a buildpack, you can use the `-b` flag on your push command:
```
$ cf push hello-diego --no-start -b nodejs_buildpack
```

To see the built-in buildpacks:
```
$ cf buildpacks
Getting buildpacks...

buildpack              position   enabled   locked   filename   
java_buildpack         1          true      false    java-buildpack-v3.4.zip   
ruby_buildpack         2          true      false    ruby_buildpack-cached-v1.6.12.zip   
nodejs_buildpack       3          true      false    nodejs_buildpack-cached-v1.5.4.zip   
go_buildpack           4          true      false    go_buildpack-cached-v1.7.1.zip   
python_buildpack       5          true      false    python_buildpack-cached-v1.5.4.zip   
php_buildpack          6          true      false    php_buildpack-cached-v4.3.2.zip   
staticfile_buildpack   7          true      false    staticfile_buildpack-cached-v1.3.0.zip   
binary_buildpack       8          true      false    binary_buildpack-cached-v1.0.1.zip
```

You can also specify a buildpack by its git repo:
```
$ cf push hello-diego-static -b https://github.com/cloudfoundry/staticfile-buildpack.git
```

#### Health checks

Before Diego, you could specify the `--no-route` option on your `cf push` command to disable the built-in check that your app is listening on the port specified by the environment variable `PORT`.  This is useful for "worker" type apps that aren't serving web traffic.  With Diego, you need to also set the health check to `none` or it will assume your app is crashing.  You can set this with a `cf set-health-check` command, or on your `cf push`:
```
$ cf push hello-diego-worker --health-check-type none
```
The two options are `port`, which is the default and `none`, which still checks for process health but does not check if your app is listening on the port.

#### App file permissions

When pushing Diego apps from a Mac or Linux system, your app file permissions are now preserved.  Previously, they were all set to `0744`.  Make sure before pushing your Diego app that your files have the correct permissions (for example, if using the `binary_buildpack`, ensure that your binary has execute permissions).  If you are pushing apps from a Windows system, this change does not apply.

#### Reference
https://github.com/cloudfoundry-incubator/diego-design-notes/blob/master/migrating-to-diego.md
