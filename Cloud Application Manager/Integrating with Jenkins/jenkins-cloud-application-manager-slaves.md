{{{
"title": "Launching Slaves via Cloud Application Manager",
"date": "10-01-2018",
"author": "Modified by Gavin Lai",
"attachments": [],
"contentIsHTML": false
}}}

Slave nodes run Jenkins tasks on remote machines in any cloud. If you configure cloud plugins like AWS to launch slaves and then write command line scripts to set up slave build environments then Cloud Application Manager and the Cloud Application Manager Jenkins plugin can save you the hassle of both tasks.
By configuring the slave node once in Cloud Application Manager, you can reuse it across development, testing, staging, and production. Using Cloud Application Manager, you can launch slaves on any OS, flavor, and cloud. As an example, watch this video on how we use Jenkins slaves to run tests for a sample JBoss app.

<iframe src="//player.vimeo.com/video/113452091" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

**In this article:**
* Configure a Slave
* Configure Jenkins to build with slaves using Cloud Application Manager
* Find a slave from Cloud Application Manager

### Configure a Slave

Configure a Jenkins slave in Cloud Application Manager. Later, you’ll call this slave from Jenkins using the Cloud Application Manager plugin.
**IMPORTANT:** This slave configuration is Debian based, so remember to select a Debian Ubuntu Linux image in the policy at deploy time.

**Steps**

1. Log in to Cloud Application Manager.

2. Create a Jenkins slave box. From the Boxes page, click **New** > **Script**. Name the box, tag it Linux, and save.

	![eb-slaves1](../../images/cloud-application-manager/eb-slaves1.png)

3. Configure the box. Under Configuration > Variables, create two text variables (JENKINS_URL and JNLP_SLAVE_OPTIONS) in uppercase and leave their values empty.

	![eb-slaves2](../../images/cloud-application-manager/eb-slaves2.png)

	![eb-slaves3](../../images/cloud-application-manager/eb-slaves3.png)

   Under Configuration > Events, add an install, start, and stop script. Copy, paste each script below and save:
**install**. This script installs the latest version of Java if unavailable and downloads the slave agent from the Jenkins server.

   ```
   #!/bin/bash
	 sudo groupadd jenkins
	 sudo useradd -m -d /var/lib/jenkins -G sudo -g jenkins jenkins
   apt-get -y update
	 JENKINS_HOME=~jenkins
   if [ -z $(which java 2>/dev/null) ]
   then
       apt-get install default-jre -y
   fi

      apt-get -y install git

   # Download the Jenkins agent
   wget {{ JENKINS_URL }}/jnlpJars/slave.jar -O ${JENKINS_HOME}/slave.jar
   ```

   **Start**. This script starts the slave agent.

   ```
   #!/bin/bash

	 JENKINS_HOME=~jenkins
	 # Execute the agent and save the PID
	 cd ${JENKINS_HOME}
	 nohup java -jar ${JENKINS_HOME}/slave.jar {{ JNLP_SLAVE_OPTIONS }} > ${JENKINS_HOME}/slave.log 2>&1 &

	 echo $! > ${JENKINS_HOME}/slave.pid
   ```

   **Stop**. This script kills the agent when the retention period on Jenkins ends.

   ```
   #!/bin/bash

   # Stop the agent
   SLAVE_PID=$(cat slave.pid)
   if [ -n ${SLAVE_PID} ]
   then
       kill -9 ${SLAVE_PID}
   fi

   ```

![eb-slaves3-1](../../images/cloud-application-manager/eb-slaves3-1.png)

4. Create a deployment policy with infrastructure metadata to build the Jenkins slave environment.
   * IMPORTANT: Don’t deploy the Jenkins slave box! Just create the policy. Jenkins will use the policy to launch the slave on-demand via Cloud Application Manager to the cloud provider you choose.

   On the Boxes page, click New > Deployment Policy. In the dialog, select a provider account, and name the policy.

   Under Claims, type or select a linux tag. Claim tags define the policy at a high level. It defines the type of platform, flavor, image, and so on. When configuring the slave in Jenkins, you provide this claim tag to deploy the slave. The claim tag must match the requirement tag in the Jenkins slave box.

  ![eb-slaves4](../../images/cloud-application-manager/eb-slaves4.png)

   Edit the policy.

![eb-slaves4-1](../../images/cloud-application-manager/eb-slaves4-1.png)

Make sure you select a Debian Ubuntu Linux image, select a firewall rule that allows traffic to the instance, and make the machine IP ephemeral to open it to Internet traffic. Save the policy.

   ![eb-slaves5](../../images/cloud-application-manager/eb-slaves5.png)

### Configure Jenkins to Build with Slaves Using Cloud Application Manager

Run Jenkins jobs using slaves launched via Cloud Application Manager on any cloud. Be sure to [connect your Cloud Application Manager account](jenkins-cloud-application-manager-setup.md) in Jenkins before setting up the slave.

**Add Jenkins Slaves**

**Steps**

1. Go to the configure system page at **http://\<your Jenkins host\>/configure.**

2. Set up Jenkins to launch slaves using the slave box. Click **Add** for **Slave Configurations**.

![eb-slaves5-1](../../images/cloud-application-manager/eb-slaves5-1.png)

**Note**: Previously, you have to install [ElasticBox plugin](https://plugins.jenkins.io/elasticbox) on your Jenkins server. You can find more information [here](https://plugins.jenkins.io/elasticbox).

![eb-slaves6](../../images/cloud-application-manager/eb-slaves6.png)

3. In this section, select the slave box from the Cloud Application Manager workspace. Optionally, tag the slave instance.

	 Set **Min. No. of Instances** to 0 when you don’t want to keep idle slaves alive. Set **Max. No. of Instances** to the number of slaves you want at any given time to run Jenkins jobs.

   **IMPORTANT**: Add a label to identify the slave to Jenkins. Use underscores or dashes, but not spaces. When you create a build job (as we’ll do in the next section), you can provide this label to make Jenkins select this slave.

	![eb-slaves7](../../images/cloud-application-manager/eb-slaves7.png)

   The plugin uses the JENKINS_URL and JNLP_SLAVE_OPTIONS variables to pass Jenkins server information slaves need to connect. Leave them empty.

4. Under Deployment, select a policy from the Cloud Application Manager workspace or enter a claim tag to use any policy that matches the tag.

	 Click Advanced. For **Retention Time**, specify in minutes how long the plugin should wait before terminating an idle slave. If the slave is idle for more than 30 minutes, which is the default, the plugin terminates the slave from your provider. But for this to work, your slave must be connected to the Jenkins server.

   Under **Max. No. of Builds**, set the most builds the slave can execute. If the slave hits that number, the plugin terminates it.

5. Save the slave setup.


### Enable Slaves to Connect through a Port

When defining the [Jenkins server box](jenkins-cloud-application-manager-setup.md), we opened port 55555 on the cloud provider network to allow slaves to connect to the Jenkins server. In these steps, we open this port (or another you chose) in Jenkins server.

**Steps**

1. Go to the configure global security page at **http://\<your Jenkins host\>/configureSecurity/.**

2. Select **Enable Security** and set **Fixed** to 55555 as shown. Save the setting.

  ![eb-slaves8](../../images/cloud-application-manager/eb-slaves8.png)


### Attach Slave to a Build Job

Follow these steps to attach a slave from Cloud Application Manager to run Jenkins build jobs.

**Steps**

1. From the Jenkins server management interface, click **Configure** on any build job.

2. Select **Restrict where this project can be run**. Under **Label Expression**, type and select the label for the Cloud Application Manager slave that you gave when setting it up in Jenkins. This causes Jenkins to pick any available slave by that label.

	![eb-slaves9](../../images/cloud-application-manager/eb-slaves9.png)

3. Save the job.


### Find a Slave from Cloud Application Manager

Follow these steps to locate slaves launched via Cloud Application Manager in case you need to debug.

**Steps**

1. Go to your Jenkins server management interface at **http://\<your Jenkins host\>:8080.**

2. Click the slave if active. It’s typically named as <Jenkins slave box environment name——–ID>. Here’s an example.

	![eb-slaves10](../../images/cloud-application-manager/eb-slaves10.png)

3. Click Configure. This shows settings for the slave.

   ![eb-slaves11](../../images/cloud-application-manager/eb-slaves11.png)

4. Notice the Cloud Application Manager link to the slave instance. Click to open the slave instance in Cloud Application Manager. From there, you can debug the slave in the lifecycle editor or check the logs.

   ![eb-slaves12](../../images/cloud-application-manager/eb-slaves12.png)

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at /ProgramData/ElasticBox/Logs/elasticbox-agent.log
