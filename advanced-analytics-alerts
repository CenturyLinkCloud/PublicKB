{{{
  "title": "Advanced Analytics Alerts",
  "date": "10-07-2019",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
Users of Advanced Analytics within Cloud Application Manager's Analytics Site will find that Alerts can be generated to inform of Security and Cost-related events. Once alerts are configured, it can be determined who will address the alerts once they arrive.


### Prerequisites

* Decide who you require to process alerts - your CAM Technical Account Manager (TAM) or someone on your team.
* Gain agreement on next steps once the alert has been received
* Access to the Analytics Site
* Correct Permissions in Advanced Analytics so that from the menu you can navigate to Cost > Alerts > Manager; Security > Alerts > CloudTrail > Manager; and Security > Alerts > Resoures > Manager.

If you lack the correct permissions, please reach out to your Technical Account Manager (TAM) or, lacking a TAM, create a support ticket.


#### Important Information

By default, the notification method for alerts is email, but there are options to use lambda, slack, SNS, PagerDuty, or Syslog. Please contact your CAM TAM to assist you with enabling "Group ACL permissions for Settings, Configurations."

The same alerts are not available for all provider types.

##### Cost Alerts
Some of the reasons for Cost Alerts Include:
- Budget thresholds
- Cost fluctuations
- New Cost Allocation Tag Values
- Network Usage


1. To get started, navigate to Cost > Alerts > Manager
2. Click "+ New Alert", then choose an alert type.
3. Enter the Alert Name
4. Click Notifications. The Notifications box expands and presents configuration options.

##### Security Alerts
Not all security alert categories are available for all provider types.

**CloudTrail Alerts**

Some of the Reasons for CloudTrail Alerts Are:
- Security Related Events
- AWS Config coniguration changed
- Blocklisted IP address making Console Logins
- Snapshot or instance deletion or termination
- IAM access key actions
- Passowrd Policy Changes
- New Event Types in CloudTrail
- New Region, Service, or User Detected
- Changes to Route Tables, Security Groups, VPCs,



1. To get started, navigate to Security > Alerts > CloudTrail > Manager
2. Determine whether to use Built-In Alerts or Custom. The Alert Manager has two tabs: Built-In Alerts and Custom Alerts.

*Built-in Alerts*

* Click the title of any built-in alert to review the details.
* Fill in the Name, select the Risk Level, fill in the Custom Description, and any other fields which may be necessary.
* Click the "Notifications" link to select the email address or other notification method (see above).
* If it appears, click the "Fliters" link. The Filters section allow you to refine your search by the following parameters: region, service, event, and user.
* If it appears, clic the "Advanced Options" link. The Advanced Options section allows you to determine how the tool responds to CloudTrail events.
* The Ignored section displays all the alert results that you have ignored.

*Custom Alerts*

* Custom alerts function in the same way as the Built-In alerts.
* Go to the Alert Manager page of CloudTrail and click + New Alert or click Copy Alert in a selected built-in alert.
* Type a name for your custom alert and configure the other parameters identified in the Built-In Alert section.
* If you copied an existing built-in alert, it will pre-populate the search criteria. If your custom alert is not based on a built-in alert, you will need to select your search criteria. Click the *Alert me when I see...* drop-down menu to use the options from the built-in alert as template for your custom alert.


3. Once you have configured your alert, save it and make sure that you turn on the alert by moving the slider **ON**

**Resources Alerts**

Some of the reasons for Resource Alerts are:
- Resources are discovered and are publicly-accessible
- Resource Changes are discovered via AWS Config
- Changes are made to a security Group
- New Publicly Available Resources


1. To get started, navigate to Security > Alerts > Resources > Manager
2. Click "+ New Alert", then choose an alert type.
3. Enter the Alert Name
4. Enter Other configurable fields such as Frequency, Resources, etc. depending on the Alert Type selected
5. Click Notifications. The Notifications box expands and presents configuration options.
6. Once you have configured your alert, save it and make sure that you turn on the alert by moving the slider **ON**


##### Alert Results

The Advanced Analytics tool will send your alerts in the notification format and parameters that you configured in the Built-in and Custom Alerts tab, such as email, Slack, or SNS. It also provides you with a comprehensive and searchable list of all your alert results. To get your results, go to the left navigation pane, and choose either Cost > Alerts > Results or Security > Alerts > (CloudTrail or Resources) > Results.

The Alert Results page contains the details about your alerts: what event triggered the alert, when the alert occured, where the alert occurred geographically, and who triggered the alert.
