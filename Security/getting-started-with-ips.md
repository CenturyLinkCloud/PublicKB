{{{
  "title": "Getting Started with Intrusion Prevention System (IPS)",
  "date": "08-11-2015",
  "author": "Stephanie Wong",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Overview
The Platform CenturyLink IPS utilizes an Agent installed on your Virtual Machine (VM) that monitors the VM for suspicious activity. If suspicious activity is found, the Agent logs the activity, which it may block or stop, and reports the incident based on the IPS policy. There is a default policy associated with each VM that is automatically tuned based on the host operating system and installed applications.

This Blueprint is for the actual installation and activation of the IPS service on the VM. Other Blueprints will be available for modifications to the installation.

### Prerequisites
* A CenturyLink Cloud Account
* One of the Supported Operating Systems listed below on the Virtual Machine
* Add the following Firewall Rules to allow agent download, activation and management.

  Installing Virtual Machine - dsm.client-security.ctl.io 443/tcp
  
  Installing Virtual Machine - activate.dsm.client-security.ctl.io 443/tcp
  
  Installing Virtual Machine - relay.dsm.client-security.ctl.io 443/tcp

### Supported Managed Operating Systems
* Red Hat Enterprise Linux 5 (64-bit)
* Red Hat Enterprise Linux 6 (64-bit)
* Microsoft Windows Server 2008 Standard R2 (64-bit)
* Microsoft Windows Server 2008 Enterprise (64-bit)
* Microsoft Windows Server 2008 Enterprise R2 (64-bit)
* Microsoft Windows Server 2008 Datacenter (64-bit)
* Microsoft Windows Server 2008 Datacenter R2 (64-bit)
* Microsoft Windows Server 2012 Datacenter (64-bit)
* Microsoft Windows Server 2012 Datacenter R2 (64-bit)



### Installation Process

1. Go into the **Blueprints Library**.

  ![Control Portal](../images/client-security/gettingIPS_controlportal.png)

2. Search for **Install Intrusion Prevention** in the Refine Results section. Then, click **Install Intrusion Prevention on Linux** or **Install Intrusion Prevention on Windows**.  

  ![Search Install Linux](../images/client-security/gettingIPS_rhel_blueprintname.png) ![Notification Update Windows](../images/client-security/gettingIPS_windows_blueprintname.png)

3. Click the **deploy blueprint** button.  

  ![Configure Install Linux](../images/client-security/gettingIPS_rhel_configure.png)

4. From the **Execute on Server** drop down list, select the appropriate virtual machine. Enter and confirm the User Password.  Click the **next: step 2** button.  

  ![Configure Notifications RHEL Fields](../images/client-security/gettingIPS_rhel_blueprintfields.png)

5. Review the Blueprint parameters and click **deploy blueprint**.  

  ![Deploy Blueprint](../images/client-security/gettingIPS_rhel_deploy.png)

  **Note:** The Blueprint displays each step taken and its status during provisioning.  

  ![Blueprint Status Log](../images/client-security/gettingIPS_rhel_logstatus.png)

6. An email notification is sent to the initiator of the Blueprint for both queuing and completion.

### Agent Billing & Deactivation

Once the IPS Agent is installed on a VM, it will incur an hourly charge until the uninstall blueprint is executed successfully.

**Note:** If a VM is to be decommissioned, the agent MUST be deactivated to avoid on-going charges.

### Support

If you need assistance, please send initial contact to [help@ctl.io](mailto:help@ctl.io). You will receive an automated reply with step-by-step instructions on setting up a Zendesk user account. The Zendesk account will allow for future engagements with customer service.

**Note:** If you do not setup a Zendesk user account, support requests may get filtered as spam in the ticketing system.

### Frequently Asked Questions

**Can I make modifications to my existing policy to further customize or tune it?**

Not at this time, if you'd like to see this feature, please contact [features@ctl.io](mailto:features@ctl.io).

**What does the IPS Product Provide?**

Platform CenturyLink’s IPS service helps ensure secure protection against your Virtual Machine (VM) from known intrusion patterns that hackers utilize. It also allows you to spend less time on the maintenance of your system, instead allowing you to focus on the tasks for your core business. We will do the patching and ensure that all agents have up-to-date signatures for possible attacks.

**How do I configure the notifications settings to send alerts?**

Follow the process in the [Configuring IPS Notifications article](configuring-ips-notifications.md).

**Will you be adding support for additional Operating Systems?**

Yes, we are working on adding additional OSes. If you have a specific OS you would like to see supported, please contact features.ctl.io.

**If I decommission a Virtual Machine, do I need to uninstall the IPS agent?**

Yes, you still need to uninstall the IPS agent to avoid unnecessary charges. You can uninstall the agent via the uninstall IPS blueprint.
