{{{
  "title": "CenturyLink Cloud Anti-Affinity Policies",
  "date": "9-15-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

CenturyLink Cloud Anti-Affinity Policies
<p>CenturyLink Cloud offers customers&nbsp;<a href="http://www.centurylinkcloud.com/products/compute/hyperscale" target="_blank">Hyperscale instances</a> – an instance type that is designed for distributed workloads that require maximum performance. Hyperscale
  offers the same top-tier CPU and RAM performance found in our standard servers – and adds 100% flash storage. That means customers can typically expect at least 15,000 IOPS to turbo-charge applications. &nbsp;</p>
<p>Anti-affinity policies make it possible to spread workloads across physical hosts. When a new server is created and references an anti-affinity policy, the CenturyLink Cloud platform makes sure that all the virtual servers in that policy are distributed
  to unique physical hosts.</p>
<h3>Prerequisites to Leverage Anti-Affinity Policies</h3>
<ul>
  <li>A Hyperscale enabled Data Center. &nbsp;Today this includes VA1, UC1, GB3, IL1, CA3 &amp; NY1 with more coming online shortly.</li>
  <li>A Hyperscale Virtual Machine. &nbsp;Customers can only apply Anti-Affinity Policies to Hyperscale Virtual Machines. &nbsp;Standard Virtual Machines are not supported at this time. &nbsp;</li>
</ul>
<h3>Creating an Anti-Affinity Policy</h3>
<p>&nbsp;1. &nbsp;Select the Anti-Affinity Policies link in the Control Portal menu</p>
<p><img src="https://t3n.zendesk.com/attachments/token/RFoZHEfyTgqXHA8Ibxh3qpLfe/?name=01.png" alt="01.png" />&nbsp;</p>
<p>2. &nbsp;Select Create Anti-Affinity Policy. &nbsp;Input a name for the Policy and choose a Hyperscale Enabled Data Center (VA1, CA3, UC1 &amp; NY1). &nbsp;Anti-Affinity Policies are Data Center specific. &nbsp;Once done select the create button.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/bLBeU3m4d63vwIGwjBSQqgAsi/?name=02.png" alt="02.png" />
</p>
<h3>Creating a Virtual Machine with an Anti-Affinity Policy</h3>
<p>Perform the <a href="https://t3n.zendesk.com/entries/22603877-Creating-a-New-Enterprise-Cloud-Server" target="_blank">standard create server function</a> in Control. &nbsp;When doing so the ability to choose an Anti-Affinity policy will be available.
  &nbsp;Select the policy you wish to leverage.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/D9r19ltJp4UkXluM8YLZdmupM/?name=03.png" alt="03.png" />
</p>
<h3>Adding an Existing Virtual Machine to an Anti-Affinity Policy</h3>
<p>Navigate to the Hyperscale Virtual Machine in the Servers portion of control (quick tip: &nbsp;the Servers BETA UI does not allow this configuration currently). &nbsp;Select Settings and choose the Anti-Affinity Policy you wish this VM to leverage. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/MlJUDj2BbOdWv5pm2fPcJho6e/?name=04.png" alt="04.png" />
</p>