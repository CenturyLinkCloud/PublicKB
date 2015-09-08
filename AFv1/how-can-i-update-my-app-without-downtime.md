{{{
  "title": "Platform Specific: Does AppFog have a persistent file system?",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT

This document is for users of AppFog v1. This document does not apply to the current AppFog service that is located in CenturyLink Cloud Control Portal.

### Documentation

<p>You can update your app with zero downtime by deploying two versions of your app.</p>
<p>For example, here are the apps "example" and "example2".</p>
<pre><code>| example         | 1  | RUNNING | example.com, www.example.com  |
| example2        | 1  | RUNNING | example.aws.af.cm             |
</code></pre>
<p>Develop on the second app, example2, deploying new code until you're ready to push to example.com. This way you can live test the app without fear of affecting users.</p>
<pre><code>$ af update example2
</code></pre>
<p>Example not from the app's root directory:</p>
<pre><code>$ af update example2 --path /home/example2
</code></pre>
<p>When you're ready to push to production, first map example2 to example.com and www.example.com.</p>
<pre><code>$ af map example2 example.com 
$ af map example2 www.example.com
</code></pre>
<p>Now you have two apps running at the same URL and they're load-balanced. You can test example2 in full production at this point.</p>
<pre><code>| example         | 1  | RUNNING | example.com, www.example.com                     |
| example2        | 1  | RUNNING | example.aws.af.cm, example.com, www.example.com  |
</code></pre>
<p>Now, unmap example from example.com and www.example.com. Then map example to example.aws.af.cm and unmap example2 from example.aws.af.cm</p>
<pre><code>$ af unmap example example.com 
$ af unmap example www.example.com

$ af map example example.aws.af.cm
$ af unmap example2 example.aws.af.cm
</code></pre>
<p>Now your production and developemnt apps have been swapped:</p>
<pre><code>| example         | 1  | RUNNING | example.aws.af.cm             |
| example2        | 1  | RUNNING | example.com, www.example.com  |
</code></pre>
<p>If you run into any issues with example2, rollback is trivial. Simply map the original app, example, back to example.com and www.example.com.</p>
<p>Now you can develop against example (instead of example2) and when you're ready to deploy to production, you can reproduce the same steps as above.</p>
