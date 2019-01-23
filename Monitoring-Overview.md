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


![Monitoring site - Landing site](../../images/cloud-application-manager/msa/monitoring-landing-page.png)


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

* Name 
* Operation System 
* Agent Version
* Support ID
* Status
* Config

To view individual Agent specific details to that server, click the highlighted Agent.

You can also click the gear icon on the top right corner to **Refresh Facts** or **Refresh Config** for all listed Agents.

### Suppressions

The **Suppressions** tab provides a view of the server(s) of which Events have been suppressed. 

*Please note: Servers listed on the Suppressions tab will not have monitored events sent to our Operations Center for investigtaion and resolution.*




#### Shortcut to access Settings from context switcher

1. Access to the context switcher drop-down, located at the top navigation bar. 
2. Click on **Organizations** tab.

   ![Change CAM Workspace Scope](../../images/cloud-application-manager/admin-overview2.png)

3. Click on the **edit/pencil button**, located in the top right of the organization card. 

### Billing

Billing contents are only reachable from Management site left side navigation menu and administrator users.  
Billing allows you to access Cloud Application Manager billing section to review billing details in your Organization.  

![Billing Dashboard](../../images/cloud-application-manager/billing/billing-dashboard.png)

Billing section plots three options:

* **Dashboard** where several bar graphs show billed amount with different filters.
* **Usage History** where you can see a list with the previous months billing summary.
* **Pricing** displays the price list of the different Cloud Application Manager products and services.

See [Billing](../Billing/billing-menu.md) documentation to get knowledge about billing features.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at \ProgramData\ElasticBox\Logs\elasticbox-agent.log
