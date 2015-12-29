{{{
  "title": "Application Specific: MySQL Server Disappeared",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT

This document is for users of AppFog v1. This document does not apply to the current AppFog service that is located in CenturyLink Cloud Control Portal.

### Documentation


<pre><code>Mysql::Error: MySQL server has gone away
</code></pre>
<p>This occurs when an app attempts to use persistent MySQL connections without closing them. AppFog apps should always close database connections and should not use persistent MySQL connections.</p>
