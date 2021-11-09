{{{
  "title": "Right-sizing For the Cloud: Basic Performance Statistics on Windows Machines",
  "date": "10-26-2021",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>One of the benefits of the Lumen Cloud platform is the elasticity of resource allocation; our utility based model allows customers to pay only for the required compute resources, unlike the physical model wherein one is sizing for the maximum possible required
  resources. When greater capacity is needed, simply adjust your machines allocation to scale.</p>
<p>When planning an initial deployment, some consideration is required. Migrating workloads to a cloud environment isn’t quite as simple as a 1:1 mapping of physical to virtual resources. Nearly all hypervisors have mechanisms to consolidate resources requirements
  to extract greater performance out of lesser resources (e.g., memory ballooning, transparent page sharing, etc.).</p> 
  
<p>This article will focus on a few commands that provide better insight into real-world resource usage in the hope of “right-sizing” your
  Windows environment. These commands translate across most Operating System versions.</p>
<p>If you are looking to transition your virtualized environment to take advantage of Lumen Cloud’s enterprise performance or global data centers, you can already view most detailed resource utilization in your existing hypervisor.</p>
<p>Perfmon is a natively available Windows utility that provides insight into performance counters. This tutorial guides you through collecting data for memory, processor and disk I/O utilization.</p>

<ol>
  <li>
  <p>To launch Perfmon, go to the start menu, select the “run” command (Win+R), and type “Perfmon.”</p>
  </li>
  <li>
    <p>In the left hand column, expand “Monitoring Tools.” Right-click “Performance Monitor” and choose “New Data Collector Set.”</p>
  </li>
  <li>
    <p>Give the collector an appropriate name (i.e. “RAM”) and click next. Select the location that you wish to save the collected data (i.e., C:\perfmon) and click next. Select “Save and close.”</p>
  </li>
  <li>
    <p>In the left hand column, expand “Data Collector Sets,” then “User defined,” and select the newly created collector. In the right hand pane, double click the “System Monitor Log”</p>
  </li>
  <li>
    <p>Remove the default processor collector by clicking remove.</p>
  </li>
  <li>
    <p>Add the desired monitors for capture by selecting them and clicking “add.” Hold Ctrl while clicking to select multiple counters.</p>
  </li>
  <li>
<p>On the “File” tab, change the name of the collector to reflect the counters (i.e., “RAM”). Select “Ok”.</p>
  </li>
  <li>
<p>To start the collector, right-click and select “start.” Allow the monitor to run for the desired length of time. Right-click and select “stop” when finished collecting.</p>
  </li>
  <li>
<p>To review the report, expand “Reports” and select the appropriate collector.</p>
</p>
  </li>
  <li>
  <p>Repeat this process for the desired resources. It is recommended to collect RAM, Processor and Disk I/O information when planning for virtualization.</p></li>
</ol>


<h3>Memory</h3>
<ol>
<li><strong>Memory : Available Memory</strong>. This counter indicates the amount of memory that is left after nonpaged pool allocations, paged pool allocations, process' working sets, and the file system cache have all taken their piece. In general, Windows attempts to keep this value around 4 MB. Should it drop below this for a sustained period, on the order of minutes at a time, there may be a memory shortage. Of course, you must always keep an eye out for those times when you are simply attempting to perform memory intensive tasks or large file transfers.</li>
<li><strong>Memory : Committed Bytes</strong>. This counter indicates the total amount of memory that has been committed for the exclusive use of any of the services or processes on Windows NT. Should this value approach the committed limit, you will be facing a memory shortage of unknown cause, but of certain severe consequence.</li>
<li><strong>Memory : Page Reads/sec</strong>. This counter is probably the best indicator of a memory shortage because it indicates how often the system is reading from disk because of hard page faults. The system is always using the pagefile even if there is enough RAM to support all of the applications. Thus, some number of page reads will always be encountered. However, a sustained value over 5 Page Reads/sec is often a strong indicator of a memory shortage. 
<br>
<br>

<p>You must be careful about viewing these counters to understand what they are telling you. This counter again indicates the number of reads from the disk that were done to satisfy page faults. The amount of pages read each time the system went to the disk may indeed vary. This will be a function of the application and the proximity of the data on the hard drive.</p> 
<br>
</p>Irrelevant of these facts, a sustained value of over 5 is still a strong indicator of a memory problem. Remember the importance of "sustained." System operations often fluctuate, sometimes widely. So, just because the system has a Page Reads/sec of 24 for a couple of seconds does not mean you have a memory shortage.</li>
</ol>

<h3>Disk I/O</h3>
<ol>
  <li><strong>PhysicalDisk\Avg. Disk Queue Length.</strong> This indicates how many I/O operations are waiting for the hard drive to become available. If the value here is larger than the two times the number of spindles, that means the disk itself may be the bottleneck.</li>
  <li><strong>LogicalDisk\% Free Space.</strong> This measures the percentage of free space on the selected logical disk drive. Take note if this falls below 15 percent, as you risk running out of free space for the OS to store critical files. One obvious solution here is to add more disk space.</li>
  <li><strong>Memory\Cache Bytes.</strong> This indicates the amount of memory being used for the file system cache. There may be a disk bottleneck if this value is greater than 300MB.</li>
</ol>

<h3>Processor</h3>
<ol>
<li><strong>System\Processor Queue Length.</strong> This indicates the number of threads in the processor queue. The server doesn't have enough processor power if the value is more than two times the number of CPUs for an extended period of time.</li>
<li><strong>Processor\Processor Time.</strong> This measures the percentage of elapsed time the processor spends executing a non-idle thread. If the percentage is greater than 85 percent, the processor is overwhelmed and the server may require more
  processing power.</p>
  <br>
<p>If you need additional assistance, or have any questions about designing your cloud environment, Lumen Cloud's team of Solutions Architects are readily available to assist with planning, sizing, capacity management, and migration strategies for moving and
  managing your cloud infrastructure.</p></li>
</ol>
