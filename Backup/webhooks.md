{{{
  "title": "Simple Backup Webhooks",
  "date": "11-7-2019",
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
{
  "text": "Status: FAILED - Account: TEST - Server: testServerId20190201013933 - Account Policy Name: TestAccountPolicyName20190201013933 - Restore Point Id: c56b1fd4-b566-4044-a696-0f1311ffdeee - Finished Date/Time: 2019-02-01 01:39:40 UTC",
  "status": "FAILED",
  "account": "TEST",
  "server": "testServerId20190201013933",
  "serverPolicyId": "a73fb66e-7e77-41fa-b303-11600820d13a",
  "accountPolicyName": "TestAccountPolicyName20190201013935",
  "accountPolicyId": "96ac27e5-3e70-4ec8-8275-286c4a436ab4",
  "restorePointId": "c56b1fd4-b566-4044-a696-0f1311ffdeee",
  "finishedDate": "2019-02-01 01:39:40 UTC"
}
```

Example payload for a Backup PARTIAL Success event type:
```
{
  "text": "Status: PARTIAL_SUCCESS - Account: TEST - Server: IL1TESTWIND0803 - Account Policy Name: andy-test-windows-20181019 - Restore Point Id: 5e641ec2-24c1-40aa-a93a-d75e66f37d1220190131170408 - Finished Date/Time: 2019-02-01 01:05:00 UTC",
  "status": "PARTIAL_SUCCESS",
  "account": "TEST",
  "server": "IL1TESTWIND0803",
  "serverPolicyId": "5e641ec2-24c1-40aa-a93a-d75e66f37d12",
  "accountPolicyName": "andy-test-windows-20181019",
  "accountPolicyId": "ab8e34e6-15e1-4940-86b0-77ab68854746",
  "restorePointId": "5e641ec2-24c1-40aa-a93a-d75e66f37d1220190131170408",
  "finishedDate": "2019-02-01 01:05:00 UTC"
}
```

Example payload for a MISSING Backup event type:
```
{
  "text": "testServerId20181228013921 missed a backup expected at 2019-02-01T20:00:04.289Z for policy [TestAccountPolicyName20181228013921] with server policy id [5f3876b7-6fc9-4610-b619-85f6c01e231d] and storage region [US EAST]",
  "account": "TEST",
  "server": "testServerId20181228013921",
  "serverPolicyId": "5f3876b7-6fc9-4610-b619-85f6c01e231d",
  "accountPolicyName": "TestAccountPolicyName20181228013921",
  "accountPolicyId": "2f62f2a3-d1be-496e-ab0a-e2fa25c4b152",
  "expectedDate": "2019-02-01T20:00:04.289Z"
}
```

Example payload for a Backup SUCCESS event type:
```
{
  "text": "Status: SUCCESS - Account: TEST - Server: UC1BAADUBUN1605 - Account Policy Name: TestAccountPolicyName20181228013921 - Restore Point Id: d46dc104-2119-4288-a59c-f04f59ffb1e920190201212354 - Finished Date/Time: 2019-02-01 21:23:57 UTC",
  "status": "SUCCESS",
  "account": "TEST",
  "server": "UC1BAADUBUN1605",
  "serverPolicyId": "d46dc104-2119-4288-a59c-f04f59ffb1e9",
  "accountPolicyName": "TestAccountPolicyName20181228013921",
  "accountPolicyId": "04ea6d8d-90a5-45a3-a67d-84c2dfe20141",
  "restorePointId": "d46dc104-2119-4288-a59c-f04f59ffb1e920190201212354",
  "finishedDate": "2019-02-01 21:23:57 UTC"
}
```
