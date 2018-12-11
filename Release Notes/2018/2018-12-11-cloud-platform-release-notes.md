{{{
"title": "Cloud Platform - Release Notes: December 11, 2018",
"date": "12-11-2018",
"author": "David Gardner",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (7)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

**Support for Google Compute Deployment Manager**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports a new type of template box based on Google Deployment Manager Templates. Now you can create this new type of template box and add multiple Google Deployment templates files in YAML format to it to compose your box. Similar to the current support for AWS Cloud Formation, Azure ARM and Terraform templates, you can also define variables through Cloud Application Manager user interface, and then reference them from any Google Deployment Manager template file in the instance, with the usual Jinja format. For more information, please refer to [https://www.ctl.io/knowledge-base/cloud-application-manager/automating-deployments/google-deployment-manager/](../../Cloud Application Manager/Automating Deployments/google-deployment-manager.md)

**Instances page now displays Azure native services**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) Instances page will now list Azure native services instances, classified by Compute, Storage, Network, Database and Other types. These instances will display basic information for each type, such as subtype, region, status, name and description. A great advantage for users is that they will see at a glance all Azure instances in Cloud Application Manager user interface.

**Search by hostname in instances list**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports searching by hostname in instances list, in addition to the already existing searchable fields: _name_, _instance-id_, _service-id_, _public_ or _private IP address_, _support_id_ or _hostname_ fields_, or also by the _owner_ or _last user_ who acted on the instance.

**Improve new instance detection procedures**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) has improved its new instance detection procedure, to avoid automatic registration of cloned machines under the former existing instance. The auto-detection and registering will still work as usual for auto-scaling out events, but will prevent any other unwanted use case to be self-registered.

**New system variable service.provider_type**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports a new Jinja System Variable to allow access the provider type where the instance has been deployed to. You can refer to this new variable through the usual Jinja syntax by referencing: `{{ service.provider_type }}`. The returned value will be the corresponding descriptive name of the provider type, for example: "Amazon Web Services".

**New Cloud Formation types supported**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports additional Cloud Formation types to be used in Cloud Formation template boxes. These additional types are:

``'AWS::ServiceDiscovery::HttpNamespace', 'AWS::Lambda::LayerVersion', 'AWS::Lambda::LayerVersionPermission'``

The user can now use these new resource types in the template definition of any Cloud Formation template box, or update the template file of any existing template instance and reconfigure it to use the new resource types.
