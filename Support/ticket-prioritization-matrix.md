{{{
  "title": "Ticket Prioritization Matrix",
  "date": "4-16-2015",
  "author": "Justin Lentz",
  "attachments": [],
  "contentIsHTML": false
}}}

Tickets are worked according to priority in the order in which they are received. The priority designation indicates the level, extent, and impact on the customer.

Customers may assign the priority of normal or high to tickets they create by using the correct email address to create the ticket. Once assigned, the priority level is used to determine the resources allocated for resolving the ticket, timelines for resolution, and the escalation matrix.

Each incoming ticket is triaged and the priority evaluated according to the criteria defined below. The following matrix covers Support Incidents, Requests, Questions and Service Task Requests. Billing and Sales Inquiries are not included in this matrix or SLA.

### Support Agreement Matrix

<table class="table table--large permission-matrix">
    <thead>
        <tr class="section-header">
            <th>Priority</th>
            <th>Developer Support (Free)</th>
            <th>Professional Support</th>
            <th>Enterprise Support</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>High</strong></td>
            <td>Not Available</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td><strong>Normal</strong></td>
            <td>Available</td>
            <td>Available</td>
            <td>Available</td>
        </tr>
        <tr>
            <td><strong>Escalation Mechanism</strong></td>
            <td>Not Available</td>
            <td><a href="../Support/how-do-i-escalate-a-ticket.md">Available</a></td>
            <td><a href="../Support/how-do-i-escalate-a-ticket.md">Available</a></td></td>
        </tr>
    </tbody>
</table>

### Ticket Prioritization Matrix

<table class="table table--large permission-matrix">
    <thead>
        <tr class="section-header">
            <th>Priority</th>
            <th>Description</th>
            <th>First Response</th>
            <th>Communication</th>
            <th>Email to Create Ticket</th>
            <th>Target Restoration SLA Time <a href="#1">[1]</a></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>High</strong></td>
            <td>
                <p>Any element of the service is unavailable</p>
                <p>Any hosted server is offline or non-functional due to conditions beyond customer control</p>
                <p>Measurable performance degradation in any given datacenter</p></td>
            <td>30 minutes</td>
            <td>
                <p>Ticket entry updated hourly</p>
                <p>Incident Report may be requested by the customer for a minimum 3 hr service engagement charge</p></td>
            <td>high@ctl.io</td>
            <td>8 hours</td>
        </tr>
        <tr>
            <td><strong>Normal</strong></td>
            <td>Any new service request</td>
            <td>1 hour</td>
            <td>Updated every 8 hours</td>
            <td>normal@ctl.io</td>
            <td>3 business days <a href="#2">[2]</a></td>
        </tr>
    </tbody>
</table>

### Service Tasks

<table class="table table--large permission-matrix">
    <thead>
        <tr class="section-header">
            <th>Priority</th>
            <th>Description</th>
            <th>First Response</th>
            <th>Communication</th>
            <th>Availability <a href="#3">[3]</a></th>
            <th>Email to Create Ticket</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Normal</strong></td>
            <td>Any new service task request</td>
            <td>24 hours after request</td>
            <td>Ticket entry updated daily</td>
            <td>Completed Monday - Friday during business hours, 9am - 5pm Pacific Time</td>
            <td>servicetasks@t3n.zendesk.com</td>
        </tr>
    </tbody>
</table>


<div id="1">[1] All technical details and resources need to be available in the ticket.</div>

<div id="2">[2] Complexity of tasks will have a significant impact on the the resolution time. In most cases, the simple requests can be completed in much less time, normally 1 business day.</div>

<div id="3">[3] Service Task estimation and duties are performed during business hours, Monday through Friday, 9am-5pm Pacific Time.</div>


### FAQ

**I need a guarantee that a support request will be completed in less than the SLA time offered.**

If your support plan qualifies, you are welcome to escalate the request using our escalation procedures: [How do I escalate a ticket?](../Support/how-do-i-escalate-a-ticket.md)
