{{{
  "title": "Getting Started with CLC Ansible Modules",
  "date": "07-15-2015",
  "author": "Benjamin Harristhal",
  "attachments": [],
  "contentIsHTML": false
}}}

[Ansible](http://www.ansible.com/home) is a powerful automation tool used by Devops throughout the industry to deploy applications and manage environment complexity.  

The CenturyLink Cloud Ansible Modules allow DevOps engineers to use popular provisioning tool Ansible to define and manage infrastructure resources on the CenturyLink Cloud platform.

The CenturyLink Cloud Ansible Modules are available from [pip](https://pypi.python.org/pypi/clc-ansible-module) and [github](https://github.com/CenturyLinkCloud/clc-ansible-module)

Our modules operate seamlessly with Ansible as a bolt-on extension.  The project [README](https://github.com/CenturyLinkCloud/clc-ansible-module) provides instructions as to how to install the modules and configure your environment. We plan to integrate these modules with the Ansible project in a future release.

Modules support the following capabilities:

-	Inventory/Dynamic-Inventory.  This allows a user to focus primarily on the intent of their Playbook, without managing a list of servers within their account.
-	Create and delete an Anti-Affinity Policy for Hyperscale servers.
-	Create and delete a group within an account.  Groups help organize resources within the account hierarchy.
-	Create and delete a shared load balancer.
-	Create, manage and delete a server or a group of server resources.
-	Modify the resources currently allocated to a server.  For example, CPU and/or memory.
-	Create and delete a single Hyperscale server or multiple HyperScale servers.
-	Invoke a package against a server.  The package must be an existing package within the CenturyLink Cloud Platform.
-	Create and delete a public IP for a server.
-	Create, restore, and delete a server snapshot.

Note: Authentication is performed at the account alias level so users only have access to resources and data centers currently associated with their account.

These modules provide a useful baseline set of features to allow any user to fully leverage the power of Ansible to manage CenturyLink Cloud resources.
