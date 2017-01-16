{{{
"title": "Script Boxes",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

The Script box is the type you most commonly use to define deployments. It accepts commands in Bash, PowerShell, Salt, Ansible, Chef, or Puppet. ElasticBox provides Chef and Puppet public boxes to install and run recipes or manifests locally.

**In this article:**

* Creating your first script box
* Adding child script boxes

### Creating Your First Script Box

On the Boxes page, click **New > Script**. Enter a name, optionally a description and other [metadata](./boxes.md). Save to continue. Configure the deployment using [events](./start-stop-and-upgrade-boxes.md) and [variables](./parameterizing-boxes-with-variables.md).

When ready to test the configuration, click **Deploy**. Under the Deployment Box, search or select a deployment policy. Policies whose claims match the script box requirements appear here.

Don’t find what you need? Then click **Create a new deployment policy box**.

The easiest way to understand script boxes is to build one. Follow this tutorial to build a simple box that says [Hello World](//www.ctl.io/guides/).

### Adding Child Script Boxes

Let’s build on top of the [Hello World](//www.ctl.io/guides/) box as an example. To set up full-scale application deployments, you need to stitch components or micro components together. You do that by stacking child boxes within a parent. In this example, we’ll stack the Hello World box within another box.

Create a new Script box and call it Greeting. Tag that it needs Linux. To learn more, see requirements and auto updates under [Box Basics](./boxes.md).

![scriptboxes1.png](../images/ElasticBox/scriptboxes1.png)

Now add a new variable of type **Box**. This allows the greeting box to consume the services of another. Click **New** in the variable section and add a box variable as shown. Set the variable name to GREETER and for the value, select the **Hello World** box.

![scriptboxes2.png](../images/ElasticBox/scriptboxes2.png)

Now that Hello World is nested in the Greeting box, we can replace Hello World box variables with values we want. To do this, expand the GREETER variable and edit (click the pencil icon) the GREETING sub variable.

![scriptboxes3.png](../images/ElasticBox/scriptboxes3.png)

Edit this to say hello to someone else.

![scriptboxes4.png](../images/ElasticBox/scriptboxes4.png)

Now we overwrote the original value of the GREETING variable from the Hello World box. To go back to its original value, we can click the trash can icon to the right of the pencil icon.

**Note:** You can quickly tell which variables values are overridden because they change from italicized to regular text.

![scriptboxes5.png](../images/ElasticBox/scriptboxes5.png)

See what we did? We consumed a box configuration and changed deployment values of the child box within the context of the parent. Remember that the original child box definition of Hello World, in this case, is not affected. When you deploy the Greeting box in this example, it also deploys the Hello World box in the same instance.

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
