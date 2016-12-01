{{{
  "title": "Dedicated Load Balancer License Management",
  "date": "12-01-2016",
  "author": "Ben Heisel",
  "attachments": [],
  "contentIsHTML": true
}}}

### Overview

CenturyLink Cloud dedicated Load Balancers provisioned in a customer's environment are customer managed devices, which includes management of the vendor license. Dedicated Load Balancers are typically provisioned with a license with an expiration date of one year. An expired license may impact functionality of the Load Balancer. To obtain a new license a [Support Request](../Support/how-do-i-report-a-support-issue.md) should be submitted.

### Audience

CenturyLink Cloud customers with a dedicated Citrix Netscaler Load Balancer

### Prerequisites

* Must have an Admin login to your netscaler
* Must be able to SSH to the RNAT IP of the HA pair (typically ends with .101)
* Basic understanding of [Basic Management Using the CLI](../Network/dedicated-load-balancer-using-cli-basic-management.md)

### Detailed Steps

The Netscaler Load Balancer uses FlexLM licensing to license features on the product. A license check is done when the VPX boots. The licensing daemon (service) will start, check for a valid license and then stop the daemon (service). The VPX will then enable certain features determined by the license daemon (service). If a license is expired or invalid, the Netscaler will stop passing traffic.

#### How to determine if a VPX is not passing traffic due to an expired license

#### CLI method

1. SSH or use PuTTY on Windows to login to VPX management IP 
2. In the CLI run:
 ```
  show ns license
 ```
3. Review the output. If the Model Number ID lists 1 instead of the proper model and the Load Balancing feature says NO, the license is expired. The Model ID should read the correct model (ie: 200) and the Load Balancing feature should say YES.

#### GUI method

1. Open a browser and login to the VPX management IP.
2. On the left hand side menu, navigate to System->Licenses
3. Review output. If the Model ID lists 1 instead of the proper model and the Load Balancing feature does not have a green checkmark, the license is expired. The Model ID should reflect the correct model (ie: 200) and the Load Balancing feature should have a green checkmark.

### Determine the License Expiration Date

**Note:** This step can only be performed via SSH and the CLI. The license expiration date in not available in the GUI

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

### Notes

* Multiple licenses (including expired ones) can be present on the system. The Netscaler will enable all of the proper features from the valid license file.
* A new license can be added to a running Netscaler while it is running with an expired license. Upon restart, the Netscaler will use the new license, resulting in less downtime of the pools.
* Updating the license on a Netscaler HA pair can be performed without downtime.
