{{{
  "title": "Changing IP address on a CenturyLink Cloud hosted machines",
  "date": "5-6-2014",
  "author": "Joon Park",
  "attachments": []
}}}

<strong>SCOPE</strong>
<p>Changing IP addresses</p>

<strong>DESCRIPTION&nbsp;</strong>
<p>At this time, there is no automated way of changing IP addresses via Control Portal.&nbsp; Even with careful planning there may be times when IP addresses will need to be modified.&nbsp; This is a 2 step process to coordinate the change with the Centurylink
  Cloud Engineer.&nbsp;</p>

<strong>AUDIENCE</strong>
<p>Centurylink Cloud Users</p>

<strong>PROCESS</strong>
<ol>
  <li>
    <p>Gather the necessary information for the change.&nbsp; This will include the following</p>
  </li>
  <ol>
    <li>
      <p>Server name</p>
    </li>
    <li>
      <p>IP address to be changed, you can view your current list of provisioned IPs under Network =&gt; IP addresses</p>
    </li>
    <li>
      <p>Customer PIN</p>
    </li>
  </ol>
</ol>

<ol>
  <li>
    <p>There are 2 ways that this can be performed. </p>
  </li>
  <ol>
    <li>
      <p>Allowing a Centurylink Cloud engineer to perform the task end to end. </p>
    </li>
    <ol>
      <li>
        <p>Include the gathered information from step 1 and send mail to noc@tier3.com with subject line&nbsp; <strong>"IP change request."</strong>&nbsp; </p>
      </li>
      <li>
        <p>This mail will also include granting permission for the Cloud engineer to login to the server to make the necessary network configuration changes. </p>
      </li>
      <li>
        <p>Any downtime requirements.&nbsp; This change does require the server to go offline for a short duration &lt; 1min </p>
      </li>
    </ol>
  </ol>
</ol>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;2. &nbsp;Self-servicing the change on the server and allowing the Cloud engineer to perform the updates to Control.&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 1. &nbsp;Include the gathered information from step 1 and send mail to noc@tier3.com with subject line <strong>"IP change request (Control update only)"</strong>
</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2, &nbsp;Please obtain a valid free IP from the network page and configure on the server manually. <strong>CAUTION:</strong> &nbsp;<strong>&nbsp;This will only be applicable for IPs on the same subnet, changing the server IP address to a different network vlan will cause the server to go offline and requires a Cloud engineer to resolve!</strong>
</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;***NOTE*** Any new builds can potentially claim an IP so plan accordingly.</p>

<ol>
  <li>
    <p>Mail notification from the ticket will be sent to you upon completion of the task.&nbsp;&nbsp;</p>
  </li>
</ol>