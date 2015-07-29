{{{
  "title": "Getting Started With AppFog v1: Billing Process Overview",
  "date": "1-25-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Billing Cycle</h3>
<p>Your billing cycle begins when you start your subscription. If you start your subscription on the fifth of the month, then your account will automatically renew on the fifth of each subsequent month at the same time of day.</p>
<h3>Pricing Structure</h3>
<p>AppFog is an application hosting platform with the cost of the underlying IaaS included in the selected plan. The key differentiator between plans is the amount of runtime memory required by developer. Our goal is to reduce or virtually eliminate the system administration required to run a Production or Dev/Test application. Therefore, the tier plan pricing is centered on amount of application memory needed. There is no direct access to a server, virtual or otherwise, instead we provide the ability to deploy and manage an cloud-ready app via a web console or Command-line interface. Check out <a href="http://twelvefactor.net">The Twelve-Factor App</a> guide for more details on how to build cloud-ready applications.</p>
<p>AppFog v1 doesn't offer a-la-carte services or pricing for native (or 1st party services), but AppFog v2 (Q2 2015) will offer usage-based pricing based on memory, CPU, bandwidth, and storage needs. In the meantime, we recommend customers use one of our 3rd party add-ons for more demanding database or storage requirements. ClearDB or MongoLab are popular storage choices for more demanding applications.</p>
<p>CPU isn't particularly limited. Our Ops team monitors server CPU utilization, and we have processes in place to re-distribute app instances if they are consuming excessive CPU or I/O. AppFog isn't managed by the concept of vCPU - instead we manage our shared-tenant environment to CPU thresholds for a server remain below an appropriate threshold to minimize CPU usage conflicts.</p>
<h3>Upgrades and Downgrades</h3>
<p>When you upgrade your service, your billing cycle remains the same, and you'll automatically be charged for the difference in plans for the rest of the billing cycle (to the nearest second). For example, if you're on the $100/month (Silver plan) and upgrade to the $380/month (Gold plan) halfway through your billing cycle, you'll be charged $140 for the rest of the billing cycle (this pays for the upgrade), and then you'll be charged $380 at the beginning of the next billing cycle.</p>
<p>Similarly, when you downgrade your billing cycle remains the same. Your account will be given a pro-rated credit for the remaining unused portion of the previous level plan and then charged a pro-rated amount for the new, lower plan for the remaining days on your current billing cycle. Any credits are used up with each billing. Once they are depleted, your credit card is charged accordingly.</p>
<h3>Cancelling Your Account</h3>
<p>Within your ACCOUNT page you can cancel your account. If you are within a billing cycle the account will be active until the end of the cycle. Please note, that if you cancel after your subscription has been renewed you will still receive service for the rest of the month. If you wish to delete your account and receive a refund for that charge, send an <a href="mailto:billing@appfog.com">email to our billing team</a>. Note: Some of our users were grandfathered into a free plan in February 2014. If you are still using our old free plan and wish to delete your account, you will need to <a href="mailto:noc@ctl.io">submit a ticket</a>, as the Cancel Subscription button will not work.</p>
<h3>Updating Your Billing Information</h3>
<p>If you need to update your credit card or billing information, <a href="https://console.appfog.com/login">please log in to your account</a>, go to the ACCOUNT page and update your information.</p>
<h3>Questions?</h3>
<p>If you have questions about our billing process or need assistance, please send us an email at <a href="mailto:billing@appfog.com">billing@appfog.com</a>.</p>
