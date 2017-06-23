{{{
"title": "Using AWS GovCloud",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Using AWS GovCloud

AWS GovCloud is an isolated region designed to handle workloads of sensitive data. Why spin up machines and SSH into them to run workloads manually, when you can automate and deploy faster using [Cloud Application Manager](//www.ctl.io/guides/#cloud-application-manager)?

AWS GovCloud is available only by request. Contact [support](mailto:cloudsupport@centurylink.com) to enable it for your organization.

**In this article:**
* Connect to AWS GovCloud from Cloud Application Manager
* Add Custom AMIs
* Deploy to AWS GovCloud from Cloud Application Manager

### Connect to AWS GovCloud from Cloud Application Manager

Access to AWS GovCloud requires a [special signup process](http://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-set-up.html). When you have a GovCloud account, connect to it in Cloud Application Manager with a role based ARN following the same steps as you would for a regular AWS account.

[Step 1. Delegate a role for Cloud Application Manager in your AWS GovCloud account to allow third-party API access.](./using-your-aws-account.md)

Enter the following 3rd party IAM information for Cloud Application Manager:
* Account ID: 948203093918
* External ID: ebx
* Require MFA: Leave unselected

[Step 2. Share the role’s Amazon Resource Name (ARN) in Cloud Application Manager.](./using-your-aws-account.md)

### Deploy to AWS GovCloud from Cloud Application Manager

Select the box where you configured a workload to run remotely and choose AWS deployment settings to launch in a VM or service in the GovCloud region.

Cloud Application Manager provisions machines in EC2 or a VPC with deployment settings you pick. These settings include AMI, instance type, key pairs, availability zone, security groups, Elastic IP, block storage, load balancing, and auto scaling. After provisioning the VM or service, Cloud Application Manager deploys the box scripts to install, configure, and start the workload.

Deploy to any of the services in the AWS GovCloud region.

* [EC2 (Linux and Windows)](./using-your-aws-account.md)
* [AWS CloudFormation](../Automating Deployments/template-box.md)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:cloudsupport@centurylink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
