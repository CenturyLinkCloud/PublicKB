{{{
  "title": "User Management",
  "date": "3-11-2021",
  "author": "Brandy Smith",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description

This article will outline the User Management and Entitlement functionality that is natively available within the Edge Orchestrator Portal.
The Edge Orchestrator Portal provides multiple user management and role based access control capabilities.
These roles can be managed within the **Admin -> Roles** section of the Edge Orchestrator Portal.
They are designed to be robust enough to fit within a wide array of enterprise and managed service provider scenarios.

**Note** Not all of the User Management options or functions listed below may be available at this time. The list below is a complete list of all of the functionality we will be releasing over time.
As the Edge Orchestrator platform evolves, more features, infrastructure and compute options, functionality, and integrations will be available for Edge customers to consume, thus expanding the Management functionality.
Lumen plans to rapidly add features to the Edge Orchestrator platform.

### Roles

There are two types of roles within the Edge Orchestrator Portal.

1. Tenant
2. User based roles

Both sets of roles allow restrictions to be imposed on a user at the feature access level.
Entire sections within the appliance UI can be hidden based on the specified access levels for features within the portal.
Features have different access scopes that can be selected from and can range depending on the specific feature.
The most common scope set involves none, read, and full.
Instance Type access is also common among both role types which allow the administrator to restrict which service catalog items they are allowed to provision within the portal.

There are several handy tricks for creating new roles within the portal and users can be assigned more than one role.
When a user is assigned more than one role, permissions are granted by the role with the highest level of scope access.
This allows roles to be built with small subsets of features and combined to grant different individuals relevant permission control.


## Tenant Roles

A Tenant based role is used to ensure access control enforcement across an entire tenant with many sub-users.
This allows the subtenant to manage their own set of internal user based roles without worrying master tenant involvement in setting them up.
The master tenant is the only tenant able to create and manage these types of roles. When editing a Tenant, a singular tenant role can be assigned to the account.
Users within the tenant can be assigned roles but those user based roles will never be able to supersede the level of access granted by the tenant role.
This allows a super administrator the ability to restrict access at the department or organization level without having to worry about per user access control within said tenant.

Tenant roles also have an additional section not in User based roles related to Cloud Access. Cloud Access allows the master tenant the ability to assign cloud integration resources to specific subtenants or groups of subtenants. An example would be granting access to a specific VMware cluster only to a subset of tenants using the tenant based role control.

## User Roles

User roles can be created by any tenant given permission at the tenant role level.
These allow tenants to manage their own sets of users and their levels of access.
They also allow tenants to control which users have access to specific “Groups” for provisioning into within the portal.
Groups are not cross tenant and therefore need to be controlled within the individual tenant.

Master tenants are able to create a special type of user role called a multi-tenant user role. A multi-tenant user role is copied / duplicated down to all subtenants.
These can be viewed as pre-canned role templates available to new tenants when their account is first created.
Any changes made to the main role are propagated down to the subtenants version of the shared role so long as the subtenant has not previously adjusted/changed that role.
The moment a subtenant makes adjustments to the shared role within their account, it is unlinked from the parent role and treated entirely independently.

When a user role is copied down to a subtenant, the permission scopes cannot supersede the tenants assigned tenant role.
If they do they are automatically downgraded when propagated to the specific tenant.
Any changes made to the tenant role will automatically ensure roles within the tenant are downgraded appropriately.

## Multi-Tenant User Role Lock

As discussed above, multi-tenanted user roles are made available within all subtenants as ‘canned’ user role sets. Master tenant administrators can prevent changes to these ‘canned’ user roles by marking the box labeled ‘Multitenant LOCKED’ when creating or editing the role. In addition to preventing subtenant administrators from modifying permissions of these roles within their subtenancy, this option also ensures master tenant administrators can propagate new changes to that role. Modification of the role by the subtenant (if allowed) breaks the link back to the master tenant and the copy of the role within the subtenant will become its own unlinked role.

**Note** Multi-tenant role lock applies only to permission sets on the ‘FEATURE ACCESS’ tab.
Permissions in the ‘GROUP ACCESS’, ‘INSTANCE TYPE ACCESS’, and ‘BLUEPRINT ACCESS’ tabs are not locked.
Similarly, changes made to the role on these tabs in the master tenant are not synced down.

## Roles and Identity Sources

It is very common for large Enterprises to have an existing identity source that they would like to plug into the Edge Orchestrator Portal for authentication.
This includes services like LDAP, Active Directory, OKTA, Jump Cloud, One Login, and SAML.
When using these services it becomes important to configure a role mapping between the portal role assignments to the equivalent identity source groups/roles the user belongs to.
This is configurable within the identity source management UI.
Sections are provided allowing things like LDAP groups to be directly mapped to specific roles within the portal.
If a user matches more than one LDAP/role group then both sets of roles are applied to the user automatically.

Configuring Identity Sources is done in Tenant management or user management in **Administration > Tenants or Administration > Users**, and has to be configured on a per-tenant basis.
Additionally, administrators may opt to lock users to their mapped role or keep the roles unlocked to manually administer roles in one-off scenarios.

### Role Permissions

Permission options for sub-tenant user roles will only list options permitted by the Tenant role applied to the sub-tenant. Sub-Tenant user roles permissions cannot exceed permissions set by the overriding Tenant Role.

### User Role Permission Sections

**FEATURE ACCESS**
Controls User access level for UI sections and features in the portal.
As the Edge Orchestrator portal

**GROUP ACCESS**
Controls User access level for Groups. Groups are not a Multi-Tenant construct, only Groups created in the current Tenant will be visible.

**INSTANCE TYPE ACCESS**
Controls User access level for Instance Types. Only Instance Types created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.

**BLUEPRINT ACCESS**
Controls User access level for Blueprints during App provisioning. Only Blueprints created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.

**PERSONAS**
Controls User access to Edge Orchestrator portal Personas, at the time of this writing Users may be given access to the Standard (full the portal experience) or Service Catalog Personas

**CATALOG ITEM TYPES**
Controls User access to Catalog Item types within the Service Catalog Persona. Only Catalog Items created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.

### Tenant Role Permission Sections

**FEATURE ACCESS**
Controls Tenant access level for sections and features in the portal. The complete feature permissions grid is included below.

**CLOUD ACCESS**
Controls Tenant access level for Clouds. This list includes Clouds integrated from the Master Tenant and shared publicly. Tenants given this Tenant Role will have either Full, Read, or None access levels to a given Cloud. See the section below for more information on Cloud Access levels.

**INSTANCE TYPE ACCESS**
Controls Tenant access level for Instance Types. Only Instance Types created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.

**BLUEPRINT ACCESS**
Controls Tenant access level for Blueprints during App provisioning. Only Blueprints created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.

**CATALOG ITEM TYPES**
Controls Tenant access to Catalog Item types within the Service Catalog Persona. Only Catalog Items created in the current Tenant or those created in the Master Tenant and shared with the current Tenant will be available.

**Cloud Access Levels**
When creating or editing a Tenant Role, Master Tenant administrators can choose which publicly-visible Clouds to share with Tenants having the current Role. Access can be completely restricted or administrators can choose between Read and Full access.

**Read Access**
Master Tenant administrators can opt to give other Tenants read-level access to any integrated Clouds through the Tenant Role. A read-only Cloud allows the Master Tenant to assign resources for viewing by Subtenant users but not allow them to perform any actions or provision new Instances.

With read-level access, Subtenant users will have access to the Cloud detail page (Infrastructure > Clouds).
From the Summary subtab on the Cloud detail page, high-level information on Cloud resources are shown regardless of specific resources that have been shared with the Subtenant.
Other metrics, such as costing, resource percentages (CPU, Memory, and Storage), VM counts and host counts will only be populated when servers in the Cloud have been assigned to the Tenant.

**Full Access**
With full access, Subtenant users also have access to the Cloud detail page (Infrastructure > Clouds > Specific Cloud) and see the same level of detail as Subtenants with read-only rights. However, with full access, Subtenant users can also perform many actions including the addition of Clusters, Hosts, and VMs, changing networks, and more. This cloud will also be selectable as a provisioning target for Subtenant users when deploying Instances or Apps.

### Feature Access Permissions

Feature Access settings control permissions for sections and objects in the portal.

Permission options include:

**None**
Hidden or inaccessible for user

**Read**
User can view but cannot edit or create

**Full**
User has full access

**User**
User can access Objects they have created or own.

**Group**
User can access Objects assigned to or shared with Groups the User has access to.

**Remote Console: Provisioned**
Remote Console tab will only appear after instance is successfully provisioned.

**Remote Console: Auto Login**
RDP and SSH only, controls if user is auto-logged in to Remote Console or presented with login prompt.

### Role Mappings
Gives User Access to Role Mappings config in /admin/roles for configuring Identity Source Role Mappings without providing Access to other Identity Source configuration settings.

**Feature Access Role Permission Options**

Permission Name

Permission Options

Feature Access

Description

Recommendations

**Tenant Role Recommendations**

**Admin:** Appliance Settings

None, Full
Allows or disallows access to the Appliance and License tabs in Administration > Settings
The Appliance tab in Administration > Settings is where administrators would configure the appliance URL, Tenant and User management, email, proxy, and currency settings. Additionally, defining which Clouds are available for integration within the portal is done on this page. On the License tab information about the current license may be viewed and a new license may be applied when needed.
This permission is recommended to only be assigned to Roles utilized within the Master Tenant. Those responsible for configuring currency, email, and proxy settings for Cloud API access will need this permission.
This permission is recommended to be set to None on the Tenant Role to restrict this access for all Subtenant Users.

**Admin: Backup Settings**

None, Full
Allows or disallows access to Administration > Backups. Master Tenant administrators have additional settings for appliance backups and defaults on this page.
The Backup Settings page is where users define the default backup bucket, backup schedule, and retention count. Additionally, if given to a Master Tenant user they will have the ability to enable scheduled backups, create backups, and backup appliance.
This permission is recommended for those responsible for enabling backups and setting default backup buckets within .

**Admin: Environment Settings**

None, Full
Allows or disallows access to the Environments tab in Administration > Provisioning. When given to a Master Tenant user they may define the visibility of the environment to either private or public. When given to a Subtenant user the environments are only visible to the subtenant (private).
The Environments tab is where named environments such as development or production are created and given a description as well as a code for use within the API. A display order and visibility is also set.
This permission is recommended for those responsible for defining environments that will be available to select at provision time whether they are the Master Tenant or Subtenant users.

**Admin: Guidance Settings**

None, Full
Allows or disallows access to the Guidance tab in Administration > Settings
The Guidance tab controls global thresholds for the portal guidance recommendations
This permission is recommended for those responsible for cost and resource management

**Admin: Health**

None, Read
Determines access to the Operations > Health page, including the Health, Alarms, and Logs tabs.
The Health pages provide an overview of health, notifications from integrations, and the current UI log.
This permission is recommended for those responsible for administering and troubleshooting.
This permission is recommended to be set to None on the Tenant Role to restrict access for Subtenant users.

**Admin: Identity Source**

None, Role Mappings, Full
Allows or disallows access to create, edit, or delete integrated Identity Sources associated with subtenants. The “Role Mappings” option allows the user to edit role mappings without seeing higher level details about the integration itself (such as server IP addresses and admin usernames).
The Identity Sources page associated with the selected Tenant allows for creating, editing, and removing of identity sources in addition to configuring role mapping between the portal and the identity provider.
Full permission is recommended for those responsible for integrating the portal with Identity Providers. Role Mapping permission is recommended for those responsible for Role Based Access Control (RBAC).
This permission is recommended to be set to None for any subtenant user roles via use of a Tenant Role unless they manage their own RBAC.

**Admin: Integrations**

None, Read, Full
This allows or disallows full or read access to the Administration > Integrations.
The Administration Integrations tab is where many new or existing integration types can be configured. These include Chef, Puppet, Ansible, Salt Master, Ansible Tower, vRealize Orchestrator, Microsoft DNS, PowerDNS, Route 53, Git, GitHub, Docker, Consul, Jenkins, ServiceNow, Cherwell, Remedy, ACI, and Venafi.
This permission is recommended for those responsible for the integration between the portal and integrated technologies.

**Admin: License Settings**

None, Full
Allows or disallows access to the Licenses tab in Administration > Provisioning. When given to a Master Tenant user they may define specific subtenants in which the licenses may be used.
The Licenses tab is where software licenses may be added for tracking in the portal. the portal may then be configured to apply these licenses on provision. Currently, only Windows license types are available.
This permission is recommended for those responsible for managing Windows licenses.

**Admin: Log Settings**

None, Full

Allows or disallows access to the Administration > Logs.
The Logs page is where logs are enabled. Syslog forwarding rules, Splunk integrations and LogRhythm integrations are also configured here.
This permission is recommended for those responsible for configuring the portal log settings and integrations.
This permission is recommended to be set to None in the Tenant Role to restrict this access to Subtenant Users.

**Admin: Message of the day**

None, Full

Allows or disallows access to create and edit Message of the Day policies in Administration > Policies
The Policies page is where policies are defined. When creating a policy, users can select “Message of the Day” from the TYPE dropdown with this permission set to Full.
This permission is recommended for those responsible for publishing the Message of the Day.
This permission is recommended to be set to None in the Tenant Role to restrict this access from Subtenant Users.

**Admin: Monitoring Settings**

None, Full

Allows or disallows access to Administration > Monitoring
The monitoring settings page is where monitoring and monitoring integrations are configured. Available integrations are AppDynamics, ServiceNow, and New Relic. Monitoring checks can be turned on or off, and availability time frame, check interval period, and reported availability precision are also configured on this page.
This permission is recommended for those responsible for configuring monitoring settings and integrations.
This permission is recommended to be set to None in the Tenant Role to restrict this access from Subtenant Users.

**Admin: Plugins**

None, Full

Allows or disallows access to the Plugins tab on the Integrations page (Administration > Integrations)
The Plugins tab is where custom plugins are added to extend the portal functionality.
This permission is recommended for those responsible for extending the portal functionality through custom plugins.
This permission is recommended to be set to None in the Tenant Role to restrict this access from Subtenant Users.

**Admin: Policies**

None, Read, Full

This setting determines the level of access to Administration > Policies. When given to a Master Tenant user the ability to define Global policies and associate them with one or many Subtenants is granted. When given to a Subtenant user, a global policy applies only to their subtenant.
The Policies page is where policies are defined. On create, the type of policy is selected, a name, description, and scope are defined.
This permission is recommended for those responsible for configuring and managing policies either at the Master Tenant or Subtenant.

**Admin: Provisioning Settings**

None, Full

Allows or disallows access to the Settings tab of the Administration > Provisioning page.
The Settings tab is where global provisioning settings are configured. For Master Tenant users, these include allowing Cloud selection, allowing host selection, requiring environment selection, showing pricing, hiding datastore stats on selection, cross-Tenant naming policies, and reusing naming sequence numbers. For both Master Tenant and Subtenant users, defining the deploy archive store, cloud-init setting, the PXE boot root password, and default App Blueprint types are available.
This permission is recommended to only be assigned to roles utilized within the Master Tenant.

**Admin: Roles**

None, Read, Full

This setting determines access to the Administration > Roles page. When given to a Subtenant user, the ability to create user roles is granted. When given to a Master Tenant user, the ability to create and manage Tenant and Multi-Tenant Users roles is also granted.
The Roles page is where roles are defined. On create, a name and description are defined. Once created, the Role is accessed and feature access, Group access, Instance Type access and Blueprint access may be configured.
This permission is recommended for those responsible for configuring Role Based Access Control (RBAC) either globally or within their Subtenant.

**Admin: Service Plans**

None, Read, Full

This setting determines access to Administration > Plans & Pricing. When given to a Subtenant user, access to the Plans tab is granted. When given to a user in the Master Tenant, the Price Sets and Prices tabs are also available.
The Plans tab is where service plans are defined. On create, a name and code (for API) are defined, display order, provisioning type, storage, memory, core count and the price may be configured. Additionally, the actions menu will allow group access to be scoped.
This permission is recommended for those responsible for defining and managing pricing and applying plans.

**Admin: Tenant**

None, Read, Full

This setting determines access to the Administration > Tenants page. With this permission, local users may be created or deleted within each Tenant. Critical Note: Granting this permission to Subtenant users will expose all Tenants and Tenant users to the Subtenant.
The Tenant page is where all Tenants may be viewed, edited, created, or even deleted.
This permission is recommended to only be assigned to Roles utilized within the Master Tenant who are responsible for the creation, configuration, and/or deletion of Subtenants.
It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.

**Admin: Tenant - Impersonate Users**

None, Full

This setting allows or disallows access to impersonate users. This selection is located on the Administration > Users page in the Actions menu. When set to Full, Impersonate selection is available.
This permissions allows for users in the Master Tenant to impersonate users of the Master Tenant and Subtenants.
This permission is recommended to be assigned only to Roles utilized within the Master Tenant who are responsible for configuring RBAC or for supporting users.
It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.

**Admin: Users**

None, Read, Full

This setting determines access to the Administration > Users page (both Users and User Groups tabs). User Roles can also be set or edited when creating or editing a User on this page. Note: A Master Tenant user with the Admin: Tenants (Full) permission may also access and perform user management from the associated Tenant page.
The User tab is where all users may be viewed, edited, created, or even deleted. The User Groups tab is where User Groups may be viewed, edited, created, or even deleted. Within the portal, a User Group may be selected during provisioning in order to add each group member’s credentials to an Instance. When creating a User Group a name, description, server group (in Linux, name of the group to assign members), sudo access toggle, and a list of users are defined.
This permission is recommended for those responsible for managing users and RBAC.

**API: Execution Request**

None, Full

Allows or disallows access to an API endpoint.
This endpoint allows users to execute scripts on Instances, containers, or hosts and then polls for a response.
This permission is recommended for those responsible for arbitrary API script execution.
It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.

**Backups**

None, View, Read, User, Full

Determines access to the Backups section of the portal UI, including the Summary, Jobs, Backups, and History subpages. The “User” permission allows access only to backup objects the user owns.
The Summary subpage allows the user to see the number of configured backups, the success rate, recent failures, and the size of the backups, as well as, the upcoming and in-progress backups. The Jobs subpage is where backup jobs may be created, cloned, edited or deleted. On create, a name, code (for use within the API), retention count, and schedule are selected (Note: Selectable schedules are defined Execution Schedules which are created in the Provisioning > Automation). On the backups subpage, a list of configured backups is provided and new backups maybe created or on-demand backups may be executed. On create, the place where the target exists is selected (Instance, Host, or Provider), the source is selected and a name is defined as well as the selected execution schedule. On the History subpage both the backups and restores tabs are available. Names, statuses, start times, durations and size may be viewed.

This permission is recommended for those responsible for performing the backup and restoration of workloads.

**Backups: Integrations**

None, Read, Full

Determines access to the Backups > Integrations page.
From this page, backup integrations may be created, edited, or deleted. The page also provides the status of existing integrations. On create the integration product is selected and all associated connection and authentication information must be provided. Additionally, visibility is set to either public or private. Integrations available include Avamar, Commvault, Rubrik, Veeam, and Zerto.
This permission is recommended for those responsible for the integration between the portal and backup technologies.
It is recommended this setting be set to None on the Tenant Role to restrict access for Subtenant users.

**Infrastructure: Boot**

None, Read, Full

Determines access to the Integrations > Boot page, including the Mapping, Boot Menus, Answer Files, Images, and Discovered MAC Addresses tabs.
The Edge Orchestrator includes a PXE Server to provide for rapid bare metal provisioning.
The Boot page is where users may add, edit, or delete answer files, as well as, manage their own images or use existing ones.
Boot menus and mappings are also managed here and discovered MAC addresses are displayed.
This permission is recommend for those responsible for bare metal provisioning.

**Infrastructure: Certificates**

None, Read, Full

Determines access to the SSL Certificates tab on the Infrastructure > Keys & Certs page.
The SSL Certificates page is where certificates may be uploaded and managed. These certificates may then be used within the portal when orchestrating load balancers.
This permission is recommended for personnel who will be orchestrating and provisioning load balancers.

**Infrastructure: Clouds**

None, Read, Full

Determines access to the Infrastructure > Clouds page. The “Group” permission limits the Cloud list page (Infrastructure > Clouds) to show only Clouds in their assigned Groups.
The Cloud page is where new Clouds are integrated within the portal and existing Cloud integrations are managed. This includes creating a code for use within the API, the location, visibility, tenant, whether or not it should be enabled, and if VMs should be automatically powered on. Additionally, Clouds may be integrated from the Clouds tab of a Group detail page.
This permission is recommended for those responsible for configuring RBAC as well as those responsible for the portal Cloud Integrations.

**Infrastructure: Clusters**

None, Read, Group, Full

Determines access to the Infrastructure > Clusters page.
The Clusters page allows you to create and manage Kubernetes, Docker, and KVM Clusters, as well as Cloud-specific Kubernetes services such as EKS.
This permission is recommend for those creating and managing containers or container services.

**Infrastructure: Groups**

None, Read, Full

Determines access to the Infrastructure > Groups page.
The Groups page is where Groups are created and given a code for use within the API. Additionally, the DNS service, CMDB, service registry, and config management may be selected. Existing Clouds/Hosts or new Clouds/Hosts are added to the Group and virtual or bare metal machines may be viewed.
This permission is recommended for those responsible for configuring Role Based Access Control (RBAC).

**Infrastructure: Hosts**

None, Read, Full

Determines access to the Infrastructure > Hosts page, including the Hosts, Virtual Machines, and Bare Metal tabs.
The Hosts page provides for viewing and managing hosts, virtual machines, and bare metal hosts. On the bare metal hosts page, hosts may come from PXE boot or may be manually added. On the Hosts page hypervisors and Docker hosts are displayed. The Virtual Machines page lists all VMs. On all three pages actions may be performed against machines. Additionally, views may be refined by altering the columns displayed and CSV/JSON exporting of lists is available.
This permission is recommend for those whom need to take action on machines and those responsible for bare metal provisioning.

**Infrastructure: Keypairs**

None, Read, Full

Determines access to the Key Pairs tab on the Infrastructure > Keys & Certs page.
The Keypairs page allows for ease in accessing instances via SSH. On create a name, public key, private key, and passphrase are entered.
This permission is recommended for those whom utilize portal deployment and management of Linux Instances.

**Infrastructure: Load Balancers**

None, Read, Full

Determines access to the Infrastructure > Load Balancers page, including both the Load Balancers and Virtual Servers tabs.
The Load Balancers page is where new load balancer integrations may be configured. Additionally, existing integrations may be managed. The Virtual Servers page is where virtual servers are managed to include policies, pools, profiles, monitors, nodes, and rule scripts may be managed.
This permission is recommended for those responsible for integrating the portal with load balancers as well as those responsible for managing virtual servers.

**Infrastructure: Network Domains**

None, Read, Full

Determines access to the Domains tab on the Infrastructure > Network page.
The Domains page is where network domains are managed. Domains are used for setting FQDNs, joining Windows Instances to domains, and creating A-Records with DNS integrations. On create the domain controller and credentials for domain join must be provided.
This permission is recommended for those responsible for the portal DNS and domain-join integrations.

**Infrastructure: Network Firewalls**

None, Read, Full

Determines access to the Firewall tab on applicable network integrations detail pages
The Firewall tab is where network firewall groups and rules are viewed, created and managed
This permission is recommended for those tasked with network security management

**Infrastructure: Network Integration**

None, Read, Full

Determines access to the Integrations tab on the Network list page (Infrastructure > Network)
The integrations tab is where network integrations can be viewed, added and managed. Additionally, the detail pages for network integrations are accessed here
This permission is recommended for those tasked with handling network integrations and their use within the portal

**Infrastructure: Network IP Pools**

None, Read, Full

Determines access to the IP Pools tab on the Network list page (Infrastructure > Network)
The IP Pools tab is where IP pools from various networks are displayed. Detail pages for IP pools can also be accessed here
This permission is recommended for those tasked with IP address management

**Infrastructure: Network Proxies**

None, Read, Full

Determines access to the Proxies tab on the Infrastructure > Networks page.
The Infrastructure Networks Proxies page is where Proxy configurations are stored, which are available for use by the provisioning engines.
This permission is recommended for those responsible for configuring proxies to be used when provisioning.

**Infrastructure: Network Router DHCP Pool**

None, Read, Full

Determines access to the DHCP tab on the detail page for a Router associated with certain network integrations (Example: Infrastructure > Network > Integrations > Routers tab > selected router > DHCP tab)
The DHCP tab is where DHCP pools are viewed, created and managed
This permission is recommended for those responsible for DHCP pool management

**Infrastructure: Network Router Firewalls**

None, Read, Full

Determines access to Firewall tabs on Router Detail pages (Infrastructure > Network > Routers tab > Selected Router)
The Firewall tab is where firewall rules are viewed, created, and managed
This permission is recommended for those responsible for managing firewall rules

**Infrastructure: Network Router Interfaces**

None, Read, Full

Determines access to Interfaces tabs on Router Detail pages (Infrastructure > Network > Routers tab > Selected Router)
The Interface tab is where router interfaces can be viewed, created and managed
This permission is recommended for those responsible for network traffic flow

**Infrastructure: Network Router NAT**

None, Read, Full

Determines access to the NAT tab on Router Detail pages (Infrastructure > Network > Routers tab > Selected Router)
The NAT tab is where NAT rules are viewed, created, and managed
This permission is recommended for those responsible for network traffic flow

**Infrastructure: Network Router Redistribution**

None, Read, Full

Determines access to Route Redistribution tabs on Router Detail pages (Infrastructure > Network > Routers tab > Selected Router)
The Route Redistribution tab is where redistribution rules are viewed, created, and managed
This permission is recommended for those responsible for redistribution rules

**Infrastructure: Network Router Routes**

None, Read, Full

Determines access to Routing tabs on Router Detail pages (Infrastructure > Network > Routers tab > Selected Router)
The Routing tab is where routes are viewed, created, and managed
This permission is recommended for those responsible for network route management

**Infrastructure: Network Routers**

None, Read, Group, Full

Determines access to the Routers tab on the Infrastructure > Networks page. The “Group” permission setting allows access to objects shared to Groups associated with the user.
The Routers page is where virtual routers are created and managed from Cloud and Network integrations.
This permission is recommended for those responsible for network management.

**Infrastructure: Networks**

None, Read, Group, Full

Determines access to the Infrastructure > Networks page, including the Networks, network groups, and integrations tabs. The “Group” permission setting allows access to objects shared to Groups associated with the user.
The Networks page is where networks are configured for DHCP or static IP assignment and existing networks are displayed. The Network Groups page is where networks are grouped to allow round robin provisioning among the group. The Integrations page is where IPAM, DNS, security, service registry, and virtual network tools are integrated. These include Cisco ACI, VMware NSX T and V, Infoblox, Bluecat, phpIPAM, SolarWinds, Stealth, Microsoft DNS, PowerDNS, Route 53, and Consul.
This permission is recommended for those responsible for integration with network technologies and the configuration and management of networks to be used during provisioning.

**Infrastructure: Policies**

None, Read, Full

Determines access to the Policies tabs on the Group and Cloud detail pages (Infrastructure > Groups > selected Group OR Infrastructure > Cloud > selected Cloud).
Policies can be created from this tab which are scoped to the Cloud or Group being viewed.
This permission is recommended for users who will need to set quotas which pertain specifically to Groups or Clouds the user has access to.

**Infrastructure: Security Groups**

None, Read, Full

Determines access to the Security Groups tab on the Infrastructure > Networks page.
The Security Groups page is where Security Groups (aka virtual firewalls) are defined.
This permission is recommended for those responsible for firewall configuration and management.

**Infrastructure: State**

None, Read, Full

Determines access to the power state toggle on the Infrastructure > Hosts page.
This toggle moves Hosts between a started and stopped state.
This permission is recommended for those responsible for managing Hosts.

**Infrastructure: Storage**

None, Read, Full

Determines access to the Infrastructure > Storage page, including the Buckets, File Shares, Volumes, Data Stores, and Servers tabs.
The Servers page is where storage integrations are configured. Integrations available include 3Par, AWS S3, Dell EMC ECS and Isilon, Huawei or Open Telekom OBS and Huawei, Open Telekom, OpenStack SFS. The Volumes page is where storage volumes may be created or viewed. The File Shares page is where File Shares of types CIFS, Dell EMC ECS or Isilon, local storage, and NFSv3 may be configured. The Buckets page is where storage buckets of type AWS S3, Alibaba, Azure, Open Telekom OBS, OpenStack Swift, Rackspace CDN may be created. Storage buckets are used for Backup, Archives, and Virtual Images. The Data Store page is where permissions to data stores may be managed and new data stores are added.
This permission is recommended for those responsible for storage integrations and configurations.
This permission is recommended to be set to None on the Tenant Role to restrict access to Subtenant users.

**Infrastructure: Storage Browser**

None, Read, Full

Determines file browsing access to buckets and file shares on the Buckets and File Shares tabs of the Infrastructure > Storage page.
The Storage Browser permission allows users who also have appropriate Infrastructure: Storage permission to browse, add files and folders, download, and delete from the buckets and file shares.
This permission is recommended for those who need to browse storage.

**Infrastructure: Trust Integrations**

None, Read, Full

Determines access to the Integrations tab of the Infrastructure > Keys & Certs page.
The Integrations tab is where new trust integrations can be configured. This includes Venafi.
This permission is recommended for those responsible for the integration between the portal and Venafi.
This permission is recommended to be set to None on the Tenant Role to restrict access to Subtenant users.

**Integrations: Ansible**

None, Full

Determines access to Ansible integrations on the Administration > Integrations page.
The Integrations tab is where existing integrations are displayed and new integrations may be created. This permission applies only to existing Ansible integrations. It allows or disallows the ability to edit existing Ansible integrations.
This permission is recommended for those responsible for integrations between the portal and Ansible.
This permission is recommended to be set to None on the Tenant Role to restrict access to Subtenant users.

**Logs**

None, Read, User, Full

Determines level of access to the Logs section of the portal UI. The “User” permission will allow access only to objects the user owns.
The Logs page is where logs may be viewed.
This permission is recommended for those responsible for troubleshooting.

**Monitoring**

None, Read, User, Full

Determines level of access to the Monitoring section of the portal UI, including the Status, Apps, Checks, Groups, Incidents, Contacts, and Alert Rules subpages. The “User” permission will allow access only to objects the user owns.
The Checks page is where automatically-created checks are customized or new checks are created. The Groups and Apps pages are where checks may be grouped. The Incidents page is where incidents are created upon Check failure. The Contacts page is where contacts may be added for notifications. Then Alert Rules page is where notification are configured.
This permission is recommended for those responsible for monitoring applications, incidents, or configuring notifications.

**Operations: Activity**

None, Read

Determines access to the Activity and History tabs on the Operations > Activity page.
The Activity page displays four types of recent activities: Provisioning, Alerts, Backups, and Permissions.
This permission is recommended for those responsible to monitor or view activities and their statuses within the portal.

**Operations: Alarms**

None, Read, Full

Determines access to the Alarms tab in the Activity section (Operations > Health)
The Alarms tab is where alarms are listed and acknowledgement actions can be taken against them.
This permission is recommended for those responsible for monitoring

**Operations: Analytics**

None, Read, Full

Determines access to the Operations > Analytics page.
The Analytics page gives administrators the ability to break down costs and usage, then filter the results by relevant delineations including Groups, Clouds, Tenants or even tag values.
This permission is recommended for those responsible for understanding utilization and costs.

**Operations: Approvals**

None, Read, Full

Determines access to the Operations > Approvals page.
When a Provision Approval-type Policy is enabled for a Group or Cloud, an approval request will be created on each relevant provision attempt. These approvals can be handled directly in the portal or dealt with in ServiceNow with a properly-configured integration.
This permission is recommended for those responsible for approving, denying, or canceling approval requests.

**Operations: Budgets**

None, Read, Full

Determines access to the Operations > Budgets page.
The Budgets page is where budgets are created and applied to clouds, tenants, users, or groups.
This permission is recommended for those responsible for managing budgets.

### Operations: Dashboards

None, Read

Determines access to the Operations > Dashboard page (default portal landing page).
The Dashboard page is a single pane of glass showing quick, easy-to-read performance and configuration information about the environment.
“Read” permission is recommended for all users. When set to None, Operations > Reports becomes the default landing page and attempts to go to the Dashboard will redirect users to their User Settings page.

**Operations: Guidance**

None, Read, Full

Determines access to the Operations > Guidance page.
The Guidance page shows recommendations for resource and cost-utilization optimization.
This permission is recommended for those responsible to optimize utilization and costs of Cloud-based resources.

**Operations: Invoices**

None, Read, Full

Determines access to the Invoices tab in Operations > Costing
The Invoices tab allows access to highly-granular historical costing data
This permission is recommended for those responsible for generating invoices and analyzing spend

**Operations: Reports**

None, Read, Full

Determines access to the Operations > Reports page.
The Reports page is where reports may be generated and exported into JSON or CSV format.
This permission is recommended for those responsible for account, infrastructure, provisioning, usage, and cost reports.

**Operations: Usage**

None, Read, Full

Determines access to the Usage tab on the Operations > Activity page.
The Usage tab shows billing information for Instances and hosts that have pricing configured on their Service Plans.
This permissions is recommended for those responsible for cost accounting.

**Operations: Wiki**

None, Read, Full

Determines access to the Operations > Wiki page.
The Wiki page allows easy UI, API and CLI access to information to be referenced or shared with others. Wiki pages encompass individual Clouds, Groups, Servers, Instances, Clusters, and other pages can be manually created. Wiki pages from resources are accessible from the Operations > Wiki page or within individual resource detail pages on their respective Wiki tabs.
This permission is recommend for those responsible for documentation and knowledge management.

**Projects**

None, Read, Full

Determines access to Projects through API
Projects are used to associate resources together and apply common tags to their invoices
This permission is recommended for those responsible for cost analysis and invoice reporting

**Provisioning Administrator**

None, Full

When editing an Instance (Provisioning > Instance > selected Instance > EDIT button), this permission determines access to changing the owner of an Instance.
Allows you to change the owning user of an Instance.
This permission is recommended for those responsible to ensure all instances are owned by appropriate personnel.

**Provisioning: Advanced Node Type Options**

None, Full

This allows or disallows access to the “Extra Options” field of the Node Types tab on the Provisioning > Library page when the Node Type Technology value is set to “VMware”.
When VMware technology type is selected for a new or existing Node Type (Provisioning > Library > Node Types), the “Extra Options” field will be available in the VMware VM Options section. These allow defining advanced vmx-file parameters during provisioning.
This permission is recommended for those responsible for managing VMware Node Types (images).

**Provisioning: Allow Force Delete**

None, Full

This allows or disallows access to the “Force Delete” action on the Infrastructure > Hosts page, including the Hosts, Virtual Machines, and Bare Metal tabs. Click Delete on the actions menu to see the check box for the Force Delete action.
Allows force delete to delete instances, virtual machines or hosts but may cause orphaned objects.
This permission is recommended for those responsible to ensure orphaned objects are removed from the portal.

**Provisioning: Apps**

None, Read, User, Full

Determines access to the Provisioning > Apps page. The “User” permission will allow access to only object the user owns.
The Apps page allows Instances to be grouped and tiered logically into Apps. From this page, Apps can be deployed from existing Blueprints and Instances can be added to existing Apps. Security groups and environmental variables (Linux Only) may be added and edited. The App log, history, and monitoring tabs may be viewed.
This permission is recommended for those responsible for provisioning.

**Provisioning: Automation Integrations**

None, Read, Full

Determines access to the Integrations tab on the Provisioning > Automation page.
The Integrations tab is where new integrations can be configured. These include Chef, Puppet, Ansible, Salt Master, Ansible Tower, vRealize Orchestrator.
This permission is recommended for those responsible for the integration between the portal and integrated automation technologies.
This permission is recommended to be set to None on the Tenant Role to restrict access for Subtenant users.

**Provisioning: Blueprints**

None, Read, Full

Determines access to the Provisioning > Blueprints page.
The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type is made available.
This permission is recommended for those responsible for defining Blueprints.

**Provisioning: Blueprints - ARM**

None, Provision, Full

Determines access to ARM-type Blueprints on the Provisioning > Blueprints page. The “Provision” permission allows for provisioning Apps from ARM Blueprints without the ability to create or edit them.
The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of ARM is available.
This permission is recommended for those responsible for defining ARM blueprints.

**Provisioning: Blueprints - CloudFormation**

None, Provision, Full

Determines access to CloudFormation-type Blueprints on the Provisioning > Blueprints page. The “Provision” permission allows for provisioning Apps from CloudFormation Blueprints without the ability to create or edit them.
The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of CloudFormation is available.
This permission is recommended for those responsible for defining CloudFormation blueprints.

**Provisioning: Blueprints - Helm**

None, Provision, Full

Determines access to Helm-type Blueprints on the Provisioning > Blueprints page. The “Provision” permission allows for provisioning Apps from Helm Blueprints without the ability to create or edit them.
The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of Helm is available.
This permission is recommended for those responsible for defining Helm blueprints.

**Provisioning: Blueprints - Kubernetes**

None, Provision, Full

Determines access to Kubernetes-type Blueprints on the Provisioning > Blueprints page. The “Provision” permission allows for provisioning Apps from Kubernetes Blueprints without the ability to create or edit them.
The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of Kubernetes is available.
This permission is recommended for those responsible for defining Kubernetes blueprints.

**Provisioning: Blueprint - Terraform**

None, Provision, Full

Determines access to Terraform-type Blueprints on the Provisioning > Blueprints page. The “Provision” permission allows for provisioning Apps from Terraform Blueprints without the ability to create or edit them.
The Blueprints page allows for the creation of pre-configured, multi-tier application definitions which can be deployed via the Apps page. With this permission the blueprint type of Terraform is available.
This permission is recommended for those responsible for defining Terraform blueprints.

**Provisioning: Clone Instance**

None, Full

Determines access to the Clone Instance selection from the Actions menu on an Instance detail page
This selection launches the wizard to begin the process of provisioning an identical Instance
This permission is recommended for those responsible for provisioning.

**Provisioning: Deployment Integrations**

None, Read, Full

Determines access to the Integrations tab on the Provisioning > Deployments page.
From this page deployment integrations may be created, edited, or deleted. On create the integration product is selected and all associated connection and authentication information must be provided. Integrations available include Git, Github, and Jenkins.
This permission is recommended for those responsible for the integration between the portal and deployment technologies.
This permission is recommended to be set to None on the Tenant Role to restrict access for Subtenant users.

**Provisioning: Deployments**

None, Read, Full

Determines access to the Deployments tab on the Provisioning > Deployments page.
The Deployments page provides the ability to use git, fetch from a URL, or upload a file to be utilized during the provisioning of an Instance or pushed to an existing Instance.
This permission is recommended for those responsible for providing and managing software.

**Provisioning: Execute Script**

None, Full

Determines access to the Run Script and Apply Template selections from the Actions menu on an Instance detail page
These selections bring up a menu allowing the user to select a script and run it against the viewed Instance or select a template to write to the Instance
This permission is recommended for those running day two automations against existing Instances

**Provisioning: Execute Task**

None, Full

Determines access to the Run Task selection from the Actions menu on an Instance detail page
This selection brings up a menu allowing the user to select a Task and run it against the viewed Instance
This permission is recommended for those running day two automations against existing Instances

**Provisioning: Execute Workflow**

None, Full

Determines access to the Run Workflow selection from the Actions menu on an Instance detail page
This selection brings up a menu allowing the user to select a Workflow and run it against the viewed Instance
This permission is recommended for those running day two automations against existing Instances

**Provisioning: Import Image**

None, Full

Determines access to the Import as Image and Clone to Image selections from the Actions menu on an Instance detail page
These selections allow users to create an image from an existing Instance or import the Instance as an image to a selected bucket
This permission is recommended for those responsible for managing the library of provisionable items

**Provisioning: Instances**

None, Read, User, Full

Determines access to the Provisioning > Instances page. The “User” permission will allow access only to objects the user owns.
Provisioning > Instances is where managed Instances are displayed, including some details about each one. It also allows containers or virtual machines to be provisioned as a single horizontally-scalable entity or service suite.
This permission is recommended for those responsible for provisioning.

**Provisioning: Job Executions**

None, Read

Determines access to the Job Executions tab on the Provisioning > Jobs page.
The Job Executions page contains execution history of completed jobs, including any process outputs and error messages.
This permission is recommended for those who are responsible for managing or troubleshooting jobs.

**Provisioning: Jobs**

None, Read, Full

Determines access to the Jobs tab on the Provisioning > Jobs page.
The Jobs page is where jobs are scheduled for the execution of automation Tasks and Workflows against Instances or servers.
This permission is recommended for those responsible to schedule the execution of Tasks or Workflows.

**Provisioning: Library**

None, Read, Full

Determines access to the Provisioning > Library page, including the Instance Types, Layouts, Node Types, Option Types, Option Lists, File Templates, Scripts, Spec Templates, and Cluster Layouts tabs.
The Provisioning Library pages is where the various library elements are created and maintained. These include: Instance Types, Layouts, Node Types, Option Types, Option Lists, File Templates, Scripts, Spec Templates, and Cluster Layouts.
This permission is recommended for those responsible for managing the library.

**Provisioning: Scheduling - Execute**

None, Read, Full

Determines access to the Execute Scheduling tab of the Provisioning > Automation page.
The Execute Scheduling page is where time schedules for Jobs, including Task, Workflow, and Backup Jobs are created.
This permission is recommended for those responsible to create and manage schedules to be selected when scheduling jobs.

**Provisioning: Scheduling - Power**

None, Read, Full

Determines access to the Power Scheduling tab of the Provisioning > Automation page.
The Power Scheduling page is where startup and shutdown times are created, these schedules can be applied via policy to Groups or Clouds.
This permission is recommended for those responsible to create and manage schedules for startup and shutdown.

**Provisioning: Service Mesh**

None, Read, User, Full

Determines access to the Provisioning > Service Mesh page, including the Services and DNS tabs. The “User” permission will allow access only to objects the user owns.
The Service Mesh page displays container services and DNS information. A service mesh ensures fast and reliable communication between containerized application services.
This permission is recommended for those responsible for container management.

**Provisioning: Tasks**

None, Read, Full

Determines access to the Tasks, Workflows, and Executions tabs on the Provisioning > Automation page.
The Tasks page is where Tasks are created and managed. Task types include: scripts added directly, scripts and templates from the Library section, recipes, playbooks, salt states, puppet agent installs, and HTTP (API) calls. The Workflows page offer both Provisioning and Operational Workflows. Workflows are used to execute one or many tasks during specified phases. The Executions page shows the status of executed Tasks and Workflows.
This permission is recommended for those responsible for creating provisioning and operational scripts.

**Provisioning: Tasks - Script Engines**

None, Full

Determines access to the Tasks tab of the Provisioning > Automation page. When full permission is given, advanced Task types will be available in the TYPE dropdown menu when new Tasks are created. Advanced Task types include Groovy Script, Javascript, jRuby Script, and Python Script.
Tasks page is where tasks are created and managed. This permission adds the ability to select Groovy Script, Javascript, jRuby Script, and Python Script from the Task Types dropdown menu.
This permission is recommended for those responsible for Tasks containing advanced script capabilities.

**Provisioning: Thresholds**

None, Read, Full

Determines access to the Scale Thresholds tab of the **Provisioning > Automation** page.
The Scale Thresholds page is where preconfigured settings for auto-scaling Instances is configured. When adding auto-scaling to an Instance, existing Scale Thresholds can be selected to define auto-scaling rules.
This permission is recommended for those responsible for defining auto-scaling for Instances.
This permission is recommended to be set to None or Read on the Tenant Role to restrict access for Subtenant users.

**Provisioning: Virtual Images**

None, Read, Full

Determines access to the Provisioning > Virtual Images page.
The Virtual Images page displays a list of all images, local and synced, that are available to deploy. Available images include those that are shipped with the portal, synced from integrated clouds, and uploaded directly into the portal by the user.
This permission is recommended for those who are responsible for image management.

**Remote Console**

None, Provisioned, Full

Determines access to the console on a Host detail page (Infrastructure > Hosts > selected Host, VM, or Bare Metal resource > Console tab). The “Provisioned” permission gives access to the console only for resources the logged in user has provisioned.
Remote console access for Instances, hosts, virtual machines, and bare metal.
This permission is recommended for those who need console access for provisioned Cloud resources.

**Remote Console: Auto Login**

No, Yes

This allows or disallows the ability to automatically log into the remote console.
The portal will automatically log into the machine using the credentials defined on the VM or Host. The credentials are defined either from the virtual image used, added via cloud-init or VMware Tools using the global cloud-init settings (Administration > Provisioning), or the Linux or Windows settings defined in User Settings.
This permission is recommended when an organization utilizes the portal to create user accounts on provisioned or managed machines, as well as, allow remote console access.

**Security: Scanning**

None, Read, Full

Determines access to the Security Packages tab on the Jobs list page (Provisioning > Jobs), Security Scanning type Jobs, and Security Subtab inside the Software tab on a server detail page where the results of security scans are viewed
Allows access to view, create, and run security scans on existing systems, as well as view the results of previously-run scans
This permission is recommended for those responsible for security compliance of existing systems

**Service Catalog: Catalog**

None, Full

Determines access to the Catalog page of the Service Catalog Persona view.
The Dashboard is the default landing page for the Service Catalog Persona view. It displays featured Catalog Items, recently-ordered Catalog items, and an abbreviated list of Inventory items.
This permission is recommended for users who will use the Service Catalog Persona to select items for provisioning

**Service Catalog: Dashboard**

None, Read

Determines access to the Dashboard page of the Service Catalog Persona view.
The Dashboard is the default landing page for the Service Catalog Persona view. It displays featured Catalog Items, recently-ordered Catalog items, and an abbreviated list of Inventory items
This permission is recommended for users who will use the Service Catalog Persona for quick access to new Inventory items and featured Catalog items.

**Service Catalog: Inventory**

None, Full

Determines access to the Inventory page of the Service Catalog Persona view.
The Inventory is the complete list of user-owned items provisioned from the Service Catalog.
This permission is recommended for users who will use the Service Catalog Persona and need to be able to view details on the items they’ve provisioned from the Catalog.

**Snapshots**

None, Read, Full

Determines access to the “Create Snapshot” function in the Actions menu on an Instance detail page (Provisioning > Instances > selected Instance).
This permission is recommended for Instance owners who should be allowed to take snapshots.

**Tools: Archives**

None, Read, Full

Determines access to the Tools > Archives page.
Archives provides a way to store files and make them available for download by scripts and users. Archives are organized by buckets. Each bucket has a unique name that is used to identify it in URLs and Scripts.
This permission is recommended for those responsible for storage or scripts which will use the Archive.

**Tools: Cypher**

None, Read, User, Full, Full Decrypt

Determines access to the Tools > Cypher page. The “User” permission will allow access only to objects the user owns. The “Full Decrypt” permission will allow for decryption of secrets.
Secure key/value store. Cypher keys can be used in scripts.
Recommended for those who need to store or use security key value pairs.

**Tools: Image Builder**

None, Read, Full

Determines access to the Tools > Image Builder page, Image Builds, Boot Scripts, and Preseed Scripts tabs.
The Image Builder tool creates vmdk, qcow2, vhd and raw images. The Image Builder creates a blank VM in VMware, attaches an OS ISO, executes a boot script on the VM at startup via VNC, which calls a Preseed script that runs the unattended OS installation and configuration. The platform then executes an OVA export of the completed vmdk to the target storage provider and converts the image to all other specified formats.
Recommended for those who are responsible for image creation.

**Tools: Kubernetes**

None, Read, User, Full

Allows for the management of Kubernetes clusters via the API (may be deprecated in the near future).
Allows for the management of Kubernetes clusters via the API
This permission is recommended for those who need to manage Kubernetes clusters via the API.
It is recommended this permission is set to None on the Tenant Role to restrict access for Subtenant users.

**Tools: Migrations**

None, Read, Full

Determines access to the Tools > Migrations page
The Migration tool creates a snapshot of an existing VM, converts it to the destination format and provisions the machine on the target.
Recommend only for those responsible for lifting and shifting VMs.
It is recommended this permission is set to None on the Tenant Role to restrict access for Subtenant users.

**Tools: Self-Service**

None, Read, Full

Determines access to the Tools > Self-Service page
The Self-Service pages allows administrators to configure easily-deployable catalog items for Service Catalog Persona users
Recommended for those tasked with creating and curating items for the self-service catalog

**None - No Permissions**

None

When all permissions are set to None, the following behavior can be expected: This allows only access to the User Setting page displayed, which is accessed by clicking on the user’s name in the upper-right corner of the application window.
The User Settings page is where users may upload their photo, enter values for username, first name, last name, email address, and password, as well as, defining both user-specific Linux and Windows settings (usernames, passwords, and SSH Key for Linux to be added to machines during provisioning). Additionally, generating and refreshing API Access tokens is done via this page.

### Creating Roles

User Roles
User Roles can be single or Multitenant.
A Multitenant User Role is automatically copied into all existing subtenants as well as placed into a subtenant when created. Useful for providing a set of predefined roles a Customer can use. The Multitenant Locked option prevent subtenant from modifying FEATURE ACCESS settings in the Role. Note Group, Instance Type and Blueprint Access settings will still be editable as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

**Important**

Multitenant Roles still need to be configured/managed be each subtenant, as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

*Note
User Roles cannot exceed Tenant Role permissions. If a Multitenant User Role has higher permissions than the Tenant Role assigned to a subtenant, the Multitenant User Role permissions in that Tenant will automatically be reduced to match the Tenant Role permissions.

**Create a Single Tenant User Role**

In the Master Account, navigate to Administration -> Roles

Select + CREATE ROLE

Enter a name for the Role and optional Description

For TYPE, select “User Role”

Leave the “Multi-tenant Role” checkbox blank.

Optionally select an existing Role to copy in the COPY FROM ROLE dropdown. * This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.

Select SAVE CHANGES

After saving the Role will be created, and you will be redirected to the Roles Permissions settings.

**Create a Multitenant User Role**

A Multitenant User Role is automatically copied into all existing subtenants as well as placed into a subtenant when created. Useful for providing a set of predefined roles a Customer can use. The Multitenant Locked option prevent subtenant from modifying FEATURE ACCESS settings in the Role. Note Group, Instance Type and Blueprint Access settings will still be editable as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

In the Master Account, navigate to Administration -> Roles

Select + CREATE ROLE

Enter a name for the Role and optional Description

For TYPE, select “User Role”

Optionally select an existing Role to copy in the COPY FROM ROLE dropdown. * This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.

Select the Multitenant ROLE checkbox

Optionally select the Multitenant LOCKED checkbox * When enabled, the FEATURE ACCESS settings in the Role will not be editable by subtenants. Group, Instance Type and Blueprint Access settings will still be editable as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

Select SAVE CHANGES

After saving the Role will be created, and you will be redirected to the Roles Permissions settings.

**Important**

Multitenant Roles still need to be configured/managed be each subtenant, as Groups are unique per Tenant, and Instance and Blueprints can be a mix of unique and shared items.

*Note
User Roles cannot exceed Tenant Role permissions. If a Multitenant User Role has higher permissions than the Tenant Role assigned to a subtenant, the Multitenant User Role permissions in that Tenant will automatically be reduced to match the Tenant Role permissions.

## Tenant Roles

A Tenant Role sets the highest possible permissions for a Tenant.
User Roles within that Tenant cannot exceed those of the Tenants assigned Tenant Role.
Tenant Roles can be assigned to single or multiple Tenants, and do not apply to the Master Account.

To create a Tenant Role:

In the Master Account, navigate to **Administration -> Roles**

Select + CREATE ROLE

Enter a name for the Role and optional Description

For TYPE, select “Tenant Role”

Optionally select an existing Role to copy in the COPY FROM ROLE dropdown.
*This will configure the new Role with the same configuration as the selected role to copy. A new role that is not copied from another role will be generated with all permissions set to NONE.

Select SAVE CHANGES

After saving, the Role will be created and you will be redirected to the Roles Permissions settings.
