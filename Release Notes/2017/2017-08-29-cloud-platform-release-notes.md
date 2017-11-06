{{{
"title": "Cloud Platform - Release Notes: August 29, 2017",
"date": "8-29-2017",
"author": "Matt Schwabenbauer",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (1)

* __Cloud Application Manager__

  - __Cloud Optimization__

    Customers who are interested in moving their Amazon Web Services account to CenturyLink for Consolidated Billing and Platform Support will now experience a completely automated process of account migration. Users will now receive an automated invitation (via the root account email or within the "My Organization" feature of the AWS Account) for accepting the migration process on their AWS Management Console. Once accepted, our automated process migrates their AWS account to CenturyLink. For full details, please visit our [Knowledge Base article](https://www.ctl.io/knowledge-base/cloud-application-manager/cloud-optimization/partner-cloud-integration-aws-existing).
     
    Cloud Application Manager customers who are interested in moving or creating  a new  Microsoft Azure Account to CenturyLink for Consolidated Billing and Platform Support can now consume the full services offered by Microsoft Azure. Previously customers were limited to consume only IaaS products. Customers who have signed up for Microsoft Azure account between January and September of 2017 will not see any impact to their existing infrastructure that they deployed in Microsoft Azure. However, their access policies will be updated to allow them to procure full Microsoft Azure services. 

### Announcements (3)

* __Load Balancing as a Service__

    - __Additional Algorithm Support: Weights Enabled__
    
    Load Balancing as a Service has expanded its Algorithm support to include the ability to apply weights to designated nodes.  The concept of weights can be applied to all support Algorithms (URL Hash, Source IP, Least Conn, and Round Robin).  The ability to apply weights will help to ensure that nodes designated with a higher weight are then apportioned a greater number of request.

    - __Additional Health Check Support: HTTP__

    Load Balancing as a Service has expanded support for Health Checks to include HTTP.

    For an HTTP health check probe to be considered successful, the instance must return a valid HTTP 200 or 300 level response. If it does this a specified number of times in a row, the health check returns a status of HEALTHY for that instance. 

* __Infrastructure as a Service__

    - __Hyperscale server provisioning in IL1 and UC1 has been disabled__

    The ability to provision Hyperscale servers has been disabled in the UC1 and IL1 locations. Other IaaS server types have not been affected.
