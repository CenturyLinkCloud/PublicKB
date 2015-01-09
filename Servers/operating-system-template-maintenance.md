{{{
  "title": "Operating System Template Maintenance",
  "date": "1-10-2014",
  "author": "Chris Little",
  "attachments": []
}}}

<h3>Description&nbsp;</h3>
<p>As part of the CenturyLink Cloud platform customers are able to deploy base Operating System templates of various Linux and Windows flavors. &nbsp;Frequently, clients wish to understand how these templates are maintained and updated. &nbsp;This KB provides
  a list of FAQ's to address these queries.</p>
<h3>Audience</h3>
<ul>
  <li>CenturyLink Cloud Clients</li>
</ul>
<h3>Frequently Asked Questions</h3>
<p>Q: &nbsp;From what sources are the OS binaries obtained?</p>
<p><em><strong>A: &nbsp;OS binaries are obtained from the vendors software repository. &nbsp;For Microsoft platforms this is part of the SPLA library. &nbsp;For Linux platforms it varies by flavor but all Linux OS software binaries are obtained from known sources such as Redhat.com, Ubuntu.com, Centos.org or debian.org.</strong></em>
</p>
<p><em><strong>&nbsp;</strong></em>Q: &nbsp;When are OS Templates modified or updated?</p>
<p><em><strong>A: &nbsp;OS templates are not on a fixed maintenance schedule today. &nbsp;Generally, OS templates are updated if issues are identified with the template or new features are released on the cloud platform that require changes to the base templates. &nbsp;As such, clients are always encouraged to update/patch Operating Systems deployed in the Cloud platform to current levels post build.</strong></em>
</p>
<p>Q: &nbsp;What quality controls are placed around OS templates that are provided as part of the Cloud platform?</p>
<p><em><strong>A: &nbsp;Any templates that are updated or new templates being deployed are subject to our strict Q&amp;A process. &nbsp;No templates are deployed out to production until they pass a long list of Q&amp;A activities. &nbsp;These include, but are not limited to:</strong></em>
</p>
<ul>
  <ul>
    <ul>
      <li>
        <p><em><strong>Build new server from template</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Clone the newly built server</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Archive / Restore</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Add Public IP</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Execute Script/Software</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>All Power operations (Power On, Off, Reboot, Shutdown etc)</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Convert to Template / Convert to Server from Template</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Autoscale (if applicable)</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Change Resources (CPU/RAM)</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Add/modify storage</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Snapshot / Revert to snapshot</strong></em>
        </p>
      </li>
      <li>
        <p><em><strong>Delete Server</strong></em>
        </p>
        <strong><em><br /></em></strong>
      </li>
    </ul>
  </ul>
</ul>
<p>&nbsp;</p>