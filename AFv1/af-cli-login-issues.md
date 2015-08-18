{{{
  "title": "Platform Specific: AF CLI Login Issues",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT

This document is for users of AppFog v1. This document does not apply to the current AppFog service that is located in CenturyLink Cloud Control Portal.

### Documentation

<p>If you can log into the web console, but you're running into issues with the <code>af login</code> command, try this:</p>
<pre><code>$ rm ~/.af_token
$ af login
</code></pre>
