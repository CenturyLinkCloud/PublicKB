{{{
  "title": "AppFog University: Scaling Your Application on PaaS",
  "date": "1-20-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}



<p><strong>Overview</strong><br /> One of the key tenets of Cloud Computing is scalability. Whether discussing SaaS, PaaS, or IaaS, the Cloud allows applications to easily grow with user demand. While scaling in each type of Cloud has different considerations, in this post, we aim to focus primarily on PaaS. We'll be covering different types of scaling approaches, when to choose which, and how to test your scaling strategy. Let's jump right in.</p>
<p><strong>Vertical vs. Horizontal scaling</strong><br /> We'll start with vertical scaling, also referred to as "scaling up" or "concurrent computing." Vertical scaling is the easiest method of scaling and the "traditional way" of adding capacity to an environment. Vertical scaling often means increasing the RAM or computational power of a particular instance or virtual machine. With many IaaS or PaaS systems, this can be done with a few clicks or via a simple API call. Do note, however, that upgrading and downgrading your application in a single-node environment doesn't always come without downtime, which should be strongly considered in your overall strategy.</p>
<p>Horizontal scaling, also referred to as "scaling out" or "distributed computing," is the more difficult of the two methods of scaling, since applications and infrastructures need to be able to handle these changes on the fly. That being stated, horizontal scaling is often the most effective and ideal way of scaling, especially in cloud-ready applications and environments. Horizontal scaling has the huge benefit of not having the hard limit that you face in the vertical scenario; a single node can only scale to a finite point, whereas a horizontally scaling cloud can grow quite fluidly. If your new application is written to horizontally scale or your legacy application has been retrofitted to do so, horizontal scaling should absolutely be taken into consideration prior to going live with your application.</p>
<p><strong>When to choose which scaling strategy</strong><br /> Now that we understand the differences between vertical and horizontal scaling, we need to explore when each is the best fit. This decision may seem daunting for folks new to Cloud applications but it shouldn't be. We'll break it down simply for you below.</p>
<p><strong>Consider vertical scaling when:</strong></p>
<ul>
<li>You have legacy applications which can only function in a single-node configuration and aren't designed for multi-node segmentation. Example: an application, if run on multiple web instances, would be unaware of replicating the data from a current session to each of the other nodes.</li>
<li>You aren't concerned with high availability or geo-redundancy. If you have a non-critical or non-production app and the provider has issues with portions of the infrastructure, you are ok with some downtime.</li>
<li>You have a clear understanding of the maximum amount of scaling your application will ever need and it fits within the confines of a single node.</li>
</ul>
<p><strong>When to choose horizontal scaling:</strong></p>
<ul>
<li>If high availability or geographic redundancy is important to you. There are many different levels of high availability. Having multiple nodes within a single provider's infrastructure is a smart choice for overcoming fact-of-life scenarios such as bad hardware, network issues, etc., but high availability in different geographic regions with the same provider adds an extra level of protection in case of catastrophic failure in one or more regions.</li>
<li>If multi-provider redundancy is an attractive proposition. Spreading your application across multiple providers can be a great option to mediate the impacts of provider-wide failures. As an added benefit, instances with different providers spread across different geographies can also aid in the distribution of your application for the lowest latency to your customers.</li>
<li>If you'd like to easily upgrade portions of your application without taking your entire environment down. With a horizontally scaling app, chances are good that your application is split into functional sections, and you can easily service specific sections without scheduling a maintenance outage.</li>
<li>If your application is already designed for multi-tenant environments.</li>
</ul>
<p>These are not steadfast rules but rather general guidelines. Other exploration into areas such as the cost-benefit analysis of each strategy should be considered as well. You may see different results based on your specific application's needs and there is no one-size-fits-all playbook here.</p>
<p><strong>How to test your scaling strategy</strong><br /> Testing your scaling strategy is important. When deploying an app in a Platform-as-a-Service Cloud, 10% of your time should be spent on functional deployment and 90% should be spent on testing and tuning. Services such as  <a href="http://newrelic.com" data-cke-saved-href="http://newrelic.com">New Relic</a> and our Add-On option <a href="blitz.md">Blitz.io</a> offer an incredible amount of help in performance testing and pinpointing bottlenecks in your applications.</p>
<p>While testing, be sure to adjust different user concurrency values and inspect the response times, as this data can help sort out bottlenecks at different layers of your application (web, database, etc.) or within the application code itself.</p>
<p><strong>Conclusion</strong><br /> This information will hopefully get you off to a good start on the basics of scaling in the Cloud. We have some other relevant content which you might want to check out, including <a href="http://university.appfog.com/best-practices-for-new-apps">PaaS Best Practices for New Apps</a> and <a href="migrating-legacy-apps-to-the-cloud-with-paas.md">Migrating Legacy Apps to the Cloud with PaaS</a>. If you have any questions about scaling your applications, feel free to shoot us a note at university@appfog.com or add to the comments below.<br /> </p>
