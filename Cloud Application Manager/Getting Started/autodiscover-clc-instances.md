{{{
"title": "Auto-discover CenturyLinkCloud instances",
"date": "02-15-2016",
"author": "Ranga Chakravarthula",
"attachments": [],
"contentIsHTML": false
}}}

### Auto-discover CenturyLink Cloud VM instances

Cloud Application Manager can auto-discover your existing CenturyLink Cloud VM instances that have been provisioned directly using the provider console outside of Cloud Application Manager. With this capability, even if some of your teams are using CenturyLink Cloud Console to provision instances, you can import them into Cloud Application Manager and manage their lifecycle and also view them as part of the Admin Console Cloud Reports. The discovered instances will exist only as an instance. Cloud Application Manager does not create a corresponding Deployment Policy as part of registration process.

### When you add CenturyLink Cloud as a provider for the first time

As soon as you add CenturyLink Cloud as a provider in your workspace, Cloud Application Manager will auto-discover those instances that exist in CenturyLink Cloud and save them in the Unregistered instances tab under the Provider details. You can follow the on-screen instructions to register them in Cloud Application Manager.

### If you have existing CenturyLink Cloud provider in Cloud Application Manager

The next time you click on sync, Cloud Application Manager will auto-discover those instances that exist in CenturyLink Cloud but have not been provisioned using Cloud Application Manager and save them in the Unregistered instances tab under the Provider details. You can follow the on-screen instructions to register them in Cloud Application Manager.

### Auto-discover and register CenturyLink Cloud Server instances in Cloud Application Manager

![Unregistered Instances](../../images/cloud-application-manager/clc-provider-unregisteredinstances.png)

![Register Instance](../../images/cloud-application-manager/clc-provider-registerInstance.png)

![Register Instance Successful](../../images/cloud-application-manager/clc-provider-successfullyregistered.png)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
