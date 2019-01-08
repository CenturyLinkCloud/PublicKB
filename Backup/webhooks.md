{{{
  "title": "Simple Backup Webhooks",
  "date": "12-20-2018",
  "author": "John Gerger",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
The Simple Backup Service now supports **Webhooks** which send push notifications to an HTTP endpoint specified by the customer. This FAQ addresses commonly asked questions about the service. For a walkthrough of how to use Webhooks, see [Configuring Webhooks and Consuming Notifications](https://www.ctl.io/api-docs/v2/#webhooks-configuring-webhooks-and-consuming-notifications).

**Q: What exactly is a Webhook?**

A: Webhooks make it possible to create push notification solutions. Backup events (e.g. "Backup failures") are sent in real-time to a web endpoint configured for the Webhook. Whenever an event occurs, a JSON message is sent as an HTTP POST request.

**Q: In what scenario would I use a Webhook?**

A: Webhooks provide the opportunity to immediately see what's going on within your backup environment. This allows you to quickly and easily monitor and respond to backup events.

**Q: What triggers a Webhook?**

A: There are currently Webhooks for four major categories: Backup Failure, Backup Partial Success, Missing Backups, and Backup Success.

- **Backup Failure** Triggered on a backup that has completed with a status of Failure.
- **Backup Partial Success**. Triggered on a backup that has completed with a status of Partial Success.
- **Missing Backups** Triggered when a server has not initiated a backup within 1 hour of the scheduled start time on the backup policy.
- **Backup Success**. Triggered on a backup that has completed with a status of Success.

**Q: Where do I go to set up a Webhook?**

A: Webhooks are available within the Simple backup UI in a sub-menu called "Webhooks". Customers can set a target URL for each Webhook event listed.

**Q: Are there any requirements for the service that receives the Webhook notification?**

A: Listener services must be on the public internet in a location reachable by the CenturyLink Cloud platform. If a customer plans on consuming this data within an internal system, consider using a reverse proxy or another mechanism to forward traffic from a public-facing web service to an internal system.

**Q: What happens if the destination is unreachable?**

A: There is no guaranteed delivery with CenturyLink Cloud Webhooks. We make a single attempt to send a message to the designated endpoint and if it fails, it is not retried. This means two things: (1) design your endpoints to be highly available and withstand failures of any single component in the solution, and (2) rely on a combination of Webhooks and daily email reports to monitor your backup environment completely.

**Q: What data is sent in the Webhook event notification?**

Example payload for a Backup FAILURE event type:
```
{ "text": "Status: FAILED  -  Account: TEST  -  Server: testServerId20190102013933  -  Account Policy Name: TestAccountPolicyName20190102013933  -  Restore Point Id: 3f68fa31-731e-4c77-bbc1-8892ec8667e4  -  Finished Date/Time: 2018-12-20 01:39:38 UTC" }
```

Example payload for a Backup PARTIAL Success event type:
```
{ "text": "Status: PARTIAL_SUCCESS  -  Account: TEST  -  Server: IL1TESTWIND0803  -  Account Policy Name: ZZZ USERS  -  Restore Point Id: 5346562d-7d8c-47a6-a11f-fc1f5d0b269320190102125152  -  Finished Date/Time: 2018-12-20 18:00:36 UTC" }
```

Example payload for a MISSING Backup event type:
```
{ "text": "testServerId20181228013921 missed a backup expected at 2018-12-20T17:00:06.476Z for policy [TestAccountPolicyName20181228013921] with server policy id [e6ac019b-c646-359a-83a4-b81b5cc1c512] and storage region [US WEST]" }
```

Example payload for a Backup SUCCESS event type:
```
{ "text": "Status: SUCCESS  -  Account: TEST  -  Server: TESTUBUNTUTEST  -  Account Policy Name: ZZZ etc  -  Restore Point Id: aee021f6-e9d3-4c13-bff1-a9733bef753220190102170143  -  Finished Date/Time: 2018-12-20 17:01:45 UTC" }
```
