{{{
"title": "Cloud Platform - Release Notes: December 3, 2019",
"date": "12-3-2019",
"author": "Anshul Arora",
"keywords":["centurylink", "cam", "alm", "optimization","cpc"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (4)

#### [CenturyLink Private Cloud on VMware Cloud Foundation](https://www.ctl.io/centurylink-private-cloud-on-vmware-cloud-foundation/) (CPC on vCF)

##### Branding Update
We are ready to roll out our new branding for the HTML5 interface for vCD. This will be included with all new builds and added to our upgrade process for existing customers.

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### Billing simplification

As a result of the billing simplification initiative, Cloud Application Manager is removing the invoice line-items regarding past-month updates. To avoid these updates, we will bill all the Cloud Application Manager vendor related usages in arrears, so that your December invoice will only include updates from October usage, and the actual Cloud Application Manager November usage will be charged on your January 2020 invoice. Cloud Application Manager billing usage history will reflect the changes to the invoice and has removed the billing cycle dropdown as a consequence of this billing simplification.

##### New provider type for Compute instances

Cloud Application Manager has added the support for the Compute instances provider type. Any owned infrastructure can be brought to Cloud Application Manager by installing the Cloud Application Manager agent and registering it to Compute Instances Provider using a self-register code snippet. This will enable the lifecycle of the instance through Cloud Application Manager like with any other natively-deployed instance. For more information see [Using Compute Instances](../../Cloud Application Manager/Deploying Anywhere/using-compute-instances.md)

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are: "AWS::GameLift::MatchmakingConfiguration", "AWS::GameLift::MatchmakingRuleSet", "AWS::GameLift::Queue" and "AWS::GameLift::Script". Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.

