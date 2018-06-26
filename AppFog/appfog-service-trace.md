{{{
  "title": "Getting started with Trace by RisingStack",
  "date": "May 19, 2016",
  "author": "RisingStack, Inc.",
  "attachments": [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

![Trace by RisingStack - Node.js Microservice Monitoring](https://trace.risingstack.com/images/trace-logo-white.svg)

### Company Overview

RisingStack is an enterprise Node.js consulting and development company and a silver member of the Node.js Foundation. RisingStack provides SaaS Application Performace Monitoring (APM) solutions specifically designed for Node.js microservices.

### Service Description

Trace from RisingStack is a microservice monitoring and debugging tool that empowers developers to capture all the essential metrics required to successfully operate microservice-oriented applications. Features include: anomaly detection, distributed transaction tracking, and process monitoring for your services.

For more information, please visit https://trace.risingstack.com/

### Audience

AppFog Users, Developers, Microservice Architects

### Prerequisites

- A Control account and AppFog Developer permissions
- Agreement to the [Trace Terms of Services](https://trace-docs.risingstack.com/docs/term-of-services)

### Provisioning Trace by RisingStack

#### Display Trace Service details in AppFog Marketplace

```bash
cf marketplace -s trace
```

#### Provision the Trace Service

This will create a Trace service for your targeted Space and establish the single sign-on (SSO) connection between AppFog and Trace, enabling you to access the Trace dashboard. Note: You should only provision one Trace account for each Space:

```bash
cf create-service trace freebeta name-of-my-trace-instance
```

#### Binding Trace to Applications

You must bind the Trace instance you have created to each application you would like to monitor with it. If you bind a Trace instance but fail to install and include the npm package in your application, the Trace dashboard will not recieve your application's monitoring events:

```bash
cf bind-service name-of-my-application name-of-my-trace-instance
```

#### Adding Trace

_Step 1:_ To add Trace to your application, first install the npm package:

```bash
npm install @risingstack/trace --save
```

_Step 2:_ Once you have added the package, make sure to include it **as the first line of your application**:

```javascript
require('@risingstack/trace')
```

You are now ready to push your changes, and Trace will begin capturing your application's performance events. You are all done!

Open the Trace dashboard from the AppFog GUI by clicking on the service URL on the bound application's dashboard or the Space Overview services listing.  Alternatively, open the Trace dashboard using this link available from the CLI:

```bash
cf service name-of-my-trace-instance
```

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to provisioning the Trace service on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Trace Support website](http://trace-docs.risingstack.com/)
* For issues related to AppFog, please consult the [AppFog Knowledge Base](../AppFog)
