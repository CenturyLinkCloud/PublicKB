{{{ "title": "ElasticBox Commands",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

The Set and Config commands are useful to generate dynamic values for the variables in your box at deploy time. The notify command is useful to allow other instances to react to those changes.

* Set command
* Config command
* Notify command

### Set Command

Use the command to programmatically set the value of variables you don’t know beforehand, like authentication keys. Do this in the parent box to set the values of its variables or of variables in the child box scripts.

**Syntax**

To set the value of a parent box variable:

```
elasticbox set <variable_name> <variable_value> -box <box_name>
```

To set the value of a child box variable in the parent:

```
elasticbox set <childbox_variable_name>.<variable_name> <variable_value> -box <box_name>
```

| Parameter | Type | Description |
|-----------|------|-------------|
| box | String | Optional. Box name to run the command from SSHing into the instance of the deployed parent box. The parameter can include nested child box references. |

**Example**

This event script uses the Set command to generate a dynamic string based on the password, address, and username variables. At deploy time, when the script is executed, the resulting value stored in MONGODB_CONNECTION_STRING is used to log in to the MongoDB instance.

```
elasticbox set MONGODB_CONNECTION_STRING "mongodb://$user:$pass@$address.public:27017/elasticbox?safe=true"
```

### Config Command

Use the Config command on file variables to generate dynamic values when deploying. A file variable usually has additional scripts to configure your application. For ElasticBox to know what dynamic values to return, include variables or binding references in the files. Then call the file from an event using the Config command.

To get the file on to the virtual machine, use cURL or Wget like commands. When deploying, ElasticBox replaces the variables or binding references with configuration values, executes the file, and stores the result in an output file.

**Syntax**

```
elasticbox config -i <input_file> -o <output_file> -box <box_name> -t <template_engine>
```

| Parameter | Type | Description |
|-----------|------|-------------|
| i | String | 	Optional. Input file to run the Config command. When you don’t specify, the command reads data from standard input. |
| o | String | Optional. Output file that stores the configuration values. When you don’t specify, the command directs the data to standard output. |
| box | String | Optional. Box name to run the command from SSHing into the instance of the deployed parent box. |
| t | String | Optional. Template engine type, which is either Jinja2 or Velocity. If you set this flag, the command gives the values of the variables that match the template type in the file. If you don’t set the flag, the command gives values for variables of both template styles. |

**Example**

Suppose you upload a CHEF_DEFAULT_RB file to the Chef box. This file has a Rails cookbook script that refers to three Chef box variables (folder, RAILS_APP, and CLONE_URL).

Here are the file contents:

```
# Default Recipe

include_recipe "git"

include_recipe "nodejs"
include_recipe "sqlite"

#if (${RAILS_APP} != '')
application 'web_app' do
        path '${folder}/${RAILS_APP}'
        owner 'root'
        group 'root'
        repository '${CLONE_URL}'

        rails do
                bundler true
                precompile_assets true
                database do
                adapter "sqlite3"
                database "db/${RAILS_APP}.sqlite3"
                end
        end
end
#end
```

In order for ElasticBox to act on this file at deploy time, use cURL or WGET commands in an event script on the Chef box to download the file into the virtual machine. Then, pass the file through the Config command in the event script so that ElasticBox executes the Chef box variables in it.

Here the Config Command is run on the file:

```
curl -ks ${CHEF_DEFAULT_RB} | elasticbox config -o
cookbooks/${CHEF_COOKBOOK_NAME}/recipes/default.rb
```

At deploy time, ElasticBox runs the Config command on the CHEF_DEFAULT_RB file, replaces the variables with actual deploying values, and stores the file as default.rb in the specified path on the virtual machine.

### Notify Command

Use the command to programmatically send a notification to all instances that bind to the current instance.

**Syntax**

To send notification to all instances binding to the current one:

```
elasticbox notify
```

**Usage**

The most common use is to send a notification after executing one or several `elasticbox set` commands. The idea is that you can notify instances that are using those variables via bindings.

**Example**

A common pattern is to have variables that symbolize the state of the instance and use `elasticbox notify` to specify that status. For example, you could have a REPLICA_SET_READY variable. When the MongoDB replica set is initialized you set it to true in the instance and execute `elasticbox notify`. All instances binding to the previous one can check the variable REPLICA_SET_READY and execute some configurations if the value is true. If it is not true then it can skip that configuration, and they will be reconfigured (and that code executed) by that instance when the service is ready.

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
