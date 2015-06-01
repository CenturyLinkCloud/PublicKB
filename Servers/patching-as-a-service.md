{{{
  "title": "Patching as-a-Service",
  "date": "5-29-2015",
  "author": "Benjamin Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}



### Description

This document describes how to launch a blueprint for patching and how to collect information on patches deployed.

Operating Systems may be patched on CenturyLink Cloud via a blueprint. This service allows the user to patch a VM to the latest available patches provided by the OS vendor. The blueprint will kick off one or multiple attempts to apply patches, including a series of reboots. Reboots will cease and the execution will complete when there are no more patches to apply.

Currently, the Operating Systems that may be updated with this service are:

* Windows 2012
* Windows 2012R2

### Audience:

CenturyLink Cloud Users

### Support:

This service has been tested for the scope identified within this article. Product improvement is important to us so our Product Team will be aware of issues related to this service, but no one will providing direct client support. If you have suggestions for improvement, please submit a feature request.

### Pricing
This service is currently free of charge.

# Blueprint

### Steps:

1\. **Maintenance Mode**

  The process initiated by the Blueprint may include several, automated reboots, so please disable alerts by putting the VM in maintenance mode.

2\. **Locate the correct Blueprint in the Blueprint Library**

  For Windows 2012, and Windows 2012R2, locate and select “Windows Update Scripts.”

![Windows Update Blueprint](../images/Patching/PatchaaS_WindowsUpdateHover.png)

3\. **Click the Deploy Blueprint Button**

4\. **Set Required Parameters**

Select whether you want to run under the default server administrator or specify credentials.
Select the server you want to patch from the drop down.
Press the green “next step 2” button.

5\. **Review and Confirm the Blueprint**

6\. **Deploy the Blueprint**

Once verified, click on the “deploy blueprint” button. You will see the deployment details stating the Blueprint is queued for execution.
This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment times may vary. Please wait for the build queue to update deployment status.

You should receive an email notifying you the server patching has begun.

7\. **Deployment Complete**

The execution will continue even after the completion of the blueprint so please leave your VM in maintenance mode until you receive an email informing you of completion.

8\. **Execution Complete**

<p>After the patching is complete you will receive an email that patching is complete. Please remove the VM from maintenance mode.</p>


# Summary of All Patches Deployed to a Server

A history of all executions against your server is available for your review. The response will contain a high-level overview of all the patches installed for each execution and when they were applied.


![Patching Summary](../images/Patching/PatchaaS_Summary.png)

#### Authentication

Reference [API Documentation about authentication](https://www.centurylinkcloud.com/api-docs/v2/#authentication) to retrieve the Bearer token to include in all other requests.

## URL

### Structure

```
Get  http://patching-dev.useast.appfog.ctl.io/rest/{accountalias}/server/{servername}/patch

```

### Example

```
Get  http://patching-dev.useast.appfog.ctl.io/rest/osd/server/VA1OSDTEST01/patch
```

## Request

####URI and Querystring Perameters

| Name | Type | Description |
| --- | --- | --- |
| accountalias | string | Short code for a particular account |
| servername | string | The control-portal name assigned as VM creation, comprised of datacenter code, account alias, custom name, and two-digit number |

## Response

| Name | Type | Description |
| --- | --- | --- |
| execution_id | string | The execution ID associated with a particular patch |
| status | string | Could be pending or completed |
| start_time | date/Time | Either the start time of the entire execution (which contains all initiations) or a particular initiation.|
| end_time |  date/Time | Either the end time of the entire execution (which contains all initiations) or a particular initiation. |
| init_messages | complex | Shows the quantity of initiations |
| init_begin_message | string | "Invoking SUS API" |
| init_end_mesasge | string | identifies how many updates were installed and the URLS of the patches |

# Detail of Patches Deployed in an Execution

Details on all attempted patches for a single execution against a server are available for your review. The response will contain information from the vendor about the patch and the status of the attempt.

![Patching Detail](../images/PatchaaS_Detail.png)

#### Authentication

Reference [API Documentation about authentication](https://www.centurylinkcloud.com/api-docs/v2/#authentication) to retrieve the Bearer token to include in all other requests.

## URL

### Structure

```
Get https://patching-dev.useast.appfog.ctl.io/rest/{accountalias}/server/{servername}/patch/{execution_id}
```

### Example

```
Get http://patching-dev.useast.appfog.ctl.io/rest/osd/server/VA1OSDTEST01/patch/VA1-123456
```

## Request

####URI and Querystring Perameters

| Name | Type | Description |
| --- | --- | --- |
| accountalias | string | Short code for a particular account |
| servername | string | The control-portal name assigned as VM creation, comprised of datacenter code, account alias, custom name, and two-digit number |
| execution_id | string | Correlation ID for all the patches included with a single update execution, obtained from the Patch Summary response or emails regarding a patch request. The execution ID format will be aa#-######. |



## Response

| Name | Type | Description |
| --- | --- | --- |
| execution_id | string | The execution ID associated with a particular patch |
| status | string | Could be pending or completed |
| start_time | date/Time | When this value is superior to patches, indicates the start time of the entire execution (which contains all initiations). When this value is inferior to patches, indicates the start time of the patch.|
| end_time |  date/Time | When this value is superior to patches, indicates the end time of the entire execution (which contains all initiations). When this value is inferior to patches, indicates the end time of the patch. |
| Duration | string | The minutes and seconds between the start and end time. |
| begin_message | string | "Update Process BEGIN" |
| end_message | string | "Updating Complete" |
| patches | Number | Quantity of patches installed |
| patch_begin_message | string | Identifies the Software or OS updated and the reference number (KB#######) for that particular update |
| patch_end_message | string | Result code from the vendor, defining the possible results of an install. https://msdn.microsoft.com/en-us/library/windows/desktop/aa387095(v=vs.85).aspx |
| status | string | for an individual patch, could be pending, completed, or failed |
