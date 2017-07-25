{{{
  "title": "CDN services with CenturyLink Cloud",
  "date": "11-25-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Customers may deploy CDN, using one of CenturyLink’s CDN partners. To inquire about CDN services, please send an email to: <a href="mailto:CDNRequests@centurylink.com">CDNRequests@centurylink.com</a>.</p>
<p>Alternatively, you may contact your account representative.</p>
<p>From there, you will be asked to fill out a configuration form with key details of your project. Examples of some of these requirements are listed below.</p>
<h3><strong>For a CDN Caching Property:</strong></h3>
<h4>Implementation Style (choose one)</h4>
<ul>
  <li>Object Caching: the CDN delivers only objects with URLs that reference the CDN Property ID.</li>
  <li>Whole Site Caching: the CDN delivers the entire site; all pages and embedded resources.</li>
</ul>
<h4>Delivery Type (choose one)</h4>
<ul>
  <li>HTTP: non-secure delivery only</li>
  <li>HTTPS Shared Cert: secure delivery using a Shared Certificate from the CDN provider</li>
  <li>HTTPS Premium Cert: secure delivery using customer provided certificate</li>
  <li>HTTP &amp; HTTPS Premium Cert: non-secure and secure delivery with customer provided certificate.</li>
</ul>
<h4>Supername (please specify)</h4>
<p>DNS Name for website. The Supername varies based on Delivery Type, for example:</p>
<ul>
  <li>HTTP: cdn.foo.com</li>
  <li>Shared Cert: secure.footprint.net/foo/</li>
  <li>Premium Cert: cdn.foo.com</li>
</ul>
<p>Supernames must be unique and be a valid hostname with at least two dots and may contain alphanumeric characters, dash and underscore.</p>
<h4>Aliases (please specify)</h4>
<p>Aliases are additional Supernames to reference the same content in cache; treated as synonyms of the primary Supername. Must be unique and follow the same rules as Supername.</p>
<h4>Origin Server Type (choose one)</h4>
<ul>
  <li>Customer Origin (additional details required)</li>
  <li>CDN Origin Storage (additional details required)</li>
</ul>
<h4>Content Freshness (choose one)</h4>
<ul>
  <li>Honor Cache Control Headers from Origin</li>
  <li>Set Override Policies on CDN (additional details required)</li>
</ul>
<h4>Caching Regions (choose all that apply)</h4>
<p>Specify where you wish your content to be cached on the CDN Network (regional rates apply) and an expectation of the amount (GB) of content delivered from each selected region.</p>
<ul>
  <li>North America/Europe</li>
  <li>Asia</li>
  <li>South America</li>
  <li>Middle East/Africa</li>
</ul>
<h3><strong>For a On Demand Streaming Property:</strong></h3>
<h4>Delivery Type (choose one)</h4>
<ul>
  <li>HTTP/RTMP</li>
  <li>HTTPS/RTMPe</li>
</ul>
<h4>Streaming ID (please specify)</h4>
<p>Also known as Flash Media Server (FMS) application - a combination of lower case alphanumeric characters, maximum 10. No special characters with the exception of dash (-) to differentiate between different FMS applications.</p>
<h4>Supername (please specify)</h4>
<p>Designated hostname used to direct traffic to the CDN. The Supername must be unique and be a valid hostname with at least two dots and may contain alphanumeric characters, dash and underscore.</p>
<h4>Origin Server Type (choose one)</h4>
<ul>
  <li>Customer Origin (additional details required)</li>
  <li>CDN Origin Storage (additional details required)</li>
</ul>
<h4>Content Freshness (choose one)</h4>
<ul>
  <li>Honor Cache Control Headers from Origin</li>
  <li>Set Override Policies on CDN (additional details required)</li>
</ul>
<h4>Streaming Regions (choose all that apply)</h4>
<p>Specify where you wish your content to be cached on the CDN Network (regional rates apply) and an expectation of the amount (GB) of content delivered from each selected region.</p>
<ul>
  <li>North America/Europe</li>
  <li>Asia</li>
  <li>South America</li>
  <li>Middle East/Africa</li>
</ul>
