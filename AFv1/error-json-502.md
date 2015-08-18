{{{
  "title": "Application Specific: Error (JSON 502)",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT

This document is for users of AppFog v1. This document does not apply to the current AppFog service that is located in CenturyLink Cloud Control Portal.

### Documentation


<p>The most common reason for this error, is your application running out of available RAM. When this happens, AppFog kills the app and attempts to re-spawn it. While it's down, you see 404. To fix this, simply add more RAM to your app:</p>
<pre>$ af mem &lt;appname&gt; &lt;memory&gt;
</pre>
