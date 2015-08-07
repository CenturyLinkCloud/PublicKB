{{{
  "title": "Nessus Security Vulnerability Scanning",
  "date": "07-01-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
Centurylink Cloud customers can leverage Nessus Security Vulnerability scanning services via [Service Task](http://www.ctl.io/service-tasks) to discover security vulnerabilities on Cloud Virtual Machines provisioned across the platform.

### How To Request a Nessus Security Vulnerability Scan
Customers should request a [Service Task](../Service Tasks/requesting-service-tasks-on-centurylink-cloud.md) for [Nessus Security Vulnerability Scanning](http://www.ctl.io/service-tasks/#nessus). In the request customers should supply the following information:

* Customer Alias & [Pin](../Support/pin-authentication-for-support-requests.md)
* Time (including time zone) you wish the scan to run
* The list of Virtual Servers & IP addresses (public, private or both) you want scanned
* For **Credentialed** Vulnerability Scans the customer may be required to provide valid credentials

### Best Practices
It is recommended Nessus Security Vulnerability Scan's are performed during non-peak business hours to reduce impact on services.

### Vulnerability Listing
A [complete listing of the security vulnerabilities](http://www.tenable.com/plugins/index.php?view=all) can be found on the Tenable Network Security website.

### Sample Reports
Customers can [view sample reports](http://www.tenable.com/products/nessus/sample-reports) on the Tenable Network Security website.

### FAQ

**Q: Do Vulnerability Scanning services require an agent?**

A: No

**Q: Are user accounts or credentials required for Vulnerability Scanning?**

A: Yes, if you wish to run a Credentialed Vulnerability Scan.  Customers have the choice of between **Network-based Scans (Uncredentialed)**, **Credentialed**, or both.

**Q: What is the expected response time to schedule and receive my Vulnerability Scan?**

A: Please refer to our [Ticket Prioritization Matrix](../Support/ticket-prioritization-matrix.md)
