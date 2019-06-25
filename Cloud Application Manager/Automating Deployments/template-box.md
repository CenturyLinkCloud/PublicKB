{{{ "title": "Template Boxes",
"date": "12-21-2018",
"author": "Cristina Torres, Amalia Garcia de Mirasierra",
"attachments": [],
"contentIsHTML": false,
"keywords": ["arm","azure resource manager", "terraform", "aws","cloudformation","template box", "google deployment manager",  "cloud application manager", "deployment templates", "cam", "alm", "application lifecycle management"]
}}}
**In this article:**

- [Overview](#overview)
- [Audience](#audience)
- [Prerequisites](#prerequisites)
- [Deploy Using CloudFormation Templates](#deploy-using-cloudformation-templates)
- [Deploy Using Azure Resource Manager Templates](#deploy-using-azure-resource-manager-templates)
- [Deploy Using Terraform Templates](#deploy-using-terraform-templates)
- [Deploy Using Google Templates](#deploy-using-google-templates)
- [Getting General Support](#getting-general-support)

### Overview

This article is meant to assist users of Cloud Application Manager willing to use Template Boxes to create, edit or deploy any of the template technologies supported by Cloud Application Manager.

### Audience

All users of Cloud Application Manager who wants to define and use Template Boxes.

### Prerequisites

* An active *Cloud Application Manager* account
* Having configured a provider of any type supported by the template boxes type that you will use

### Deploy Using CloudFormation Templates

The Cloud Application Manager CloudFormation box type runs on the [AWS CloudFormation service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

The Cloud Application Manager enables the deployment and management of AWS services using an API.

So why use the Cloud Application Manager to launch services directly in Amazon?

Cloud Application Manager allows customers to standardize enterprise services across multiple cloud and infrastructure environments. By using cloud native templates, IT organizations can build a catalog of applications and services that users can consume on-demand. Not only can it manage services across multiple providers but also multiple subscriptions by using the abstraction between applications and infrastructure (e.g. deployment policies).

It supports all CloudFormation templates available from AWS. Leverage services such as EC2, Elastic Block Store, Simple Notification Service, Elastic Load Balancing and Auto Scaling, RDS, S3, DynamoDB, Elastic IPs, and much more.

Cloud Application Manager supports all CloudFormation templates available from AWS. Leverage services such as EC2, Elastic Block Store, Simple Notification Service, Elastic Load Balancing and Auto Scaling, RDS, S3, DynamoDB, Elastic IPs, and much more.

For more information, go to [AWS templates](../Automating Deployments/aws-template-box.md).

### Deploy Using Azure Resource Manager Templates

The Cloud Application Manager Azure Resource Manager Template box allows you to run any Azure service on Cloud Application Manager. This allows you to use the power of Cloud Application Manager (instance history, Lifecycle Editor, bindings, box versioning) combined with any service supported by Azure Resource Manager.

To learn more about:

How to write ARM Templates [see](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-authoring-templates).

To review the many services available in Microsoft Azure Resource Manager take a look at the official documentation [here](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-supported-services).

For more information, go to [ARM templates](../Automating Deployments/arm-template-box.md).

### Deploy Using Terraform Templates

A Terraform Template box allows you to apply a **Terraform version 0.11** configuration consisting of one or many files on the following Providers:
-  Amazon Web Services
-  CenturyLink Cloud
-  CenturyLink Private Cloud on VMware Cloud Foundation
-  Google Cloud Platform
-  Microsoft Azure
-  VMware vCenter/vSphere
-  VMware vCloud Director

This feature provides you with the ability to use the power of Cloud Application Manager (instance history, Lifecycle Editor, bindings, box versioning) combined with any service supported by Terraform.

#### To learn more about Terraform

In order to understand Terraform's configurations language see [Terraform 0.11 documentation here](https://www.terraform.io/docs/configuration-0-11/index.html). Currently Cloud Application Manager can deploy **Terraform version 0.11** templates.

For more information on how to use Terraform with Cloud Application Manager, go to [Terraform templates](../Automating Deployments/terraform-template-box.md).

### Deploy Using Google Templates

With Google Deployment Manager you can automate the creation and management of Google Cloud Platform resources, by writing flexible declarative template and configuration files.

This allows you to use the power of Cloud Application Manager (instance history, Lifecycle Editor, bindings, box versioning) combined with any service supported by Google Deployment Manager.

For more information, go to [Google templates](../Automating Deployments/google-deployment-manager.md).

### Getting General Support

Customers can contact the CenturyLink Global Operations Support center (support desk) directly for getting help with Cloud Application Manager as well as any other supported product that they’ve subscribed to.  Below are three ways to get help.

#### Contact:

1. **Phone:** 888-638-6771

2. **Email:** incident@centurylink.com

3. **Create Ticket in Cloud Application Manager:** Directly within the platform, users can “Create Ticket” by clicking on the “?” symbol in upper right corner near the users log-in profile icon.  This takes users directly to the Managed Servicers Portal where they can open, track and review status of issues that have been raised with the support desk.  Additionally, this is how a TAM can be engaged as well.

#### Instructions:

1. Provide your name
2. Cloud Application Manager account name
3. A brief description of your request or issue for case recording purposes

The support desk will escalate the information to the Primary TAM and transfer the call if desired.
