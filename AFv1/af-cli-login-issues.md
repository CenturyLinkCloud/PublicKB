{{{
  "title": "Platform Specific: AF CLI Login Issues",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>If you can log into the web console, but you're running into issues with the <code>af login</code> command, try this:</p>
<pre><code>$ rm ~/.af_token
$ af login
</code></pre>
