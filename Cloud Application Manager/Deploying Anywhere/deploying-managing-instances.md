{{{ "title": "Deploying and Managing Instances",
"date": "11-27-2018",
"author": "Guillermo Sánchez",
"keywords": ["cam", "instances", "lifecycle", "deploy", "deployment-policy"],
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Instances page](#instances-page)
* [Deploying a New Instance](#deploying-a-new-instance)
* [Scheduling Instances](#scheduling-instances)
* [Handling Instance Lifecycle States](#handling-instance-lifecycle-states)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

This article is meant to assist Cloud Application Manager customers in the management of their instances.

### Audience

Cloud Application Manager customers.

### Prerequisites

An active Cloud Application Manager account.

### Instances page

The Instances left side menu option of the Applications site allows you to see at a glance a view of all instances you have access to through your configured providers in your current scope.

![All instances page](../../images/cloud-application-manager/instances/all-instances.png)

There are three different submenu options under Instances:

* **All**: shows all type of instances, either registered or unregistered.

* **Registered**: shows only registered instances, which are the ones deployed through or imported into Cloud Application Manager. In these instances, you can do lifecycle management by executing lifecycle events or using the lifecycle editor to change variables, event scripts or box versions of the instance. You can also select a specific state among the available ones (Online, Unavailable, Processing, Shutdown, Terminated) to show only the instance in the selected state.

* **Unregistered**: shows only unregistered instances, which are the ones accessible into all the defined providers that were not deployed through Cloud Application Manager. They are discovered in the synchronization event of a provider and are classified by Type and Subtype.
  * Type: One of Compute, Network, Database, Storage or Other
  * Subtype: this is the instance class, specific to each provider type. For example, for AWS type providers we can see VPC or Application Load Balancers (for Network type instances), and S3 or Elastic Block Storages (for Storage type instances)

  You can also select a specific state among the available ones (Active, Inactive) to show only the instance in the selected state.

The Instances page displays on the top of the page a new button, a search field  and a filters and instance view buttons. The search field allows you to find any instance looking for most of the instance fields such as name, instance-id, service-id, public or private IP address, support_id, hostname, owner or last user who acted on the instance.

Below this components you can find the corresponding list or graph of instances, depending on the view type that is selected.

In the instances list, any Compute type unregistered instance can be registered (imported) into Cloud Application Manager to enable lifecycle management on it (an icon button allowing it will appear at the end of its row), so it will be shown from them on as a registered instance in the corresponding views. The Unregistered Instances tab in the provider details page remains unchanged showing only compute registerable instances. If you want to bulk register (import) several instances from the same provider, use this feature from there instead, where bulk register is also available as a bulk action.

#### Instance view types

In the top right corner of the Instances page there are several icons to select the type of view that is being shown:

![Instances view types](../../images/cloud-application-manager/instances/instance-view-types.png)

These icons are respectively:

* **Topology view**: shows a graph with the instances type and its relationships (bindings)
* **List view** (default): shows a list view of all instances
* **Provider view**: shows a list view of all instances grouped by provider
* **Map view**: shows a world map view of all instances grouped by location

#### Instance view filters

There is a filter icon button next to the view types icon that makes visible all available filters for the view:

![Instances view filters](../../images/cloud-application-manager/instances/instance-filters.png)

These filters are dynamically filled with the valid values, allow multiple selections in values and are respectively:

* **Cost Center**: Filter by cost centers responsible for instances
* **Workspace**: filter by any accessible workspace containing instances
* **Providers**: filter by available provider types or providers
* **Types**: filter by available types or subtypes
* **Location**: filter by available location, including Global
* **Tags**: filter by defined tags in instances

Some of the filters, such as Providers and types, have two level of filtering (i.e., provider type and provider), allowing a mixed selection of levels. For example, you can select AWS provider type to show all AWS providers instances, and a specific Microsoft Azure provider to also show this provider instances in the same view.

### Deploying a New Instance

An instance is an instantiated version of a box launched to provider’s virtual infrastructure or your own. Follow these steps to launch one.

**Steps**

1. Click **Instances** > **New**
2. Select a box. You can search and look through the tabs.

  ![Explore to select box from catalog](../../images/cloud-application-manager/deploy-instance-selectboxfromcatalog-1.png)

  * **Boxes**. Shows boxes you created in your workspace.
  * **Explore**. Shows default boxes available to all Cloud Application Manager users. These include service boxes such as Linux Compute, Windows Compute; includes AWS services like MySQL Database, Oracle Database, DynamoDB, PostgreSQL Database, and S3 bucket; and includes the Azure Microsoft SQL Database service. You can directly launch an instance to these database services. While you can’t modify those boxes, you can combine them with other boxes to build multi-tiered applications.

  **Note:** Don’t find a box you’re looking for? Check if you’re in the right workspace. Remember that you may not have access if the box is no longer shared with you.

3. In the New Instance dialog, specify the instance name and deployment policy.

   **Name.** Give a name to recognize the instance.

   **Deployment Policy.** Select a previously created deployment policy or create a new one. For details, see [Creating a Deployment Policy](../Automating Deployments/deploymentpolicy-box.md).

4. In the New Instance dialog, pass deployment parameters under **Variables**. Before launching, you can override and provide fresh values.

  ![Providing default configuration values to new instances](../../images/cloud-application-manager/instance-provideconfigurationvalues-2.png)

  * Listed here are all the variables defined in the main box as well as those within nested boxes or box type variables.
  * Required variables are marked with an asterisk. To see all variables including optional ones, click Show More.
  * When a variable is required, you must specify its value to launch an instance of the box. If optional, you can launch without giving values, and do it later in the [lifecycle editor](../Core Concepts/lifecycle-editor.md).
  * [Binding type variables](../Automating Deployments/parameterizing-boxes-with-variables.md) are also listed here. Depending on how it’s defined in the box, you can select as its value any instance or that of a specific box type deploying or active in the workspace.

### Scheduling Instances

Save on compute and hosting costs by scheduling instances at launch time. Rather than remember to turn off a machine manually, schedule it to stop automatically at your convenience. When launching, you can schedule an instance to shut down or terminate at a given UTC time.

We notify you of instances about to expire in 24 hours by email at around 12 AM UTC. From the email, you can navigate to the instance page and change the schedule if you like. If you don’t get this email, check your email spam filters or check if [SMTP outbound is on](../Appliance/appliance-initialsetup.md) in the setup console for the Cloud Application Manager appliance.

Follow these steps to schedule an instance.

**Steps**
1. From the Instances page, click **New**.
2. Select a box you want to deploy.
3. In the New Instance dialog, select the **Shutdown** or **Terminate** operation from the **Expiration** drop-down.  
  Select **Always on** if you don’t want to schedule anything. Shutdown powers off the instance while Terminate deletes the instance on the provider’s side.

  ![Instance expiration operation](../../images/cloud-application-manager/schedule-instance-chooseoperation-6-2.png)

4. For the selected operation, set a predefined or custom UTC schedule.

  ![Scheduling shutdown for new instances](../../images/cloud-application-manager/schedule-instance-selectschedule-7-2.png)

5. When done, click **Deploy**.

  **Note:** Even if you don’t schedule an instance at the time of deploying, you can do so later. Once online, you can go to an instance page and in **Edit Details**, set the schedule.

  Besides the user interface, you can automatically schedule instances using the instances API with a [POST or PUT](https://www.ctl.io/api-docs/cam/#application-lifecycle-management-instances-api) request.

### Handling Instance Lifecycle States

Instance actions (on the instances page or the lifecycle editor) trigger deployment-related event scripts from your box. Take these actions to start, stop, terminate an instance, and even perform upgrades or make changes to your live instance.

Some actions are available only after the instance changes state. For example, you can’t forcibly terminate an instance until you’ve terminated it first.

Go to the Admin Console to [manage several instances](../Administering Your Organization/manage-assets-monitor-usage.md) spread across users and workspaces in your organization.

  ![Instance actions menu](../../images/cloud-application-manager/instance-states-8-2.png)

**Reconfigure**

This executes the configure events from the box.

**Reinstall**

This re-runs the install scripts from your boxes onto the existing virtual infrastructure. This is useful if you made changes to your scripts within this instance, say to upgrade the instance to a new box version. A reconfigure automatically follows the reinstall.

**Power On**

This virtually powers on your instance. It’s useful in case you’ve shut the instance down. After powering on, the configure and start scripts from the box execute.

**Shut Down**

This runs the stop scripts from your box instance and cleanly shuts down the OS. It’s useful if your instance does not need to be up 24/7. As some cloud providers only charge for running instances, this can save money.

**Terminate**

This executes the dispose scripts from your box instance and then deletes the virtual infrastructure. You can’t revert the action and since you can lose data, be sure that you want to perform this action in the first place.

**Force Terminate**

If a Terminate fails for some reason (maybe a broken dispose script), then this forcibly deletes the virtual infrastructure. If you previously terminated or deleted an instance from the provider’s side, the instance may linger in Force Terminate in Cloud Application Manager. Give it a couple of minutes then try to force-terminate again.

**Force Online**

Allow user with "Admin" role to reset the state of an instance in case it went into the "unavailable" state when the last attempted operation was Reconfigure or Reinstall.

**Delete**

Click the delete icon after you Terminate or Force Terminate an instance. Until then, the box instance page and logs are retained in the Cloud Application Manager database. However, delete completely removes the box instance page.

**Clone**

This creates a new instance with the selected instance’s settings, but you can modify all of them before launch the new deployment.

**Update Instance**

This lets you modify the box version; you can select one of the other box versions. After choosing the new version, the instance is going to be reinstalled.

**Edit Details**

This shows the instance’s details that you can modify. These details are: icon, name, description, tags, expiration, updates (available for box versions only) and automatic reconfigure.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at /ProgramData/ElasticBox/Logs/elasticbox-agent.log
