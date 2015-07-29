{{{
  "title": "Migrating Legacy Apps to the Cloud with PaaS",
  "date": "1-20-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p><strong>Overview:</strong><br /> A common misconception in the Cloud world is that the Cloud is only good for green field apps -- apps which are new and not shackled by the constraints of legacy design. While starting fresh oftentimes *can* be easier, it doesn't have to be the only option when considering migrating to the Cloud. Many brown-field apps, those which were created in a pre-Cloud era, often can and should be ported to the Cloud. In the following post, we aim to discuss some of the important theories and concepts for moving legacy apps to the Cloud.</p>
<p>Most cloud apps are developed with elastic scaling, statelessness, and automation in mind. Let's look at how each of these characteristics are important when considering your app migration plan.</p>
<p><strong>Key areas of focus for migrating apps to the Cloud:<br /> </strong></p>
<ul>
<li>Automating the installation and deployment processes of your application is most often the "low hanging fruit" for migrating to the Cloud.  Consider starting here first. This will lessen the human error-rate of manual deployments and set you up for better elasticity in the long run.</li>
<li>Elasticity. Even if your application isn't fully automated for auto-scale, the elasticity which the Cloud provides is beneficial. Start using elasticity immediately to your advantage, even if your implementation is crude at first.</li>
<li>Simplicity. If your current applications depend on custom-binaries, custom-compiled version of apache, php, etc. or other fine-tuning, seek ways to have the apps run in a standard environment. PaaS setups employ best-practicies configurations which are standard in nature.</li>
</ul>
<p>Now that we have a few ares to direct our focus on, lets talk about the most daunting part of it all: getting started.</p>
<p>How to get started:</p>
<ol>
<li>Identify which individual services make up the application, how each are interconnected with one another, and which dependent upon others. This helps determine how many resources are needed for each part of your application lifecycle.</li>
<li>Identify the devops phases which compromise the services' lifecycle. Map out processes including install, initialize, start, stop, and shutdown. Capturing each process and mapping it into a script or automated task, gets you a long way.</li>
<li>Migrate static assets to a CDN service</li>
<li>Decouple dependent services in your application from each other and compartmentalize them.</li>
</ol>
<p><strong>Which apps should be migrated first?</strong><br /> <strong>Enterprises:</strong> For enterprises, it frequently makes sense to start with the lowest-risk, lowest-value apps first. These apps give you and your team invaluable learning and experience in moving applications without a large risk factor. Applications with bursty traffic patterns and usage should be the next to be migrated. Leave large, complex, high-IO applications towards the end of your migration strategy when your team is comfortable with what it takes to move to the cloud.</p>
<div><strong>SMBs &amp; Startups:</strong> For smaller companies and startups, the Cloud is perfect for those cool, new cutting-edge web apps which haven't yet been developed or those that operate on a very traditional stack. Applications which require very specific tweaks and customizations should be modified to run on standard environments before jumping into the Cloud with them, esp. high-traffic/high bandwidth ones.</div>
<div> </div>
<div><strong>Conclusion</strong><br /> One of the most important points companies of all sizes should focus on is the environment they choose to move their applications into. An environment which runs on an open-soruce stack, devoid of vendor lockin and proprietary technology is preferred. This will enusre as you build your apps in the cloud, you can do so on a standard configuration which can be ported to any provider you wish.</div>
<div>
<p>As we have discussed, PaaS offerings are great for hosting legacy applications. Platform as a Service solutions allow your developers to focus on their core competencies vs. the hassles of infrastructure. The less time you and your team spend on maininging infrastructure, the more time you can add value and innovation to your product or service for your customers.</p>
<p>Sources:<br /><a href="http://natishalom.typepad.com/nati_shaloms_blog/2012/06/lessons-from-amazon-rds-on-bringing-existing-apps-to-the-cloud.html">http://natishalom.typepad.com/nati_shaloms_blog/2012/06/lessons-from-amazon-rds-on-bringing-existing-apps-to-the-cloud.html</a><br /><a href="http://www.zdnet.com/news/moving-apps-to-the-cloud-why-when-and-how/6344653">http://www.zdnet.com/news/moving-apps-to-the-cloud-why-when-and-how/6344653</a><br /> </p>
</div>
