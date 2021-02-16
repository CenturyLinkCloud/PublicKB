{{{
"title": "Cloud Platform - Release Notes: December 5, 2017",
"date": "12-05-2017",
"author": "Ben Stephan",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (1)

__Cloud Application Manager__

* __Anomaly Detection and Forecasting Alerting__

  Anomaly Detection and Forecasting Alerting is now Live!

  This new feature set exposes alerting based on statistical analysis that can be applied to any metric being collected by the CAM Monitoring Agent. This feature includes checks for both metric forecasting and anomaly detection that is based on triple exponentially smoothed (Holt Winters) forecast of the data set.

  Product Highlights include:

  - Anomaly Detection – Alert based on any observed metric data that falls outside of the historical operating norms. This feature allows for threshold-less alerting that triggers when the metric deviates from it’s predicted value.
  - Forecasting – Alert based on projected future states of metric data.  Allows for the configuration of thresholds that are detected to be crossed within some arbitrary future time frame.
  - Any generated alerts will be sent to a Lumen operator for evaluation, notification, and remediation.
