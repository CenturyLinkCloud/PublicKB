{{{
  "title": "Troubleshooting Application Deployment Issues",
  "date": "07-17-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Audience

Application developers

### Overview

When deploying an application to a remote platform you may find that problems occur that either didn't surface in a local application development environment. This article is focused on providing information on how to debug application deployment issues on AppFog.

### Accessing Logs

The most common way to troubleshoot application deployments is to look at your applications logs.

```
$ cf logs myapp --recent
Connected, dumping recent logs for app myapp in org ACME / space Dev as me...
```

This will dump the recent logs from your application to the console.

If you want to watch the logs while interacting with the application you can run the command without the `--recent` option.

```
$ cf logs myapp
Connected, tailing logs for app myapp in org ACME / space Dev as me...
```

Now whenever the application is accessed the logs will be dumped to the console until you stop the command execution.

### Additional Information

The Cloud Foundry Foundation has an article on troubleshooting application deployments on Cloud Foundry (on which AppFog is based).

https://docs.cloudfoundry.org/devguide/deploy-apps/troubleshoot-app-health.html