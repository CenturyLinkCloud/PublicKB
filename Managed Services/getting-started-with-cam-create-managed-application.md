{{{
  "title": "Getting Started with Managed Applications in CAM",
  "date": "12-18-2017",
  "author": "Keith Homco",
  "attachments": [],
  "contentIsHTML": false
}}}

### Create Managed Application in Cloud Application manager

Learn how to create a Managed Application within CAM, to be supported and managed by CenturyLink.  At the time of writing this article, this is intended for internal users of CenturyLink and most specifically those familiar with Managed Services Anywhere.  As the process is refined, the creation of Managed Applications will be expanded to a wider audience. This includes customers wanting their custom applications managed by CenturyLink.

Before you start, sign up for an Cloud Application Manager account (account currently expected to be within the CenturyLink organization).

Then, follow these simple steps.

* Configure a script box for your application
* Create script box to be Managed version of your application
* Add Managed Application script box as variable
* Pass necessary values to Managed Application script box
* Create Monitoring policy
* Publish your script box


### Configure Script Box for Your Application

We suggest, from experience, to develop the installation and configuration of your application in a script box that could be deployed independently of being managed. Following this practice allows for taking existing applications developed in script boxes and applying the following steps to make it a Managed Application.

So, that is what we will do for simplicity of this article; I will use an existing script box available in CAM.  I will use the MongoDB Server script box.

![cam-mongodb-scriptbox.png](../images/cloud-application-manager/cam-mongodb-scriptbox.png)

Now that my work here is done, let's move on to the next step.

### Create Managed Script Box for Your Application

Here we will create another script box that will act as a container for our application installation/deployment as well as the efforts of make managed.  Below is our new Managed MongoDB Server script box.

![msa-managed-mongodb-scriptbox.png](../images/managed-services-anywhere/msa-managed-mongodb-scriptbox.png)

Here I have gone ahead and added the Managed Application script box (**TODO: explain how/where to find this script box**) as well as the MongoDB Server script box as variables.

**Note: Select the appropriate platform (windows/linux) implementation of the Managed Application script box for your needs.**

![msa-managed-mongodb-scriptbox-vars.png](../images/managed-services-anywhere/msa-managed-mongodb-scriptbox-vars.png)

### Pass Application Values to Managed Application Box

Learn how to pass values to the Managed Application script box for making your application available for support by CenturyLink.

First, I should point out the lifecycle events of a Managed Application. When a Managed Application is deployed, the Make Managed process will be triggered and executed on the compute prior to your application script box.  It is during your script box execution that the Managed Application script box will execute at both the **pre_start** and **start** lifecycle events.  The **pre_start** is simply detecting whether or not the Make Managed process for the compute was successful prior to moving forward.  If it had failed silently for some reason, the script box will be halted here.

Then, it is expected that the application being managed would be either started already or be started in the **start** lifecycle event.  This is where the order of the variables shown earlier is important; the application script box must come **before** the Managed Application script box. It should only be after the application has successfully started that a call to make it managed be made.

So, with all of that said, we will actually be using any lifecycle event prior to the **pre_start** to pass the appropriate values to the Managed Application script box. This is typically best suited to be done in the **configure** event of the parent script box: *Managed MongoDB Server* script box in this case.

Below is an expanded view of the boxes included in this script box and their respective variables for reference.

![msa-managed-mongodb-scriptbox-expanded.png](../images/managed-services-anywhere/msa-managed-mongodb-scriptbox-expanded.png)

Here is a figure of the partially expanded events section. Note that **configure** is the only populated event for the parent script box, as it is acting as a kind of mapping between the application script box and the Managed Application script box.

![msa-managed-mongodb-events-expanded.png](../images/managed-services-anywhere/msa-managed-mongodb-events-expanded.png)

And you can see that I have populated the **configure** event with some code.  Below are the contents of that lifecycle event:

```shell
$username = "{{ mongo.username }}"
$password = "{{ mongo.password }}"
$log_path = "{{ mongo.LOG_PATH }}"
$port     = "{{ mongo.mongodb }}"
$db_path  = "{{ mongo.DB_PATH }}"

$config = "{'username': '$username', 'password': '$password', 'db_path': '$db_path', 'logs': '$log_path', 'db_port': '$port'}"

elasticbox set app.vars.APPLICATION_NAME "mongodb"
elasticbox set app.vars.APPLICATION_DESCRIPTION "My managed cross-platform document-oriented database"
elasticbox set app.vars.APPLICATION_VERSION "{{ mongo.VERSION }}"
elasticbox set app.vars.APPLICATION_CONFIG $config
```

The above shell script is essentially mapping values from the MongoDB Server script box installation over to the Managed Application script box.  The **APPLICATION_CONFIG** is intended for any additional metadata you wish to provide about the application that would be valuable for its ongoing support.

Also note the **APPLICATION_NAME**; this value is important as it will be used to map this application with its corresponding monitoring policy in the next step.

### Create Monitoring Policy

Let's head over to the Monitoring page (https://monitoring.cam.ctl.io/) where we will create the appropriate policy for monitoring our application.  I will keep it simple for the sake of this article, but do be sure to create a thorough policy for monitoring your application.

**Note: Create your policy in the same workspace as you created your managed application script box**

After creating the monitoring policy, send an email to <watcher-be-doing-good-stuff-deez-dayz@ctl.io> with the following content:

```
Dear Watcher-People,

I am requesting the creation of a new Managed Application for "<name-of-managed-application>" with the monitoring policy named "<name-of-monitoring-policy>" under the "<name-of-workspace-scriptbox-resides>" workspace.

Please review the policy and provide the JSON of the policy along with the application name of "<name-of-application-defined-in-scriptbox>" to the Managed Services Anywhere team for review.

Thank you,
<your-coolest-nickname-ever>
```

The Watcher team will use their special powers to transform the policy into a JSON document that the Managed Services Anywhere team can consume and store with a mapping to the application name provided.  This way, whenever the application is deployed, this monitoring policy will be applied.

Expect to receive an email from Managed Services Anywhere informing you of this part of the process being complete.

### Publish your Managed Application

Learn to publish your new Managed Application script box to the public catalog.

This step can be done in parallel to the previous step of creating the monitoring policy.  There is no need to wait for a response from MSA before publishing your script box.

Publishing your script box is explained well at the following location: https://www.ctl.io/knowledge-base/cloud-application-manager/tutorials/publish-script-box/
