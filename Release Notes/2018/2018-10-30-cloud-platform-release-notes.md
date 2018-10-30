{{{
"title": "Cloud Platform - Release Notes: October 30, 2018",
"date": "10-30-2018",
"author": "Christine Parr",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

**Billing Dashboard Graph Improvements**

[Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) provides an improved graph for Billing Dashboard in which you can see usage charges split by category for the given period being displayed. There is also a new filter to specify the type of charges you want to be displayed in the graph, to better understand the different charges the user has seen in his latest invoices. The categories displayed as separate bars and available in the filter are:

* Application Lifecycle Management
* Managed Services Anywhere
* Cloud Application Manager Support
* Integrated Azure Services
* Integrated AWS Services

The graph also shows the legend in the bottom with the total charges of the displayed period for every category.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

**Support for Terraform Template Boxes**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports a new type of template boxes based on Terraform. You can now create these template boxes and add multiple Terraform template files to compose your box. Similar to the current support for Cloud Formation and Azure ARM templates, you can also define variables through the Cloud Application Manager user interface. They will be added to your templates, and the variables you define in your template files will be detected and added to the variables section in the template box details page. Terraform modules are also supported by using Terraform template box variables inside another Terraform box.

Terraform is a provider-agnostic templating system, so whenever you define a Terraform template box in Application Lifecycle Management, you can select which provider to deploy to among the supported provider types: AWS, Microsoft Azure, Google Cloud Platform and CenturyLink Cloud.

For more information, refer to [Template Boxes](../../Cloud Application Manager/automating-deployments/template-box.md).

**Support for New AWS Instance Type**

Application Lifecycle Management now supports G3s, the latest Amazon Web Services instance type. Once you synchronize your AWS provider in Cloud Application Manager, you will be able to select this Instance type in your Deployment Policy boxes by searching in the search box of the Instance Type dropdown.

**Support for New Google Cloud Platform Region**

Application Lifecycle Management now supports a new Google Cloud Platform region: Asia East 2, and its corresponding zones. Once you synchronize your Google Cloud provider in Cloud Application Manager, you will be able to select in your Deployment Policy boxes the zones corresponding to the new region.

### Announcements (1)

#### Intel Discloses Three Security Vulnerabilities

As part of the August 14th disclosure by Intel, three security vulnerabilities have been named:

* CVE-2018-3646 (L1 Terminal Fault - VMM)
* CVE-2018-3620 (L1 Terminal Fault - OS)
* CVE-2018-3615 (L1 Terminal Fault – SGX, SMM)

CenturyLink is actively conducting patching and other remediation activities across all of our infrastructure. At this time, there is no indication that these vulnerabilities have impacted us or have been used to attack our customers.

Also, please note: While CenturyLink is patching our environment, we want to remind our customers that they are responsible for updating the operating system of their cloud virtual and bare metal servers. We are actively working to apply the latest patches to our Operating System templates to ensure any new virtual servers are not at risk of these vulnerabilities. We recommend you check with your operating system vendor(s) and system manufacturer(s) and apply any updates as soon as they are available.

See our full post [here](https://www.ctl.io/blog/post/intel-discloses-three-security-vulnerabilities/).
