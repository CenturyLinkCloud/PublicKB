{{{
"title": "Lifecycle Editor",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Lifecycle Editor

The Lifecycle Editor offers a single, unified interface to test and refine your box configurations in live deployments. The editor is powerful because you can reapply box changes and look at how they’re executed immediately on the instance through logs.

**In this article:**

* Launching the Lifecycle Editor
* Modifying a Box Instance
* Re-launching the Instance with Changes
* Viewing instance logs
* Versioning with Push and Pull

### Launching the Lifecycle Editor

Right after you launch an instance, the Lifecycle Editor is available on the instance profile page. To get to it, click an instance from the Instances page as shown.

![lifecycle-editor-1.png](../images/ElasticBox/lifecycle-editor-1.png)

The instance profile page shows the activity feed of the instance during its entire lifecycle and lets you take actions on the instance. Click the Lifecycle Editor to edit and make changes on the running instance.

![lifecycle-editor-2.png](../images/ElasticBox/lifecycle-editor-2.png)

### Modifying a Box Instance

Edit the box configuration of a running instance by modifying its event scripts and variable values. While you can change existing configuration, you can’t add new events or variables. For example, you’ll have to go back to the box catalog if you want to change the underlying boxes that your instance consumes.

**Changing Events**

[Events](./start-stop-and-upgrade-boxes.md) let you control the lifecycle of your application in the virtual infrastructure. Change them to modify how your application behaves.

![lifecycle-editor-3.png](../images/ElasticBox/lifecycle-editor-3.png)

1. To edit an event, traverse the box topology, and select the event. In this example, we selected the install event of the NODE box.
2. Make event script changes in the event tab. The tab shows an asterisk to indicate any unsaved changes.
3. When done, click **Save**.

**Changing Variable Values**

You can redeploy an instance with different parameters by changing the [variable](./parameterizing-boxes-with-variables.md) values.

* To edit variable values, click the pencil icon for a variable and change its value.
* To edit file type variables, click the pencil icon and click **Edit File**.

![lifecycle-editor-4.png](../images/ElasticBox/lifecycle-editor-4.png)

**Changing Binding Variable Values**

When an instance depends on another box or service–like a load balancer, caching, or database service–you can link them together with a [binding](./parameterizing-boxes-with-variables.md). In the Lifecycle Editor, you can modify the binding value to select a different instance.

![lifecycle-editor-5.png](../images/ElasticBox/lifecycle-editor-5.png)

1. Under the Variables section, click the pencil icon to edit the binding variable.
2. For its value, select a deploying or running instance from your current workspace. To reset the current value, click the trash icon.

### Re-Launching the Instance with Changes

Once you’ve saved changes in the lifecycle editor, they are locally stored until you trigger a lifecycle action on the instance. You can re-apply changes to the running instance by triggering an install or configure event, which runs the box event scripts in the virtual infrastructure. To learn about other actions you can take, see [Handling Instance Lifecycle States](./deploying-managing-instances.md).

In this example, we click **Reinstall** to run install type events in the virtual environment. Install type events include all the install and post install event scripts in the main and nested boxes.

**Note:** When an action is triggered, the instance is in the process of changing state. During this time, it’s in view-only mode and you can’t edit its configuration. But, you can view logs. Once the scripts are executed, you can go back to editing the instance.

![lifecycle-editor-6.png](../images/ElasticBox/lifecycle-editor-6.png)

### Viewing Instance Logs

The logs panel presents the standard output of event scripts that were executed on the target virtual machine. After making script changes and triggering a lifecycle action on the instance, you can readily see their run output here.

Click **Logs** to monitor the progress on the instance while its being re-installed and reconfigured.

![lifecycle-editor-7.png](../images/ElasticBox/lifecycle-editor-7.png)

### Versioning with Push and Pull

Changes you make in the Lifecycle Editor are local to the instance and are not propagated back to the box in the catalog. You can however, do a push from the instance back to the box definition. This makes a new version of the box available with these changes in the Versions tab. This is pretty useful for iteratively developing boxes without having to re-deploy from scratch.

Additionally you can also pull a version from the box definition. This is useful if you wish to revert to a different version or want to upgrade an instance to the latest version of a box.

Click the up arrow to push or the down arrow to pull as shown in the variables section.

![lifecycle-editor-8.png](../images/ElasticBox/lifecycle-editor-8.png)

* Push creates a new version of the box in the box catalog based on the changes made in the Lifecycle Editor. This updates both the event scripts of that box as well as the variable contents.
* Pull copies the version you select of the box from the box catalog and brings it onto the box instance. This is useful for either upgrading an instance to a new version of a box or for reverting changes.

**Note:** ElasticBox provides default boxes that are available to all users. You can use them for your deployments and modify, test the instance configuration in the Lifecycle Editor. However, because everyone accesses these boxes, you can’t push or pull to modify their box definition.

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](https://www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
