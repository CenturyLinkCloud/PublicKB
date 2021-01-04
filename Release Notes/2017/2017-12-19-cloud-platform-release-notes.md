{{{
"title": "Cloud Platform - Release Notes: December 19, 2017",
"date": "12-19-2017",
"author": "Ranga Chakravarthula",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (3)

##### Cloud Application Manager

###### Monitoring

__Graphing of Anomaly Detection and Forecasting__

This new feature set now allows for graphing of anomaly detection and forecasting in Cloud Application Manager Monitoring.  This relates to the previously released monitoring checks that utilize metric forecasting based on triple exponentially smoothed (Holt Winters) of datasets to provide anomaly detection.  This toolset provides visualization and insight for users to better understand how anomaly detection can be applied to their datasets to achieve a higher order level of event detection with Cloud Application Manager Monitoring. Helper utilities also provided to assist users in defining forecast based anomaly detection checks and their parameters.

Product Highlights include the following "functions" that can be applied to any dataset:

*	**Forecast** – Graphs based on projected future states of metric data.  Future time periods can be specified for any metric (including those originating from AWS CloudWatch.  This allows to visualize the calculation of forecasts.

*	**Confidence** – A tool to calibrate the uncertainty in a forecasted dataset.  This allows for the visualization of anomalies as a signal crosses over a confidence interval.

*	**Anomaly** – Visual representation of the degree of aberration within a signal.


__AWS Dashboards is now Live!__

Cloud Application Manager customers can now see their AWS CloudWatch metrics on the new dashboard landing page.  Information about their AWS infrastructure and services can be viewed in an easy to read dashboard.

Product Highlights Include:

*	Users will be able to list & switch between their AWS providers within a Workspace. 

*	Upon selecting a Provider, users will be able to see a subset of their configured AWS services

*	With a single click, each individual metric graph on the dashboard will allow the user to do a deep dive on our more detailed graph page. 

##### Managed Services Anywhere

__Support for Microsoft Windows 2016 Operating System__

Managed Services Anywhere now includes support for Microsoft Windows 2016 Standard and Datacenter on AWS and Azure. Deployment of the cloud providers’, AWS or Azure, OS image along with the cloud providers’ licensing are supported. Customers deploying the Windows 2016 Standard or Datacenter Operating System now have an option to "Delegate OS Management" to Lumen. With Lumen managing their virtual machine instances, customers enjoy all the benefits of Managed Services Anywhere listed here. Pricing for Managed Services Anywhere is defined here.



### Enhancements (2)

##### Cloud Application Manager

###### Cloud Optimization

__Invoice Updates__

Going forward, customers will see two separate line items on their invoices, one for AWS EC2 on-demand instances and one for AWS EC2 usage associated with Reserved Instances. A 5% efficiency rebate will be applied to on-demand instance charges and appear as its own line item

###### Dedicated Cloud Compute

__Windows Server 2016 on Dedicated Cloud Compute__

Customers of Dedicated Cloud Compute (DCC) now have the option to provision a managed Windows Server 2016 virtual instance using the new DCC UI.