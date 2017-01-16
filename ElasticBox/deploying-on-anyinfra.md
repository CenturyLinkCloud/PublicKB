{{{ "title": "Deploying to Any Infrastructure",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Deploying to Any Infrastructure

**In this article:**
* Overview
* How to deploy with the ElasticBox agent
* ElasticBox agent command

### Overview

You can launch boxes on any infrastructure by running the ElasticBox agent. The agent is required to execute box variables and scripts and run lifecycle operations. To install the agent, you run a Bash command. The infrastructure can be a virtual machine in your laptop, physical machines on premise, a datacenter, or any cloud provider environment. We support running it on Linux distributions Debian 6 and 7, Ubuntu 12.04 and 14.04, RedHat 6.x, CentOS 6.x, and any AWS Linux AMI. No matter where you choose to deploy, boxes launch consistently as they would on any cloud provider.

![deploy-via-myserver-1.png](../images/ElasticBox/deploy-via-myserver-1.png)

### How to Deploy with the ElasticBox Agent

Run the ElasticBox agent on the Linux machine where you want to launch the box. Once the box is launched, sign in to ElasticBox and access the instance from the Instances to edit its box makeup, debug, or manage its lifecycle. Follow these steps to launch a box on your infrastructure.

**Before You Begin**

* Make sure you have a box configured and ready to launch.
* Get the target infrastructure where you want to launch your box up and running first. This can be any Linux machine running a supported image.

**Steps**

1. SSH into the machine to run the agent. Here as an example, we SSH into a Linux machine running Ubuntu 12.04 in AWS.

`ssh -i /Users/mrina/Documents/AWS_Private_PublicKeyPairs/AWSEC2_KeyPair/useast-mrina.pem ec2-user@54.163.174.41`

2. Launch an instance of a box using the the ElasticBox agent. In this example, we launch an instance of the public [MongoDB box](./sample-deploy-mongodb.md) in AWS.

`curl -sLk https://ebx.co | sudo bash -s -- -b "MongoDB Server" -n "test" -V username=admin123 -V password=password12345 -t 314a36ad-74b6-4205-9e33-eac9970e4a1b`

### ElasticBox Agent Command

Use cURL to download and run the agent with piped parameters.

**Syntax**

`curl -sLk https://ebx.co | sudo bash -s -- -b "<box name or ID>" -n "<environment nameID>" -t <your_authentication_tokenID> -V <variable_name="variable value"ID> [-o "ID<owner IDID>"] [-d] [-H] [h] [f]
`
**Parameters**

| **Parameter**  |  **Description** |
|----------|:-----|
| -b | Specify a box by name or ID. If you give the name, the latest version of the box is launched. If you give the ID that specific version of the box is launched. You can get the ID from the box URL. |
| -n | Give a name to identify the environment where you launch the box, such as dev or test. If you don’t provide one, ElasticBox uses the box name or ID. |
| -t | Enter your [authentication token](./admin-access.md), which you can get from your account in the ElasticBox website. If you run the agent command without this parameter, you’re prompted to enter it later. |
| -V | If a box needs values for certain variables before launching, you can pass each in this format: -V variable_name1=variable_value -V variable_name2=variable_value |
| -o | Optionally, specify in lowercase the box owner ID to tag an instance with this information. You can get the ID when you try to share the box with an owner. The owner can be an account or a workspace. The owner ID is visible within parentheses next to the display name. |
| -d | Optionally, see all the values in each step of the shell script as it executes the box you specified in the target environment. |
| -h| Get help and usage examples with this option. |
| -H | Specify the hostname vanity URL if using the appliance.
| -f | Force the agent to install. If an ElasticBox agent is previously running on the machine, the force flag kills and reinstalls the agent. |

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
