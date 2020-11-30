{{{ "title": "Customer Testing on CLC",
        "date": "05-23-2016",
        "author": "Platform Security",
        "attachments": [],
        "contentIsHTML": false,
        "sticky": false
 }}}

### Description

There are three types of testing that we see our customers wanting or needing to perform: load testing, penetration testing, and vulnerability scanning. Each type has its own potential impact to the platform, which is why we have requirements for notifying us ahead of time, during the testing process and afterward.

### Audience

Lumen Cloud Users

### Impact

|                          | **Potential Impact** | **Comments**                                                                                                                |
|--------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------|
|**Load Testing**          |High                  |May run into automated throttling and may be shut down due to abuse monitoring on network bandwidth, CPU, or disk usage.     |
|**Penetration Testing**   |Med                   |May run into automated throttling and possibly be shut down due to abuse monitoring if performed outside customer’s own VLAN.|
|**Vulnerability Testing** |Low                   |No impact to other customers.                                                                                                |

### Detailed Information

### Load Testing

Any test intended to find either limits or performance degradation points in systems.  

**Required Notification:** Lumen does not allow customers to perform load testing except in very special, highly controlled circumstances that must be closely coordinated ahead of time.  Advance notice to the CLC help desk (in all cases) by opening a ticket at help@ctl.io and coordinating with a Customer Care Engineer during the testing.

Tools used for testing include: LoadRunner, NeoLoad, Rational Performance Tester, Jmeter, The Grinder, and other similar tools.

### Penetration Testing

Any test intended to exploit known, or to find new, vulnerabilities in systems, applications or infrastructure configurations.  

Note that Lumen does not allow customer testing of any parts of the shared infrastructure, any testing must be scoped within a customer’s own deployed solution.

**Required Notification:** Advanced notice to the CLC help desk if the testing is performed on CLC infrastructure by opening a ticket at help@ctl.io.  Also, report any findings related to CLC infrastructure vulnerabilities by opening a ticket at security@ctl.io.

Tools used for testing include: Metasploit, ZAP, Burp Suite, protocol fuzzers, and other similar tools.

### Vulnerability Scanning

This is a test that only looks for known vulnerabilities or configuration weaknesses in applications, systems or infrastructure, but does not actually attempt to exploit them.  

Note that Lumen does not allow customer testing of any parts of the shared infrastructure, any testing must be scoped within a customer’s own deployed solution.

**Required Notification:** Allowed in customer’s own infrastructure without advanced notice to CLC.  If CLC infrastructure is to be scanned, we request advanced notice and a report of any findings related to CLC infrastructure vulnerabilities by opening a ticket at security@ctl.io.

Tools used for testing include: Nessus, OpenVAS, QualysGuard, Nexpose, Core Impact, Nmap, and other similar tools.
