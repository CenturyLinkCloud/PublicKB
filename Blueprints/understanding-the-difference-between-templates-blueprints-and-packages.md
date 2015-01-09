{{{
  "title": "Understanding the difference between Templates, Blueprints and Packages",
  "date": "12-4-2014",
  "author": "Eric Schubert",
  "attachments": []
}}}

<p>Update: November 18, 2014 by David Shacochis</p>
<p>This article can be helpful to differentiate between Templates, Blueprints and Packages - all critical elements of the CenturyLink Cloud orchestration system we collectively call the Blueprint Engine. &nbsp;&nbsp;</p>
<p><strong>Templates</strong>
</p>
<p>A Template is the basic model from which each Server gets created. &nbsp;The platform has a number of <a href="https://t3n.zendesk.com/entries/23104781-Server-Template-Object">standard Templates</a> which are replicated to all Nodes, and in addition customers
  can <a href="https://t3n.zendesk.com/entries/22353625-How-To-Create-Customer-Specific-OS-Templates">create their own custom templates</a>. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/gyCrzsmLVmuCHhbcsibBpihgx/?name=template.png" alt="template.png" />
</p>
<p><strong>Image 1 &nbsp;- converting a single server to a template</strong>
</p>

<p><strong>Blueprints</strong>
</p>
<p>A Blueprint is a saved workflow that can be defined and re-played at any time on the platform. &nbsp;During the Blueprint design process, customers do not incur billable costs. &nbsp;Customers are simply creating a workflow plan that orders steps across
  three categories: (1) cloud provisioning tasks; (2) software package installs; (3) script package execution. Users can add and reorder steps to the workflow as needed. Customers can define incredibly complex environments and invoke them at any time
  with single-click simplicity. The platform will also estimate the running costs of the Blueprint once deployed. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/dceDNDuViw5KezqPXesW2girn/?name=reordertasks.png" alt="reordertasks.png" />
</p>
<p><strong>Image 2 - Reorder tasks in the Blueprint designer</strong>
</p>
<p>Blueprints are the perfect model for SaaS providers bringing on a new customer in a "hosted private" model. Create a sub account, single click deploy your SaaS app Blueprint and the new customer is online and billing.</p>
<p>Blueprints are also ideal fits for creating server environments to support a software development lifecycle stage. &nbsp;From test/dev/QA/Prod, any app stack you are running, make it a blueprint, single click deploy to spin up a new copy of the app stack
  for testing or QA and tear it down when you’re done or deploy it to production.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/MlPp8DRJr4KB9OtbYvjPpFkiw/?name=deploy.png" alt="deploy.png" />
</p>
<p><strong>Image 3 - Single click deploy with built in costing model</strong>
</p>

<p><strong>Packages</strong>
</p>
<p>Packages are invoked software which customizes a Server Template. &nbsp;Packages come in two types: Software Packages and Script Packages, each can be called from within a Blueprint or applied directly to the Server via the Control interfaces such as
  the Create Server screen or the Group Management screen.</p>

<p><img src="https://t3n.zendesk.com/attachments/token/FddSwzCTXoE04CCqNQ02OZa9S/?name=scripts.png" alt="scripts.png" />
</p>
<p><strong>Image 4 - Script packages can be applied to Blueprints, new server builds or a group of existing servers</strong>
</p>

<p><strong>Summary</strong>
</p>
<ul>
  <li>A Template is the basic model from which each Server gets created.</li>
  <li>A Blueprint is a saved workflow that can be defined and re-played at any time on the platform.
    <br />
  </li>
  <li>A&nbsp;Package is an invoked piece of software, uploaded to the cloud platform, which customizes a Server Template.</li>
</ul>