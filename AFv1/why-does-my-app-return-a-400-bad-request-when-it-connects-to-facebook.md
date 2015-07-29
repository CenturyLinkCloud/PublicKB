{{{
  "title": "Application Specific: Why does my app return a 400 bad request when it connects to Facebook?",
  "date": "1-27-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>This occurs when an app is within an infrastructure that is currently blacklisted by Facebook.</p>
<h4>Why did Facebook block certain IP’s?</h4>
<ul>
<li>This was done in resolve the adverse impact of abusive apps uploaded by free account owners to our EU-AWS and AP-AWS infra’s.</li>
</ul>
<h4>How do we get them to unblock our IP’s?</h4>
<ul>
<li>AppFog is currently working to resolve this error with the assistance of Facebook. In order to get these IP’s unblocked by Facebook, they will need to deem the IP’s as safe and non-malicious in order to put them onto their whitelist.</li>
</ul>
<h4>To workaround this issue, please clone your app to our CLC or AWS-East infrastructures.</h4>
<pre>$ clone &lt;src-app-name&gt; &lt;dest-app-name&gt; &lt;infra&gt;</pre>
<p>If you're having issues with <code>clone</code>, you can use the <code>pull</code> and <code>push</code> commands together.<br />You can find information on that in our <a href="push-pull-and-update-commands.md">PUSH, PULL and UPDATE Commands</a> document.</p>
