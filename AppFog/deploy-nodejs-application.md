{{{
  "title": "Deploying a Node.js Application",
  "date": "05-01-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Audience

Application developers

### Overview

AppFog includes the [Cloud Foundry Node.js buildpack](https://github.com/cloudfoundry/nodejs-buildpack) by default. This enables the deployment of Node.js applications with a limited amount of configuration changes to an existing application.

There are three main considerations for running a Node.js applications on AppFog:

1. Adding a start script configuration to package.json
2. Identify Node.js version to use at runtime in package.json
3. Bind to the port provided to the application via the VCAP_APP_PORT environment variable

### Adding "start" Script Configuration

In the application's package.json, there is an ability to [set the "scripts"](https://docs.npmjs.com/misc/scripts) that can be executed via the `npm` command. Here is an example:

```
{
	"name": "demo-app",
	"version": "0.1",
	"scripts": {
		"start": "node app.js"
	},
	...
}
```

Now when you run `npm start` in the top-level application directory it will run `node app.js`. The Node.js buildpack automatically tries this default defined command when staging your application into AppFog.

An alternative is the send the command that AppFog should execute to start your application [using the command line](http://docs.cloudfoundry.org/devguide/deploy-apps/app-startup.html) or [Cloud Foundry manifests](http://docs.cloudfoundry.org/devguide/deploy-apps/manifest.html) approaches.

#### Start via Command Line

To send your start command via the Cloud Foundry command line you can use the `-c` option to `cf push`:

```
$ cf push yourappname -c 'node app.js'
```

#### Start via Cloud Foundry Manifest

You can specify the command to run your application using the "command" attribute in a manifest.yml file in your top-level application directory. Here is an example manifest.yml:

```
--- 
applications: 
- name: yourappname 
  memory: 256M 
  command: node app.js
```

### Identify Node.js Version to Use at Runtime

It is common for Node.js applications to need particular versions to run successfully. In a package.json file you can configure the version of Node.js to use at runtime. Here is an example package.json using Node.js version 0.10.38:

```
{
	"name": "demo-app",
	"version": "0.1",
	...
	"engines": {
		"node": "0.10.38"
	},
	...
}
```

Now the Node.js buildpack will stage the application to run using version 0.10.38 in AppFog.

### Bind to AppFog Supplied Port

When developing a Node.js application locally, you might run your application on the default port [3000] or configure it to run on a statically supplied port of your choosing. In order for your application to be made available on the Internet, your application must bind to the port supplied to it from AppFog. The port is supplied to your application at runtime via the VCAP_APP_PORT environment variable. In Node.js applications you can easily read in environment variables using `process.env.[ENV_VAR_NAME]`. Here is example code using the Express Node.js module that listens on the AppFog supplied port while still allowing local development to use a statically supplied port number [3000]:

```
var app = express();
app.listen(process.env.VCAP_APP_PORT || 3000);
```

### Deploying Your Application

Now that your Node.js application is ready for successful deployment into AppFog, you can run the following Cloud Foundry CLI command from your top-level application directory:

```
$ cf push yourappname
```
