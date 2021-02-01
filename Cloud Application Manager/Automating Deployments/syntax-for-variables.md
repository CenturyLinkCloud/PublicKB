{{{
"title": "Jinja Templating for Variables",
"date": "12-28-2018",
"author": "Julio Castanar",
"keywords": ["cam","alm","boxes", "box", "jinja" ],
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Syntax for Binding Type Variables](#syntax-for-binding-type-variables)
* [Syntax for Other Variable Types](#syntax-for-other-variable-types)
* [Syntax for System Variables](#syntax-for-system-variables)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article is meant to assist Cloud Application Manager customers who want to create and manage boxes.  
It explains how to use the **variable syntax conventions: the Jinja2 syntax**.  
When configuring an application deployment in a box, you can define its deployment parameters as variables. In order for Cloud Application Manager to execute them during a deployment, they need to be referenced in the configuration [event scripts](start-stop-and-upgrade-boxes.md) following the Jinja2 syntax in these sections. [Jinja2](http://jinja.pocoo.org/docs/dev/) is a templating language in Python that we follow for the variable syntax conventions.


### Audience

Cloud Application Manager Users using Application Lifecycle Management (ALM) features.

### Prerequisites

* Access to [Applications site](https://cam.ctl.io/#/boxes) (Application Lifecycle Management module) of Cloud Application Manager as an authorized user of an active Cloud Application Manager account.

* A box already configured in Cloud Application Manager. See [administering providers](../Administering Your Organization/admin-overview.md).

### Syntax for Binding Type Variables

A binding type variable lets you connect to one or more services running on separate infrastructure.  
Bindings provide data like connection string URLs or environment or variable values of the instances to which they point.

Besides configuring bindings, you can reference them in box event scripts to derive data from them to enable instance connectivity.  

To get values from bindings in the *parent box* event scripts, follow this syntax:
* Returns the value of the variable in the instance to which the binding points:

    ```
    `\{{ binding_variable_name.variable }}` or `\{{ binding_variable_name[n].variable }}`
    ```
    Here “n” refers to a particular instance associated with the binding.

* Returns the public address of the instance to which the binding points:

    ```
    `\{{ binding_variable_name.address.public }}`
    ```

* Returns the private address of the instance to which the binding points:

    ```
    `\{{ binding_variable_name.address.private }}` 
    ```

To get values from bindings in *child boxes*, follow this syntax.

* Gives the value of the variable in a bound box in the box type variable.

    ```
    `\{{ boxtype_variable_name.binding_variable_name.variable }}`
    ```

### Syntax for Other Variable Types

Use other variable types to get or set dynamic configuration values when deploying. To get or set values, refer to variables in event scripts of the parent box. From the parent box, you can refer to the variables in it as well as in those of the child boxes.

To get variables values in the *parent box* event scripts, follow this syntax:

* Returns the value of the variable.

    ```
    `\{{ variable_name }}`
    ```

* Returns the value of the variable in the box type variable. This is how you get values of variables in *child boxes*.

    ```
    `\{{ boxtype_variable_name.variable_name }}`
    ```

    **Note:** There’s no limit to the number of child boxes boxes you can traverse. For example, to get the value of a variable from a box nested two levels deep, use this syntax:

    ```
    `\{{ boxtype_variable_name.boxtype_variable_name.variable_name }}`
    ```

To set or change variable values in the *parent box* event scripts, follow this syntax with the set command. 

* Sets the value of the variable:

    ```
    `<variable_name> <variable_value>`
    ```

* Sets the value of the variable in the box type variable. This is how you set values for variables in child boxes:

    ```
    elasticbox set `<boxtype_variable_name>.<variable_name> <variable_value>`
    ```

For examples, see the [Set Command](../../Cloud Application Manager/Automating Deployments/cloud-application-manager-commands.md).

### Syntax for System Variables

In addition to variables you create, all boxes deployed through Cloud Application Manager use system variables. They represent Cloud Application Manager assets used for a deployment such as environment or box. They also contain information about the virtual infrastructure such as public, private IP addresses, and the virtual machines or services.

To get values of default deployment variables in parent box event scripts, follow this syntax:

| Variable | Returned value |
|-----------------------------------|------------------|
| `\{{ environment }}` | Name of the environment where the box is deployed like a box deployed to<br/>an environment named Test. |
| `\{{ machine }}` | Name of the virtual infrastructure where Cloud Application Manager runs the script.<br/>It has the eb-XXXXX-1 format. |
| `\{{ instance }}` | ID for the instance in the i-XXXXXX format. |
| `\{{ service }}` | Dynamic ID for type of service used to generate machines and services for the instance. Cloud Application Manager uses this service ID, say eb-XXXXX, to create resources with the provider such as servers, security groups, and so on. |
| `\{{ service.provider_type }}` | Underlying provider type descriptive name the instance has been deployed into. |
| `\{{ addresses }}` | Public and private IP addresses of all instances deployed for a box. |
| `\{{ address.public }}` | Public IP address of the current instance. |
| `\{{ address.private }}`| Gives the private IP address of the current instance. |
| `\{{ box }}` | Name of the parent box deployed. |
| `\{{ folder }}` | Current working directory (CWD) path where Cloud Application Manager executes scripts in the instance.

**Note:** When the instance is provisioned on a service, like AWS RDS, Cloud Application Manager stores deployment information in these variables:

| Variable | Returned value |
|----------|----------------|
| `\{{ address.public }}` | Public IP address of the instance. |
| `\{{ address.private }}` | Private IP address of the instance. |
| `\{{ username }}` | Instance username. |
| `\{{ password }}` | Instance password. |

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at \ProgramData\ElasticBox\Logs\elasticbox-agent.log
