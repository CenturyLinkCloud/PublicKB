{{{
  "title": "AppFog University: PaaS Best Practices for New Apps ",
  "date": "1-20-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p><strong>Overview<br /> </strong>Harnessing the power of the Cloud, specifically via a Platform-as-a-Service offering, can liberate developers from the painful overhead of infrastructure and hardware management. The added ease and reduced complexity of a PaaS solution does not come without a cost, however. Developers must ensure applications are "Cloud-ready" in their design. In this post, we explore some of the basic concepts behind building Cloud-ready apps and the best practices in doing so.</p>
<p><strong>Best Practice #1: Design applications assuming your infrastructure will fail</strong><br /> One of the primary characteristics of Cloud application development is the inherent "pessimism" surrounding the design approach. Cloud developers architect apps counting on parts of their infrastructure, and even the application itself failing, and failing somewhat frequently. Hardware failures, power outages, networking issues, natural disasters, and an over-taxed app from heavy traffic, are all ways an application can fail. So while its human instinct to embrace positivity in most cases in life, best practices here deem us to think about and prepare for the worse.  As such, the applications Cloud developers create should be fault-tolerant and intelligently know how to re-generate themselves on fresh infrastructure. They should pick up where they left off when things break or go awry. These characteristics are often referred to as self-replicating and auto-healing technologies.</p>
<p>Now that we know we need to plan for the worst, lets review a few points to ponder when planning to build a Cloud-ready, fault-tolerant application. Questions one might ask themselves include:</p>
<ul>
<li>How will my app handle a compute, storage, or DB node failure?</li>
<li>How is the failure recognized and alerted upon?</li>
<li>How can the failure be solved in an automated fashion with no human interaction?</li>
<li>Where are the single points of failure in my application and environment? How can I eliminate them?</li>
<li>How is automatic fail-over initiated?</li>
<li>What happens when a portion of the application breaks and/or becomes unresponsive?</li>
</ul>
<p>With the above questions in your mind, a core set of best-practices for fault tolerance and auto-healing come to mind. During the application design phase, consider:</p>
<ul>
<li>Using a stateless vs. stateful application design</li>
<li>Deploying your application across multiple providers and geographies</li>
<li>Using a robust application monitoring solution</li>
<li>Using a queuing mechanism so the app knows where it left off after a failure</li>
<li>Ensuring deamons and scripts re-initiate after an application or system failure</li>
<li>Having an automated backup/restore plan for worst case scenarios</li>
</ul>
<p>Properly executing on these points may be headache-inducing during the development process but will save years of grief down the road when the application is in production.</p>
<p><strong>Best Practice #2: Design applications with elasticity in mind<br /> </strong>First off, you may or may not have already seen one of our other posts on <a href="http://university.appfog.com/scaling-your-application-on-paas/">Cloud Scaling Basics</a>; its a relevant read and a good pre-requisite to this discussion. Most folks consider elasticity in Cloud applications of equal importance to properly designed fault-tolerance. Whether you intend to scale your application manually/proactively ahead of big events, or you wish to automate with an auto-scale strategy, your application certainly needs to be scaling-aware and play nicely when re-sized.</p>
<p>Part of achieving elasticity is ensuring your application can communicate effectively with your Cloud provider to automate replication of itself as additional resources are needed. The application should be able to provision the resources it needs at any point in time on its own. The end goal for elasticity is when replication is occurring, the application can easily take advantage of  additional resources without any manual code adjustments.  Keep in mind that your web layer, application layer, db layer, etc. will all have different elasticity processes and requirements.</p>
<p>With elasticity also comes ease of deployment. Make sure you can recreate your development, staging and production environments with a few clicks easily; this reduced human-releated errors in deployment. This is often less work to achieve in a  PaaS then it is in a IaaS.</p>
<p><strong>Best Practice #3: Design applications for simultaneous stream processing</strong><br /> The cloud allows applications to easily process data in simultaneous streams. The multi-threading capabilities of modern servers allow your application to access and process data faster and more efficiently.  When data is distributed across multiple web-servers (via load-balancing) or multiple database servers (via replication) the performance of your application can grow exponentially. Processing multiple streams per node and multiple streams across multiple nodes in tandem should both be explored.</p>
<p><strong>Best Practice #4: Dynamic Assets vs. Static Assets</strong><br /> Application data (dynamic data) and static data (images, videos, user-uploaded content, etc.) should live in two very different places in the Cloud. In the old days (5-7 years ago) both types of data usually resided in the same environment. Today, in the Cloud, dynamic application code can and should sit on the compute layer itself while static assets are best served from a Cloud storage solution with CDN such as AWS S3 (link) or Rackspace Cloud Files (link).</p>
<p>Why is always utilizing a Cloud Store w/ CDN a best practice? For several reasons including:</p>
<ul>
<li>The data is closer to the end user for faster delivery</li>
<li>Performance benefits in high-traffic situations (distributed network of CDN caching servers vs. your sole local environment)</li>
<li>It can be more cost-efficient (high traffic scenarios often cost less when served from a CDN vs. deploying the suitable infrastructure)</li>
<li>It's the best way to have data-integrity for PaaS's without a durable block file system (it keeps user data from falling out of sync on app restarts/failures)</li>
</ul>
<p>Applications do need to undergo a certain amount of customization in order to utilize a Cloud storage solution with CDN, but the added effort needed for this is almost always well worth the time expenditure.</p>
<p><strong>Best Practice #5: Removing the inter-dependency of application components</strong><br /> The more a developer can architect his/her application and its components to function on their own without dependence upon other components, the better the application will perform. If one component fails or has reduced response times, the other parts of the application should continue to function normally. Also, by separating your application into components, it allows you to easily horizontally scale each part of your application, giving the parts that need the extra attention, the right attention.</p>
<p>Removing this inter-dependency is often achieved with by implementing a queing system. Popular queuing systems such as <a href="http://www.rabbitmq.com">RabbitMQ</a> or <a href="http://www.iron.io/products/mq">IronMQ</a> ensure different parts of the application can elegantly interoperate with each other and can handle the flow of I/O across the message bus efficiently.  We'll have a dedicated article on message queuing in the cloud coming very soon.</p>
<p><strong>Conclusion</strong><br /> Hopefully the few best-practices discussed above will help get you started with developing Cloud-ready applications. Certainly there are additional things to keep in mind when it comes to architecting Cloud apps, and we'd love to hear the most important ones from you. Shoot us a note: <a href="mailto:university@appfog.com">university@appfog.com</a> or write us in the comment section below with your further thoughts on this subject.</p>
<p><strong>Sources:</strong><br /> <a href="http://www.12factor.net">http://www.12factor.net</a><br /> <a href="http://media.amazonwebservices.com/AWS_Cloud_Best_Practices.pdf">http://media.amazonwebservices.com/AWS_Cloud_Best_Practices.pdf</a><br /> <a href="http://www.infoworld.com/d/cloud-computing/developing-cloud-apps-whats-different-675?page=0,0">http://www.infoworld.com/d/cloud-computing/developing-cloud-apps-whats-different-675?page=0,0<br /> </a></p>
