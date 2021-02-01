{{{
  "title": "What to expect from Lumen Cloud on a Security Issue",
  "date": "9-22-2016",
  "author": "Gavin McMurdo",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description (goal/purpose)</h3>
<p>This KB covers what behavior customers can expect from Lumen Cloud Operations in the case of a Security Incident. </p>
<h3>Audience</h3>
<ul>
  <li>Lumen Cloud Customers</li>
</ul>
<h3>"A server in Lumen Cloud's public cloud is being scanned"</h3>
<ol>
  <li>This is a very common situation and, statistically, this will happen to any server exposed on the Internet at least once every 72 hours. The majority of these scans are throttled in order to avoid detection. As such this will not trigger alarms, and Lumen Cloud engineers will not be aware of the attack.</li>
</ol>
<h3>"A server in Lumen Cloud's public cloud is being attacked"</h3>
<ol>
  <li>Low-volume attack: The majority of attacks are throttled in order to avoid detection and to leverage a server exploit. As such this will not trigger any any alarm, and therefore Lumen Cloud Operations will not be aware of the attack.</li>
  <li>High-volume attack (DDoS): These types of attacks are designed to overwhelm the capabilities of the server. If the volume of the attack is high enough, it will will be detected by Lumen Cloud's monitoring infrastruture and Lumen Cloud's support engineering staff
    will initiate a Security Incident. In the majority of cases, the #1 priority is to mitigate the attack, and therefore it is possible that the mitigation might require that we disable the offending server(s). The Lumen Cloud support team will open a ticket to the account administrators, identified in Control.</li>
</ol>
<div>
  <h3>"Someone has filed an abuse complaint"</h3>
  <ol>
    <li>The Lumen Cloud support team will initiate a Security Incident and open a ticket against the server(s) identified in the report, submitted to account administrators. They are notified via email.</li>
    <li>Lumen Cloud is contractually bound to ensure that these complaints are investigated. If server administrators do not investigate this report within an expected timeframe, it may be necessary for us to suspend operation of the server. </li>
  </ol>
</div>
<div>
  <h3>"What does the Lumen Cloud support team do during a Security Incident?"</h3>
  <ol>
    <li>Notify our Security team about the incident.</li>
    <li>Assess the validity of security reports and other signals being receivied. If the support team has access to the affected devices, such as our cloud infrastructure or a Managed server, we will investigate it.</li>
    <li>If we do not have access to the server, the team will open a ticket in the Lumen Cloud ticketing system with all of the account administrators of that server on the ticket. The customer will be asked to take prompt action by investigating the issue.</li>
    <li>In cases where the Security&nbsp;Incident&nbsp;is determined to be adversely impacting other customers, our engineers will take immediate steps to mitigate the situation and verify that service is fully restored to normal operating status.</li>  
  </ol>
</div>
<div>&nbsp;</div>
