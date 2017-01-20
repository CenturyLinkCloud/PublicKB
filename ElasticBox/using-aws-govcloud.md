{{{
"title": "Using AWS GovCloud",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Using AWS GovCloud

AWS GovCloud is an isolated region designed to handle workloads of sensitive data. Why spin up machines and SSH into them to run workloads manually, when you can automate and deploy faster using [ElasticBox](//www.ctl.io/guides/)?

AWS GovCloud is available only by request. Contact [support](mailto:support@elasticbox.com) to enable it for your organization.

**In this article:**
* Connect to AWS GovCloud from ElasticBox
* Add Custom AMIs
* Deploy to AWS GovCloud from ElasticBox

### Connect to AWS GovCloud from ElasticBox

Access to AWS GovCloud requires a [special signup process](http://docs.aws.amazon.com/govcloud-us/latest/UserGuide/getting-set-up.html). When you have a GovCloud account, connect to it in ElasticBox with a role based ARN following the same steps as you would for a regular AWS account.

[Step 1. Delegate a role for ElasticBox in your AWS GovCloud account to allow third-party API access.](./using-your-aws-account.md)

Enter the following 3rd party IAM information for ElasticBox:
* Account ID: 948203093918
* External ID: ebx
* Require MFA: Leave unselected

[Step 2. Share the role’s Amazon Resource Name (ARN) in ElasticBox.](./using-your-aws-account.md)

### Deploy to AWS GovCloud from ElasticBox

Select the box where you configured a workload to run remotely and choose AWS deployment settings to launch in a VM or service in the GovCloud region.

ElasticBox provisions machines in EC2 or a VPC with deployment settings you pick. These settings include AMI, instance type, key pairs, availability zone, security groups, Elastic IP, block storage, load balancing, and auto scaling. After provisioning the VM or service, ElasticBox deploys the box scripts to install, configure, and start the workload.

Deploy to any of the services in the AWS GovCloud region.

* [EC2 (Linux and Windows)](./using-your-aws-account.md)
* [AWS RDS](./using-your-aws-account.md)
* [AWS S3](./using-your-aws-account.md)
* [AWS DynamoDB](./using-your-aws-account.md)
* [AWS CloudFormation](./cloudformation-box.md)

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
