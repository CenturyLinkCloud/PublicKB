{{{
  "title": "Local Development with CenturyLink WordPress as a Service",
  "date": "07-30-2015",
  "author": "Matt Wittmann",
  "attachments": [],
  "contentIsHTML": false
}}}

IMPORTANT NOTE
--------------

CenturyLink Cloud WordPress hosting is currently in a Limited Beta program with specific customers by invitation only
and is not intended for production usage.

During the Limited Beta there is no production Service Level Agreement.

Prerequisites
-------------

1. You have [created your WordPress site](getting-started-with-wordpress-as-a-service.md).
2. You have [cloned your WordPress site's git repository](wordPress-site-updates-with-git.md).
3. You have downloaded and installed [VirtualBox](https://www.virtualbox.org/).
4. You have downloaded and installed [Vagrant](https://www.vagrantup.com/).
5. The Vagrant plug-in [Hosts Updater](https://github.com/cogitatio/vagrant-hostsupdater) has been installed
   *(optional)*.

Introduction
------------

WordPress is infinitely customizable with themes and plug-ins galore. A best practice is for WordPress developers
to preview their changes on their local machine before uploading them to their production host. CenturyLink WordPress hosting makes these easy by integrating with Vagrant. Using Vagrant, a full development
environment can be created in minutes with the whole LEMP (Linux, nginx, MySQL, PHP) stack running inside a virtual
machine.

Creating the Local Development Environment
------------------------------------------

After the WordPress site's git repository has been cloned, change into its directory.

Optionally, the `.env.local` file may be changed to set values like WordPress keys and salts, the site name, etc.
These parameters should be configured first if it is desired that they be customized. If these are changed after
the first provisioning, the Vagrant box may first need to be destroyed and re-upped for changes to take effect.

Next run:

```
vagrant up
```

The centurylinkcloud/wp-developer Vagrant box will be downloaded, which can take some time for the first run.
After that, it will provision the box and try to set your hosts file to map `192.168.33.10` to `wp.dev` if the
Hosts Updater Vagrant plug-in is installed.

Navigate to [http://wp.dev/](http://wp.dev/) or [http://192.168.33.10/](http://192.168.33.10/) if the
Hosts Updater plug-in has not been installed. This gives access to the WordPress application running
from the local git repository. As changes are made, they will be immediately live on the local site.

When you are satisfied with your changes, you may commit them and push them back up to CenturyLink's git
hosting. Please review the [Knowledge Base article on git cloning and pushing](wordPress-site-updates-with-git.md).

### Note

Database and configuration changes (plug-in settings, content posts, etc.) are not synchronized with the live site and
*vice versa*.

WordPress Administration
------------------------

The WordPress administrative username is `wp-developer`, and the password is `password`.

MySQL
-----

You can use the MySQL command-line interface to work with your database; the password should be `vagrant`:

```
vagrant ssh
mysql --user=root --password=root wp-developer
```

You can exit the MySQL CLI by typing:

```
\q
```

Exit out of the Vagrant SSH session by typing:

```
exit
```

For more details, see the [MySQL documentation](https://dev.mysql.com/doc/refman/5.5/en/mysql.html).

### Note

Local database changes are not reflected on the live site and *vice versa*!

Resetting the Local Environment
-------------------------------

The database content can be cleared and the .env.local fully reloaded by resetting the local environment. Changes
relating to the file system, such as added plug-ins, will not be destroyed; such files will need to be
deleted.

```
vagrant destroy
vagrant up
```
