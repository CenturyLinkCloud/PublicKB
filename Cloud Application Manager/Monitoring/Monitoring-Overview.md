{{{
"title": "Monitoring site overview",
"date": "01-23-2019",
"author": "Thomas Broadwell",
"keywords": ["cam administration", "management", "overview", "cam", "monitoring", "settings", "policies", "manage policies", "monitoring checks"],
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Landing page](#landing-page)
* [Dashboards](#dashboards)
* [Events](#events)
* [Policies](#policies)
* [Suppressions](#supressions)
* [Graph](#graphing)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)

### Overview

Cloud Application Manager **Monitoring Site** is where you can view metrics on providers and administer monitoring checks and policies for systems and services.  

* In the Dashboards page you will view AWS and Azure metrics along with Watcher agent metrics. 
* The Events page will display any active events within the selected context (Org/CostCenter/Workspace).
* The Policies page displays configured policies and allows for the manipulation of policies.
* The Agents page lists deployed agents and details about the agent, the host VM and the policies that are applicable. 
* The Suppression site provides the ability to view, edit or delete suppressions for monitored servers.  
* The Graph page provides graphical representation of agents' and cloud providers' metrics over specified time periods.

### Audience

All users with Cloud Application Manager access.

### Prerequisites

* The user must have access to the workspace where the monitored assets are configured.
* The user should be at the organization level scope to access the Settings 
* Access to Cloud Application Manager, [Monitoring Site](https://monitoring.cam.ctl.io/) options in the left side menu.

### Navigation

When you first access the Cloud Application Manager Monitoring Site, you will land on the **Events** tab by default. The lefthand navigation contains each of the Monitoring Site components:

* Dashboards
* Events
* Policies
* Agents
* Suppressions
* Graph

### Dashboards
The **Dashboards** tabs allows customers to view multple cloud native monitoring data for Microsoft Azure & Amazon Web Services (AWS) providers. 

Providers must be configered through **Managed Services Anywhere**. If you have no Providers configured, you can click on the **Add AWS Dashboard** or **Add Azure Dashboard**. Click the **"Getting Started with Managed Services Anywhere"** link for step by step instructions.
LINK TO KB Article: https://www.ctl.io/knowledge-base/cloud-application-manager/managed-services/getting-started-with-cam-enable-managed-provider/


### Events

The **Events** tab provides a view of events that may be a warning or critical to your infrastructure based policy checks. 

Each event shown contains the **Agent**, **Check**, **Info**, and **Options** for the Event.

**Agent**
* Agent Hostname
* IP Address
* Status - *Critical or Warning*

**Check reporting Event**
* Name and output

**Info**
* Count of consecutive times the check was reported
* Last Occurence Date and time

**Options** (gear icon)
* Suppress Agent - suppresses all further Events from the Agent
* Suppress Check - suppresses all further Events from the Check 
* Delete Event - delete the reported Event and reset count

### Policies

Policies are a collection of checks that can be configured and applied to one or more agents. 

The **Policies** tab provides a list of policies setup for by your organization by Scope. Your current selected Workspace defines the Organization, Cost Center, and Workspace as your default view. To view additional details about each Scope, you can click the arrow located to the left of each Scope.

Scopes:
* Global - Monitoring Specific 
* Organization - exists in CAM
* Cost Center - exists in CAM
* Workspace - exists in CAM
* Provider- exists in CAM
* Agent - Monitoring Specific

You can add a new policy by clicking **New** or view categories by clicking **Check Catalog**. 

### Agents

The **Agents** tab provides a view of the existing monitored Agents for the selected Workspace. Agents are listed by **Name**, **Operating System**, **Agent Version**, **Support ID**, **Status**, and **Config**.

* Name - Hostname of Host VM
* Operating System - Deployed Operating System of Host VM
* Agent Version - Version of the running Agent
* Support ID - Unique Identifier for Lumen Operations Center
* Status - State of the Agent *(Online or Offline)*
* Config - Depicts availability of updates for the Agent

To view an individual Agent specific details to that server, click the highlighted Agent.

You can also click the gear icon on the top right corner to **Refresh Facts** or **Refresh Config** for selected Agent(s) listed.

### Suppressions

The **Suppressions** tab provides a view of the server(s) of which Events have been suppressed. 

*Please note: Servers or Checks listed on the Suppressions tab will not have monitored events sent to our Operations Center for investigtaion and resolution.*

### Graph

The **Graph** tab allows the capability to create a custom graph of selecetd Metrics from a selected Source (Agent or Provider.) 

To create a graph, click in the **Select Source** section and select a source from the drop down then click in the **Select Metrics** section to select a source from the drop down. Multiple Sources and Metrics can be chosen and will be shown with an overlay.

For the Chart type, you can click the radio button next to Line Chart, Area Chart, or Multi-Bar Chart.

To view metrics from a certain date or time, click and make your selections in the **From** and **Until** sections. Results will then populate in the graph below and continue to refresh the data until you exit the tab. 



