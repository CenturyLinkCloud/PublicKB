{{{
  "title": "Migrating Environment Variables and Add-Ons",
  "date": "09-24-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

### Obtain AppFog v1 Environment Variables

AppFog v1 Add-Ons utilize environment variables for connecting to the third-party service. You may continue use of your existing Add-On service on AppFog v2 by migrating the environment variable. There are several options for obtaining your application's current environment variables for migration to AppFog v2.

* Via the web console navigate to the Mission Control page of your app. Then select the "Env Variables" tab from the left menu.
* From your terminal use the AF tool command:
<pre>$ af env &lt;appname&gt;</pre>
* Example:
<pre>
+--------------------+-------------------------------------------------------------------------------------------------+
| Variable           | Value                                                                                           |
+--------------------+-------------------------------------------------------------------------------------------------+
| MONGOLAB_URI       | mongodb://af_2flljdwn:wmsgkkl8bfmfv6v8jtq2evlula@ds051953.mongolab.com:51953/af_2flljdwn        |
| ELEPHANTSQL_URL    | postgres://vegluupq:G4zVUrvfU_liSp8scxbeQm_qGtUObdl@pellefant.db.elephantsql.com:5432/vegluupq |
| IRON_MQ_TOKEN      | JcwY4lyrdfEw74qKVaTqgCVJ--Q                                                                     |
| IRON_MQ_PROJECT_ID | 560ae7ddff1d320060000a0                                                                        |
+--------------------+-------------------------------------------------------------------------------------------------+
</pre>
* Use the AppFog API to obtain a JSON object containing the application's environment variables, along with additional useful information. You will need your AF token, typically located in your home directory as .af_token. 
<pre>`$ curl -X GET -H Authorization:'$TOKEN' https://api.appfog.com/apps/<appname>`</pre>
* Example curl for app "addon_test":
<pre>
{"name":"addon_test","staging":{"model":"php","stack":"php"},"uris":["2remove.aws.af.cm","addon_test.aws.af.cm","removeurl.aws.af.cm"],"instances":1,"runningInstances":1,"resources":{"memory":128,"disk":1024,"fds":256},"state":"STARTED","services":["mysql-0c3b"],"version":"8e3832c7695ad0f75cb258edea628c177d69b2a3-6","env":["MONGOLAB_URI=mongodb://af_2flljdwn:wmsgkkl8bfmfv6v8jtq2evlula@ds051953.mongolab.com:51953/af_2flljdwn","ELEPHANTSQL_URL=postgres://vegluupq:G4zVUrvfU_liSp8scxbeQm_qGtUObdl@pellefant.db.elephantsql.com:5432/vegluupq","IRON_MQ_TOKEN=JcwY4lyrdfEw74qKVaTqgCVJ--Q","IRON_MQ_PROJECT_ID=560ae7ddff1d320060000a0"],"meta":{"debug":null,"console":null,"version":29,"created":1443557061},"infra":{"provider":"aws","name":"aws"}}
</pre>

### Import Environment Variables to AppFog v2
* If you don't have your app deployed yet: [How to Migrtate an App](how-to-migrate-an-application.md)
* Environment variables can be viewed or set in AppFog v2 with the following commands:
<pre>$ cf env &lt;appname&gt;</pre>
<pre>$ cf set-env &lt;appname&gt; &lt;variable&gt;  &lt;value&gt;</pre>
* Example:
<pre>$ cf set-env addon_test IRON_MQ_TOKEN JcwY4lyrdfEw74qKVaTqgCVJ--Q</pre>
More information on working with AppFog v2 environment variables can be found at [Cloud Foundry Environment Variables](http://docs.run.pivotal.io/devguide/deploy-apps/environment-variable.html).
