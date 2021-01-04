{{{
  "title": "Operating System Template Maintenance",
  "date": "1-10-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description </h3>
<p>As part of the Lumen Cloud platform customers are able to deploy base Operating System templates of various Linux and Windows flavors. Frequently, clients wish to understand how these templates are maintained and updated. This KB provides a list of FAQ's to address these queries.</p>
<h3>Audience</h3>
<ul>
  <li>Lumen Cloud Clients</li>
</ul>
<h3>Frequently Asked Questions</h3>
<h4>Q: From what sources are the OS binaries obtained?</h4>
<p>A: OS binaries are obtained from the vendors software repository. For Microsoft platforms this is part of the SPLA library. For Linux platforms it varies by flavor but all Linux OS software binaries are obtained from known sources such as Redhat.com, Ubuntu.com, Centos.org or debian.org.
</p>
<h4> Q: When are OS Templates modified or updated?</h4>
<p>A: OS templates are not on a fixed maintenance schedule today. Generally, OS templates are updated if issues are identified with the template or new features are released on the cloud platform that require changes to the base templates. As such, clients are always encouraged to update/patch Operating Systems deployed in the Cloud platform to current levels post build.
</p>
<h4>Q: What quality controls are placed around OS templates that are provided as part of the Cloud platform?</h4>
<p>A: Any templates that are updated or new templates being deployed are subject to our strict Q&amp;A process. No templates are deployed out to production until they pass a long list of Q&amp;A activities. These include, but are not limited to:
</p>
    <ul>
      <li>
        <p>Build new server from template
        </p>
      </li>
      <li>
        <p>Clone the newly built server
        </p>
      </li>
      <li>
        <p>Archive / Restore
        </p>
      </li>
      <li>
        <p>Add Public IP
        </p>
      </li>
      <li>
        <p>Execute Script/Software
        </p>
      </li>
      <li>
        <p>All Power operations (Power On, Off, Reboot, Shutdown etc)
        </p>
      </li>
      <li>
        <p>Convert to Template / Convert to Server from Template
        </p>
      </li>
      <li>
        <p>Autoscale (if applicable)
        </p>
      </li>
      <li>
        <p>Change Resources (CPU/RAM)
        </p>
      </li>
      <li>
        <p>Add/modify storage
        </p>
      </li>
      <li>
        <p>Snapshot / Revert to snapshot
        </p>
      </li>
      <li>
        <p>Delete Server
        </p>
        <br />
      </li>
    </ul>
