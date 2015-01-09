{{{
  "title": "CenturyLink Cloud Network Load Balancing Health Check Services",
  "date": "10-31-2014",
  "author": "Chris Little",
  "attachments": []
}}}

CenturyLink Cloud Platform Load Balancing Health Check Services
<p>The CenturyLink Cloud platform provides load balancing services using the Citrix Netscaler VPX product. &nbsp;Customers who leverage this platform can use a variety of health checks to validate the availability of infrastructure services.</p>
<ul>
  <li>Tcp (default): &nbsp;The NetScaler appliance establishes a 3-way handshake with the monitor destination, and then closes the connection.</li>
  <li>Ping (default): &nbsp;The NetScaler appliance sends an ICMP echo request to the destination of the monitor and expects an ICMP echo response.</li>
  <li>HTTP-EVC (upon special exception approval): &nbsp;The NetScaler establishes a TCP connection with the monitor destination. By default the monitor will issue an http /get request and expect a valid status 200 OK. &nbsp;Customers wishing to define specific
    -send and -receive parameters (strings) can elect to do so. &nbsp; &nbsp;</li>
</ul>
<p>By default Tcp and Ping monitors are created as part of any load balancing group. &nbsp;Customers who elect to leverage custom parameters (strings) for the HTTP-EVC monitor should provide valid -send and -receive parameters as part of the load balancing
  request. &nbsp;CenturyLink Cloud encourages the use of status pages to perform the HTTP-EVC health check. &nbsp;Examples are shown below:</p>
<ul>
  <li>-Send Parameter (string): &nbsp;Get /serverstatus.html&nbsp;</li>
  <li>-Receive Parameter (string): Website Online</li>
</ul>
<p>Customers who require special health checks outside the items listed in this KB or require further information should contact the NOC.</p>