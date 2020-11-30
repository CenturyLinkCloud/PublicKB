
{{{
  "title": "Getting Started with Docker Trusted Registry - Blueprint",
  "date": "11-11-2015",
  "author": "Albert Choi",
  "attachments": [],
  "contentIsHTML": false
}}}

![Docker Logo](../../images/docker-hub-logo.png)

### Technology Profile
Installation instructions for deploying the [Docker Trusted Registry](https://docs.docker.com/docker-trusted-registry) blueprint.

### Description
The Docker Trusted Registry (hereafter DTR) blueprint based on Docker-CS (commercial support) provides a secured, private hosted Docker registry appliance.

### Audience
Lumen Cloud Users

### Impact
After reading this article, you should have a configured Docker registry ready to be configured with license key and SSL certs.

### Prerequisite
* 2 cores, 4GB memory, ~500GB disk
* A DTR License key obtainable [here](https://www.docker.com/pricing)

### Postrequisite
To access your application from a computer outside the Lumen Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
* Recommended: [VPN Access](../../Network/CenturyLink Cloud/how-to-configure-client-vpn.md) (optional) will allow you to access your server over the internal network interfaces.
* Optional: [Add a Public IP](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal.
* [Allow incoming traffic](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) for port `443` by clicking on the Servers Public IP through the Control Portal.

### Deploying the "Install Docker Trusted Registry on Ubuntu" Blueprint

#### Steps to Deploy Blueprint
1. Locate the DTR Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for "Docker" in the keyword search on the right side of the page.
   * Click on the "Install Docker Trusted Registry on Ubuntu" Blueprint.
   * Click the `deploy blueprint` button.

2. Customize the Blueprint.
   * Set standard settings for your Server.
   * Customize server name as appropriate.
   * Credentials are not needed for the related tasks.

3. Review and Confirm the Blueprint
   * Click `next: step 2`.
   * Verify your configuration details.

4. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

5. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.


### Access the administrative interface server
After your Blueprint deploys successfully, please follow these instructions to access your server:
* If a public IP is assigned to the server, navigate in a browser to https://PUBLIC_IP.
* Over VPN, navigate to the server's private IP address via https://PRIVATE_IP.

The Docker Trusted Registry administrative webapp should load. By default, DTR generates a set of default SSL certs so your browser's security warnings may be safely ignored. Once you're connected to the admin interface, be sure to configure external domain, SSL, and license settings.

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no Docker-CS (commercial support) license costs or additional fees bundled in.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to Docker licensing, please visit the [Docker CS Support website](https://www.docker.com/support).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).
