{{{
  "title": "Cloud Application Management Monitoring for Managed OS Introduction",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Introduction
The Cloud Application Manager [Monitoring UI](https://monitoring.cam.ctl.io) is a centralized location where users can view policies, alerts and general configuration for servers that are being monitored as part of our [Managed OS Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/) offering. If interested in using this service/feature in a standalone fashion or suggestions for enhancements please contact us at [feature@ctl.io](mailto:feature@ctl.io).  


### Overview
This document describes how to access the Monitoring UI, and provides a breakdown of the different views that are available in each of the main components of the UI which consists of Events, Policies, Servers, Suppression, and Graphing.


![MonitoringLeftNavScreenShot](../../images/MonitoringLeftNavScreenShot170601.png)


##### Servers
This section lists all of the server being monitored for the selected workspace. Clicking on an individual server will provide details specific to that server and also the current status of all checks being reported back from the server.  

##### Events
On the Events tab there is a list of all active events (i.e. check that are out of their configured bound) for that workspace.  This includes statuses warning and critical, the check-type, its output, count and last occurrence.

##### Suppressions
In this area, you can view the server(s) of which traps have been suppressed, the period of time and reasoning for which the suppression is valid. Any server(s) listed here will not have its monitored events send to our operations center for investigation and resolution.  

##### Policies
Monitoring policies are groupings of one or more server checks available to be applied to a server within the selected workspace. Within the policy itself you can view the server checks and their associated configuration parameters along with the servers currently applied under that policy.  

##### Graphs
For servers that have 'metric' server checks applied to them, for which all Managed OS server do for CPU, Memory and Disk by default, you can display the data in area, line or multi-bar formats over the selected period of time via specific timeframes or generalized (i.e. now, last hour).

##### Workspaces
![MonitoringWorkspaceScreenShot](../../images/MonitoringWorkSpaceScreenShot170601.png)

After logging in the user will be in their personal workspace. Click on the workspace switcher to choose the workspace of which server(s) you wish to view.  


### Logging into the Monitoring UI.

![GlobalNavScreenShot](../../images/GlobalNavScreenShot170601.png)

After logging into Cloud Application Manager you can navigate to the Monitoring UI by clicking on the monitoring link as shown below.



### Monitoring Portal Functionality

The Monitoring Portal is intended to offer our customers visibility into the status of their environment. If you have any questions about what is being displayed or you would like to request modification the setup please open a ticket with our operations teams [here](http://managedservices.ctl.io).  

### Managed OS Default Policies

* The default monitoring policy for supported linux images can be found [here](CTLCloudMonitoringDefaultPolicy-Linux.md)
* The default monitoring policy for supported Windows images can be found [here](CTLCloudMonitoringDefaultPolicy-Windows.md)
