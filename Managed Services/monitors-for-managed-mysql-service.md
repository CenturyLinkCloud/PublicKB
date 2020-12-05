{{{
  "title": "Monitors for Managed MySQL Service",
  "date": "10-14-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The following table details the monitors supported for the Managed MySQL service on Lumen Cloud:</p>
Monitors for MySQL Server Service
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
        <p>MySQL Error Log</p>
      </td>
      <td>
        <p>The MySQL error log is polled for the words “ERROR” or “FAILED” will trap (case ignored)</p>
      </td>
      <td>
        <p>Instant</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>MySQL Process</p>
      </td>
      <td>
        <p>Check if the MySQL Server process is running</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Remote Root</p>
      </td>
      <td>
        <p>Checks for root account available from anything other than local host</p>
      </td>
      <td>
        <p>24 Hours</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Root Password</p>
      </td>
      <td>
        <p>Checks for root password</p>
      </td>
      <td>
        <p>24 Hours</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Anonymous</p>
      </td>
      <td>
        <p>Checks for anonymous accounts</p>
      </td>
      <td>
        <p>24 Hours</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Key Buffer Used %</p>
      </td>
      <td>
        <p>Checks percentage of maximum amount of Key Buffer used since startup</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Write hit</p>
      </td>
      <td>
        <p>Ratio of key writes to hard disk to key writes to RAM</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Read hit</p>
      </td>
      <td>
        <p>Ratio of key reads from hard disk to key reads from RAM</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>% of Total Questions</p>
      </td>
      <td>
        <p>Percentage of Slow Queries of all statements</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>% of Max used</p>
      </td>
      <td>
        <p>Percentage of Max used connections to Max Connection Size</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>InnoDB Buffer Pool Size</p>
      </td>
      <td>
        <p>Configured size of InnoDB Buffer Pool size</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>InnoDB Buffer Pool Usage</p>
      </td>
      <td>
        <p>Buffer Pool Used</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
    <tr>
      <td>
        <p>InnoDB Buffer Pool % Used</p>
      </td>
      <td>
        <p>Percentage of Buffer Pool used</p>
      </td>
      <td>
        <p>1 Minute</p>
      </td>
    </tr>
  </tbody>
</table>
