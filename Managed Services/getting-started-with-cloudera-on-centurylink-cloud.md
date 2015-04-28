{{{
  "title": "Getting Started with Cloudera on CenturyLink Cloud",
  "date": "04-28-2015",
  "author": "Tim Baumgartner",
  "attachments": [],
  "contentIsHTML": false
}}}

<p>Cloudera Hadoop combines Apache Hadoop with a number of other open source projects to create a single, massively scalable system where you can unite storage with an array of powerful processing and analytic frameworks.</p>
<p>Here’s how to create a managed Cloudera Hadoop environment in CenturyLink Cloud.</p>
<p><strong>1.&nbsp;Search for “Cloudera” in the Blueprints library. Then, click the version and cluster configuration Blueprint that suits your needs.</strong>
</p>
<p><img src="../images/Cloudera/Cloudera_Article_1.png" alt="CLC Search Cloudera Blueprint" />
</p>
<p><strong>2. Click on the "Deploy Blueprint" button.</strong>
</p>
<p><img src="../images/Cloudera/Cloudera_Article_2.png" alt="CLC Deploy Cloudera Blueprint" /></p>
<p><strong>3.&nbsp;Fill out the appropriate details for the CLC Managed Cloudera Hadoop Blueprint.</strong>
</p>
<p><img src="../images/Cloudera/Cloudera_Article_3.png" alt="CLC Build Cloudera Servers" />
</p>
<p><strong>4.&nbsp;Select your Cloudera Version and Components.</strong>
<br/>The User name and Password you set here will be your login for Cloudera Manager, Hue and, if installed, Navigator.
</p>
<p><img src="../images/Cloudera/Cloudera_Article_4.PNG" alt="CLC Select Cloudera Components" />
</p>
<p><strong>5.&nbsp;Verify your configuration details.</strong>
</p>
<p><img src="../images/Cloudera/Cloudera_Article_5.PNG" alt="CLC Verify Cloudera Configuration" />
</p>
<p><strong>6.&nbsp;Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.</strong>
</p>
<p><img src="../images/Cloudera/Cloudera_Article_6.png" alt="CLC Cloudera Blueprint Executing" /></p>
<p>You will receive emails as each server is being built and then you will receive an additional email stating that the entire Cloudera cluster build is complete. Please do not use the servers until you have received this final email.</p>
<p><strong>NOTE:</strong>&nbsp;The server now has the Cloudera Hadoop software installed and activated - your instances will be unmanaged or managed, based on the Blueprint deployed.</p>
<p><strong>FREQUENTLY ASKED QUESTIONS</strong>
</p>
<p><strong>Q: How do I create more nodes?</strong>
</p>
<p>A: You can create additional nodes for your CenturyLink Cloud Managed Cloudera Hadoop cluster by running the “Add Node” Blueprint.</p>
<p><strong>Q: How is the CenturyLink Cloud for Managed Cloudera Hadoop priced?</strong>
</p>
<p>A: CenturyLink Cloud Managed Cloudera Hadoop is priced by [the instance, billed hourly].</p>
<p><strong>Q: What Versions of Cloudera Hadoop does CenturyLink Cloud support?</strong>
</p>
<p>A: CDH5 Express (unmanaged), CDH5 Basic (managed), CDH5 Basic + HBase (managed), CDH5 Enterprise Data Hub (managed).</p>
<p><strong>Q: Which additional Hadoop components are available?</strong>
</p>
<p>A: Currently the following components are availabe and are pre-configured based on industry best practices when the cluster builds:
<ul>
 <li>Accumulo</li>
 <li>HBase</li>
 <li>Impala</li>
 <li>Key-Value Store Indexer (Requires HBase and Solr)</li>
 <li>Navigator (Not available for the Express Version)</li>
 <li>Sentry</li>
 <li>Solr</li>
 <li>Spark</li>
</ul>
<br>
For a description of each component visit the <u>[Cloudera Add-On Services Available on CenturyLink Cloud](Cloudera-Add-On-Services-Available-on-CenturyLink-Cloud.md)</u>article.
</p>
<p><strong>Q: How do I access Cloudera Manager, Hue or Navigator?</strong>
</p>
<p>A: Cloudera Manager, Hue or Navigator can be accessed on the first Node, port 7180 for Cloudera Manager, port 8888 for Hue and port 7187 for Navigator via an SSH port on a public IP or by using <u>[VPN](../Network/how-to-configure-client-vpn.md)</u>.
<br>
For a detailed guide of Cloudera Manager on CenturyLink Cloud, download the <u>[CenturyLink Cloud Cloudera Manager Guide](https://www.centurylinkcloud.com/knowledge-base/attachments/CenturyLink_Cloudera_Manager_Guide_11032014.pdf/)</u>.
</p>
<p><strong>Q: What cluster options are available on CenturyLink Cloud?</strong>
</p>
<p>A: The Blueprints come in 1 and 4 server configurations. You can use the “Add Node” Blueprint to scale the cluster to meet your needs.</p>
<p><strong>Q: Can the customer provide their own Cloudera Hadoop License?</strong>
</p>
<p>A: Not at this time.
</p>
<p><strong>Q: Can *un-managed* Cloudera Hadoop Environment be converted to *Managed* (or vice versa)?</strong>
</p>
<p>A: This capability is not available at this time.</p>
