{{{
  "title": "Install Symas OpenLDAP Silver",
  "date": "12-18-2015",
  "author": "Matt Hardin",
  "attachments": [],
  "contentIsHTML": false
}}}

![Symas Corp.](../../images/symas-logo.png)

### Technology Profile
Symas OpenLDAP Silver is an LDAP v3 server based on the popular OpenLDAP software, which is noted for its performance, flexibility, and stability. The Silver version features the Lightning Memory-mapped Database but is otherwise limited in that it lacks the ability to act as a replication provider and does not have the ability to communicate with or authenticate to Active Directory or other directory servers. It is therefore best suited for evaluations, proofs of concept, and directories that are not mission-critical. For enterprise-grade directory servers, please consider one of our other Symas OpenLDAP offerings.

### Description
This Blueprint installs a copy of Symas OpenLDAP Silver on the designated system.

* Licensing and Source Code
Symas OpenLDAP Silver is licensed under several Open Source licenses included in the file /opt/symas/etc/Symas-OpenLDAP-Copyrights.txt. Use of this software implies acceptance of these licenses. To obtain the source code that went for Symas OpenLDAP Silver, send a request by email to support@symas.com. There is a handling fee of US$50.

For more information, please visit http://symas.com.

### Audience
Lumen Cloud Users

### Impact
After reading this article, the user should be able to install Symas OpenLDAP, deploy a sample database and run example searches on sample data contained in the installation.

Dependencies/Conflicts
Symas OpenLDAP Silver is fully self-contained and does not depend on any external software. It does not conflict with any other known software, including copies of OpenLDAP installed as part of the Red Hat distribution.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.

Minimum System Requirements:
* A virtual machine running a supported OS: CentOS or Red Hat 5, 6, or 7.
* Two or more CPU cores.
* Sufficient RAM to accommodate the database working set in the directory.
* 4-6 GB of available disk space.

### Postrequisite
To access your application from a computer outside the Lumen Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully.

* [Add a Public IP](../../Network/Lumen Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal.

* [Allow incoming traffic](../../Network/Lumen Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through the Control Portal and configuring appropriately.
  * The default ports to access the application are: `389` (ldap://), `636` (ldaps://).

### Deploying the 'Install Symas OpenLDAP Silver' Blueprint

#### Steps to Deploy Blueprint
1. Locate the Install Symas OpenLDAP Silver Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Symas” in the keyword search on the right side of the page.
   * Locate the 'Install Symas OpenLDAP Silver' Blueprint.

2. Choose and Deploy the Blueprint.
   * Make sure the system on which you plan to deploy the Blueprint has sufficient disk space and RAM to accommodate the intended size of your directory.
   * Click the "Symas OpenLDAP Silver Installation" Blueprint.
   * Wait for the deployment to complete successfully.
   * You can now either run the example script or configure OpenLDAP to provide directory services.

3. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

4. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

5. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Deploy Symas OpenLDAP Silver Example Script
Symas OpenLDAP Silver includes a script that will configure the directory server, initialize it with some sample data, start it, and run an example search. This is a good first-step if you’re not familiar with OpenLDAP or just want to verify that the server is working properly.

Note: This script overwrites any pre-existing configurations. Only run this script if you’ve made backups of the symas-openldap.conf and slapd.conf files. If you are running the script after a fresh installation, these files won’t exist, so there’s nothing to worry about.

#### Steps to Run the Sample Script
1. Login to the system as root.
   * Change directory to /opt/symas/etc/openldap

2. Enter the command:
   `sh exampledb.sh`

3. Follow the prompts.

By the end of the script you should have a running directory server that has been loaded with some example data and you should see an example of the ldapsearch command.

#### Configure OpenLDAP
Note: If you ran the example script described above, Steps 1 and 2 below aren’t necessary.
1. Login to the system as root change directory to /opt/symas/etc/openldap.

2. Copy the file symas-openldap.conf.default to symas-openldap.conf and edit as needed.

3. Copy the file slapd.conf.default to slapd.conf.

4. Edit the slapd.conf file as needed.

5. Run the following command to check the syntax of the slapd.conf file and make sure it does not return any errors. If it does, correct them and re-run the command.
   * `/opt/symas/bin/slaptest`

6. Start Symas OpenLDAP by issuing the following command:
   * `/etc/init.d/solserver start`

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no fees associated with the use of Symas OpenLDAP Silver.

### Frequently Asked Questions

#### Who should I contact for support?
* Symas OpenLDAP Silver is provided AS-IS and does not include technical support. If you need a professionally supported version of OpenLDAP, please consider one of our other Symas OpenLDAP offerings.

* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).

#### Additional Resources
- http://symas.com
- http://www.openldap.org

* Contacting Symas
- Telephone: +1 650-963-7601
- Toll-Free: 855-LDAP-GUY
- Email: support@symas.com
