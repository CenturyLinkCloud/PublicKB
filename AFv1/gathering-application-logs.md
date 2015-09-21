{{{
  "title": "Application Specific: Gathering Application Logs",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT

This document is for users of AppFog v1. This document does not apply to the current AppFog service that is located in CenturyLink Cloud Control Portal.

### Documentation


<p>Have you attempted to use <code>af logs #APPNAME</code> or <code>af restart #APPNAME --trace</code>?</p>
<p>You can also use <code>af help logs</code> and <code>af help start</code> to get information on the syntax.</p>
<p>Because of the way the apps are wrapped in <a href="https://cloudfoundry.org">Cloud Foundry</a> (which is what AppFog is based on), there isn't a way to see processes from a single app. You can try using <code>af logs #APPNAME --all</code> for better granularity, but that's the best we can do, unfortunately.</p>
