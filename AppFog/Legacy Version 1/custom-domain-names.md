{{{
  "title": "Customize: Custom Domain Names",
  "date": "1-28-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog allows you to associate a custom domain name with your application, so that when a user types <code>www.myamazingwebapp.com</code> into their browser's address bar, your web application is loaded.</p>
<p>To do this, follow the steps below:</p>
<ul>
<li>First, configure AppFog to redirect requests to your application using either the <a href="#web-console">Web Console</a> or the <a href="#CLI">Command-line Tool</a>.</li>
<li>Then you'll need to <a href="#custom-domain-dns">update your DNS Records</a> maintained by your Domain Name provider or on your Authoritative Name Server.</li>
</ul>
<h3 id="custom-domain-app-console">Web Console</h3>
<ol>
<li>Head over to the <a href="https://console.appfog.com">app console</a> and click on your app.</li>
<li>Click on the "Domain Names" tab on the left.</li>
<li>Add your custom domain name in the field and hit the "Update" button.</li>
</ol>
<p>Alternatively, you can use the CLI to map the custom domain to your application -- follow the instructions below.</p>
<h3 id="custom-domain-af-cli">Command-line Tool</h3>
<ol>
<li>If you haven't already, install the <a href="http://docs.appfog.com/getting-started/af-cli">af command line tool</a> and log in.</li>
<li>Map the domain. $<code>af map</code></li>
</ol>
<p>For example:</p>
<pre>$ af map {appname} www.example.com</pre>
<h3 id="custom-domain-dns">Update your DNS Records</h3>
<blockquote><strong>Note: </strong>If you intend to use SSL with your site, <strong><em>STOP HERE</em></strong> and go check out our <a href="http://docs.appfog.com/customize/ssl">SSL for Custom Domains</a> documentation. It includes information on the different DNS configuration needed for SSL Endpoint termination.</blockquote>
<p>We recommend using the <code>www.</code> subdomain as your canonical domain. Here's how to do that:</p>
<h4>Redirect Your Root Domain</h4>
<p>At your DNS host, set up a redirect (302) from your root domain (<code>yourdomain.com</code>) to <code>www.yourdomain.com</code>.</p>
<p>This is a fairly standard tool that DNS services provide. If you don’t see an option for it at your domain host, contact their support services and they should be able to do that for you. If your DNS provider does not offer the redirect option it is possible to set up an A Record for your root domain. Please contact our <a href="mailto:noc@ctl.io">Support</a> staff and they will provide an IP address. This is not our recommended configuration. <em>Please be aware that these IP addresses are subject to change without prior notice.</em></p>
<h4>Create a CNAME Alias</h4>
<p>Depending on which infrastructure your app is running on, create a CNAME alias record for <code>www.yourdomain.com</code> to:</p>
<p>CenturyLink Cloud (Santa Clara, CA):</p>
<pre>cname01.uc01.clc.af.cm</pre>
<p>AWS US East (Virgina):</p>
<pre>cname01.aws.af.cm</pre>
<p>AWS Europe West (Ireland):</p>
<pre>cname01.eu01.aws.af.cm</pre>
<p>AWS Asia Southeast (Singapore):</p>
<pre>cname01.ap01.aws.af.cm</pre>
<hr />
<p>That's it! DNS propagation can take anywhere from a few minutes to 48 hours dep ending on your location, but once that's finished your app should resolve at your new custom domain.</p>
