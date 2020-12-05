{{{
  "title": "Troubleshooting Potential Network Performance Issues with WinMTR",
  "date": "4-14-2014",
  "author": "Dave Burkhardt",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>In the event a network performance issue is suspected, tools such as WinMTR (or MTR for Linux) can help isolate where a degradation might be occurring between two systems. That said, the instructions below provide a step-by-step guide how to utilize WinMTR
  to troubleshoot a potential issue:</p>
<p>1. Download the latest version of WinMTR and extract the WinMTR.exe file to your desktop (or a location on your hard drive).</p>
<p>2. Start the WinMTR executable, enter an IP address or a domain name (e.g., google.com) within the "Host" window, and then select "Start". Note, here is a legend what each column indicates to its corresponding row or hop/node:
  <br />Hostname — IP address or domain name of the hop. "No response from host" value may indicate blocking of ICMP packages on this hop
  <br />Nr — Order number of the hop in a route
  <br />Loss % — Percent of the lost packet responses from the node listed
  <br />Sent — Sent requests to this node
  <br />Recv — Obtained responses from the node
  <br />Best — the lowest (best) time of delay in milliseconds (mms)
  <br />Avrg — Average time of delay in mms
  <br />Worst — Maximum (the worst) time of delay in mms
  <br />Last — Time of delay of the last obtained package in mms</p>
<p>3. Wait at least 5 minutes for WinMTR to gather data from each hop. Note, there is no indication the program has completed and WinMTR will continuously check each node until you select the "Stop" button.</p>
<p>4. Inspect each hop and look for anomalies. Key indicators there might be a problems with a specific node/hop:</p>
<p>- If the "Sent" columns shows a higher number than the "Recv" column (e.g., Sent &nbsp;= 60 packets but Recv&nbsp;only equals 40 replies), this indicates a "packet loss" on that hop</p>
<p>-The "Avrg" mms exceeds ~75mms and "Worst" exceeds ~200mms</p>

<p>If it is believed a network problem might be present with connecting to one of your Lumen Cloud (CTL-C) hosts, please follow the steps above and enter the CTL-C IP address in question as the "Host". Note, if for example you are testing from a system
  that resides outside of CTL-C's platform, and you observe one of the first few hops towards the top of the WinMTR results window is problematic, the issue is likely an issue with your local network or ISP, but if the aforementioned anomalies are present
  towards the lower results, please follow these steps:</p>
<p>A. Select "Export TEXT", enter a file name, and then save the .txt file to your hard drive.</p>
<p>B. Email CTL-C's noc with this file, and also state in the message:
  <br />- The date and window of time the WinMTR session ran (WinMTR session export from 12/31/13 between 2:00-2:05pm GMT)
  <br />- The IP address of the system where the WinMTR session was executed from. Note, if the session was ran across the Internet (versus between CTL-C systems), please state this IP address (e.g., https://www.google.com/#hl=en&amp;q=what+is+my+ip)
  <br />- The IP address and hostname of the CTL-C system in question</p>
