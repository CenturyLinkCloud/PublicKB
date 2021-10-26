{{{
  "title": "Getting Started with Managed Tomcat",
  "date": "10-26-2022",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Apache Tomcat is an open source software implementation of the Java Servlet and JavaServer Pages technologies. As a collaboration of best-of-breed developers from around the world, Apache Tomcat has rapidly become one of the leading Web servers. Here's
  how to create a managed Tomcat environment in Lumen Cloud.</p>

<b>NOTE</b>: Before you can deploy Managed Tomcat, you must create a Managed Red Hat server.

<p>1. Log on to the <a href="//control.ctl.io/">Control Portal</a>. Using the left side navigation bar, click <b>Orchestration</b> > <b>Blueprints Library</b>. Click the “CLC Managed Apache Tomcat” Blueprint.
</p>

<p>2. Click the <b>DEPLOY BLUEPRINT</b> button.
</p>
<p>3. Fill out the appropriate details for the CLC Managed Apache Tomcat Blueprint.
</p>
<p><b>NOTE</b>: Please choose the same server for both the Installation and Registration of Managed Apache Tomcat. This server must have Managed Red Hat installed, otherwise the Blueprint will fail.</p>
<p>Ensure that the appropriate services that are included within Apache Tomcat are installed, i.e., Tomcat v7, Tomcat v8 or Tomcat v8.5.</p>
<p>4. Verify that the information is correct.</p>

<p>5. Once verified, please click the <b>DEPLOY BLUEPRINT</b> button. You will be presented with the deployment details along with an email stating the Blueprint has been queued.
</p>
<p>You will receive an email that your Blueprint has been installed when the Blueprint is complete.</p>
<p><b>NOTE</b>: The server now has the Managed Apache software installed and activated.
</p>
<h3>&nbsp;FREQUENTLY ASKED QUESTIONS</h3>

<p><strong>Q: How is the Lumen Cloud for Managed Apache Tomcat priced?</strong>
</p>
<p>A: Lumen Cloud Web Software for Apache is priced by the VM, billed hourly.</p>
<p><strong>Q: Can the customer have multiple Apache Tomcat Instances installed on the same server?</strong>
</p>
<p>A: No, however all versions of Tomcat support the installation and configuration of "Multiple JVM's" on the same Tomcat server.</p>
<p><strong>Q: What Versions of Apache Tomcat does Lumen Cloud support? </strong>
</p>
<p>A: Lumen Cloud Supports Tomcat V7, Tomcat v8 and Tomcat v8.5.</p>
<p><strong>Q: What operating systems are supported for Managed Apache? </strong>
</p>
<p>A: Managed Red Hat.
</p>
<p><strong>Q: Can *Un-managed* Tomcat Services be converted to *Managed* (or vice versa)?</strong>
</p>
<p>A: This capability is not available at this time.</p>
