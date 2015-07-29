{{{
  "title": "Application Specific: Error 402",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>Resource pool issues can usually be resolved by bypassing the cache with the <code>--no-resources</code> flag:</p>
<pre><code>$ af update &lt;appname&gt; --no-resources
</code></pre>
<p>Sometimes symbolic links in your code base can cause this error, especially with Node apps. This command will list all of the symbolic links in your directory:</p>
<pre><code>$ find . -type s | xargs -l
</code></pre>
<p>If it's a node app, it's likely you have a <code>node_modules/.bin</code> directory, and that may be the problem. Usually, you can just delete the entire <code>.bin</code> directory if you aren't using it.</p>
<p>You can also add the following to your <code>.afignore</code> file:</p>
<pre><code>node_modules/.bin/
</code></pre>
