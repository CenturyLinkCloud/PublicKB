{{{
"title": "Using Compute Instances",
"date": "11-05-2019",
"author": "Sharon Wang",
"attachments": [],
"contentIsHTML": false,
"keywords": ["cam", "cloud application manager", "self register", "byoi", "bring your own infrastructure", "compute instances", "physical provider"]
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Create a new Compute Instances Provider](#create-a-new-compute-instances-provider)
* [Register a Server into the Compute Instances provider](#register-a-server-into-the-compute-instances-provider)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article is meant to assist users of Cloud Application Manager trying to register their stand-alone/physical machines to CAM. You can bring your own infrastructure to Cloud Application Manager by installing the Cloud Application Manager agent and register it to Compute Instances Provider. This will enable lifecycle of the instance through Cloud Application Manager like with any other natively-deployed instance.

### Audience

All users of Cloud Application Manager who wants to register their stand-alone machines to Compute Instances Provider.

### Prerequisites

* An active **Cloud Application Manager** account
* Any infrastructure capable of running Cloud Application Manager Agent.

### Create a new Compute Instances Provider

To create a new provider, select **Compute Instances** from the Provider list and give it a name, then click on **Save**

![New compute instances provider](../../images/cloud-application-manager/deploying-anywhere/compute-instances/compute_instances_1.png)

**Note**: Unlike other provider types, this one does not require any synchronization process and it does not support deployment policies either, since there is no direct deployment support on it.

### Register a Server into the Compute Instances provider

You can launch boxes on any infrastructure by running the Cloud Application Manager agent. The agent is required to execute scripts, manage box variables and run lifecycle operations. Once the provider is created, users can register VMs or physical machines to this Provider by using the code snippet provided by clicking **Self-Register Scripts**

![Self-Register Scripts button](../../images/cloud-application-manager/deploying-anywhere/compute-instances/compute_instances_2.png)

There are 2 scripts for Windows and Linux OS. In this article, we use Windows server as an example:

![Self-Register Scripts](../../images/cloud-application-manager/deploying-anywhere/compute-instances/compute_instances_3.png)

**Note**: If the proxy is specified, the snippet with be updated dynamically with its values to allow the machine to contact back to Cloud Application Manager through it.

Copy the script and run on the Windows server we have on CLC to trigger the self-register process:

![Windows PowerShell script](../../images/cloud-application-manager/deploying-anywhere/compute-instances/compute_instances_4.png)

The provider activity log will show an activity when an instance is asking to be registered in the provider. Once the script is completed, you can see the server registered:

![The new instance registered in CAM](../../images/cloud-application-manager/deploying-anywhere/compute-instances/compute_instances_5.png)

If you click on the instance, the instance details page will be displayed:

![The new instance registered details](../../images/cloud-application-manager/deploying-anywhere/compute-instances/compute_instances_6.png)

To learn more about Cloud application manager Self Register Instances, please review the [Self Register Instances](../Getting Started/self-register-instances.md) article.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of an error registering an instance, share the instance to a workspace that your organization and Cloud Application Manager support group can access and attach the logs.

* Linux: SSH into the instance and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at \ProgramData\ElasticBox\Logs\elasticbox-agent.log
If you have additional questions, please [contact Cloud Application Manager Support](mailto:incident@CenturyLink.com)
