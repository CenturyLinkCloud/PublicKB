{{{
  "title": "Monitors for Managed Apache HTTPd Server",
  "date": "10-14-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The table below lists the supported monitors for the Managed Apache HTTPd Server service.</p>
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
        <p>Process Monitor</p>
      </td>
      <td>
        <p>Verifies that Apache is running; if process is not running will automatically restart service. If this fails an alarm will be generated to Operations for resolution.</p>
      </td>
      <td>
        <p>1 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Response Time</p>
      </td>
      <td>
        <p>The amount of time it takes the Apache HTTPd server to respond to a simple request. The threshold is configurable. The default is greater than 2.00 seconds.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Requests Per Second</p>
      </td>
      <td>
        <p>Enabled Monitors the number of requests per second, if past a default value (75) this will throw an alert to Operations.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Total Accesses</p>
      </td>
      <td>
        <p>Watches total number of pages accesses; if greater than 100,000 in a 5 minute window will throw an alert to Operations.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Authentication failures</p>
      </td>
      <td>
        <p>Alerts Operations in the event an authentication fails.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Log “error”</p>
      </td>
      <td>
        <p>Monitors web server log for all Errors.</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Log “fail”</p>
      </td>
      <td>
        <p>Monitors web server log for all Failures.</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Log “warn”</p>
      </td>
      <td>
        <p>Monitors web server log for all warnings.</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Log custom check</p>
      </td>
      <td>
        <p>Customer is able to define custom defined log keyword checks in log entries.</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Busy Workers %</p>
      </td>
      <td>
        <p>Monitors the percentage of busy works versus max clients. The threshold is configurable. The default threshold is &gt;99%</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Clients in Keep Alive %</p>
      </td>
      <td>
        <p>Monitors the percentage of clients in keep alive state versus max clients. The threshold is configurable. The default threshold is &gt;25%.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Clients in DNS Lookup %</p>
      </td>
      <td>
        <p>Monitors the percentage of clients in the dns lookup state versus max clients. The threshold is configurable. The default threshold is &gt;25%.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Clients in Logging %</p>
      </td>
      <td>
        <p>Monitors the percentage of clients in the logging state versus max clients. The threshold is configurable. The default threshold is &gt;80%.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Total Mem Usage %</p>
      </td>
      <td>
        <p>Monitors the total memory usage of all httpd processes versus total physical memory of the system. The threshold is configurable. The default threshold is &gt;50%.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>URL Monitor</p>
      </td>
      <td>
        <p>Remote monitor, which traverses the Internet and performs a simple http request and alerts when the specified timeout is exceeded. The default timeout is 120 seconds. The threshold is configurable and can be managed through the SAVVIS
          Station Portal.</p>
      </td>
      <td>
        <p>5 Min</p>
      </td>
    </tr>
  </tbody>
</table>
<p><strong>&nbsp;</strong>
</p>

<p><strong>&nbsp;</strong>
</p>
