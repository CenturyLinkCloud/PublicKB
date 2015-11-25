{{{
  "title": "SoftNAS: How to update",
  "date": "11-11-2015",
  "author": "Maxim Volkov",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Introduction

<p>SoftNAS Cloud is a software behind virtual NAS appliance provided by SoftNAS, LLC - CenturyLink ecosystem partner. The software gets updated on a regular bases to receive bug fixes and new features. This brings the necessity to periodically upgrade your SoftNAS. Here we will describe this procedure.</p>

### Prerequisites

<div>
<ol>
<li>A SoftNAS appliance was [ordered](../ecosystem-partners/marketplace-guides/getting-started-with-softnas-cloud-file-gateway-partner-template.md) and [set up](../using-a-software-defined-virtual-nassan-on-centurylink-cloud.md)  in CenturyLin Cloud.</li>

<li>You do have administrative rights to access the appliance's GUI interface.</li>
<li>Your SoftNAS Cloud license is active.</li>
</ol>
</div>

### Preparation

<p>The update process will interrupt normal operation of your NAS, so you have to make sure that any processes using the virtual appliance are stopped. Normally the entire operation ma take up to five minutes to download fresh package, install it and resume operation, so you have to account for some down time.</p>

<p>The upgrade is data-safe, however, as precaution is always good idea to backup your data and/or for perform a [snapshot](../creating-and-managing-server-snapshots.md) of an entire VM.

### Update process (GUI)

![Update window](../images/softnas-update-1.png)

<p>Log in into your appliance

<ol>
  <li>Navigate to: Settings >> Software Updates
  <li>Compare the current version and the available one
  <li>Initiate update by clicking "Apply Update Now" button

You will be presented with confirmation window.

![Update window](../images/softnas-update-2.png)

Once agreed, the update process will begin and you will be presented with the download process bar.

Once download is complete, installation will began automatically and you will lose web connectivity to your SoftNAS GUI interface due to restart. You can re-login back to it momentarily and start verification process.

That concludes SoftNAS Cloud software update using GUI.

### Update process (CLI)

As well it is possible to perform SoftNAS update using a command line interface. To use this method you must have a shell access to the server where SoftNAS appliance is hosted.

A "softnas-cmd" command allows to perform many different operations, however for the purpose of this document we'll concentrate on a few related to the update it self:

<ul>
<li>login - Login to SoftNAS.</li>
<li>checkupdate - Check if new software updates are available.</li>
<li>executeupdate - Execute and apply software updates.</li>
<li>statusupdate - Return the status on an update that is currently in progress.</li>

</ul>

A typical session would look like this:

#### 1. Authentication.

##### Command
softnas-cmd login USERNAME PASSWORD --base_url https://localhost/softnas --pretty_print

##### Response
    {
        "result": {},
        "session_id": 408,
        "success": true
    }

#### 2. Check for the update candidate version.
##### Command
softnas-cmd checkupdate

##### Response I - A new software is available for installation
    {
      "success" : true,
      "session_id" : 408,
      "result" : {"success":true,"msg":"A newer version is available",
      "records":{
        "statusupdate":"",
        "version":"3.4.0",
        "newversion":"3.4.1",
        "updateavailable":true,
        "msg":"A newer version is available",
        "recent_versions":[]
      },
      "total":6}
    }

##### Response II - A running software is up to date
    {
        "result": {
            "msg": "You are running the latest version",
            "records": {
                "msg": "You are running the latest version",
                "newversion": "3.4.1",
                "recent_versions": [],
                "statusupdate": "",
                "updateavailable": false,
                "version": "3.4.1"
            },
            "success": true,
            "total": 6
        },
        "session_id": 408,
        "success": true
    }


#### 3. Start update process.
##### Command
softnas-cmd executeupdate

##### Response
      {
        "success" : true,
        "session_id" : 408,
        "result" : {
          "success":true,
          "msg":"Update was started successfully. Version '3.4.1' installation is underway...",
          "records":{"newversion":"3.4.1",
          "msg":"Update was started successfully. Version '3.4.1' installation is underway..."},
          "total":2
        }
      }

#### 4. Check update status.

##### Command
softnas-cmd statusupdate
##### Response I - Installation is in progress
      {
        "success" : true,
        "session_id" : 408,
        "result" : {
          "success":true,
          "msg":"Installing packages...",
          "records":{
            "msg":"Installing packages..."},
            "total":1
          }
      }

##### Response II - SoftNAS is rebooting
      {
        "success" : true,
        "session_id" : 408,
        "result" : {
          "success":true,
          "msg":"Updating SoftNAS Console (updates available after next reboot - no reboot required now)...",
          "records":{
            "msg":"Updating SoftNAS Console (updates available after next reboot - no reboot required now)..."},
            "total":1
          }
      }

##### Response III - Update is finished
      {
        "success" : true,
        "session_id" : 408,
        "result" : {
          "success":true,
          "msg":"OK.",
        "records":{
          "msg":"OK."
          },
        "total":1
        }
      }

That concludes SoftNAS Cloud software update using CLI tool.

### Conclusion

Both update options are achieving same goal and you should use the most suitable in your case. The advantage of CLI style, however, is its suitability to be used in update automation.

</div>
