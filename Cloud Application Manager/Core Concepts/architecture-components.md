{{{
"title": "Architecture components",
"date": "05-22-2019",
"author": "Diego Sanjuan",
"attachments": [],
"contentIsHTML": false,
"keywords": ["cam", "cloud application manager", "architecture", "components", "agents", "websockets", "workflow", "services"]
}}}


**In this article:**


* [Overview](#overview)
* [Audience](#audience)
* [CAM Agents](#cam-agents)
* [Websockets](#websockets)
* [API Services](#api-services)
* [Orchestration Workflow](#orchestration-workflow)
* [Connectivity and Required Firewall Rules](#connectivity-and-required-firewall-rules)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)


### Overview


This article is meant to assist users of Cloud Application Manager to learn about its components and interaction as follows:

* **CAM agents** - functions, interactions, installation, and requirements
* **Websockets** - functions, interactions
* API Services - functions, interactions
* Orchestration Workflow - functions, interactions
* Connectivity and Required Firewall Rules


### Audience


All Cloud Application Manager users who want to learn about Cloud Application Manager component's architecture and its connectivity requirements.


![Cloud Application Manager Components](../../images/cloud-application-manager/components.png)


### CAM Agents


Are responsible of execute event scripts in virtual machines deployed using script boxes and return their execution results. Also provide to backend network information about virtual machine regularly to inform user about virtual machine availability.

Agent is bootstrapped and installed, in each virtual machine registered in CAM, making use of diverse execution mechanisms provided by public and private cloud providers. i.e. in AWS cloud init is used for download and install it.

Cloud Application Manager agent is written in python and it requires in linux machines to have python installed, and at least version 2.7.x to work properly.

Agents require outbound connectivity to [https://cam.ctl.io](https://cam.ctl.io) to be able to call back and communicate results and request more work to be done on its virtual machine.

Cloud Application Manager agent supports proxy configuration to call back when it's deployed in constrained/secured environments.


### Websockets


Cloud Application Manager uses websockets protocol for agent's communication and UI data interchange with Cloud Application Manager backend. They support real time notifications and data updates required by Cloud Application Manager's UI.


### API Services


Our services provide necessary [CAM API REST](https://www.ctl.io/api-docs/cam/) endpoints which are used by Cloud Application Manager UI when requesting operations and retrieving data items. These endpoints are also used by Cloud Application Manager command line tool [ebcli](../Tutorials/ebcli-tutorial.md) to list, provision and manage the lifecycle of your workloads based on box configuration.


### Orchestration Workflow


We have asynchronous and persistent long-running workflows which are responsible for all cloud provider provisioning and orchestration to fulfill user requests and provide an updated work plan for CAM agents. It also takes care of the provider's synchronization process and recurrent or scheduled tasks.


### Connectivity and required firewall rules


Allow Income traffic to 443 (https) port (OPEN) to your Cloud Application Manager Data Center Edition (appliance) for UI, API calls and CAM agents requests

Allow Outcome traffic to 443 (https) port from virtual machines network or its VPC so CAM agents are able to communicate with Cloud Application Manager SaaS or onpremises Appliance

Also, if you are using private cloud providers, take into account that to use some of them Cloud Application Manager requires more ports to be open so it could communicate with their API and metadata endpoints to request new deployments or retrieve metadata and configuration parameters:

|  PROVIDER     |  PORTS                                                                |
|---------------|-----------------------------------------------------------------------|
| VMWARE vCenter| INCOME ports to be OPEN: 443 ssl, 8085                                |
| OpenStack     | INCOME ports to be OPEN: 443 ssl, 5000, 35357, 8774, 8776, 9292, 8004 |


### Contacting Cloud Application Manager Support


We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:cloudsupport@centurylink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at C:\ProgramData\ElasticBox\Logs\elasticbox-agent.log
