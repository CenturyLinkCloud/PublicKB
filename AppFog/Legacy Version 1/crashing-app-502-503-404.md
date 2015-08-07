{{{
  "title": "Application Specific: Crashing App (502/503/404)",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>If your app is at less than 100% "Running" status or you're seeing the AppFog error page, it means one or more instances of your app have crashed. You can check this status with the following command:</p>
<pre><code>$ af crashes &lt;appname&gt;
</code></pre>
<p>You can get your app's crashlogs with the following:</p>
<pre><code>$ af crashlogs &lt;appname&gt;
</code></pre>
<p>(Or if your app has multiple instances:)</p>
<pre><code>$ af crashlogs &lt;appname&gt; --all
</code></pre>
