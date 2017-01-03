{{{
"title": "Workspaces and Sharing",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Workspaces & Sharing
In this article:
* Overview
* Creating and Adding Members to Workspaces
* Sharing Boxes, Instances, and Providers

### Overview

In ElasticBox, boxes let you deliver applications predictably. Sharing enables others to reuse your box configuration or work collaboratively to build better applications.

ElasticBox lets you share three types of assets: boxes, instances, and providers. You decide the level of access that works best when you share. Share with users or with workspaces and give them view or edit access. When you share with a workspace, all workspace members get equal access to an asset.

A workspace is a shared environment in which members of that workspace can access the same providers, boxes, and instances. When you first sign in to ElasticBox, you only have a personal workspace called My Workspace. After that, you can create your own workspaces or be invited to others’. Workspaces are contextual. When you switch workspaces you see a whole different group of instances, boxes, and providers, which belong only to that workspace.

**Example**

Say you have a Jenkins box that integrates and stages code for testing. You want to collaborate with other Jenkins experts to make the box configuration highly usable. So you give their workspace edit access. Next, the QA team needs this box to deploy and run tests, so you give their workspace view access. Now the QA team can deploy Jenkins instances, but as you’d expect, they aren’t allowed to change the underlying Jenkins box definition.

### Creating and Adding Members to Workspaces

To create a workspace, click **New Workspace**.
![workspace-and-sharing1.png](../images/ElasticBox/workspace-and-sharing1.png)

This brings up the New Workspace dialog. Here you can upload an icon for the new workspace, give it a name, and add users. To add users just start to type the name of the user in the Members field. ElasticBox generates a list based on a match of the text.
![workspace-and-sharing2.png](../images/ElasticBox/workspace-and-sharing2.png)

When you add a user, they automatically get access to the workspace and any assets it contains, such as providers, boxes, and instances.

**Managing Workspaces**
When you create a workspace, you are its owner and as such you can edit and manage it.
To edit a workspace you created, click the pencil icon for the workspace.
![workspace-and-sharing3.png](../images/ElasticBox/workspace-and-sharing3.png)

In this dialog, you can add and remove users as well as delete the workspace.
![workspace-and-sharing4.png](../images/ElasticBox/workspace-and-sharing4.png)

### Sharing Boxes, Instances, and Providers
When you create a box, launch an instance, or add a provider you own the asset by default. You can control how others use it by giving them view or edit access. Edit access gives users the same level of access as the owner. Only, they can’t delete the asset.

**Steps**
1. From the box, instance, or provider detail page, click **Share**.
   ![workspace-and-sharing5.png](../images/ElasticBox/workspace-and-sharing5.png)

2. In the sharing dialog, type the name of the users or workspaces you want to share with and select them.
   ![workspace-and-sharing6.png](../images/ElasticBox/workspace-and-sharing6.png)

3. For each user or workspace that you added, give view or edit access. They get edit access by default.
   ![workspace-and-sharing7.png](../images/ElasticBox/workspace-and-sharing7.png)

**Stop Sharing**
To discontinue sharing with a user or workspace, open the sharing dialog, and remove them.
![workspace-and-sharing8.png](../images/ElasticBox/workspace-and-sharing8.png)

**Transfer Ownership**
Sometimes, because your role in the organization changes, you may want to transfer an asset you own to another user or workspace. To change owners, open the sharing dialog, and make another user or workspace the owner. An asset can only have one owner at a time.
![workspace-and-sharing9.png](../images/ElasticBox/workspace-and-sharing9.png)

**Sharing Boxes**
When you want others to change your current box configuration or collaborate with you to define a better box, give them edit access to it. Give view access only when they need to consume your box configuration, but not make changes, like deploying for example.

View only gives them access to versions of the box, not the current state of its configuration, which may or may not be stable. When stable, the scripts and variables are working, version the box and then give view access to those that need it.

In view mode, users automatically get access to all versions of a box, but can’t share with others. They can do the following:

* Access all versions of the box in read-only mode.
* Deploy a box.
* View events and variables.
* Pull a box version into the instance lifecycle editor to update configuration.

**Sharing Instances**
A couple of reasons to share instances is to let others use it or get help with testing or debugging for example. If it’s the latter, you can get help by giving them edit access to your instance. That lets them make changes to your instance configuration.

Also you may give view access to make an instance available for others to use, say as a binding. For example, although view access to a database instance prevents developers from making changes to the database configuration, they can bind to it and run tests.

**Sharing Providers**
Sharing providers has its benefits. You can give view access to company-approved providers and let users deploy to that particular provider. When teams deploy to a shared provider, you can track org-wide usage and compliance cohesively. Provider accounts can be shared only in the Enterprise Edition.

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
