{{{
"title": "Set up a Development Environment Using ElasticBox and Vagrant",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Set up a Development Environment Using ElasticBox and Vagrant

In this 90-minute walkthrough, learn how to launch production-ready development and test environments from boxes on to your laptop using the [ElasticBox agent](./deploying-on-anyinfra.md). With boxes, you can launch development environments in the same way as production letting developers test changes realistically.

**Scenario**

We’re going to define a Rails development environment in boxes and launch them using the ElasticBox agent on to your Mac laptop running a virtual machine on Vagrant and VirtualBox. The environment is based on a sample Ruby on Rails app that uses MySQL as a database.

**Learning Objectives**

This tutorial helps you learn these concepts:

* Define any module or application in boxes. If some part of the environment changes in the future, you don’t have to change every developer’s laptop, only the box for example.
* Spin up applications from boxes on to any infrastructure like your laptop using the ElasticBox agent Linux Bash script.
* Work with ElasticBox and Vagrant to launch local environments. Run applications inside a virtual machine to isolate and protect your laptop from a different OS and runtime.

**Let’s get started:**
* Before you begin
* Define dev environment in boxes
* Launch dev environment using the ElasticBox agent
* Verify dev environment

### Before you begin

To get started, set up the following:

1. Sign up for an ElasticBox account. It’s free!

2. Fork a sample Rails app from this [GitHub repository](https://github.com/railstutorial/sample_app_rails_4). Clone it in your Mac laptop as shown. This creates a local copy of the sample Rails app.

    ![tutorial-vagrant-1.png](../images/ElasticBox/tutorial-vagrant-1.png)

3. Install VirtualBox, a free open source virtualizer to run your dev environment. To install, run this command in your Mac laptop terminal:

   ```
   brew cask install virtualbox
   ```

4. [Install Vagrant](https://docs.vagrantup.com/v2/installation/) on your Mac laptop to isolate your development environment in VirtualBox:

    ```
    brew cask install vagrant
    ```

5. Install a Vagrant Ubuntu 14.04 Linux image:

    ```
    vagrant box add ubuntu/trusty64 https://vagrantcloud.com/ubuntu/boxes/trusty64
    ```

6. Create a Vagrantfile that we’ll use later to provision the image:

    ```
    vagrant init ubuntu/trusty64
    ```

___


### Define Dev Environment in Boxes

We log in to ElasticBox and define modules of the Rails dev environment in multiple boxes and stack them into a single box at the end.

**Nodejs Box**

This installs Javascript runtime for the Rails app.

**Steps**

1. Create a new box called Nodejs based on Linux Compute.

2. Add an options variable called APT_GET_UPDATE with a **no** value.

3. Copy/paste this script in a **post\_install** event:

    ```
    #!/bin/bash

    \{{ 'apt-get update' if APT_GET_UPDATE == 'yes' }}
    apt-get -q -y install nodejs
    ```

    ![tutorial-vagrant-2.png](../images/ElasticBox/tutorial-vagrant-2.png)

___

**Rails Dependencies Box**

This installs all the dependencies for the Rails app.

**Steps**

1. Create a new box called Rails Dependencies based on Linux Compute.

2. Add the following variables:
    * Port variable called http set to **3000**.
    * Box variable called ruby pointing to the default **Ruby** box.
    * Box variable called nodejs pointing to the **Nodejs** box.

    ![tutorial-vagrant-3.png](../images/ElasticBox/tutorial-vagrant-3.png)

___


**Rails with GitHub Box**

**Steps**

1. Create a new box called Rails with GitHub based on Linux Compute.

2. Add these box variables:
    * Box variable called rails pointing to the **Rails Dependencies** box.
    * Box variable called github pointing to the **GitHub** box.

    ![tutorial-vagrant-4.png](../images/ElasticBox/tutorial-vagrant-4.png)

___


**MySQL Ubuntu Box**

This installs MySQL server and creates a database.

**Steps**

1. Create a new box called MySQL Ubuntu based on Linux Compute.

2. Add the following variables:
    * Options variable called APT_GET_UPDATE set to **yes**
    * Text variable called BIND_ADDRESS set to **0.0.0.0**
    * Text variable called DATA_DIR set to **/var/lib/mysql**
    * Text variable called LOG_ERROR set to **/var/log/mysql/error.log**
    * Text variable called MAX_ALLOWED_PACKET set to **32M**
    * Text variable called MAX_CONNECTIONS set to **100**
    * Port variable called MYSQL_PORT set to **3306**
    * Text variable called ROOT_PASSWORD set to **elasticbox123**
    * File variable called my_cnf with this script uploaded as a text file:

    ```
	  #
    # The MySQL database server configuration file.
    #
    # You can copy this to one of:
    # - "/etc/mysql/my.cnf" to set global options,
    # - "~/.my.cnf" to set user-specific options.
    #
    # One can use all long options that the program supports.
    # Run program with --help to get a list of available options and with
    # --print-defaults to see which it would actually understand and use.
    #
    # For explanations see
    # http://dev.mysql.com/doc/mysql/en/server-system-variables.html

    # This will be passed to all mysql clients
    # It has been reported that passwords should be enclosed with ticks/quotes
    # especially if they contain "#" chars...
    # Remember to edit /etc/mysql/debian.cnf when changing the socket location.
    [client]
    port    = \{{ MYSQL_PORT }}
    socket    = /var/run/mysqld/mysqld.sock

    # Here is entries for some specific programs
    # The following values assume you have at least 32M ram

    # This was formally known as [safe_mysqld]. Both versions are currently parsed.
    [mysqld_safe]
    socket    = /var/run/mysqld/mysqld.sock
    nice    = 0

    [mysqld]
    #
    # * Basic Settings
    #
    user    = mysql
    pid-file  = /var/run/mysqld/mysqld.pid
    socket    = /var/run/mysqld/mysqld.sock
    port    = \{{ MYSQL_PORT }}
    basedir   = /usr
    datadir   = /var/lib/mysql
    tmpdir    = /tmp
    lc-messages-dir = /usr/share/mysql
    skip-external-locking
    #
    # Instead of skip-networking the default is now to listen only on
    # localhost which is more compatible and is not less secure.
    bind-address    = \{{ BIND_ADDRESS }}
    #
    # * Fine Tuning
    #
    key_buffer    = 16M
    max_allowed_packet  = \{{ MAX_ALLOWED_PACKET }}
    thread_stack    = 192K
    thread_cache_size       = 8
    # This replaces the startup script and checks MyISAM tables if needed
    # the first time they are touched
    myisam-recover         = BACKUP
    #max_connections        = \{{ MAX_CONNECTIONS }}
    #table_cache            = 64
    #thread_concurrency     = 10
    #
    # * Query Cache Configuration
    #
    query_cache_limit = 1M
    query_cache_size        = 16M
    #
    # * Logging and Replication
    #
    # Both location gets rotated by the cronjob.
    # Be aware that this log type is a performance killer.
    # As of 5.1 you can enable the log at runtime!
    #general_log_file        = /var/log/mysql/mysql.log
    #general_log             = 1
    #
    # Error log - should be very few entries.
    #
    log_error = \{{ LOG_ERROR }}
    #
    # Here you can see queries with especially long duration
    #log_slow_queries = /var/log/mysql/mysql-slow.log
    #long_query_time = 2
    #log-queries-not-using-indexes
    #
    # The following can be used as easy to replay backup logs or for replication.
    # Note: If you are setting up a replication slave, see README.Debian about
    #       other settings you may need to change.
    #server-id    = 1
    #log_bin      = /var/log/mysql/mysql-bin.log
    expire_logs_days  = 10
    max_binlog_size         = 100M
    #binlog_do_db   = include_database_name
    #binlog_ignore_db = include_database_name
    #
    # * InnoDB
    #
    # InnoDB is enabled by default with a 10MB datafile in /var/lib/mysql/.
    # Read the manual for more InnoDB related options. There are many!
    #
    # * Security Features
    #
    # Read the manual, too, if you want chroot!
    # chroot = /var/lib/mysql/
    #
    # For generating SSL certificates I recommend the OpenSSL GUI "tinyca".
    #
    # ssl-ca=/etc/mysql/cacert.pem
    # ssl-cert=/etc/mysql/server-cert.pem
    # ssl-key=/etc/mysql/server-key.pem


    [mysqldump]
    quick
    quote-names
    max_allowed_packet  = \{{ MAX_ALLOWED_PACKET }}

    [mysql]
    #no-auto-rehash # faster start of mysql but no tab completion

    [isamchk]
    key_buffer    = 16M

    #
    # * IMPORTANT: Additional settings that can override those from this file!
    #   The files must end with '.cnf', otherwise they'll be ignored.
    #
    !includedir /etc/mysql/conf.d/
    ```

3. Copy/paste the following script in a **post_install** event:

    ```
	  #!/bin/bash
    \{{ 'apt-get update' if APT_GET_UPDATE == 'yes' }}
    export DEBIAN\_FRONTEND=noninteractive
    apt-get -q -y install mysql-server
    elasticbox config -i config/database.template.yml -o config/database.yml
    # Set Password
    mysqladmin -u root password \{{ ROOT_PASSWORD }}

    # Make accessible from all ips
    mysql -uroot -p\{{ ROOT_PASSWORD }} --execute "GRANT ALL PRIVILEGES ON *.* to 'root'@'%'; FLUSH PRIVILEGES;"
    ```

    ![tutorial-vagrant-5.png](../images/ElasticBox/tutorial-vagrant-5.png)

___

**Rails Dev Env Box**

This box installs a development environment with the sample Rails app, runtimes, and MySQL database.

**Steps**

1. Create a new box called **Rails Dev Env** based on Linux Compute.

2. Add the following variables:
    * Box variable called mysql that points to the** MySQL Ubuntu** box
    * Box variable called rails that points to the **Rails with GitHub** box

3. Expand the rails box variable all the way down to the ruby box. Set RVM_RUBY_VERSION to **ruby-2.0.0-p576**.

4. Expand the github box variable, and in the git_repo box, set values for these variables as follows:
    * BRANCH to **master**
    * CLONE_DIRECTORY to **/vagrant**
    * CLONE_URL to **https://github.com/< your_fork_of_the_sample_Rails_app >**

5. Copy/paste this script into a **post_configure** event:

    ```
    #!/bin/bash
    source "/usr/local/rvm/scripts/rvm"
    cd \{{ rails.github.git_repo.CLONE_DIRECTORY }}
    cp config/database.yml.example config/database.yml

    # ruby dev packages to support building gems from source
    apt-get -y install ruby2.0-dev libreadline-ruby2.0 libruby2.0 libopenssl-ruby

    # nokogiri requirements
    apt-get -y install libxslt-dev libxml2-dev

    # app specific
    bundle install --without production
    bundle exec rake db:migrate
    ```

6. Copy/paste this script into a start event:

    ```
    #!/bin/bash
    source "/usr/local/rvm/scripts/rvm"
    cd \{{ rails.github.git_repo.CLONE_DIRECTORY }} && rails server -p \{{ rails.rails.http }} -d
    ```

    ![tutorial-vagrant-6.png](../images/ElasticBox/tutorial-vagrant-6.png)

___


### Launch Dev Environment Using the ElasticBox Agent


Launch the Rails Dev Env box on your Mac laptop virtual machine running on Vagrant and VirtualBox as follows.

**Steps**

1. Search for the Vagrantfile on your Mac laptop. Open and replace contents with these lines. They ask Vagrant to provision the Linux Ubuntu image with the Rails Dev Env box using the agent script:

    **IMPORTANT**: Replace the token in the -t flag with your own authentication token.

    ```
    # -*- mode: ruby -*-
    # vi: set ft=ruby :

    # Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
    VAGRANTFILE_API_VERSION = "2"

    Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    # All Vagrant configuration is done here. The most common configuration
    # options are documented and commented below. For a complete reference,
    # please see the online documentation at vagrantup.com.

    # Every Vagrant virtual environment requires a box to build off of.
    config.vm.box = "ubuntu/trusty64"
    config.vm.network "forwarded_port", guest: 3000, host: 3100
    config.vm.provision :shell, inline: 'curl -kLsS ebx.co | sudo bash -s -- -b "Rails Dev Env" -n laptop -t 04329c63-78b7-4313-bc09-8090e3a7e93d'

    end
    ```

2. Move the Vagrantfile to the sample_app_rails_4 folder cloned in your Mac laptop. Commit and push this change to your forked repo in GitHub.

    ![tutorial-vagrant-7.png](../images/ElasticBox/tutorial-vagrant-7.png)

3. In your Mac laptop terminal, go to the sample_app_rails_4 directory as in this example:

    ```
    cd /Users/mrina/sample_app_rails_4
    ```

4. Bring up the Vagrant Ubuntu image in VirtualBox and launch the Rails dev environment with this command:

    ```
    vagrant up
    ```

    Right away, the box is provisioned per the Vagrantfile and it soon registers in ElasticBox. Check your ElasticBox workspace for the online Rails Dev Env instance. This can take a few minutes.

    ![tutorial-vagrant-8.png](../images/ElasticBox/tutorial-vagrant-8.png)

5. Once online, from the instance **Endpoints** tab, copy the Rails app IP address.

    ![tutorial-vagrant-9.png](../images/ElasticBox/tutorial-vagrant-9.png)

6. In your Mac laptop terminal, SSH into your Vagrant virtual machine from the sample_app_rails_4 directory:

    ```
    vagrant ssh
    ```

7. Open the Rails app in the virtual machine using xdg-open. If you don’t have xdg-utils, install it first as shown.

    ```
    sudo apt install xdg-utils
    ```

    ```
    xdg-open
    ```

    ![tutorial-vagrant-10.png](../images/ElasticBox/tutorial-vagrant-10.png)

___

### Verify Dev Environment

Let’s now run some tests to verify that the dev environment is working.

**Steps**

1. Open a new terminal in your Mac laptop and go to the sample_app_rails_4 directory.

2. SSH into the virtual machine:

    ```
    vagrant ssh
    ```

3. Go to this vagrant directory:

    ```
    cd /vagrant
    ```

4. Migrate Rails tests as follows:

    ```
    bin/rake db:migrate RAILS_ENV=test
    ```

5. Finally, run tests with this command:

    ```
    rspec spec
    ```

You should see all the tests pass. Congratulations! You’ve successfully deployed a Rails development environment on your laptop using ElasticBox and Vagrant.

![tutorial-vagrant-11.png](../images/ElasticBox/tutorial-vagrant-11.png)

To quit the Vagrant virtual environment, run this command:

```
exit
```

After completing the tutorial, be sure to terminate the instance in your ElasticBox workspace by selecting the gear icon and clicking **Terminate**. Then delete the Vagrant virtual machine with this command:

```
vagrant destroy
```

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](https://www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
