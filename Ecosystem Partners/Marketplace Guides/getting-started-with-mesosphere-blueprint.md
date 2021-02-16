{{{
  "title": "Getting Started with OSS Mesosphere - Blueprint",
  "date": "11-09-2015",
  "author": "Albert Choi",
  "attachments": [],
  "contentIsHTML": false
}}}

<img src="../../images/ecosystem-mesosphere-logo.png" style="border:0;max-width: 300px;"/>

### Technology Profile
Notes on installing a basic [Mesosphere](https://mesosphere.com) cluster to Lumen Cloud.

This article assumes familiarity with Mesosphere and a basic working knowledge of the Lumen Cloud Control Portal.

### Description
This article pertains to version 0.1 of the Mesosphere Cluster blueprint and as such should be considered a technical preview. Advanced Mesosphere administration and scaling is beyond the scope of this article.

For more information, visit the official Mesosphere [documentation](https://docs.mesosphere.com/) and [support](https://docs.mesosphere.com/support/) sites.

This Blueprint bundles the Open-Source Community release of Mesosphere. More information for commercial support for Mesosphere is available [here](https://mesosphere.com/product/).

### Audience
Architects, DevOps, Cluster administrators

### Impact
After reading this article, the user should be able to access a Mesosphere cluster consisting of 3 master and 3 slave nodes, principally via Marathon.

The initial version supports Mesos 0.25, Marathon 0.11, and docker 1.9 (docker-engine).

Bare Metal support is not yet supported.

### Prerequisites
Required Compute:
* ~10 cores, ~20GB memory, ~100GB disk

### Postrequisite
To access your application from a computer outside the Lumen Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
* Recommended: Set up a [Load Balancer](../../Network/Lumen Cloud/creating-a-self-service-load-balancing-configuration.md) for your slave nodes. Note, you'll need to gather the IP addresses of your slave nodes as well as install an http(s) server for this to be useful.
* Optional: [VPN Access](../../Network/Lumen Cloud/how-to-configure-client-vpn.md) (optional) will allow you to access the mesos masters directly for troubleshooting/logs/etc.
* Optional: Set up a [Public IP](../../Network/Lumen Cloud/how-to-add-public-ip-to-virtual-machine.md) or [Load Balancer](../../Network/Lumen Cloud/creating-a-self-service-load-balancing-configuration.md) on your master nodes to access Marathon publicly.

### Deploying the Mesosphere Blueprint

#### Steps to Deploy Blueprint
1. Locate the "Mesosphere Cluster" Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “mesosphere” in the keyword search on the right side of the page.
   * Locate the "Mesosphere Cluster" Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the "Mesosphere Cluster" Blueprint.

3. Build Server(s).
   * Set root password for all built servers.
   * Customize Group/Network settings.

4. Customize Server Name(s).
   * Set unique names for each server.

5. Select at least 3 nodes to be "Master" mode.
   * Select Mode => Master.

6. Remaining nodes should be set as "Slave" mode.
   * Select Mode => Slave.

7. Set the same Master nodes for each Installation.

8. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

9. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

10. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Deploy additional slaves to an existing cluster
"Mesosphere Installer" is available as a Script Package for horizontally scaling your cluster.

#### Steps
1. Deploy or Identify an Existing Server.
   * Identify the server targeted to add as an additional slave. The target server OS should be Ubuntu 14 64-bit. The server must be a server within your Lumen Cloud account.

2. Select 'Execute the Package on a Server Group'.
   * Packages can be executed on one more more servers in a Group. Search for the public script package named "Mesosphere Installer".
   * See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

3. Configure the Parameters.
   Set the following application parameters:
   * Select Mode => Slave.
   * Select your Master nodes from the master1, master2, and master3 drop-downs. Each should be unique and correspond to the same selections when the cluster was set up.

4. Deploy the Script Package.
   * Once verified, click the `execute package` button.
   * This will kick off the deployment process and load a page where you can track the progress. Deployment will typically complete within a few minutes.

5. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Access the Marathon UI
After your Blueprint deploys successfully, connect through the [VPN](../../Network/Lumen Cloud/how-to-configure-client-vpn.md) and access one of the master nodes on port 8080 in your browser. Alternatively, access a public IP set up through a [Load Balancer](../../Network/Lumen Cloud/creating-a-self-service-load-balancing-configuration.md).

### Installing a custom http router
Post this marathon job to access a basic router.

	{
	  "id": "/router",
	  "cpus": 0.25,
	  "mem": 128,
	  "instances": 1,
	  "constraints": [["hostname", "UNIQUE"]],
	  "cmd": "/usr/local/bin/nginx",
	  "container": {
	    "type": "DOCKER",
	    "docker": {
	      "image": "acker/mesosphere-router:latest",
	      "forcePullImage": true,
	      "network": "BRIDGE",
	      "portMappings": [
	          {
	              "containerPort": 8080,
	              "hostPort": 80,
	              "protocol": "tcp"
	          },
	          {
	              "containerPort": 8443,
	              "hostPort": 443,
	              "protocol": "tcp"
	          }

	      ]
	    }
	  },
	  "healthChecks": [{
	      "protocol": "TCP",
	      "gracePeriodSeconds": 600,
	      "intervalSeconds": 30,
	      "portIndex": 0,
	      "timeoutSeconds": 10,
	      "maxConsecutiveFailures": 2
	  }]
	}


Bound on port 80 on the host slave node, this container will resolve the http host to an existing target marathon app.

Here is an example job to test routing:

	{
	  "id": "/dirlist--foobar--com",
	  "cpus": 0.25,
	  "mem": 64,
	  "cmd": "python3 -m http.server 8080",
	  "instances": 2,
	  "container": {
	    "type": "DOCKER",
	    "docker": {
	      "image": "python:3",
	      "forcePullImage": true,
	      "network": "BRIDGE",
	      "portMappings": [
	          {
	              "containerPort": 8080,
	              "protocol": "tcp"
	          }
	      ]
	    }
	  }
	}


For example, `curl -vv -H "Host: dirlist.foobar.com"" 34.34.34.34` should resolve to the `dirlist` container.

### Troubleshooting
If on the initial install your apps are not running and stuck in deployment, restart the cluster of servers once.


### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no Mesosphere license costs or additional fees bundled in for the Community Release.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Mesosphere Cluster Blueprint on Lumen Cloud, licensing or accessing the deployed software, please visit the [Mesosphere Support website](https://docs.mesosphere.com/support/).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).
