{{{
  "title": "Platform Specific: How do I move my apps and data to another Account?",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ol>
<li>
<p>Send us the email address you want to associate with the “Destination” account. We will create a New account on the same plan type as your “Original” account.</p>
</li>
<li>
<p>You will need to complete the account verification steps.</p>
</li>
<li>
<p>There are two ways to download your code:</p>
<ol>
<li>
<p>Via the AppFog command-line tool (AF CLI):</p>
<ul>
<li>Open up your command line and log in to the “Original” account.</li>
<li>Download all of your applications using this command (which will download a copy of the source code to your current system folder):</li>
</ul>
<p>$ af pull &lt;app_name&gt;`</p>
</li>
<li>
<p>Via the App in the Web Console:</p>
<ul>
<li>Go to the <a href="https://console.appfog.com/login">login page</a> and log in.</li>
<li>Go to your App (you should be on the "Mission Control" tab) and click the "Download Source Code" button to download your application code.</li>
</ul>
</li>
</ol>
</li>
<li>
<p>Next, get a database dump of each database using the export services command:</p>
<pre><code>$ af export-service &lt;service_name&gt;
</code></pre>
</li>
<li>
<p>Finally, list the env vars for each app using the command:</p>
<pre><code>$ af env &lt;app_name&gt;
</code></pre>
</li>
<li>
<p>Log out of the “Original” account and login to the “Destination” account via the CLI.</p>
</li>
<li>
<p>In the “Destination” account, upload and deploy your applications using the upload/push syntax:</p>
<pre><code>$ af push &lt;app_name&gt;
</code></pre>
</li>
<li>
<p>Add each apps env vars using the command:</p>
<pre><code>$ af env-add &lt;app_name&gt; &lt;variable [=] value&gt;
</code></pre>
</li>
<li>
<p>Create and import your data using the "import services" command for importing data into the new service:</p>
<pre><code>$ af import-service &lt;service&gt; &lt;url&gt;
</code></pre>
</li>
<li>
<p>Test the newly created applications in the “Destination” account and confirm they are functioning as expected.</p>
</li>
<li>
<p>Remove your applications on your "Original" account. <span style="color: #990000;"><strong>IMPORTANT DISCLAIMER: Please ONLY do this step if you are certain your applications and services are functioning as they should on the new accounts.</strong></span> Log out of your "Destination" account and then log back in to your "Original" account. Remove all applications and services from your "Original" account via one of two methods:</p>
<ol>
<li>
<p>Applications and Services can be removed with the AF CLI using these commands:</p>
<p><code>$ af delete &lt;app_name&gt;</code> and <code>$ af delete-service &lt;service-name&gt;</code></p>
</li>
<li>
<p>Or from the web console by logging in and doing the following:</p>
<ul>
<li>Go to "Apps": select apps &gt; app_name &gt; settings &gt; delete app</li>
<li>Go to "Services": select services &gt; select service to delete</li>
</ul>
</li>
</ol>
</li>
</ol>
