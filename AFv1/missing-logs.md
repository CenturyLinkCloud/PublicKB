{{{
  "title": "Application Specific: Missing Logs",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT

This document is for users of AppFog v1. This document does not apply to the current AppFog service that is located in CenturyLink Cloud Control Portal.

### Documentation


<p>Apps that have crashed or failed to deploy are wiped (with their logs) after an hour. In the event that <code>af logs</code> returns no data, you should check <code>af crashes</code> and <code>af crashlogs</code>. Failing that, restart and check logs again.</p>
