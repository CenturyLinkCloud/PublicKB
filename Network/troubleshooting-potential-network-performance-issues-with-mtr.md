{{{ 
"title": "Troubleshooting Potential Network Performance Issues with MTR", 
"date": "6-20-2017",
"author": "John Bach",
"attachments": [],
"contentIsHTML": false 
}}}

In the event a network performance issue is suspected, tools such as WinMTR (or MTR for Linux) can help isolate where a degradation might be occurring between two systems. That said, the instructions below provide a step-by-step guide how to utilize MTR to troubleshoot a potential issue:
To download "mtr" package on Red Hat or Ubuntu, follow these instructions:
1. Red Hat/CentOS - run "yum install mtr".
2. Ubuntu: type "sudo apt-get install mtr".

Once installed, run the command as root (or preface with sudo). There are two arguments we like to have in order to display both the "AS" (routing identifier) and to see the IP address of each hop. Example: mtr --aslookup --show-ips 1.2.3.4

In this example, we see some hops have packet loss (see Loss% column), but the final one doesn't. In such a case, there is no issue other than ping/ICMP packets being discarded as they are deprioritized. As long as the final hop shows no loss, there likely isn't an issue. This example is not using --aslookup or --show-ips parameters, but the principle is the same.

|Hop|Host|Loss%|Snt|Last|Avg|Best|Wrst|StDev|
|---|----|-----|---|----|---|----|----|-----|
|1.|10.254.109.1|26.9%|387|2.7|3.0|1.6|20.8|2.1|
|2.|206.142.225.194|0.0%|387|3.0|3.2|1.9|19.9|1.7|
|3.|206.142.225.217|0.0%|387|113.3|29.5|2.1|329.1|50.9|
|4.|hr4-v3007.lo1.savv|0.0%|387|3.0|6.2|1.9|65.6|9.4|
|5.|206.25.42.90|0.0%|387|6.7|8.4|4.4|39.0|3.3|
|6.|204.70.206.66|0.0%|387|4.2|11.0|3.4|207.2|23.7|
|7.|ldn-brdr-02.inet.q|0.0%|387|3.7|7.7|3.5|98.7|10.0|
|8.|lon3-brdr-01.inet.qw|1.6%|387|6.2|7.0|5.5|26.7|2.5|
|9.|195.66.225.175|0.0%|387|5.7|7.1|5.4|26.5|2.5|
|10.|54.239.100.88|20.9%|387|283.2|226.0|18.5|365.5|106.7|
|11.|54.239.100.105|14.2%|387|16.4|17.0|15.4|30.3|1.8|
|12.|54.239.42.141|85.8%|387|79.4|18.6|16.3|79.4|8.4|
|13.|???|100%|
|14.|???|100%|
|15.|52.93.36.54|5.4%|387|34.3|28.1|16.9|125.8|12.5|
|16.|52.93.36.135|41.6%|386|16.4|18.1|15.8|36.3|2.0|
|17.|178.236.0.213|0.0%|386|18.4|18.3|16.7|38.9|2.1|
|18.|ec2-34-250-205-217.|0.0%|386|16.0|16.9|15.4|42.4|2|

This example shows loss. The final hop (18) shows 87% packet loss. The loss starts showing up at hop 10 or 11 and carries down all the way to the last hop. The best way to identify the likely router that is causing the loss, look backwards from the final hop until you find a router showing Loss% greater than zero. The hop just below that would be where the likely cause of the packet loss is from.

In this case, hop 10 or 11 is likely the internet router that is causing the loss. We see 4% loss starting at hop 10 and every hop downwards has greater than 0% loss.

|Hop|Host|Loss%|Snt|Last|Avg|Best|Wrst|StDev|
|---|----|-----|---|----|---|----|----|-----|
|1.|10.254.109.1|27.6%|453|2.9|3.1|1.5|21.9|2.2|
|2.|206.142.225.194|0.0%|453|2.5|3.2|1.9|33.7|2.4|
|3.|206.142.225.217|0.0%|453|2.5|28.8|2.0|266.7|49.7|
|4.|hr4-v3007.lo1.savv|0.0%|453|2.5|6.3|1.9|75.7|9.2|
|5.|206.25.42.90|0.0%|453|6.9|8.1|4.5|25.9|2.8|
|6.|204.70.206.66|0.0%|453|5.0|9.9|3.5|281.7|23.0|
|7.|63-235-41-109.dia|0.0%|453|4.6|7.4|3.5|64.2|9.0|
|8.|lon3-brdr-01.inet.|0.2%|453|6.4|7.4|5.4|35.9|3.6|
|9.|195.66.225.175|0.0%|453|7.8|7.2|5.3|30.2|2.6|
|10.|54.239.100.88|4.0%|453|279.0|120.3|16.9|429.2|111.6|
|11.|54.239.100.105|15.0%|453|17.4|17.0|15.3|36.5|2.1|
|12.|54.239.42.141|88.9%|453|17.0|17.6|16.2|23.6|1.2|
|13.|???|100%|
|14.|???|100%|
|15.|52.93.36.58|12.0%|452|36.6|31.6|18.3|155.1|14.2|
|16.|52.93.36.155|54.1%|452|18.1|18.0|16.2|35.4|2.1|
|17.|176.32.107.11|84.7%|452|18.4|18.2|16.7|22.0|1.1|
|18.|ec2-34-250-205-2|87.8%|452|17.8|17.1|15.5|23.2|1.3|

If the above scenario is the case, then the issue is whom to contact to get help with this loss. If the IP address before the hop with loss is owned by your ISP, then you should contact your ISP and create a ticket to investigate. If the issue starts towards the bottom of this list, then it's likely that you'll need to open a ticket with CenturyLink Cloud. To do this, e-mail to help@ctl.io and provide the output of your MTR as well as other details such as your source IP (google search "what's my ip"), what time it occurred (include timezone), and whether you're connected via a VPN tunnel or direct connection.
