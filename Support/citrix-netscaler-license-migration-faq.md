{{{
  "title": "Citrix NetScaler License Migration FAQ",
  "date": "11-23-2020",
  "author": "Ben Heisel",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Effective December 1, 2020, Citrix NetScaler Dedicated Load Balancer licenses will no longer be made available by Lumen Public Cloud as a service offering. **Prior to February 1, 2021 action is required to prevent any loss of service on your load balancer. Lumen Public Cloud will not be able to restore service for license related issues.**

Existing NetScaler Load Balancers will continue to operate on the Lumen Public Cloud platform; however, Customers need to take action and must obtain a new license by contacting Citrix directly, as described in Option 2 below.

New Citrix Netscalers can still be deployed as a billable [Service Task](https://www.ctl.io/lumen-public-cloud/service-tasks/#171), but will now require the customer to provide their own license.


### Audience

Lumen Cloud customers with a dedicated Citrix NetScaler Load Balancer and license provided by Lumen through the Lumen Public Cloud service.

### Prerequisites to enable the license updates

* Must have an Admin login to your NetScaler
* Must be able to SSH to the RNAT IP of the HA pair (typically ends with .101)

### Why Did Lumen Cloud Make This Decision

Establishing a direct purchasing relationship with Citrix for dedicated NetScaler products creates a direct customer support relationship for an improved support experience.


### Customer Responsibilities and Options

Customers have two options outlined below, both require customer action and communication with Lumen.

Customers must review the options below, choose the option that fits their needs, and notify Lumen no later than February 1, 2021 of their decisions.

#### Option #1:
Decommission the dedicated Citrix NetScaler Load Balancer and license provided by Lumen Public Cloud.

**Required Customer Action:**
Delete the relevant servers via the Control Portal

#### Option #2:
Keep the dedicated Citrix NetScaler Load Balancer servers and purchase a new license directly from Citrix.

**Required Customer Action**
Contact Citrix and obtain a new license file from Citrix and install it on the load balancer prior to February 1, 2021

Customers can reach out to the Citrix inquiry page to engage Citrix by following the steps below.

1)	Please visit https://www.citrix.com/contact/form/inquiry/.
2)	Fill out the form with your contact information.
3)	Select product interest “Citrix Application Delivery (ADC)” from the drop down on the form.
**Citrix rebranded the Citrix NetScaler offer to be named Citrix Application Delivery Controller**
4)	A Citrix representative will contact you to discuss the best options for license procurement and support.


### Frequently Asked Questions

**Q: When Will I Need A New License?**

As of December 1, 2020 Lumen Public Cloud will no longer sell new Citrix NetScaler licenses.  
All customers with a dedicated Citrix NetScaler Load Balancer and license provided by Lumen Public Cloud will need to obtain a new license directly from  Citrix by February 1, 2021 if they choose to continue the service.

**Q: What if I no longer want or need the dedicated Citrix NetScaler Load Balancer offer that is provided by Lumen Public Cloud AND also do not want to purchase a new license from Citrix?**

If you wish to no longer have a dedicated Citrix NetScaler Load Balancer delete the relevant servers via the Control Portal.

**Q: What if I do nothing?**

Customers who take no action will continue to be billed for the Citrix NetScaler licenses until January 31, 2021. After January 31, 2021 the customer’s dedicated Citrix NetScaler Load Balancer environment(s) will no longer have an active license(s) and upon reboot the NetScaler will stop passing traffic.

**Q: How Do I Know When My Current License Expires?**

**Note:** This step can only be performed via SSH and the CLI. The license expiration date in not available in the GUI.

1. SSH or use PuTTY on Windows to login to the NetScaler management IP
2. In the CLI, type the command word shell to get to a UNIX shell prompt
    ```
    shell
    ```

3. Review the /var/log/license.log file to confirm the location and filename of the license file in use.
    ```
    cat /var/log/license.log | grep -v lmgrd  | grep "License file"
    ```

4. The license file should be in the /nsconfig/license directory. The license.log file can be listed to determine when was the last time the NetScaler ran the license daemon to check the license.
    ```
    ls -la /var/log/license.log
    ```

5. Navigate to the /nsconfig/license directory.
    ```
    cd /nsconfig/license
    ```

6. Review the file listed as the license file obtained in step 3. This example uses the license file named license.lic.
    ```
    cat license.lic | grep INCREMENT
    ```

7. Observe the lines in the file that start with the word **INCREMENT** in all capital letters. This line contains the license expiration date.

**Q: What Happens If My License Expires?**

The NetScaler Load Balancer uses FlexLM licensing to license features on the product. A license check is done when the NetScaler boots. The licensing daemon (service) will start, check for a valid license and then stop the daemon (service). The NetScaler will then enable certain features determined by the license daemon (service). If a license is expired or invalid, the NetScaler will stop passing traffic.

**Q: How Do I Determine If Traffic Is Not Passing Due To An Expired License?**

#### CLI Method

1. SSH or use PuTTY on Windows to login to NetScaler management IP
2. In the CLI run:
    ```
    show ns license
    ```

3. Review the output. If the Model Number ID lists 1 instead of the proper model and the Load Balancing feature says NO, the license is likely expired as the last license validation failed. The Model ID should read the correct model (i.e.: 200) and the Load Balancing feature should say YES.

#### GUI Method

1. Open a browser and login to the NetScaler management IP.
2. On the left-hand side menu, navigate to System->Licenses
3. Review output. If the Model ID lists 1 instead of the proper model and the Load Balancing feature does not have a green checkmark, the license is likely expired as the last license validation failed.. The Model ID should reflect the correct model (i.e.: 200) and the Load Balancing feature should have a green checkmark.


**Q: How Do I Install A New License?**

#### Helpful Links
- Users may need to [configure Java](https://support.citrix.com/article/CTX200399) to ensure they can access the Web GUI.
- There are [NetScaler Browser Requirements](https://docs.citrix.com/en-us/netscaler/12/faqs/GUI-faq.html).
- Citrix has a robust documentation library and their [Licensing Overview](https://docs.citrix.com/en-us/netscaler/12/licensing/netscaler-licensing-overview.html) and [Licensing](https://docs.citrix.com/en-us/citrix-gateway/13/licensing.html) articles pages may be useful.

### Updating Licenses

There are two methods depending on if you are updating a lone LB or an HA pair. Steps for each situation are below.

#### HA Pair

1. The following steps will need to be performed on each node, starting with the secondary load balancer first.
    - For non-Windows users connect to the RNAT IP over SSH and add `.old` to the license filename, then use SCP to upload the file to `/nsconfig/license`.
    - For Windows users, here are instructions for doing this via [WinSCP](https://winscp.net):
      1. Connect to the RNAT IP.
      2. You will see a screen with an explorer pane on the left and one on the right. The left one is your local machine. The right one is the NetScaler to which you just connected.
      3. In the right pane, double-click the up arrow.
      4. Double-click "nsconfig" to open that folder.
      5. Open the license folder.
      6. On the left pane, browse to the local license file.
      7. On the right pane, add `.old` to the current license name.
      8. Drag the new license from the left pane to the right pane.
2. Once the new license has been uploaded to both nodes, identify and reboot the secondary device to pick up the new license.
    1. Open two tabs in a web browser.
    2. Connect to one management IP in one tab and the other management IP in the other tab.
    3. On the left, expand "System" then click "High Availability". You will then see which is the primary node and which is the secondary node.
    4. Start on the secondary device, expand "System", click diagnostics, then in the menu select command line interface.
    5. Enter `save ns config`
    6. Enter `reboot`.
    7. Enter `yes` if prompted.
    8. Wait for the secondary device to finish booting (you will be able to log back in via the website).
3. In the GUI of the secondary device, open the command line interface again like you just did a few steps ago.
    1. Enter `show ha node`. The output should indicate that the appliance is a secondary node and the state of synchronization.
    2. If synchronization is *not* disabled, run `set ha node -hasync disabled`.
    3. Run `force failover` to switch the secondary to primary.
    4. Reboot the secondary node (formerly the primary node) so it can pick up the new license.
4. Some settings can get lost during this process. Repeat these next steps for each device.
    1. Expand the "System" section, then verify that Load Balancing and SSL Offloading have a green check in the Licenses section.
    2. Check the bottom of the left-hand column, it should say "model ID: 200". If not, you need to check and possibly re-apply the license file or reach out to our support team for assistance.
    3. Click "Settings" on the left-hand menu, then click the "Configure basic features" link in the main frame.
    4. Check everything *except NetScaler Gateway* and click OK.
    5. Click the "Configure advanced features" link.
    6. Enable "responder" and click OK.
5. Now it's time to verify functionality. Connect to GUI on your new primary device (the first one you rebooted, or connect via RNAT).
    1. Click "Dashboard" at top left.
    2. Ensure that the “Established Client vs Server Connections” graph shows active connections.

#### Standalone

This process is very similar to handling the HA pair except no failover is needed.


1. Rename the expired license file, then copy the new license to the NetScaler.
   - For non-Windows users connect to the RNAT IP over SSH and add `.old` to the license filename, then use SCP to upload the file to `/nsconfig/license`.
   - For Windows users, here are instructions for doing this via [WinSCP](https://winscp.net):
      1. Connect to the RNAT IP.
      2. You will see a screen with an explorer pane on the left and one on the right. The left one is your local machine. The right one is the NetScaler to which you just connected.
      3. In the right pane, double-click the up arrow.
      4. Double-click "nsconfig" to open that folder.
      5. Open the license folder.
      6. On the left pane, browse to the local license file.
      7. On the right pane, add `.old` to the current license name.
      8. Drag the new license from the left pane to the right pane.
2. Save the configuration and reboot
    1. SSH or use PuTTY on Windows to login to the NetScaler management IP
    2. Enter `save ns config`
    3. Enter `reboot`
    4. Enter `yes` if prompted

### Notes

* Multiple licenses (including expired ones) can be present on the system. The NetScaler will enable all the proper features from the valid license file.
* A new license can be added to a running NetScaler while it is running with an expired license. Upon restart, the NetScaler will use the new license, resulting in less downtime of the pools.
* Updating the license on a NetScaler HA pair can be performed without downtime.
