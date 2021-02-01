{{{
  "title": "Monitors for Managed Microsoft SQL Server Service",
  "date": "10-14-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The following tables detail the monitors supported for the Managed MS SQL service on Lumen Cloud:</p>
Monitors for Microsoft SQL Server Service
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
        <p>MS-SQL Error Log</p>
      </td>
      <td>
        <p>The MS-SQL error Log is polled for errors and failures</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Windows Event Log</p>
      </td>
      <td>
        <p>The Event log is polled for MS-SQL Server errors</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL Server Service</p>
      </td>
      <td>
        <p>Service The MS-SQL Server Service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL Agent Service</p>
      </td>
      <td>
        <p>The MS-SQL Server Agent Service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL SSIS Service</p>
      </td>
      <td>
        <p>Alarms if the MS-SQL SSIS Service is not running</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Number of Deadlocks /sec</p>
      </td>
      <td>
        <p>Alarms when there is a Deadlock</p>
      </td>
      <td>
        <p>15 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL Server CPU Usage</p>
      </td>
      <td>
        <p>The MS-SQL Server Process is over 90%</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL Server Memory Usage</p>
      </td>
      <td>
        <p>The MS-SQL Server database engine memory usage is greater than 85% of the total server memory</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Database Unavailable</p>
      </td>
      <td>
        <p>Alarms when a database is not online</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Blocking</p>
      </td>
      <td>
        <p>Alarms on any SPID is blocked by another SPID or a Full Scan</p>
      </td>
      <td>
        <p>10 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Failed SQL Job</p>
      </td>
      <td>
        <p>Alarms on any SQL job with a failure status</p>
      </td>
      <td>
        <p>15 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Database Last Backed Up</p>
      </td>
      <td>
        <p>Alarms when a database has not been backed up in the past 24 hours or more</p>
      </td>
      <td>
        <p>15 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Database File Free Space</p>
      </td>
      <td>
        <p>Alarms when a databases' data or log files percentage of free space is below X. Only applies to databases that are not set to auto grow.</p>
      </td>
      <td>
        <p>15 Min</p>
        
      </td>
    </tr>
  </tbody>
</table>
Monitors for Microsoft SQL Database Mirroring
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
        <p>Log Send Queue Size</p>
      </td>
      <td>
        <p>Alarms when the Log Send Queue size is above 256MB</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Redo Queue Size</p>
      </td>
      <td>
        <p>Alarms when the Redo Queue size is above 256MB</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>ACK Latency</p>
      </td>
      <td>
        <p>Alarms when the ACK Latency time is above 700 ms</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Mirror Status</p>
      </td>
      <td>
        <p>Alarms when a Database Mirror is in an Invalid state</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
  </tbody>
</table>

Monitors for Microsoft SQL Server Analysis Services
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
        <p>MS-SQL OLAP Error Log</p>
      </td>
      <td>
        <p>The MS-SQL Analysis Services error Log is polled for errors and failures</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL OLAP Service State</p>
      </td>
      <td>
        <p>The MS-SQL Analysis Services Service is stopped</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL OLAP CPU Usage</p>
      </td>
      <td>
        <p>The MS-SQL Analysis Services Process is over 90%</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL OLAP Memory Usage</p>
      </td>
      <td>
        <p>The MS-SQL Analysis Services memory usage is greater than 85% of the total server memory</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL OLAP Connection Failures</p>
      </td>
      <td>
        <p>Alarms when an application cannot successfully connect to the MS-SQL Analysis Services Service</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL OLAP Deadlocks</p>
      </td>
      <td>
        <p>Alarms when a deadlock occurs in the OLAP engine</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL OLAP I/O Errors</p>
      </td>
      <td>
        <p>Alarms when an I/O error is incurred in the OLAP cube</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
  </tbody>
</table>
Monitors for Microsoft SQL Server Reporting Services
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
        <p>MS-SQL SSRS Error Log</p>
      </td>
      <td>
        <p>The MS-SQL SSRS error Log is polled for errors and failures</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL SSRS Service State</p>
      </td>
      <td>
        <p>The MS-SQL SSRS Service is stopped</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL SSRS CPU Usage</p>
      </td>
      <td>
        <p>The MS-SQL SSRS Process is over 90%</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL SSRS Memory Usage</p>
      </td>
      <td>
        <p>The MS-SQL SSRS memory usage is greater than 85% of the total server memory</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL SSRS Errors</p>
      </td>
      <td>
        <p>Alarms when an HTTP 400 or 500 Error is thrown</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MS-SQL SSRS Server Busy Errors</p>
      </td>
      <td>
        <p>Alarms when an HTTP 503 Error is thrown for insufficient server resources</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
  </tbody>
</table>

