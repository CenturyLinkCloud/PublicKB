{{{
  "title": "Monitors for Managed Microsoft Active Directory Service",
  "date": "10-14-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The following table details the monitors that are enabled for the Managed Microsoft Active Directory Service on CenturyLink Cloud:</p>
<table>
  <thead>
    <tr>
      <td>
        <p>Monitor</p>
      </td>
      <td>
        <p>Description</p>
      </td>
      <td>
        <p>Frequency</p>
      </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p>Replication Queue</p>
      </td>
      <td>
        <p>Alarms when the number of Active Directory synchronizations queued is above 1</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>DNS Failures</p>
      </td>
      <td>
        <p>Alarms when the number of Failed DNS Zone Transfer requests is above 1</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>DNS CPU Usage</p>
      </td>
      <td>
        <p>Alarms when the DNS service consumes more than 75% of the CPU</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>DNS Memory Usage</p>
      </td>
      <td>
        <p>Alarms when the DNS service consumes more than 35MB of memory</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>FRS CPU Usage</p>
      </td>
      <td>
        <p>Alarms when the FRS service consumes more than 80% of the CPU <strong>(2003 only)</strong>
        </p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>FRS Memory Usage</p>
      </td>
      <td>
        <p>Alarms when the FRS service consumes more than 10MB of memory <strong>(2003 only)</strong>
        </p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Active Directory CPU Usage</p>
      </td>
      <td>
        <p>Alarms when Active Directory consumes more than 80% of the CPU</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Active Directory Memory Usage</p>
      </td>
      <td>
        <p>Alarms when the DNS service consumes more than 60MB of memory</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>LDAP Bind Time</p>
      </td>
      <td>
        <p>Alarms when the Bind Time is over 600 milliseconds</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Time Offset</p>
      </td>
      <td>
        <p>Alarms when the time offset between the local Domain Controller and the PDC is greater than 1 second</p>
      </td>
      <td>
        <p>15 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Subnet Undefined</p>
      </td>
      <td>
        <p>Alarms when a subnet is not defined for a site in Active Directory</p>
      </td>
      <td>
        <p>Instantly</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Connectivity</p>
      </td>
      <td>
        <p>Alarms when a Domain Controller cannot be pinged, is not registered in DNS, cannot be reached via RPC or cannot be reached via LDAP</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Replication</p>
      </td>
      <td>
        <p>Alarms when Replication is failing between Domain Controllers</p>
      </td>
      <td>
        <p>15 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Topology</p>
      </td>
      <td>
        <p>Alarms when the Active Directory Topology does not include all Domain Controllers</p>
      </td>
      <td>
        <p>15 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Cut Off Servers</p>
      </td>
      <td>
        <p>Alarms when a Replication Partner is offline</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Advertising</p>
      </td>
      <td>
        <p>Alarms when a Domain Controller in unable to come online</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Role Holder Check</p>
      </td>
      <td>
        <p>Alarms when a Domain Controller cannot locate a Role Holder</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Intersite Replication</p>
      </td>
      <td>
        <p>Alarms when Intersite replication is failing</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>FSMO connectivity</p>
      </td>
      <td>
        <p>Alarms when a Domain Controller cannot reach a Role Holder</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Active Directory Services</p>
      </td>
      <td>
        <p>Alarms when a core service for Active Directory is not running</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>SYSVOL Access</p>
      </td>
      <td>
        <p>Alarms when the SYSVOL share is unreachable</p>
      </td>
      <td>
        <p>5 Minutes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Incoming/Outgoing Replication</p>
      </td>
      <td>
        <p>Alarms when replication is failing</p>
      </td>
      <td>
        <p>10 Minutes</p>
      </td>
    </tr>
  </tbody>
</table>
