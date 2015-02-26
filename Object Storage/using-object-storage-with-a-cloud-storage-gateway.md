{{{
  "title": "Using Object Storage with a Cloud Storage Gateway",
  "date": "1-7-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

Using Object Storage with a Cloud Storage Gateway
<p>CenturyLink Cloud customers may wish to leverage our S3 compatible Object Storage with Cloud Storage Gateway appliances. A cloud storage gateway is a network appliance or server which resides at the customer premises and translates cloud storage
  APIs such as SOAP or REST to block-based storage protocols such as iSCSI or file-based interfaces such as NFS or CIFS. Unlike the cloud storage services which they complement, cloud storage gateways use standard network protocols which integrate
  with existing applications. Cloud storage gateways can also serve as intermediaries to multiple cloud storage providers. Some cloud storage gateways also include additional storage features such as backup and recovery, caching, compression, encryption,
  storage de-duplication and provisioning.</p>
<p>There are many Cloud Storage Gateway appliances on the market today. In this knowledge base we will focus on&nbsp;<a href="http://www.twinstrata.com/">TwinStrata</a>. The TwinStrata CloudArray&nbsp;provides customers various
  delivery models for the CloudArray product and Cloud Storage. Customers should validate with their Cloud Storage Gateway provider the support of an S3 compatible Object Storage. </p>
<h3>Supporting Information</h3>
<p>Information and details around the CenturyLink Cloud Object Storage can be found in our&nbsp;<a href="https://t3n.zendesk.com/forums/20789095-Object-Storage"><strong>Knowledge base</strong></a>. It is also important to note that
  CenturyLink Cloud provides no support for any 3rd party Cloud Storage Gateways. We are simply providing cloud based storage for use with these Cloud Storage Gateways.  </p>
<h3>Prerequisites</h3>
<ul>
  <li>A CenturyLink Cloud Account</li>
  <li>TwinStrata CloudArray Virtual or Physical Appliance Base Configuration</li>
  <li>An object storage user is created in the CenturyLink Cloud Control Portal. <a href="https://t3n.zendesk.com/entries/21648384-Using-Object-Storage-from-the-Control-Portal">See this KB</a>
  </li>
  <li>The Cloud Storage Gateway has internet access ports as defined by the TwinStrata Installation Documentation.</li>
</ul>
<h3>Configuring CenturyLink Cloud as a Cloud Provider</h3>
<p>1. Select the Cloud Providers link in the TwinStrata CloudArray Dashboard</p>
<p><img src="https://t3n.zendesk.com/attachments/token/9qglxzzyfxjcuvz/?name=cloud+providers+01.png" alt="cloud_providers_01.png" />
</p>
<p>2. Select Configure New Cloud Provider and Select <strong>S3 Compatible</strong>
</p>
<p><strong><img src="https://t3n.zendesk.com/attachments/token/zgglh9shasiukpo/?name=cloud+providers+02.png" alt="cloud_providers_02.png" /></strong>
</p>
<p>3. Enter the details required to connect to the selected Cloud Provider. </p>
<ul>
  <li>Currently Object Storage is only available out of our Canada Region. <strong>The Node URL is ca.tier3.io</strong>
  </li>
  <li>Provide the&nbsp;<strong>access key id</strong> and&nbsp;<strong>secret access key&nbsp;</strong>for the user created in the prerequisites</li>
  <li>Encryption, Compression and SSL are recommended</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/1awhhwleoylupqf/?name=cloud+providers+03.png" alt="cloud_providers_03.png" />
</p>

<h3>Configuring TwinStrata CloudArray</h3>
<p>Customers should consult best practices and installation guides from TwinStrata to finalize the configuration of the TwinStrata Cloud Array appliance. This includes, but is not limited to, Cache, Provisioning Policies and NAS or iSCSI services.
  </p>

<p><strong>Last Updated WED, 06 FEB 2014, 15:00 PM EST</strong>
</p>
