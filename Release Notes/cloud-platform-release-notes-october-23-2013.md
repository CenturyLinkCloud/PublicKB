{{{
  "title": "Cloud Platform – Release Notes: October 23, 2013",
  "date": "10-21-2014",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (3)</strong>
</p>
<hr />
<ul>
  <li><strong>Cloud Webhooks (beta). </strong>This new feature -- the first of its kind in a public IaaS cloud -- lets customers subscribe to events that occur in the CenturyLink Cloud. When an event occurs, a message is immediately sent to an HTTP endpoint specified
    by the customer. Some details:
    <ul>
      <li>Webhooks exist for account, user, and server events.</li>
      <li>Configured through the CenturyLink Cloud Control Portal.</li>
      <li>JSON messages sent via POST to an internet-accessible HTTPS endpoint.</li>
      <li>Parent accounts can choose to receive webhook events for any child accounts.</li>
      <li>There is no guaranteed delivery or retries if the customer endpoint is offline.</li>
    </ul>
    <p><img src="https://t3n.zendesk.com/attachments/token/izfvcti9swrvqqz/?name=release10_23_01.png" alt="release10_23_01.png" />
    </p>
    <p>Please see KB article "<a href="https://t3n.zendesk.com/entries/22671399-Configuring-Webhooks-and-Consuming-Notifications">Configuring Webhooks and Consuming Notifications</a>" for additional details on what platform actions trigger each Webhook.</p>
  </li>
  <li><strong>New REST-based API (beta).&nbsp;</strong>The second major version of the CenturyLink Cloud API is underway. This month, we released the Groups API in the new API model. Some details about the new (Groups) API:</li>
  <ul>
    <li>Pure, REST-based JSON API that uses HTTP verbs and URIs in a standard way.</li>
    <li>Relies on an authentication scheme that uses customer credentials (not a generic API user) to retrieve user information that includes the user's roles, and a security token that will authenticate and authorize subsequent API requests. Tokens are valid
      for two weeks.</li>
    <li>API is geo-load balanced and available in each CenturyLink Cloud data center.</li>
    <li>The API has complete parity with actions available in the CenturyLink Cloud Control Portal. Groups API supports: creating groups, retrieving groups, issuing power operations against groups, snapshotting groups, get and set resource limits for a group, and more.
      See the <a href="https://t3n.zendesk.com/categories/20067994-API-v2-0">KB articles about the new Groups API</a> for more details on how to securely interact with each resource.</li>
  </ul>
  <li><strong>Updated Site Navigation. </strong>A Control Portal redesign is underway, with the first phase being a refresh of the site navigation. The individual menu lists are gone and replaced by a single menu that contains all the site actions. The topmost
    navigation also includes a simplified set of actions. For more about the thinking behind this change, see the blog post <a href="http://www.tier3.com/blog/full/tier-3-setting-the-bar-control-portal-ui-evolution-under-way">CenturyLink Cloud Setting the Bar: Control Portal UI Evolution Under Way</a>.&nbsp;Note
    that all users will have a "first run" experience that walks them through the new UI when they next log in.
    <p><img src="https://t3n.zendesk.com/attachments/token/y5o5oiqz2st90qw/?name=ControlNav2.gif" alt="ControlNav2.gif" />
    </p>
  </li>
</ul>
<p></p>
<p><strong>Minor Enhancements/Fixes (3)</strong>
</p>
<ul>
  <li><strong>Added Remote-Identity to Site to Site VPN.&nbsp;</strong>When customers choose to enable NAT-T during the Phase 1 IKE step of creating a site-to-site VPN, then can now input a remote-identity value.</li>
  <li><strong>Load Balancer Supports IPs in Parent Network.&nbsp;</strong>Sub accounts can share the network of their parent accounts. The self-service load balancer now supports creating a pool with account servers that reside on the parent network.</li>
  <li><strong>Bandwidth Graph Updated. </strong>The bandwidth graph on the CenturyLink Cloud Dashboard has been updated with the correct units. Instead of showing bytes transferred for a given day, the graph shows the Mb/s consumed.</li>
</ul>
<p>&nbsp;<strong>For a demo of these features, please visit:&nbsp;<a href="http://www.slideshare.net/Tier3Cloud/tier-3-october-2013-release-webcast-recording">http://www.slideshare.net/Tier3Cloud/tier-3-october-2013-release-webcast-recording</a></strong>
</p>