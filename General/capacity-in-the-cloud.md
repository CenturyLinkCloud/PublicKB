{{{
  "title": "Capacity in the Cloud",
  "date": "11-25-2014",
  "author": "Gavin McMurdo",
  "attachments": []
}}}

<h3>Description (goal/purpose)</h3>
<p>Capacity management in the cloud is a backend function that takes a number of inputs and then uses predictive analysis to determine what, when and where additional infrastructure needs to be deployed.</p>
<h3>Audience</h3>
<ul>
  <li>All</li>
</ul>
<h3>High-level details &nbsp;</h3>
<ol>
  <li>As part of the Cloud Platform, we track a number of key metrics that we use as data inputs. &nbsp;Some of the metrics that we track are CPU, RAM, disk space allocated / used, &nbsp;IOPS, &nbsp;network throughput.</li>
  <li>In addition to the data collected from the systems in production, we also collect softer data from our sales force, partners and customers that we are planning to perform large migrations or have special project needs.</li>
  <li>All of these data inputs are collected and then processed using a predictive analytics engine to forecast what infrastructure equipment needs to be ordered, in what location and what timeframe it needs to be delivered by. &nbsp;</li>
  <li>We have a high water mark of 70% that initiates a mandatory capacity expansion which ensures that we have a safety net. &nbsp;This ensures that hat we do not oversubscribe&nbsp;the optimal performance characteristics are maintained.</li>
</ol>
<div></div>
<h3>Q &amp; A</h3>
<div>
  <p><strong>Q</strong> - I would like yo know more about your "predictive analysis" engine so that I can use it in company. How do I get more details about it?
    <br /><strong>A</strong> - We see the "predictive analysis" engine as core IP of the cloud platform and therefore do not share any of the details. In addition, we are an agile shop and therefore in the spirit of agile, we are constantly improving the engine
    in order to ensure that we have better accuracy and also support the new features being added to the Cloud.</p>
  <p>
    <br /><strong>Q</strong> - I have a large project that I would like to move to your cloud, how do I ensure that you have the capacity.
    <br /><strong>A</strong> - As part of the cloud capacity plan, we always have a large amount of headroom to handle customers expansions however if you would like to reduce risk and ensure that it is on our radar, please contact your account managers so
    that they can notify us.</p>
  <p><strong>Q</strong> - I would like to see your capacity numbers and help you plan to handle my workload.
    <br /><strong>A</strong> - Thank you very much for your willingness to engage with us, we love customers like you who are willing to add human cycles in order to ensure that we can keep on the correct path. The capacity management system is an algorithm
    that is implemented in the platform code and therefore the way to engage is to submit features. A KB detailing how to engage can be found here: https://t3n.zendesk.com/entries/21699874-How-do-I-submit-a-feature-request- &nbsp;If you have a large workload,
    please refer to the large project question.</p>
  <p><strong>Q</strong> - Does your capacity management system take into consideration performance characteristics of a server?
    <br />A - Yes, we monitor a number of performance metrics that are used as inputs.</p>
  <p><strong>Q</strong> - Is capacity management part of your rhythm of the business?
    <br /><strong>A</strong> - Yes, the outputs of the capacity management tooling are reviewed on a weekly and monthly basis.</p>
</div>