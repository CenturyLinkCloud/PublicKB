{{{
  "title": "Exchange Mailbox Server Memory Usage",
  "date": "1-14-2013",
  "author": "Mark Turpin",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>You may notice that your Exchange mailbox server[s] have maxed out available memory (85%+). It is completely normal for this to happen. The Exchange process store.exe will show most of the available memory allocated to it in task manager.
  &nbsp;This is in order to allocate as much data in memory address space as possible, so that each user experiences great performance in their Outlook clients.&nbsp;
  <br />
  <br />If another process should need the more memory, the Exchange store.exe process will released it as required. <strong>This is by design.</strong>
  <br />
  <br />By default, the msExchESEParamCacheSizeMax key is not set, which means the store can allocate the memory it needs dynamically. ESE (store.exe) will grow the cache to consume almost all available RAM on the server if there is no other memory pressure
  on the system For example, if the server contains 16gb physical memory, if there is no other memory pressure, one could expect that the store.exe process will grow to use up to 14gb memory (16gb minus 2gb allocated to Kernel mode). This much larger
  database cache size results in greatly reduced disk I/O, and is preferred anyways, as reading information from memory is much faster than reading information from disk. If memory pressure occurs, as when other applications request/require memory, ESE
  will appropriately&nbsp;shrink the size of the database cache. It’s not recommended to modify the msExchESEParamCacheSizeMax attribute of the information store object.&nbsp;Lowering this value may degrade performance, in terms of server performance
  as well as in terms of end-user experience.</p>
<p>Article credit:</p>
<p>http://blogs.technet.com/b/maliks/archive/2012/04/25/exchange-2010-store-exe-service-takes-high-memory-utilization.aspx</p>