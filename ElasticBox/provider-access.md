{{{
"title": "Enable Access to Cloud Providers",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Enable Access to Cloud Providers
By default, all public and private cloud providers are enabled for ElasticBox users. As an ElasticBox administrator, you can enable or disable providers for the entire organization in the [admin console](./admin-overview.md). You can turn off a particular provider if you don’t want people to deploy to it.

Enabling provider access does not automatically register providers for use but determines which ones users can connect and deploy to.

In the admin console, you can control access under **Providers > Clouds**.
![admin-cloud1.png](../images/ElasticBox/admin-cloud1.png)

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](https://www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
