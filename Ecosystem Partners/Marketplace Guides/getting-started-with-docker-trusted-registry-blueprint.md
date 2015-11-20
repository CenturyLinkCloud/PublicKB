
{{{
  "title": "Getting Started with Docker Trusted Registry - Blueprint",
  "date": "November 11, 2015",
  "author": "Albert Choi",
  "attachments": [],
  "contentIsHTML": false
}}}


![docker hub](https://docs.docker.com/dist/assets/images/logo.png)


### Technology Profile

Installation instructions for deploying the [Docker Trusted Registry](https://docs.docker.com/docker-trusted-registry) blueprint. 


### Description

The Docker Trusted Registry (hereafter DTR) blueprint based on
Docker-CS (commercial support) provides a secured, private hosted
docker registry appliance.

### Audience

CenturyLink Cloud Users

### Impact

After reading this article, you should have a configured docker
registry ready to be configured with license key and SSL certs. 

### Prerequisite

- 2 cores, 4GB memory, ~500GB disk
- A DTR License key obtainable [here](https://www.docker.com/pricing)

### Postrequisite

To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. Recommended: [VPN Access](../../Network/how-to-configure-client-vpn.md) (optional) will allow you to access your server over the internal network interfaces.
  2. Optional: [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
    1. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for port 443 by clicking on the Servers Public IP through Control Portal

### Deploying the "Install Docker Trusted Registry on Ubuntu" Blueprint

#### Steps to Deploy Blueprint

1. **Locate the DTR Blueprint**

1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for "docker" in the keyword search on the right side of the page.
  3. Click on the "Install Docker Trusted Registry on Ubuntu" Blueprint.
  4. Click the "deploy blueprint" button.

3. **Customize the Blueprint**

  1. **Set standard settings for your Server**
  2. **Customize server name as appropriate**
  3. **Credentials are not needed for the related tasks**

4. **Review and Confirm the Blueprint**

  1. Click "next: step 2"
  2. Verify your configuration details.

5. **Deploy the Blueprint**

  1. Once verified, click on the "deploy blueprint" button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**

  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.


### Access the administrative interface server

After your Blueprint deploys successfully, please follow these instructions to access your server:

  1. If a public IP is assigned to the server, navigate in a browser to https://PUBLIC_IP
  2. Over VPN, navigate to the server's private IP address via https://PRIVATE_IP

The Docker Trusted Registry administrative webapp should load. By default, DTR generates a set of default SSL certs so your browser's security warnings may be safely ignored.

Once you're connected to the admin interface, be sure to configure external domain, SSL, and license settings. 

### Pricing

The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. There are no Docker-CS (commercial support) license costs or additional fees bundled in. 

### Frequently Asked Questions

#### Who should I contact for support?

* For issues related to Docker Licensing, please visit the [Docker CS Support website](https://www.docker.com/support)
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
