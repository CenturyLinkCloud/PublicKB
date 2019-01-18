{{{
"title": "Boxes",
"date": "12-28-2018",
"author": "Julio Castanar",
"keywords": ["cam","alm","boxes", "box"],
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Boxes](#boxes)
* [Understanding Box Basics](#understanding-box-basics)
* [Box management](#box-management)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article is meant to assist Cloud Application Manager customers who want to create and manage boxes.

### Audience

Cloud Application Manager Users using Application Lifecycle Management (ALM) features.

### Prerequisites

* Access to [Applications site](https://cam.ctl.io/#/boxes) (Application Lifecycle Management module) of Cloud Application Manager as an authorized user of an active Cloud Application Manager account.

### Boxes

Boxes are the templates that store application automation. An instance is a box you install on virtual infrastructure provisioned to a public, private cloud provider, or your own infrastructure. Take a [quick tour](https://www.ctl.io/guides/) to understand the layout of boxes and instances in Cloud Application Manager.

Boxes contain scripts, variables, and metadata to automate processes when instantiated on cloud infrastructure. Stitched together, boxes model complex processes like deploying or upgrading multi-tier enterprise scale applications.

So how do boxes work?. A typical application stack may consist of multiple boxes, each one modeling a step of the application’s install. For example, one might model the install of runtime requirements (such as PHP libraries). Another might model the install of a web server (such as Apache). And a third might model connecting to a source control repository (such as Git), pulling the latest code, and installing it on the virtual server. When stacked and instantiated these three boxes install an application. At the same time, each box is independent, reusable and can be consumed by other applications.

### Understanding Box Basics

#### New Box

To create a new box, click **New**. Select a box type to match your automation:

* [Application](../Automating Deployments/application-box.md) - Configure several boxes to deploy an application with a single click.
* [Script](../Automating Deployments/script-box.md) - Automate using Bash, PowerShell, Salt, Ansible, Puppet, or Chef.
* [Container](../Automating Deployments/docker-container-service.md) - Automate using container technology like Docker.
* [Template](../Automating Deployments/template-box.md) - Automate using AWS CloudFormation templates, ARM templates or Terraform templates.
* [Deployment Policy](../Automating Deployments/deploymentpolicy-box.md) - Select and share infrastructure resources, networking, and more from a cloud provider.

Fill mandatory fields (with an *) and define some basic metadata described below.

#### Box metadata

| Metadata | Box Type | What it Means |
|--------------|--------------|---------------------|
| Name,<br/>Description,<br/>Icon | All | Give it a name and optionally a description and an icon. |
| Requirements | Script,<br/> Template,<br/> Container | It’s good practice to tag the runtime that the box requires to deploy. Cloud Application Manager auto suggests tags like Linux, Ubuntu, Java and so on. When ready to launch the box, you are presented with deployment policies that match the requirements. These deployment policies provide the right infrastructure or services the box needs to deploy.<br/>**Note:** In CloudFormation boxes, the tags help you to look for binding instances. |
| Automatic<br/>Updates | Script,<br/>Template,<br/>Container | Select the level of updates to automatically apply to instances you launch of a box version:<br/>+ **Off** - It’s turned off by default.<br/>+ **All Updates** - Applies all changes.<br/>+ **Minor & Patch Updates** - Applies minor and patch changes to the version deployed.<br/>+ **Patch Updates** - Applies only the patch changes to the version deployed. |
| Provider | Deployment<br/>Policy | Select the cloud provider registered in Cloud Application Manager for which you will carve out infrastructrure resources in the policy. |
| Claims | Deployment<br/>Policy | Tag the services and infrastructure that a policy provides like Linux, Ubuntu 12.04, load balancing, and so on for deployments. Add claims so that the boxes with matching requirements can successfully deploy using the right policy. |
| Instance Lifespan | Deployment<br/>Policy | Determines how to [schedule instances](../Deploying Anywhere/deploying-managing-instances.md#scheduling-instances) for automatic **expiration** |

<br/><br/>

### Box management
Once you create a box, you can configure and manage it in this panel:<br/>

![Box management page core concepts](../../images/cloud-application-manager/core-concepts-boxes1.png)


#### Box Functions
Box Functions (marked with 1 in the figure) execute several commands for the Box

| Function | Description |
|------------|----------------|
| Deploy | [Launch a new instance](../Deploying Anywhere/deploying-managing-instances.md) of the box draft with this option. This lets you select a specific deployment policy to launch on a cloud provider. |
| Gear Menu | From here, you can edit basic metadata of the box, share or delete it.<br/>**Edit Details** - Allows box basic properties edition.<br/> **Clone** - Duplicates current box with same basic configuration.<br/>**Share** - Invite team members to [collaborate](workspaces-and-collaboration.md) and improve the configuration or just let them deploy the box.<br/>**Delete Box** - Removes current Box |

#### Box Sections

Box Sections (marked with 2 in the figure) display several configurations of the Box

| Section | Description |
|------------|----------------|
| **Overview** | Get detailed information about your box. |
| **Code** | Automate how a piece of software deploys in the virtual environment by parameterizing with [variables](../Automating Deployments/parameterizing-boxes-with-variables.md) and [events](../Automating Deployments/start-stop-and-upgrade-boxes.md). |
| **Versions** | Keep track deployment configuration changes with the help of [versioning](../Automating Deployments/version-control.md). Versions let you consume different configurations of the same box in multiple deployments. From this tab, you can create a new version, see a diff of what changed, or restore a version as the box draft. |


### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at \ProgramData\ElasticBox\Logs\elasticbox-agent.log
