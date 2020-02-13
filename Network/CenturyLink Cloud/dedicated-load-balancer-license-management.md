{{{
  "title": "Dedicated Load Balancer License Management",
  "date": "12-01-2016",
  "author": "Ben Heisel",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

CenturyLink Cloud (CLC) dedicated Load Balancers provisioned in a customer's environment are customer-managed devices, which includes management of the vendor license. Dedicated Load Balancers licenses are typically provisioned with an expiration date of one year. An expired license may impact functionality of the Load Balancer. To obtain a new license file a [Support Request](../../Support/how-do-i-report-a-support-issue.md) should be submitted. Steps for installing the new license file are below.

### Audience

CenturyLink Cloud customers with a dedicated Citrix Netscaler Load Balancer

### Prerequisites

* Must have an Admin login to your Netscaler
* Must be able to SSH to the RNAT IP of the HA pair (typically ends with .101)
* Basic understanding of [Basic Management Using the CLI](../CenturyLink Cloud/dedicated-load-balancer-using-cli-basic-management.md)

### Detailed Steps

The Netscaler Load Balancer uses FlexLM licensing to license features on the product. A license check is done when the VPX boots. The licensing daemon (service) will start, check for a valid license and then stop the daemon (service). The VPX will then enable certain features determined by the license daemon (service). If a license is expired or invalid, the Netscaler will stop passing traffic.

### Determining If a VPX Is Not Passing Traffic Due to an Expired License

#### CLI Method

1. SSH or use PuTTY on Windows to login to VPX management IP
2. In the CLI run:
    ```
    show ns license
    ```

3. Review the output. If the Model Number ID lists 1 instead of the proper model and the Load Balancing feature says NO, the license is expired. The Model ID should read the correct model (i.e.: 200) and the Load Balancing feature should say YES.

#### GUI Method

1. Open a browser and login to the VPX management IP.
2. On the left-hand side menu, navigate to System->Licenses
3. Review output. If the Model ID lists 1 instead of the proper model and the Load Balancing feature does not have a green checkmark, the license is expired. The Model ID should reflect the correct model (i.e.: 200) and the Load Balancing feature should have a green checkmark.

### Determining the License Expiration Date

**Note:** This step can only be performed via SSH and the CLI. The license expiration date in not available in the GUI.

1. SSH or use PuTTY on Windows to login to the VPX management IP
2. In the CLI, type the command word shell to get to a unix shell prompt
    ```
    shell
    ```

3. Review the /var/log/license.log file to determine the location and filename of the license file in use.
    ```
    cat /var/log/license.log | grep -v lmgrd  | grep "License file"
    ```

4. The license file should be in the /nsconfig/license directory. The license.log file can be listed to determine when was the last time the VPX ran the license daemon to check the license.
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

### Updating Licenses

CLC will provide the license file(s) with corresponding LB management and RNAT IP addresses; you are responsible for installation of the license file(s) on your devices. You or your team should have received the login credentials for your dedicated load balancer during its creation, but let us know if you need assistance with accessing the management functions of the load balancer.

There are two methods depending on if you are updating a lone LB or an HA pair. Steps for each situation are below.

#### HA Pair

Users may need to [configure Java](../../General/CenturyLinkCloud/how-to-configure-java-settings-to-access-web-user-interfaces.md) to ensure they can access the Web GUI.

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
    1. SSH or use PuTTY on Windows to login to the VPX management IP
    2. Enter `save ns config`
    3. Enter `reboot`
    4. Enter `yes` if prompted

### Notes

* Multiple licenses (including expired ones) can be present on the system. The Netscaler will enable all the proper features from the valid license file.
* A new license can be added to a running Netscaler while it is running with an expired license. Upon restart, the Netscaler will use the new license, resulting in less downtime of the pools.
* Updating the license on a Netscaler HA pair can be performed without downtime.
