{{{
  "title": "AppFog University: Setting up a Redundant Cloud PaaS Environment",
  "date": "1-20-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Overview</strong><br /> Setting up a redundant, High Availability Platform-as-a-Service environment for your Cloud application can be a fairly straightforward proposition when you have the right plan in place. Let's review what you should consider when maximum uptime for your PaaS applications is paramount for your business.</p>
<p><strong>A Common Misconception</strong><br /> Many folks assume that the Cloud, especially in Platform-as-a-Service form, solves all of their redundancy and scalability problems out of the box, without any user-intervention needed. This isn't the case and I'm here to break the bad news that no Cloud solution does this. So, where does your PaaS provider help you in your path towards HA and where do you need to step in to fill in the gaps?</p>
<p>PaaS providers generally have their core infrastructure set up in a high-availability manner. Load-balancers, git-servers, storage servers, etc. are all designed with fail-over and redundancy in mind. PaaS service consoles and support systems also almost always created to stay online when things go wrong. This, however, leaves a few critical things out of the equation. A few questions to ask yourself might be: Is the application server(s) you are hosting on redundant by default? What about your database? Is it set up for auto-failover and replication? What if your PaaS provider has a total meltdown in their DC? Will your app still be alive?</p>
<p>Chances are, it won't. So, here's what needs to be done.</p>
<p><strong>Intra-Provider High Availability</strong><br /> First things first; let's get your application running on multiple web nodes. Most PaaS providers do not actively fail over your codebase when its on a single instance. Deploying two or more instances in a load-balanced fashion is the first step to intra-provider HA. Achieving this multi-node support should be a breeze compared to IaaS solutions. Most PaaS systems allow you to scale with a drag and a click of a mouse or a simple CLI command.</p>
<p>Your application's database is also the other big point to consider. Is it replicated by default? What if the cluster its being from served fails? Using a DB-specifc solution for your database needs can be a big step towards the needed redundancy of your application. Two immediate suggestions to easily implement this come to mind:</p>
<ol>
<li>Amazon RDS in a Fail-Over Configuration - A good solution for read-replicas, read concurrency, and basic failover.</li>
<li>Xeround - A great solution for clustering, read/write concurrency, self-healing, multi-zone auto-failover, as well as auto-scaling.</li>
</ol>
<p>With your web and database layers in mind, you've got some assurance that your application will stay up from standard provider-related failures.</p>
<p>However, our planning for the worst shouldn't stop here. What if your PaaS provider's entire infrastructure fails? Or, what if THEIR provider's infrastructure they deploy on fails? In many business situations, we need to address this as well.</p>
<p><strong>Inter-Provider High Availability</strong><br /> This is where we get fancy. Let's take the HA environment we discussed above and now replicate its across multiple providers to alleviate any provider-specific failures. If your PaaS provider offers one-click deployments across multiple environments such as Rackspace, AWS, HP Cloud, etc. then its going to be relatively easy to build geo-redundancy. Here's a playbook on what to do:</p>
<ol>
<li>Deploy your application on infrastructure A, at subdomainA.domain.com</li>
<li>Copy your deployment to infrastructure B, at subdomainB.domain.com</li>
<li>Use a provider like Neustar DNS [link] to set up geographic round-robin dns between app A on subdomain A and app b on subdomain B, load-balacing to domain.com. This will give your multi-provider resiliency and source-detection performance benefits.</li>
<li>Make sure to update both applications with each code push.</li>
</ol>
<p>Now, we have HA at two levels, at the infrastructure level and at the provider level. This provides for a great amount of robustness in your environment.</p>
<p><strong>Conclusion</strong><br /> Every application you deploy in a PaaS environment which is for production use should at least be set-up with intra-provider HA. The large benefits you gain from doing at least some sort of HA significantly outweigh the costs. For those of you who are interested in a detailed walkthrough of setting both types of HA up, please let us know as we will be creating a detailed guide soon.<br /> </p>
