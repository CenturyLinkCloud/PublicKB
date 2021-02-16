{{{
"title": "Cloud Platform - Release Notes: May 09, 2017",
"date": "5-09-2017",
"author": "Matt Farrell",
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (2)

* __Network Exchange__

Network Exchange, which provides self-service, automated interconnection for application components within Lumen Hybrid IT environments, has been released into production in a limited availability. It is available to serve use cases that had previously been addressed with Lumen Cloud-Network Services (CNS) in a limited set of six data centers - LO1, TR1, NJ2, DC2, CH3 and SC8. For more information on this new product, please visit the [product page](https://www.ctl.io/network-exchange) and visit the [Network Exchange KB](https://www.ctl.io/knowledge-base/network/network-exchange/), including the Getting Started Guide.

* __Status.ctl.io__

Lumen Cloud Status Chrome Extension: Real-time updates of status.ctl.io

Status.ctl.io provides the status of the Lumen Cloud platform and the available services. You can use this extension to see the real-time, overall status for the platform and it's services. The icon will show a blue dot if there is planned maintenance in progress, or an orange or red icon if a service is temporarily disrupted. Hovering over the icon will give you a brief description of the current status. To get more detailed information, click on the icon to go to the front page of the status application!

https://chrome.google.com/webstore/detail/centurylink-cloud-status/abhpdblgadmelnffnnfddppakgbfimmj?hl=en

### Enhancements (1)

* __Cloud Application Manager__

We would like to share with you what’s new in our next release.

Application Lifecycle Management

- Auto discover brownfield instances in Microsoft Azure

- Starting this release, Cloud Application Manager will auto-discover your existing Microsoft Azure Virtual Machine instances that have been provisioned directly using the provider console outside of Cloud Application Manager. With this capability, even if some of your teams are using Microsoft Azure Console to provision instances you can still import them into Cloud Application Manager, manage their lifecycle, and view them as part of the Admin Console Cloud Reports. The discovered instances will exist only as an instance. Cloud Application Manager does not create a corresponding Deployment Policy as part of registration process.

Organization and Cost Center Dashboards

- Organization and Cost Center administrators will now have a Dashboard view.

- The Cost Center Dashboard provides real-time information of monthly quota, cloud provider usage, and cost by workspace. The cost center functionality that was available as part of Admin Console has now been merged into Cost Center Settings. Cost Center administrators can now configure quotas on cloud providers and enforce them using the Cost Center Settings, which was previously available only to Organization Administrators via the Admin Console.

- The Organization Dashboard provides real time usage of total infrastructure spend across cloud providers, Provider usage, and costs by cost center.

AWS Management Console Access

- Starting this release, after configuring an AWS account within Cloud Application Manager, users can directly navigate to their AWS Management console with Single Sign On. Cloud Application Manager leverages the IAM policy that was setup initially and allows users to logon to AWS Management Console without requiring additional authentication. Users who have access to the AWS provider account within Cloud Application Manager will be able to leverage the single sign on functionality.

Managed Services Anywhere

- Managed Operating System on Microsoft Azure

- Starting this release, Cloud Application Manager customers can get Managed Services on their workloads residing in Microsoft Azure Cloud. Managed Services on Microsoft Azure includes Access, Configuration, Change, Monitor, Incident, and Patch management of Microsoft Azure Virtual Machine instances residing in any region. For further information on this service, please visit https://www.ctl.io/cloud-application-manager/managed-services-anywhere/

Additional monitoring capabilities for Managed Operating System on AWS

- Lumen Operators now can configure additional Cloud Watch alerts for Managed Operating System on AWS. Part of our support for Managed Operating System customers is our automated monitoring process, which constantly monitors a customer’s infrastructure and alerts our Support personnel to any issues. Our automated monitoring process relies on an agent installed on the AWS EC2 instance as part of “Delegate OS Management” functionality. We now can use AWS Cloud Watch to get additional insights into the managed instance. If you would like to take advantage of these additional monitoring capabilities, please reach out to us using our support options within Cloud Application Manager or write us at incident@centurylink.com

Cloud Optimization

- AWS Resale in the US is Live! From the AWS Provider, users will see radio buttons for requesting new and existing AWS accounts for consolidated billing and platform level support. Users have the option to migrate existing accounts or create new ones, after agreeing to terms. Actual processing of the request could take anywhere between 2-4 weeks.

Impact

- This release has no impact on current deployments.

Support

- As always if you have any questions, please feel free to write us at incident@CenturyLink.com. In addition to reaching us via email, you can now reach us via Phone at the following numbers:
    - United States: 1-888-638-6771
    - Canada: 1-866-296-5335
    - EMEA: 00800 72884743
    - Asia Pacific: +65 6768 8099

- For further information please visit https://www.ctl.io/cloud-application-manager/#Support
