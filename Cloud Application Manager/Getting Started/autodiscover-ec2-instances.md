{{{
"title": "Auto-discover AWS EC2 instances",
"date": "07-30-2018",
"author": "Guillermo Sanchez",
"attachments": [],
"contentIsHTML": false
}}}

### Auto-discover AWS EC2 instances

**In this article:**
* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [When you add AWS as a provider for the first time](#when-you-add-aws-as-a-provider-for-the-first-time)
* [If you have an existing AWS provider in Cloud Application Manager](#if-you-have-an-existing-aws-provider-in-cloud-application-manager)
* [Type of instances you can register](#type-of-instances-you-can-register)
* [Auto-discover and register AWS EC2 instances in Cloud Application Manager](#auto-discover-and-register-aws-ec2-instances-in-cloud-application-manager)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview
Cloud Application Manager can auto-discover your existing AWS EC2 instances that have been provisioned directly using the provider console outside of Cloud Application Manager. With this capability, even if some of your teams are using AWS EC2 Console to provision instances, you can import them into Cloud Application Manager and manage their lifecycle and also view them as part of the Dashboard Cloud Reports. The discovered instances will exist only as an instance. Cloud Application Manager does not create a corresponding Deployment Policy as part of registration process.

### Audience

Users who want to register their AWS EC2 instances into Cloud Application Manager to enable lifecycle management on them.

### Prerequisites

An active Cloud Application Manager account and an existing AWS account with active EC2 instances.

### When you add AWS as a provider for the first time

As soon as you add AWS as providers in your workspace, Cloud Application Manager will auto-discover those instances that exist in AWS and save them in the Unregistered instances tab under the Provider details. You can follow the on-screen instructions to register them in Cloud Application Manager.

### If you have an existing AWS provider in Cloud Application Manager

The next time you click on sync, Cloud Application Manager will auto-discover those instances that exist in AWS EC2 but have not been provisioned using Cloud Application Manager and save them in the Unregistered instances tab under the Provider details. You can follow the on-screen instructions to register them in Cloud Application Manager.

To register AWS EC2 instance, an additional step is required. Cloud Application Manager uses UserData to install the Cloud Application Manager agent on provision time. Since the instance was initially provisioned outside of Cloud Application Manager, users have to execute a script to install the Cloud Application Manager agent.

### Type of instances you can register

You can register the following type of instances into Cloud Application Manager:

1. **EC2 regular instances**: stand-alone EC2 deployed instances.
2. **EC2 CloudFormation instances**: instances deployed as part of a CloudFormation template. Only the EC2 instance will be imported, and when deleted only the instance would be affected, no other resources that might have been deployed by the same Cloud Formation template would be deleted along with the instance.
3. **EC2 instances from an Auto-scaling group or template**: the instances belonging to an Auto Scaling Group or Template will be shown grouped under the Register Instances page and they will be imported as a whole into a single instance that will contain all the related machines. Once properly registered (either providing the certificate for Cloud Application Manager to access the machines and install the agent or when the agent is installed manually), all the machines would be shown in Cloud Application Manager into the instance details page, and all auto-scaling events would be detected and the instance details updated to show the current machines available into the group. If you terminate the instance in Cloud Application Manager, all the machines of the group would be terminated.

### Auto-discover and register AWS EC2 instances in Cloud Application Manager

* Choose an unregistered instance of your provider

![Unregistered Instances](../../images/cloud-application-manager/aws-registerInstance-tuto01.png)

* Start registering

![Register Instance](../../images/cloud-application-manager/aws-registerInstance-tuto02.png)

* Unsuccessful Registration

![Unsuccessful registering](../../images/cloud-application-manager/aws-registerInstance-tuto03.png)

* Go to the instance details

![Detail of unregistered instance](../../images/cloud-application-manager/aws-registerInstance-tuto04.png)

* Get the endpoint address for ssh connection

![Endpoint address](../../images/cloud-application-manager/aws-registerInstance-tuto05.png)

* Use your token key-pair and connect to the instance

![SSH connected](../../images/cloud-application-manager/aws-registerInstance-tuto06.png)

* Copy the script for manual creation of the agent

![Copy script](../../images/cloud-application-manager/aws-registerInstance-tuto07.png)

* Use your favorite editor to create the shell script and fix execution permission

![Create shell script](../../images/cloud-application-manager/aws-registerInstance-tuto08.png)

* Start agent

![Start elasticbox agent](../../images/cloud-application-manager/aws-registerInstance-tuto09.png)

* The instance is now successfully registered

![Start elasticbox agent](../../images/cloud-application-manager/aws-registerInstance-tuto10.png)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
