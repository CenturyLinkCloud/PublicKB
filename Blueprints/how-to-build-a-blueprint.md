{{{
  "title": "How to build a Blueprint",
  "date": "12-2-2014",
  "author": "Shantu Roy",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Updated: December 2nd, 2014 by Keith Resar</p>
<h3>Description:</h3>
<p>The purpose of this documentation is to introduce and explain the process and detail the steps on how to construct a blueprint.</p>
<h3>Steps:</h3>
<p><strong>1. Locate "Design a Blueprint"</strong>
</p>
<ul>
  <li>Log into the CenturyLink Cloud Control Portal and from the power menubar select&nbsp;<strong>Design Blueprint</strong>
  </li>
</ul>
<p><strong><img src="https://t3n.zendesk.com/attachments/token/BNUkB19Ag86QK32ZC95DqcTDc/?name=Screen+Shot+2014-12-02+at+2.07.41+PM.png" alt="Screen_Shot_2014-12-02_at_2.07.41_PM.png" /></strong>
</p>
<p><strong>&nbsp;</strong>
</p>
<p><strong>&nbsp;2. Define Blueprint Metadata</strong>
</p>
<ul>
  <li>Define a name, version number and privacy setting for the blueprint.
    <br />
    <br />
  </li>
  <li>Fill out information about company size, and a description that would help the user of the blueprint quickly understand the purpose of the blueprint.&nbsp; Lastly add in some information about the capabilities of the blueprint.&nbsp; All these items
    help in searching for a blueprint later on.
    <br /><img src="https://t3n.zendesk.com/attachments/token/aHB8ZMcVEbFuOopLnKr4BrnSY/?name=Screen+Shot+2014-12-02+at+2.09.53+PM.png" alt="Screen_Shot_2014-12-02_at_2.09.53_PM.png" />
  </li>
  <li>Click "Next" to progress to the next stage of Blueprint configuration.</li>
</ul>
<div><strong>&nbsp;</strong>
</div>
<div><strong>3. Define Servers </strong>(optional)</div>
<div>In this screen, define the servers that are needed to support the blueprint.&nbsp; Servers do NOT have to be defined as a blueprint could consist solely of configuration against an existing environment.</div>
<div>
  <ul>
    <li>Select "Add Server" option.
      <br /><img src="https://t3n.zendesk.com/attachments/token/UJIYmDbK3XteKdclSFr3TfqIc/?name=Screen+Shot+2014-12-02+at+2.13.49+PM.png" alt="Screen_Shot_2014-12-02_at_2.13.49_PM.png" />
    </li>
    <li>Pick an existing server template, name the server, provide a description and adjust the number of CPUs and memory needed for the server.
      <br /><img src="https://t3n.zendesk.com/attachments/token/EUR2r0qfw2oLMH9TpOebzIUWx/?name=Screen+Shot+2014-12-02+at+2.14.56+PM.png" alt="Screen_Shot_2014-12-02_at_2.14.56_PM.png" />
    </li>
    <li>Lastly any additional task(s) can be assigned. The tasks include and not limited to adding disks, network interfaces or even public ip mappings in addition to rebooting servers.&nbsp;
      <br /><img src="https://t3n.zendesk.com/attachments/token/VX7qBbETYXhdeYqYL7Hrpx5le/?name=Screen+Shot+2014-12-02+at+2.15.47+PM.png" alt="Screen_Shot_2014-12-02_at_2.15.47_PM.png" />
    </li>
    <li>Additional software and scripts can be installed as well; the selection can be from publicly available software packages all the way to private software packages that are unique to the customer.&nbsp; If any of the software packages require any parameters,
      you will be prompted to enter in values.In addition to software packages, scripts can also be run against the server. &nbsp;<img src="https://t3n.zendesk.com/attachments/token/WaFm6NAeFWw87X12iYpWooN7k/?name=Screen+Shot+2014-12-02+at+2.16.57+PM.png"
      alt="Screen_Shot_2014-12-02_at_2.16.57_PM.png" />
    </li>
    <li>Once all the software, tasks and scripts have been selected, they can be arranged to the required execution order.
      <br /><img src="https://t3n.zendesk.com/attachments/token/9acEOIZtuEW0HMWyw9gyDy55E/?name=Screen+Shot+2014-12-02+at+2.18.11+PM.png" alt="Screen_Shot_2014-12-02_at_2.18.11_PM.png" />
    </li>
    <li>Click the "Apply" button.</li>
  </ul>
  <div><strong><img src="https://t3n.zendesk.com/attachments/token/xwhtwQAgLGpqBopAaCotVs0KJ/?name=Screen+Shot+2014-12-02+at+2.18.57+PM.png" alt="Screen_Shot_2014-12-02_at_2.18.57_PM.png" /></strong>
  </div>
  <div></div>
  <div><strong>4. Add an Existing Blueprint to this Blueprint</strong>
  </div>
  <div>During this step the option is available to call other blueprint from the one being designed.&nbsp; This feature greatly helps in giving the ability to treat blueprints as components and be able to be put together in a highly customizable way.</div>
  <div>
    <ul>
      <li>On the third step of the Blueprint Designer, choose the "Add Blueprint" button.
        <br /><img src="https://t3n.zendesk.com/attachments/token/Mf07Cz4lA0q1qymCkDRDWLdaL/?name=Screen+Shot+2014-12-02+at+2.21.47+PM.png" alt="Screen_Shot_2014-12-02_at_2.21.47_PM.png" />
      </li>
      <li>Select an existing blueprint nest into what you're currently creating. &nbsp;This modular design allows for easy re-use and nesting means no duplication definitions to maintain across your service catalog.
        <br /><img src="https://t3n.zendesk.com/attachments/token/vVLVEuXFfd9UMdGXV70EWDCKw/?name=Screen+Shot+2014-12-02+at+2.22.42+PM.png" alt="Screen_Shot_2014-12-02_at_2.22.42_PM.png" />
      </li>
    </ul>
    <div><strong>&nbsp;</strong>
    </div>
    <div><strong>5. Publish the Blueprint</strong>
    </div>
    <div>This step allows you to review the blueprint configuration and make any last minute changes before it is published with the associated privacy attributes.&nbsp; The publishing mechanism submits the blueprint for an automated review by the build system.&nbsp;
      Any inconsistencies are flagged and the publishing processes will error out if exceptions are encountered.</div>
    <div><img src="https://t3n.zendesk.com/attachments/token/IdQTXrZERierunNjQWPtGjLZz/?name=Screen+Shot+2014-12-02+at+2.24.27+PM.png" alt="Screen_Shot_2014-12-02_at_2.24.27_PM.png" />
    </div>
    <div></div>
    <div><strong>&nbsp;</strong>
    </div>
    <div><strong>6. Locate Published Blueprint</strong>
    </div>
    <div>Upon successful publication process, the blueprint will show up on the main blueprint dashboard.&nbsp; This dashboard by default will show all of blueprints that are available to be deployed by the user in the specific account.&nbsp; Additionally,
      filtration criterion like author, size of company and operating system, can be applied to trim the displayed blueprints. &nbsp;These filterable components are on the right side of the screen.</div>
    <div><img src="https://t3n.zendesk.com/attachments/token/xNLLJRIY21vg5yEohMgkeYy22/?name=Screen+Shot+2014-12-02+at+2.25.56+PM.png" alt="Screen_Shot_2014-12-02_at_2.25.56_PM.png" />
    </div>
  </div>
</div>