{{{
"title": "Cloud Platform - Release Notes: April 10, 2018",
"date": "04-10-2018",
"author": "Ranga Chakravarthula",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (1)

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/)

##### [Application Lifecycle Management](//www.ctl.io/cloud-application-manager/application-lifecycle-management/)

Application Lifecycle Management now offers a Workload Map view into the instances page, where users can see in which regions they have instances deployed, and how many. Users can also identify by color if there is an issue (red or orange) or all instances are online (green) in that region.

### Enhancements (1)

#### [CenturyLink Private Cloud on VMware Cloud Foundation](//centurylink-private-cloud-on-vmware-cloud-foundation)

Customers of CenturyLink Private Cloud on VMware Cloud Foundation now have the option for CenturyLink provided OS licenses, for Microsoft Windows and/or Red Hat Enterprise Linux.

### Announcements (2)

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/)

##### Amazon Web Services

This message is a follow-up to AWS's communication about Certificate Transparency for ACM certificates:

Google Chrome will require logging of all publicly trusted certificates issued on or after April 30, 2018 in at least two Certificate Transparency (CT) logs[1]. Any certificate issued after that date that is not in the CT logs will produce an error message in the Google Chrome browser.
Starting April 24, 2018, ACM will publish certificates to CT logs on issuance, and on renewal. No action from you is required if you want ACM to publish your certificates to CT logs, which will avoid Google Chrome displaying error messages for your certificates.

CT logs are available for public download. Some information from your certificates, including your domain names, e.g. www.example.com, will be in these logs. Please note, these logs *do not* contain the private key for your certificate. We recognize that there can be times when you do not want logging of your certificate. You can disable CT logging for ACM certificates. For instructions and examples, refer to the AWS Security blog post[2] or the ACM User Guide[3].

[1] https://www.certificate-transparency.org/
[2] https://aws.amazon.com/blogs/security/preparing-for-aws-certificate-manager-acm-certificate-transparency/
[3] https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html

Sincerely,
Amazon Web Services

#### [Load Balancer as a Service (LBaaS)](//www.ctl.io/load-balancing/)

CenturyLink Cloud is excited to release a new load balancer service in our AU1 location. We’re calling it Load Balancer as a Service (LBaaS). We added more features that allow you to focus on your business while we help service your infrastructure. You get to keep all of the features that are available in the current Shared Load Balancer service, but we’ve added a few new things to get excited about:

• TCP load balancing
• Load balance on any port 23 and up
• Configurable health checks

These new features are presently available in our AU1, CA3, DE1, DE3, GB3, IL1, NY1, SG1, UC1 and VA1 locations with plans to enable additional locations in the coming months. Be on the lookout for future announcements regarding service expansion. Please note, our Shared Load Balancer service will continue to be available in all other locations until they are LBaaS enabled.

For information on pricing for LBaaS and Shared Load Balancer, see [pricing](//www.ctl.io/pricing).
