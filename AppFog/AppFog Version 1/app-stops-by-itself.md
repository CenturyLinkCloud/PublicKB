{{{
  "title": "Application Specific: App Stops by Itself",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>An app stopping by itself generally indicates that it has crashed. When your app crashes, AppFog automatically attempts to re-spawn it, but only a limited number of times. If it continues to crash repeatedly, it will remain stopped. You can check your crashes with <code>af crashes</code>:</p>
<pre><code>$ af crashes &lt;appname&gt;
</code></pre>
<p>And you can check the crash logs:</p>
<pre><code>$ af crashlogs &lt;appname&gt;
</code></pre>
<p>If your app has more than once instance:</p>
<pre><code>$ af crashlogs &lt;appname&gt; --all
</code></pre>
<p>The most common reason for an app to crash is running out of memory. You should find a log message indicating as much in your error logs</p>
<pre><code>$ af files &lt;appname&gt; --all /logs/stderr.log

FATAL -- : Memory limit of 256M exceeded.
FATAL -- : Actual usage was 300M, process terminated.
</code></pre>
