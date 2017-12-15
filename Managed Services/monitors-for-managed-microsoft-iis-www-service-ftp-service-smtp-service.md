{{{
  "title": "Monitors for Managed Microsoft IIS - WWW Service, FTP Service, SMTP Service",
  "date": "10-14-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The following tables detail the monitors support for the Managed Microsoft IIS WWW, FTP, and SMTP Services.</p>
Monitors for Microsoft IIS WWW Service
<table>
  <tbody>
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
    <tr>
      <td>
        <p>IIS CPU Usage</p>
      </td>
      <td>
        <p>The IIS inetInfo process is over 90%</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS Memory Usage</p>
      </td>
      <td>
        <p>The IIS inetInfo process memory usage is greater than 90% of the total server memory</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS ASP State Service</p>
      </td>
      <td>
        <p>The IIS ASP.net State service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS Admin Service</p>
      </td>
      <td>
        <p>The IIS Admin (inetInfo) service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS WWW Service</p>
      </td>
      <td>
        <p>The IIS W3SVC service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS Application Host Helper Service</p>
      </td>
      <td>
        <p>The IIS Application Host Helper service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS WAS Service</p>
      </td>
      <td>
        <p>The IIS WAS service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Windows Event Log</p>
      </td>
      <td>
        <p>The Event log is polled for IIS Errors related to the web server components of IIS</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS WWW Port Check</p>
      </td>
      <td>
        <p>Alarms if TCP Port 80 is not listening</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS Blocked Requests</p>
      </td>
      <td>
        <p>Alarms when a request was denied because a user defined bandwidth threshold was exceeded</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>IIS Not Found Errors</p>
      </td>
      <td>
        <p>Alarms when a 404 error is generated</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
  </tbody>
</table>
Monitors for Microsoft IIS FTP Service
<table>
  <tbody>
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
    <tr>
      <td>
        <p>FTP Service</p>
      </td>
      <td>
        <p>The IIS FTP service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Windows Event Log</p>
      </td>
      <td>
        <p>The Event log is polled for IIS Errors related to the FTP server components of IIS</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>FTP Port Check</p>
      </td>
      <td>
        <p>Alarms if TCP port 21 is not listening</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>FTP Bytes Sent</p>
      </td>
      <td>
        <p>Alarms if the FTP Service is sending more than x MB</p>
      </td>
      <td>
        <p>15 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>FTP Bytes Received</p>
      </td>
      <td>
        <p>Alarms if the FTP Service is receiving more than x MB</p>
      </td>
      <td>
        <p>15 Min</p>
      </td>
    </tr>
  </tbody>
</table>
<strong>&nbsp;</strong>Monitors for Microsoft IIS SMTP Service
<table>
  <tbody>
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
    <tr>
      <td>
        <p>SMTP Service</p>
      </td>
      <td>
        <p>The IIS SMTP service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Windows Event Log</p>
      </td>
      <td>
        <p>The Event log is polled for IIS Errors related to the FTP server components of IIS</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>SMTP Port Check</p>
      </td>
      <td>
        <p>Alarms if TCP port 25 is not listening</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>SMTP Connection Refused</p>
      </td>
      <td>
        <p>Alarms when the server cannot create an outbound connection</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
  </tbody>
</table>
