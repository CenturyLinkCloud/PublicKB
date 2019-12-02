{{{
"title": "Using ebcli",
"date": "05-20-2019",
"author": "Diego Sanjuan",
"attachments": [],
"keywords": ["cam", "alm", "ebcli", "tool", "command-line", "automation", "terminal", "manage"],
"sticky": true,
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Installation of ebcli command line tool](#installation-of-ebcli-command-line-tool)
* [Login into your Cloud Application Manager account with ebcli](#login-into-your-cloud-application-manager-account-with-ebcli)
* [Show available ebcli commands](#show-available-ebcli-commands)
* [Box commands using ebcli](#box-commands-using-ebcli)
* [Instance lifecycle using ebcli](#instance-lifecycle-using-ebcli)
* [ECS Image management using ebcli](#ecs-image-management-using-ebcli)
* [Workspaces list using ebcli](#workspaces-list-using-ebcli)
* [Delete Resources using ebcli](#delete-resources-using-ebcli)
* [Logout from your Cloud Application Manager account with ebcli](#logout-from-your-cloud-application-manager-account-with-ebcli)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This tutorial is meant to assist users of Cloud Application Manager to learn how to use [ebcli](https://pypi.python.org/pypi/ebcli) - our command line tool- to control their Cloud Application Manager account as follows:

* For **boxes** - how to deploy, export, import as version or as a draft, etc using ebcli.
* For **instances** - how to reconfigure, reinstall, shutdown, poweron, export, etc using ebcli.
* For **ECS images** - how to manage them using ebcli.
* For **workspaces** - how to list them using ebcli.

ebcli calls Cloud Application Manager APIs in the backend to list, provision and manage the lifecycle of your workloads based on the box configuration.

### Audience

All Cloud Application Manager users who want to control their Cloud Application Manager account using `ebcli` - command line tool.

### Prerequisites

* Access to Cloud Application Manager [Site](https://cam.ctl.io/#/login) or to an on-premises Cloud Application Manager Data Center Edition (CAM appliance).
* The user must have an existing account to login into using username and password or his preferred authentication mechanism.

### Installation of ebcli command line tool

Before you start using `ebcli`, you need to install it using `pip` which is a package manager for Python packages, or modules if you like.

If you don't have `pip` installed. Please follow this guide to install it into your computer: https://pip.pypa.io/en/stable/installing/

**Terminal Command**

Open a terminal in your computer and execute the installation command:

```
pip install ebcli
```

When the installation process ends pip should have installed ebcli and all of its required dependencies.

### Login into your Cloud Application Manager account with ebcli

Before you can control your Cloud Application Manager account with ebcli, you need to connect your account in Cloud Application Manager with ebcli.

The ebcli needs a token to login into your Cloud Application Manager account.

**Steps to create a token**

* Open https://cam.ctl.io if you are using SaaS or https://YOUR_APPLIANCE_FQDN if you are using on premises edition of Cloud Application Manager
* Login with your username and password or your preferred authentication mechanism
* Click on your user name menu (at top right corner of CAM user interface)
* Click on 'Authentication Tokens'
* Write a descriptive name for your token, i.e. ebcli
* Click on 'Create Token'
* Click on clipboard buttom at right of your token to copy it

**Terminal Command**

Open a terminal in your computer and execute the login command:

```
ebcli login
```

You will be prompt for introduccing your 'Authentication Token:', just paste your token, and hit Enter.

Now your computer will ask your keyring password to store your Cloud Application Manager token safely in your keyring.

### Show available ebcli commands

**Terminal Command**

Open a terminal in your computer and execute the login command:

```
ebcli
```

ebcli will show usage help like this one:

```
usage: ebcli [-h] [--url URL] [--token TOKEN] [--debug] [--verbose] [-j]
             {boxes,build,delete,deploy,get,export,export-instance,import,instances,login,logout,set,poweron,reconfigure,reinstall,shutdown,terminate,workspaces}
             ...
ebcli: error: too few arguments
```

**General Parameters**

| Get Boxes Option | Description |
|-------------------|-------------|
| --url | By default it's https://cam.ctl.io but you can use this to specify your APPLIANCE FQDN. |
| –-token | You can use it to specify your token in every command if you don't want to store it into your keyring. |
| –-debug | Show debug information to provide detailed traces to support in case of issues. |
| –-verbose | Show detailed information of operations and api calls requested to Cloud Operation Manager. |

### Box commands using ebcli

#### Get boxes

Use ebcli to list your boxes.

**Terminal Command**

```
ebcli boxes [-f [-f [<FIELD> [<FIELD> ...]]] [-r [<REQUIREMENT> [<REQUIREMENT> ...]]] [-w “<WORKSPACE ID>”]
```

**Parameters**

| Get Boxes Option | Description |
|-------------------|-------------|
| -f | Field or Fields you want to be listed. |
| –r | Requirements Tags which you want to use to filter your boxes. i.e. ubuntu |
| –w | Workspace which contains the boxes you want to list. |

#### Export a Box

Use the ebcli to export a box from Cloud Application Manager into JSON and text files to be able to import it after.

**Terminal Command**

```
ebcli export [--boxes-path <BOXES_PATH>] [-r] ”<box ID>”
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| –-boxes-path | Path where the boxes will be exported. |
| -r | Recursively export box and inner boxes. |

#### Import a Box

Use the ebcli to import a box from its JSON and text files into Cloud Application Manager or your appliance.

**Terminal Command**

```
ebcli import [--boxes-path <BOXES_PATH>] [-w <WORKSPACE_ID>] [-m <COMMENT>] [--image <IMAGE>] [--as-draft] box-name
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| –-boxes-path | Path where the boxes are located. |
| -w | Workspace id where the box will be imported. |
| –m | Description of the version will be created. i.e. 'Update requirements'. |
| –-image | Name of the base image to be used. i.e. ubuntu:14.04 or Centos. |
| –-as-draft | Instead of create a version the box will be imported as draft of the box. |

#### Deploy an application box

Use the ebcli to deploy an application box in your Cloud Application Manager or your appliance account.

**Terminal Command**

```
ebcli deploy [-w <WORKSPACE_ID>] [-t [<TAG> [<TAG> ...]]] [-c [<CLAIM> [<CLAIM> ...]]] input
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| -w | Workspace id where the box will be imported |
| –t | Tag or Tags which will mark and isolate your application instances and bindings. i.e. 'production us-east-1' |
| –c | Claims to select the correct deployment policies to be used by instances. i.e. 'ubuntu us-east-1' |
| –input | Application's JSON document to deploy |

### Instance lifecycle using ebcli

#### Get instances

Use ebcli to list your instances.

**Terminal Command**

```
ebcli instances [-f [<FIELD> [<FIELD> ...]]] [-t [<TAG> [<TAG> ...]]] [-w “<WORKSPACE ID>”]
```

**Parameters**

| Get Boxes Option | Description |
|-------------------|-------------|
| -f | Field or Fields you want to be listed. |
| –t | Tag or Tags used to filter your instances. i.e. 'production us-east-1' |
| –w | Workspace which contains the instances you want to list. |

#### Reconfigure an Instance

Use ebcli to execute reconfigure operation on an instance which is powered on.

**Terminal Command**

```
ebcli reconfigure ”<instance-id>”
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| instance-id | ID of the Instance which boxes you want to reconfigure. |

#### Reinstall an Instance

Use ebcli to execute reinstall operation on an instance which is powered on.

**Terminal Command**

```
ebcli reinstall ”<instance-id>”
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| instance-id | ID of Instance you want to power on. |

#### Terminate an Instance

Use ebcli to execute terminate operation on an instance which is provisioned.

**WARNING - This is a destructive operation**

***You can't connect to, restart or recover an instance after you've terminated it.***

Before you terminate the instance, verify that you won't lose any data by checking that your volumes won't be deleted on termination and that you've copied any data that you need from your instance volumes to a persistent storage service.

When an instance terminates, the data on any instance store and volumes associated with that instance are deleted.

When you terminate an instance, the whole history of the instance is kept in Cloud Application Manager and you can use it as a reference for other instances, to copy the variables or to clone the instance. The instance in your cloud provider is terminated or deprovisioned.

After you terminate an instance, it remains visible in your cloud provider console for a short period of time, and then the entry is automatically deleted. After an instance is terminated, resources such as tags and volumes are gradually disassociated from the instance.

**Terminal Command**

```
ebcli terminate ”<instance-id>”
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| instance-id | ID of Instance you want to terminate. |

#### Poweron an Instance

Use ebcli to execute reinstall operation on an instance which is shutdown.

**Terminal Command**

```
ebcli reinstall ”<instance-id>”
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| instance-id | ID of Instance you want to reinstall. |

#### Shutdown an Instance

Use ebcli to execute shutdown operation on an instance which is powered on.

**Terminal Command**

```
ebcli shutdown ”<instance-id>”
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| instance-id | ID of Instance which boxes you want to shutdown. |

#### Export Instance's Boxes

Use the ebcli to export a box from Cloud Application Manager into JSON and text files to be able to import it after.

**Terminal Command**

```
ebcli export-instance [--boxes-path <BOXES_PATH>] [-r] ”<instance-id>”
```

**Parameters**

| Option | Description |
|-------------------|-------------|
| –-boxes-path | Path where the boxes will be exported. |
| -r | Recursively export outer box and inner boxes. |
| instance-id | ID of the Instance which boxes you want to export. |

### ECS Image Lifecycle using ebcli

#### Build the Image

Use the ebcli to build the image.

**Terminal Command**

```
ebcli build ”<box ID>” [-t “<image name>”] [--image <image name>] [--boxes-path <boxes path>]
```

**Parameters**

| Deployment Option | Description |
|-------------------|-------------|
| -t | Name of the image to be build. |
| –-image | Name of the base image to be used. E.g. ubuntu:14.04 or Centos. |
| –-boxes-path | Path where the boxes are located. |

#### Push the Image

Use the docker client to push the image to your favorite docker registry. If you have questions about this step, check out the official Docker documentation about images.

**Terminal Command**

```
docker push “<image name>”
```

#### Post the Image

Use the ebcli to post the image to your box

**Terminal Command**

```
ebcli post “<docker image>”
```

### Workspaces list using ebcli

#### Get workspaces

Use ebcli to list your workspaces.

**Terminal Command**

```
ebcli workspaces [-f [<FIELD> [<FIELD> ...]]]
```

**Parameters**

| Get Boxes Option | Description |
|-------------------|-------------|
| -f | Field or Fields you want to be listed. |

### Delete Resources using ebcli

#### Delete instances, boxes, or workspaces

Use ebcli to delete your resources.

**Terminal Command**

```
ebcli delete (-b BOX_ID | -i INSTANCE_ID | -w WORKSPACE_ID)
```

**Parameters**

| Get Boxes Option | Description |
|-------------------|-------------|
| box-id | ID of box you want to delete. |
| instance-id | ID of instance you want to delete. |
| workspace-id | ID of workspace you want to delete. |

### Logout your Cloud Application Manager account with ebcli

#### Remove token from your computer's keyring

Use ebcli to logout

**Terminal Command**

```
ebcli logout
```

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:cloudsupport@centurylink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at C:\ProgramData\ElasticBox\Logs\elasticbox-agent.log
