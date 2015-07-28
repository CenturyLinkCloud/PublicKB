{{{
  "title": "Customize: Configuring SSL for a Custom Domain",
  "date": "1-28-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>SSL is automatically enabled on all apps with the AppFog-specific subdomain names, i.e. domain names that end in the following:</p>
<ul>
<li>*.aws.af.cm</li>
<li>*.ap01.aws.af.cm</li>
<li>*.eu01.aws.af.cm</li>
</ul>
<p>Note: While CLC (CenturyLink Cloud) data centers have SSL endpoints, AppFog v1 doesn't have the ability to use them. AppFog v2 will have that functionality.</p>
<h4><strong>Note: SSL for custom domain names is currently only available for:</strong></h4>
<ul>
<li>Apps deployed onto the Amazon AWS infrastructures</li>
<li>
<p>The following plans:</p>
<ul>
<li>Developer: 1 SSL Endpoint</li>
<li>Silver: 2 SSL Endpoints</li>
<li>Gold: 4 SSL Endpoints</li>
<li>Platinum: 8 SSL Endpoints</li>
</ul>
</li>
</ul>
<h3>Setting up SSL on your Custom Domain</h3>
<p>Adding SSL to your custom domain is simple. First, make sure you have the following:</p>
<ul>
<li>Your RSA private key</li>
<li>Your SSL certificate</li>
<li>Intermediate certificate from the Certificate Authority (of the same Class as your SSL certificate, if applicable)</li>
</ul>
<h3>Get an SSL Certificate</h3>
<p>If you already have a certificate, skip down to <a href="#install">the next section on installation</a>.</p>
<p>To get an SSL certificate from a Certificate Authority, you'll first need to generate an RSA private key and a Certificate Signing Request (CSR).</p>
<h4>Generate a private key</h4>
<p>You can use the <code><a href="https://www.openssl.org/source/">openssl</a></code> toolkit to generate an RSA private key and a CSR:</p>
<pre>$ openssl genrsa -des3 -out server.key 2048</pre>
<p>Note: the strength of your key is up to you (although some Certificate Authorities require a minimum bit depth). This command will create a 2048-bit key. Other values can be used. Refer to the <a href="http://www.openssl.org/docs/HOWTO/keys.txt">OpenSSL documentation</a> for more on this.</p>
<p>You'll have to use a passphrase when you generate the key, but we'll remove it later.</p>
<h4>Generate a CSR</h4>
<p>You can now use the private key you just made to generate a CSR:</p>
<pre>$ openssl req -new -key server.key -out server.csr</pre>
<h4>Get a certificate from a Certificate Authority</h4>
<p>You can now send your CSR (the <code>server.csr</code> file) to a Certificate Authority, which they'll use to generate your certificate. Once you have that, you're ready to set up SSL for your AppFog app.</p>
<h3 id="install">Install your private key and SSL certificate</h3>
<p>If your private key is password-protected, you'll have to remove the password first:</p>
<pre>$ cp server.key server.key.org
$ openssl rsa -in server.key.org -out server.key</pre>
<h4>Upload Certificate Data</h4>
<p>Now you're ready to head over to the <a href="http://console.appfog.com">AppFog web console</a>. Click on one of your apps, hit the "SSL" tab on the left, and hit the "Get Started" button.</p>
<p>On the "Upload Certificate Data" screen, click on the "Upload Your Certificate" button and navigate to your certificate file (<code>server.crt</code> if you followed the instructions above). AppFog will validate the certificate and display the certificate details.</p>
<p>Next, click on the "Upload Your Private Key" button and navigate to your (decrypted) private key (<code>server.key</code> if you followed the instructions above). Similar to the certificate, AppFog will verify the key.</p>
<p>Click "Upload Your Optional Intermediate Certificate" and select the intermediate certificate from your CA. Again, AppFog will display information about the intermediate certificate.</p>
<p>You now have an SSL terminator that should look something like:</p>
<pre>af-ssl-term-0-000000000.us-east-1.elb.amazonaws.com</pre>
<h4>Change your DNS</h4>
<p>Now head over to your DNS host and update your app's CNAME alias to point at the SSL terminator you just created. That's it! Once your new DNS settings propagate, SSL will be enabled for your app.</p>
