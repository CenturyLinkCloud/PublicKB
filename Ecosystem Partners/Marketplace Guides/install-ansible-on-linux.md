
{{{
  "title": "Install ansible on *Nix",
  "date": "2015-10-06",
  "author": "Andrew Brunette",
  "attachments": [],
  "contentIsHTML": false
}}}

### Technology Profile

Ansible is a leading orchestration architecture for automation of system configuration tasks.  

### Description
Ansible is an IT automation tool. It can configure systems, deploy software, and orchestrate more advanced IT tasks such as continuous deployments or zero downtime rolling updates.

Ansible’s main goals are simplicity and ease-of-use. It also has a strong focus on security and reliability, featuring a minimum of moving parts, usage of OpenSSH for transport (with an accelerated socket mode and pull modes as alternatives), and a language that is designed around auditability by humans–even those not familiar with the program.

We believe simplicity is relevant to all sizes of environments, so we design for busy users of all types: developers, sysadmins, release engineers, IT managers, and everyone in between. Ansible is appropriate for managing all environments, from small setups with a handful of instances to enterprise environments with many thousands of instances.

Ansible manages machines in an agent-less manner. There is never a question of how to upgrade remote daemons or the problem of not being able to manage systems because daemons are uninstalled. Because OpenSSH is one of the most peer-reviewed open source components, security exposure is greatly reduced. Ansible is decentralized - it relies on your existing OS credentials to control access to remote machines. If needed, Ansible can easily connect with Kerberos, LDAP, and other centralized authentication management systems.

For more information, please visit [Ansible.com](http://www.ansible.com)

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be able to install Ansible on an arbitrary *Nix (Linux/Unix) server

### Prerequisite
- a running *Nix server in the CenturyLink Cloud.

### Postrequisite

To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80, 443

### Deploying the <name of the blueprint> Blueprint

#### Steps to Deploy Blueprint
1. **Locate the Install Ansible Blueprint**

  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Install ansible” in the keyword search on the right side of the page.
  3. Locate the "Install Ansible on existing server" Blueprint

2. **Choose and Deploy the Blueprint.**
   Click the "Install Ansible on existing server" Blueprint.

3. **Customize the Blueprint**
  1. **Select "Deploy"**>

  2. **Enter Server Name**

4. **Review and Confirm the Blueprint**
  1. Click “next: step 2”
  2. Verify your configuration details.

5. **Deploy the Blueprint**
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no costs for using ansible, it is free open source software.

### About Ansible
Ansible is open source, python oriented automation software.  It is supported by Ansible.com, and a wide variety of web resources.  ##CenturyLink does not provide support for Ansible##

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to running ansible on CenturyLink Cloud, please use Google to research your issue.  The Github respository issues log may be helpful.  
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
