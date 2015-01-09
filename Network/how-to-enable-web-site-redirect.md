{{{
  "title": "How to Enable Web Site Redirect",
  "date": "7-30-2012",
  "author": "jw@tier3.com",
  "attachments": []
}}}

<p>Site Redirect enables the ability to do a HTTP based redirect of a web site domain name to any URL such as http://www.foo.com redirect to http://www.bar.com/happy.html. You can enable this using the portal by doing the following steps:</p>
<ol>
  <li>Log onto the portal and go to Domains &gt; Redirects</li>
  <li>Click <strong>Create Site Redirect </strong>and fill in the values correctly:</li>
  <ol>
    <li><em><strong>URL</strong></em>: This is the domain name that you would like to redirect such as www.foo.com</li>
    <li><strong><em>Redirect To</em></strong>: This is the URL to redirect any HTTP based traffic that goes to www.foo.com to such as&nbsp;http://www.bar.com/happy.html</li>
  </ol>
  <li>Once that is entered then you need to edit the DNS entry for www.foo.com to point to the correct site:</li>
  <ol>
    <li>For a CNAME record: www CNAME siteredirect.tier3.com (point the CNAME to siteredirect.tier3.com)</li>
    <li>For a A record: www A 70.42.161.28 (point the A record to 70.42.161.28)</li>
  </ol>
</ol>
<div>Once that is completed and DNS for www.foo.com now points to siteredirect.tier3.com or 70.42.161.28 it can take up to 1 hour to replicate the redirection settings.&nbsp;</div>