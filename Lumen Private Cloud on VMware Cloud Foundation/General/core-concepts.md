{{{
  "title": "Core Concepts",
  "date": "5-17-2018",
  "author": "Anthony Hakim",
  "keywords": ["cpc", "cloud", "vm", "core", "vcloud", "vapp", "template", "vcf"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we will explore the core concepts that are within the VMware vCloud Director User Interface (UI) that makes up your CenturyLink Private Cloud on VMware Cloud Foundation™ environment.

### Core Concepts
VMware vCloud Director (vCD) provides role-based access to a Web console that allows the members of an organization to interact with the organization's resources to create and work with vApps and virtual machines (VMs).

vCloud Director uses the following core components:

| Component | Definition |
| --------- | ---------- |
| Catalogs | A catalog is a collection of vApps, vApp templates, and media files in an organization. The members of an organization that have access to a catalog can use the catalog's vApp templates and media files to create their own vApps. Organization administrators can copy items from public catalogs to their organization catalog.|
| Organization | An organization is a unit of administration for a collection of users, groups, and computing resources. Users authenticate at the organization level, supplying credentials established by an organization administrator when the user was created or imported. |
| Organization Virtual Data Centers (VDCs) | An Org VDC provides resources to an organization. VDCs provide an environment where virtual systems can be stored, deployed, and operated. They also provide storage for virtual CD and DVD media. An organization can have multiple VDCs. |
| Organization VDC Networks | An Org VDC Network is contained within a vCD Org VDC and is available to all the vApps in the organization. An Org VDC Network allows vApps within an organization to communicate with each other. An Org VDC Network can be connected to an external network or isolated and internal to the organization. Only system administrators can create Org VDC Networks, but organization administrators can manage Org VDC Networks, including the network services they provide. |
| Users and Groups | An organization can contain an arbitrary number of users and groups. Users can be created locally by the organization administrator or imported from a directory service such as LDAP. Groups must be imported from the directory service. Permissions within an organization are controlled through the assignment of rights and roles to users and groups. |
| vApps | A vApp consists of one or more virtual machines (VMs) that communicate over a network and use resources and services in a deployed environment. |
| vApp Networks | A vApp Network is contained within a vApp and allows VMs in the vApp to communicate with each other. You can connect a vApp Network to an Org VDC Network to allow the vApp to communicate with other vApps in the organization and outside of the organization, if the Org VDC Network is connected to an external network. |
| vApp Templates | A vApp template is a VM image that is loaded with an Operating System (OS), applications, and data. |
