{{{
  "title": "Cloud Server Alerting FAQ",
  "date": "11-4-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3><strong>Description</strong></h3>
<p>The CenturyLink Cloud has updated the Server Alerting capabilities which offer a&nbsp;new way to create and manage alert policies.</p>

<p><strong>Q: What's new in the server alerting service?</strong>
</p>
<p>A: The CLC team upgraded multiple aspects of the service. Previously, users configured monitors for each server and viewed a reports tab to track performance. Now, you create CPU/memory/storage alert policies, apply them to servers, and consume alerts
  in 3 key ways. Alerts can be sent via email, webhook, or through visual indicators in the updated Servers user interface.</p>

<p><strong>Q: Do my old single-server monitoring policies migrate to this new alerting service?</strong>
</p>
<p>A: No. We've rebuilt the monitoring system and cannot migrate old policies to the new alert system. Any custom monitors or IPMonitors remain in place. Note that now, your alert policies can be created once, and applied to multiple servers. This will make
  it significantly easier to update policies and impact a large number of servers immediately.</p>

<p><strong>Q: Does this only work with new servers, or can I apply these policies to existing ones?</strong>
</p>
<p>A: The new alert service applies to any server, regardless of when it was built or what operating system it is running.</p>

<p><strong>Q: How do I create alert policies in the Control Portal?</strong>
</p>
<p>A: Visit the&nbsp;<strong>Alerts</strong> page using the main navigation men, then choose&nbsp;<strong>create alert policy</strong>. Provide a name for the policy and a specific utilization threshold for CPU/memory/storage that should trigger an alert.
  <br
  /><img src="https://t3n.zendesk.com/attachments/token/dluhifjpnr6kuw7/?name=monitoringfaq01.png" alt="monitoringfaq01.png" />
</p>

<p><strong>Q: Where do I add alert policies to a server?</strong>
</p>
<p>A: Alert policies are added to each server. Visit the server's settings and select the <strong>Alerts&nbsp;</strong>tab. Choose existing policies to add to the server. Changes take effect instantly.
  <br /><img src="https://t3n.zendesk.com/attachments/token/xfz5vwn3a0lgfir/?name=monitoringfaq02.png" alt="monitoringfaq02.png" />
</p>

<p><strong>Q: What kind of emails do I receive when an alert occurs?</strong>
</p>
<p>A: The CenturyLink Cloud platform will send an email to the address(es) designated in the alert policy whenever the alert threshold is exceeded. This email message identifies the name of the alert, and what capacity of the server (e.g. 80% CPU utilization)
  trigger the alert. The platform will also send a follow up email when the alert is no longer occurring.</p>

<p><strong>Q: How can I see information in the Control Portal about active alerts?</strong>
</p>
<p>A: The Control Portal now provides a powerful way to detect alerts in progress. First, the user interface navigation highlights which servers are currently in an alert stage. The alerting status rolls up to the group containing the server, and the data
  center containing the group!
  <br /><img src="https://t3n.zendesk.com/attachments/token/ftand3mijcud2dj/?name=monitoringfaq03.png" alt="monitoringfaq03.png" />
</p>
<p>The server page itself also shows the alert details. You can see both the current amount of CPU/memory/storage consumption, and where the consumption exceeded the alert threshold.
  <br /><img src="https://t3n.zendesk.com/attachments/token/vm6apqjxnfhqkpg/?name=monitoringfaq04.png" alt="monitoringfaq04.png" />
</p>

<p><strong>Q: How do alert webhooks work?</strong>
</p>
<p>A: <a href="https://t3n.zendesk.com/entries/22916235-Webhooks-FAQ">Webhooks </a>are a powerful way to build a more event-driven relationship with your cloud environment. Users of webhooks can integrate internal systems with the resources
  running in the cloud. Alerts are now available as webhooks! Whenever an alert fires, the CenturyLink Cloud platform sends out a JSON-encoded message to a web address specified by the user. These JSON messages include the name of alert, account name,
  server name, and threshold violation details. Users can choose to also receive webhook events for alerts raised in any sub accounts.
  <br /><img src="https://t3n.zendesk.com/attachments/token/jtiu0cckldrrzll/?name=monitoringfaq05.png" alt="monitoringfaq05.png" />
</p>
