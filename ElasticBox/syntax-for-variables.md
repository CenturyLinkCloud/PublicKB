{{{ "title": "Jinja Templating for Variables",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

When configuring an application deployment in a box, you can define its deployment parameters as variables. In order for ElasticBox to execute them during a deployment, they need to be referenced in the configuration [event scripts](../ElasticBox/start-stop-and-upgrade-boxes.md) following the Jinja2 syntax in these sections. [Jinja2](//jinja.pocoo.org/docs/dev/) is a templating language in Python that we follow for the variable syntax conventions.

**In this article:**

* Syntax for binding type variables
* Syntax for other variable types
* Syntax for system variables

### Syntax for Binding Type Variables

A binding type variable lets you connect to one or more services running on separate infrastructure. Bindings provide data like connection string URLs or environment or variable values of the instances to which they point.

Besides configuring bindings, you can reference them in box event scripts to derive data from them to enable instance connectivity. To get values from bindings in the parent box event scripts, follow this syntax:

* {{ binding_variable_name.variable }} or {{ binding_variable_name[n].variable }}: Returns the value of the variable in the instance to which the binding points. Here “n” refers to a particular instance associated with the binding.
* {{ binding_variable_name.address.public }}: Returns the public address of the instance to which the binding points.
* {{ binding_variable_name.address.private }}: Returns the private address of the instance to which the binding points.

To get values from bindings in child boxes, follow this syntax.

* {{ boxtype_variable_name.binding_variable_name.variable }}: Gives the value of the variable in a bound box in the box type variable.

### Syntax for Other Variable Types

Use other variable types to get or set dynamic configuration values when deploying. To get or set values, refer to variables in event scripts of the parent box. From the parent box, you can refer to the variables in it as well as in those of the child boxes.

To get variables values in the parent box event scripts, follow this syntax:

* {{ variable_name }}: Returns the value of the variable.
* {{ boxtype_variable_name.variable_name }}: Returns the value of the variable in the box type variable. This is how you get values of variables in child boxes.

    **Note:** There’s no limit to the number of child boxes boxes you can traverse. For example, to get the value of a variable from a box nested two levels deep, use this syntax: {{ boxtype_variable_name.boxtype_variable_name.variable_name }}

To set or change variable values in the parent box event scripts, follow this syntax with the set command. For examples, see the [Set Command](../ElasticBox/elasticbox-commands.md).

* elasticbox set <variable_name> <variable_value>: Sets the value of the variable.
* elasticbox set <boxtype_variable_name>.<variable_name> <variable_value>: Sets the value of the variable in the box type variable. This is how you set values for variables in child boxes.

### Syntax for System Variables

In addition to variables you create, all boxes deployed through ElasticBox use system variables. They represent ElasticBox assets used for a deployment such as environment or box. They also contain information about the virtual infrastructure such as public, private IP addresses, and the virtual machines or services.

To get values of default deployment variables in parent box event scripts, follow this syntax:

* {{ environment }}: Returns the name of the environment where the box is deployed like a box deployed to an environment named Test.
* {{ machine }}: Gives the name of the virtual infrastructure where ElasticBox runs the script. It has the eb-XXXXX-1 format.
* {{ instance }}: Gives the ID for the instance in the i-XXXXXX format.
* {{ service }}: Gives the dynamic ID for type of service used to generate machines and services for the instance. ElasticBox uses this service ID, say eb-XXXXX, to create resources with the provider such as servers, security groups, and so on.
* {{ addresses }}: Gives the public and private IP addresses of all instances deployed for a box.
* {{ address.public }}: Gives the public IP address of the current instance.
* {{ address.private }}: Gives the private IP address of the current instance.
* {{ box }}: Returns the name of the parent box deployed.
* {{ folder }}: Returns the current working directory (CWD) path where ElasticBox executes scripts in the instance.

**Note:** When the instance is provisioned on a service, like AWS RDS, ElasticBox stores deployment information in these variables:

* {{ address.public }}: Gives public IP address of the instance.
* {{ address.private }}: Gives private IP address of the instance.
* {{ username }}: Gives the instance username.
* {{ password }}: Gives the instance password.

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](../ElasticBox/troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
