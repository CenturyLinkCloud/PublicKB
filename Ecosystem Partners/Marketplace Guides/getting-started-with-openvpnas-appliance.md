{{{
  "title": "Getting Started with OpenVPN AS - Appliance",
  "date": "10-23-2015",
  "author": "Ecosystem",
  "attachments": [],
  "contentIsHTML": false
}}}

### Technology Profile
<img src="../../images/openvpnas/openvpnas_logo.png" style="border:0;float:right;max-width: 150px;">

https://openvpn.net/

##### Customer Support
| Sales Contact |
|:- |
| sales@openvpn.net |

### Description
OpenVPN Access Server is a full featured secure network tunneling VPN software solution that integrates OpenVPN server capabilities, enterprise management capabilities, simplified OpenVPN Connect UI, and OpenVPN Client software packages that accommodate Windows, MAC, Linux, Android, and iOS environments. OpenVPN Access Server supports a wide range of configurations, including secure and granular remote access to internal network and/ or private cloud network resources and applications with fine-grained access control.

### Audience
Lumen Cloud Users

### Prerequisites
* Access to the Lumen Cloud platform as an authorized user.
* control.ctl.io account with password authentication (two factor authentication not yet supported).
* A set of [API credentials](https://control.ctl.io/Organization/api/users)

### Steps to Deploy a New Appliance
1. Locate the Blueprint in Runner
   * [Direct link](https://runner.ctl.io/product/bd967fd2-1fb5-4d8c-8dca-43a753624bcd-openvpn)
   * or Navigate to [runner](https://runner.ctl.io) and search for "OpenVPN" in the keyword search.

2. Click the `run` button.

3. Set Required parameters.
   * Select datacenter, network and server group to provision the node to.
   * Optionally set the server name.
   * Fill in API Key and API Password associated with a valid [API user](https://control.ctl.io/Organization/api/users)

4. Deploy the Blueprint.
   * Once verified, click the `run` button.
   * Deployment will take a few minutes while the appliance is provisioned.
   * The name of the provisioned server should be in the deployment output at
     the end of the job.

5. Access Your Appliance.
   * Access your appliance and finalize configuration by opening an ssh
     connection to your server and logging in as the `root` user.
     Password credentials are available on the server details page.
   * Note that on first login you will finalize the configuration.
   * For proper authentication select root as your login user or if leveraging
     the default openvpn user you'll need to set the credentials for that user
     with the `passwd openvpn` command:

  `To initially login to the Admin Web UI, you must use a
  username and password that successfully authenticates you
  with the host UNIX system (you can later modify the settings
  so that RADIUS or LDAP is used for authentication instead).

  You can login to the Admin Web UI as "openvpn" or specify
  a different user account to use for this purpose.

  Do you wish to login to the Admin UI as "openvpn"?
  > Press ENTER for default [yes]: no

  > Specify the username for an existing user or for the new user account: root
  Note: This user already exists.`

### Pricing
The costs listed above in the above steps are for the infrastructure only. After
deploying this Blueprint, you may secure entitlements to the technology using
the following steps:
* Email: sales@openvpn.net

#### Additional Resources
* [OpenVPN Appliance FAQ](https://openvpn.net/index.php/access-server/section-faq-openvpn-as/virtual-appliance.html)

### Frequently Asked Questions
**Where do I obtain my license?**
Contact sales@openvpn.net.

**Who should I contact for support?**
* For issues related to deploying OpenVPN AS email sales@openvpn.net.
* For issues related to cloud infrastructure, please open a ticket using
  the [Lumen Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
