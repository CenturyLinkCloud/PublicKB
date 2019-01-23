{{{
"title": "Cloud Platform - Release Notes: January 22, 2019",
"date": "01-22-2019",
"author": "Andy Watson",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Replay Welcome Tour

Cloud application Manager users now have the ability to replay the welcome tour that was only available when accessing the application for the first time. The option to replay the welcome tour is available in the user menu when accessing through the Management or Applications sites.  Users can select the dropdown next to the user name and select the "Play Welcome Tour" option to replay the welcome tour.

##### WebPack Technology for Loading Static Resources

Cloud Application Manager now implements a new way of loading static resources through WebPack. With this new technology, users can take advantage of the improved performance of the product and faster loading times.

#### [Analytics](https://www.ctl.io/cloud-application-manager/cloud-optimization/)

##### Analytics Available for Any Type of AWS or Azure Provider

For Azure, CenturyLink now extends our Analytics offering to unmanaged, un-hardened providers. This functionality is in addition to recently-announced functionality for AWS providers. On these "Bring Your Own Cloud" providers, administrators will see an "Analytics" option, capable of activating Analytics capabilities before or after a provider has been launched. When activated, CenturyLink will read your Provider's charges in our calculation of Platform Advisory Support. A CAM administrator has access to pricing details in the Management Site of CAM.


#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### New Cloud Formation Types Supported

Application Lifecycle Management now supports additional Cloud Formation types to be used in Cloud Formation template boxes. These additional types are:
"AWS::Route53Resolver::ResolverRuleAssociation", "AWS::DocDB::DBCluster", "AWS::DocDB::DBClusterParameterGroup", "AWS::DocDB::DBInstance" and
"AWS::DocDB::DBSubnetGroup". The user can now use these new resource types in the template definition of any Cloud Formation template box or update the template file of any existing template instance and reconfigure it to use the new resource types.

### Bug Fixes (1)

#### Windows 2016 Patch for CenturyLink Cloud

Windows 2016 has been patched and the newest version is now available in CLC.  This patching was completed as part of our ongoing efforts to improve security and availability of all CenturyLink Cloud resources.
