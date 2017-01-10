{{{
"title": "Setting Up ElasticBox for Use",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Setting Up ElasticBox for Use
Once you install the appliance, set it up for others in your organization to use. At the least, assign a friendly hostname or vanity URL to point users to ElasticBox. Optionally, configure other settings such as add SSH keys to access the appliance, sync NTP system time, enable outbound email notifications, or switch to a new device to store appliance and ElasticBox data.

**In this article:**
* Initial ElasticBox Setup
* Changing the ElasticBox Hostname
* Changing the Appliance Admin Account Password
* Adding your SSH Key (optional)
* Changing NTP Time Zone (optional]
* Enabling SMTP Outbound Email (optional)
* Switching Appliance Device Root Storage

### Initial ElasticBox Setup

**Steps**

1. Log in to ElasticBox on the appliance

2. Get the ElasticBox IP address from the appliance VM console.
   ![appliance-setup1.png](../images/ElasticBox/appliance-setup1.png)

   Log in to ElasticBox with the default appliance admin credentials:
   * username: **admin@elasticbox.com**
   * password: elasticbox123

   ![appliance-setup2.png](../images/ElasticBox/appliance-setup2.png)

3. Set up ElasticBox.
   From the menu drop-down at the top right, click **Setup Console**. From this page, you can manage settings for the appliance.
   ![appliance-setup3.png](../images/ElasticBox/appliance-setup3.png)

   * Change the hostname to a friendly URL.
   * Optionally, change the default admin account password.
   * Optionally, add SSH keys to manage access to the appliance virtual machine.
   * Optionally, change the NTP time zone, which affects the timestamp in the appliance logs.
   * Optionally, enable outbound for notifications.
   * Optionally, switch the appliance device storage to increase storage or processing speed.

4. Create a new admin account for your enterprise

   Follow this step if using the ElasticBox Enterprise Edition.
   ElasticBox provides a default appliance admin account, which gives full access to manage the appliance and administer ElasticBox settings for your organization. This is like a master key, so use it only in case of emergency. To administer the appliance and ElasticBox on a regular basis, create and use a fresh admin account.

   Log out of ElasticBox. Browse to the ElasticBox IP address in the appliance VM console. Sign up for a new user account. This will serve as the new admin account.

   Log back in as the appliance admin using the credentials in step 1. Add your new user account as an administrator in the Admin Console. Going forward, use this admin account to manage the appliance and settings for your organization.

### Changing the ElasticBox Hostname
Hostname is a friendly name for the ElasticBox IP address for example, yourcompany.com:80 or name.example.com:443. The hostname should point to the IP address of the appliance virtual machine. To allow users to connect, also make sure your network firewall allows inbound traffic to the appliance IP address via TCP ports 80, 443, 5671, and 5672.
![appliance-setup4.png](../images/ElasticBox/appliance-setup4.png)

**Steps**

1. Browse to ElasticBox with the IP address in the appliance console and log in as an admin.
2. From the menu drop-down at the top right, click **Setup Console**.
3. Under Hostname, specify a valid IP or hostname that resolves to a valid IP address. Make sure that it’s a fully qualified domain name that meets the following criteria:

   * Appliance can access it.
   * Deployed instances can access it.
   * Users in the network can browse to the ElasticBox UI.

4. When done, scroll down and click **Save Settings**.

   **IMPORTANT:** When you change the hostname, any instances you launched previously can potentially become unavailable if the appliance obtains its IP address dynamically. To avoid this, set a static address for the appliance.

### Changing the Appliance Admin Account Password
Change the appliance admin account password to keep it secure.
![appliance-setup5.png](../images/ElasticBox/appliance-setup5.png)

![appliance-setup6.png](../images/ElasticBox/appliance-setup6.png)

![appliance-setup7.png](../images/ElasticBox/appliance-setup7.png)

### Adding Your SSH Key (Optional)
Allow SSH access to the appliance virtual machine for the appliance admin account. You can SSH into the appliance virtual machine only using the keys you add here. SSH access is helpful if you want to look at logs and such.
![appliance-setup8.png](../images/ElasticBox/appliance-setup8.png)

**Steps**
1. Browse to ElasticBox with the IP address in the appliance console and log in as an admin.
2. From the menu drop-down at the top right, click **Setup Console**.
3. Under SSH Access, click **Add New Key**.
4. If you don’t have one already, generate a key using ssh-keygen -t rsa and paste in the public key.
5. When done, scroll down and click **Save Settings**.

### Changing NTP Time Zone (Optional)
This shows the network time protocol (NTP) setting on the appliance. By default, it’s set to the time zone of the host running the appliance. You can optionally change the NTP server and time zone. The appliance uses this to determine the timestamp in logs.
![appliance-setup9.png](../images/ElasticBox/appliance-setup9.png)

**Steps**
1. Browse to ElasticBox with the IP address in the appliance console and log in as an admin.
2. From the menu drop-down at the top right, click **Setup Console**.
3. Under Time, specify these settings.
4. When done, scroll down and click **Save Settings**.

| Setting | Description |
|---------|-------------|
| Primary <br> NTP Server | URL or IP address of the primary NTP server. |
| Secondary <br> NTP Server | Optional. URL or IP address of the secondary NTP server. |
| Time Zone | Appliance host system time zone. |

### Enabling SMTP Outbound Email (Optional)
We recommend that you specify SMTP server settings to be able to auto send outbound email notifications in ElasticBox. The no-reply address is used in the From field. Under Email, click **ON** to enable outbound email.
![appliance-setup10.png](../images/ElasticBox/appliance-setup10.png)

**Steps**
1. Browse to ElasticBox with the IP address in the appliance console and log in as an admin.
2. From the menu drop-down at the top right, click **Setup Console**.
3. Under Email, specify these settings.
4. When done, click **Save Settings**.

| Setting | Description |
|---------|-------------|
| Server Address | Specify the hostname or IP address of the SMTP mail server, for example, smtp.example.com. |
| Port | Typically, you can specify 25 for SMTP and 465 for SMTPS. |
| No-Reply Address | Specify the email address to use in the sender address (or from) field of notification messages. |
| Authentication | Set to **ON** if your SMTP server requires authentication to send emails. |
| SMTP Username | Enter the full email address of a username, such as **username@example.com** used to authenticate with the SMTP server. |
| SMTP Password | Enter the password for the SMTP username. |
| TLS/SSL | Set to **ON** if emails are encrypted using TLS or SSL. |

### Switching Appliance Device Root Storage
When you install the appliance, the appliance VM by default gets 100 GB of virtual disk space. For more storage or faster performance, attach a new disk to the VM and make that the primary appliance storage. Do this before you start using ElasticBox. Here are the steps.

**Steps**
1. In vSphere vCenter, power off the appliance VM and attach a second virtual disk with more CPU, RAM, and disk space. For more information, see the [vCenter 5.0](http://pubs.vmware.com/vsphere-50/topic/com.vmware.ICbase/PDF/vsphere-esxi-vcenter-server-50-storage-guide.pdf) and [vCenter 5.5](http://pubs.vmware.com/vsphere-55/topic/com.vmware.ICbase/PDF/vsphere-esxi-vcenter-server-55-storage-guide.pdf) help.
2. Power on the appliance VM. In the appliance Setup Console under Block Device, select the second disk as the primary appliance storage.
   ![appliance-setup11.png](../images/ElasticBox/appliance-setup11.png)

3. When done, click **Save Settings**.

When you switch the disk, the appliance reboots and becomes unavailable for a few minutes. In that time, it copies over existing data from the other disk like specific appliance settings, logs, the database, and the saved state of RabbitMQ. It also copies all the generated data to the second disk. When the appliance VM is back online, you can start using ElasticBox.

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](https://www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
