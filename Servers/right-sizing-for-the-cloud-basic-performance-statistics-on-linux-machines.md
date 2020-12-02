{{{
  "title": "Right-sizing For the Cloud: Basic Performance Statistics on Linux Machines",
  "date": "2-20-2013",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>Right-sizing For the Cloud: Basic Performance Statistics on Linux Machines</p>
<h3>Steps</h3>

<p>One of the benefits of the Lumen Cloud platform is the elasticity of resource allocation; our utility based model allows customers to pay only for the required compute resources, unlike the physical model wherein one is sizing for the maximum possible required resources. When greater capacity is needed- simply adjust your machines allocation to scale. When planning an initial deployment, some consideration is required- migrating workloads to a cloud environment isn’t quite as simple as a 1:1 mapping of physical to virtual resources. Nearly all hypervisors have mechanisms to consolidate resources requirements to extract greater performance out of lesser resources (e.g. memory ballooning, transparent page sharing, etc.). This article will focus on a few commands which provide better insight into real-world resource usage in the hope of “right-sizing” your Linux environment. For the purpose of demonstration, an Ubuntu 12.04 server will be used, however, these commands translate across most distributions. Of course, if you are looking to transition your virtualized environment to take advantage of Lumen Cloud’s enterprise performance or global data centers, you can already view most detailed resource utilization in your existing hypervisor.</p>

<ol>
  <li>The ‘free -m’ command is a simple to understand utility which displays the amount of allocated, free and used memory (in megabytes) on your server.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/8tddwlkpixqbb5t/?name=Free.PNG" alt="Free.PNG" />
</p>
  </li>
  <li>The ‘top’ command will provide greater visibility as to exactly which processes are using the resources.
  <ol>
    <li><strong>P</strong> orders by CPU usage (default)</li>
    <li><strong>T</strong> sorts by time</li>
    <li><strong>A</strong> sorts by age (newest first)</li>
    <li><strong>M</strong> orders items by RAM usage
    <p><img src="https://t3n.zendesk.com/attachments/token/bkngblgwbwvuxa0/?name=TOP.PNG" alt="TOP.PNG" />
    </p></li>
  </ol>
  </li>
  <li>The ‘<strong>iotop'</strong> command is similar to the ‘<strong>top</strong>’ command, but displays running statistics for I/O. The appropriate package will need to be installed on certain distributions, in Ubuntu/Debian
  this is accomplished by running '<strong>sudo apt-get install iotop'</strong>.</p>
<p><strong><img src="https://t3n.zendesk.com/attachments/token/nwkmy4wj12ac6ih/?name=IOTOP.PNG" alt="IOTOP.PNG" /></strong>
</p>
<p>There are several columns displayed, showing the program ID, user, disk read, disk write, swap activity, and command. These can be useful in troubleshooting or monitoring I/O activity and determining the appropriate size for your virtual machine.</p>
  </li>
  <li>‘<strong>Perf stat</strong>’ is a powerful tool similar to PerfMon in the Windows world. It is installed by issuing the '<strong>sudo apt-get install linux-tools'</strong> (you may need to specify '<strong>apt-get install linux-tools-3.2.0-23'</strong>).
  Once the package has been installed, you can issue the '<strong>perf stat'</strong> command to start granular performance counters on processes, hardware or software cycles. For a full list of pre-defined events, use the command '<strong>perf list'</strong>.
  In this example, we look at the performance counters for the apt-get command. For detailed instructions on verbiage, please see the man page <a href="http://manpages.ubuntu.com/manpages/lucid/man1/perf-stat.1.html">here</a>.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/nzrvaxynbo9pdyo/?name=perf+stat.PNG" alt="perf_stat.PNG" />
</p>
  </li>
</ol>
