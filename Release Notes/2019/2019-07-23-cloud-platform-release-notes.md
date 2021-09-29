{{{
"title": "Cloud Platform - Release Notes: July 23, 2019",
"date": "07-23-2019",
"author": "Evan McNeill",
"keywords":["lumen", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (2)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Support for AWS Master Account to authenticate API calls

Cloud Application Manager Dedicated Edition now supports leveraging a custom Master Account as an authorization mechanism for all AWS API calls the appliance performs. In addition to the currently supported EC2 Instance Role for applications running in EC2 instances, this Master Account adds similar privileges for Cloud Application Manager appliances deployed anywhere, simplifying credential management and increasing security. Once the master account is set through the setup console, you will only be able to configure new AWS providers using an IAM Role. For more information, refer to [Cloud Application Manager Dedicated Edition with Master Account](https://www.ctl.io/knowledge-base/archive/camd-with-aws-master-account/)

#### [Managed Services Anywhere](https://www.ctl.io/managed-services-anywhere/)

##### New MS Teams Action type

We are pleased to announce the release of a new action type to the list of available Actions into the Cloud Application Manager Monitoring Site. The Cloud Application Manager Monitoring system now supports integration with MS Teams.

Collaboration software suites are becoming more leveraged by DevOps organizations for quick and easy notifications by monitoring systems. Now, along with Slack, MS Teams can receive notifications of events that occur within an MSA-enabled environment.

As with all Actions, the MS Teams Action type can be applied at all scope levels: Organization, Cost Center, Workspace, Provider and an individual agent.

### Announcements (1)

#### [Lumen Cloud](https://www.ctl.io/cloud-platform/)

##### Single Sign On for all Lumen products

This month we are deploying a new security feature. Single Sign On (SSO), will provide enhanced security capabilities and enable a single login for all your Lumen products.

Once released, you can opt into a one-time setup to create a new Master Account using the "Sign in with Lumen Master Account" button on the login page. You will then receive a one-time prompt to provide credentials to link your services to your master account. This will allow you to navigate between services without re-authenticating going forward.

Other security improvements include optional multi-factor authentication through your smart phone (soft token), and the ability to set up multiple security questions for account validation and retrieval purposes. You'll continue to see enhancements as they are released throughout the year.
