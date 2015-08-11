{{{
  "title": "Getting Started With AppFog v1: Overview",
  "date": "1-25-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Here are all thing things you need to get up and running to experiment and develop content on the AppFog PaaS.</p>
<h4>Sign Up for an Account</h4>
<p>Before you get started, you will need to sign up for an account and select a Plan. Start by going to the <a href="https://console.appfog.com/signup">sign-up page</a> and filling out the requested information as completely as possible. Before you can start uploading any apps, you'll need to verify your account, a welcome email is sent to you with a verification link. Once signed in you can select a plan. You can find more information in our <a href="billing-process-overview.md">Billing</a> article.</p>
<h4>The AF CLI Tool</h4>
<p>Now that you have signed up for an account and selected a plan, the next step is to install the tool you'll use to push, pull, and update applications and services on our platform. The AF CLI tool is a RubyGem that calls the API for all of these functions. To remotely connect your services you will also need to install another gem called Caldecott. Caldecott sets up tunneling to your services from local machine. Instructions and a more detailed overview can be found in our <a href="appfog-cli-tool-manual.md">AppFog CLI Tool Manual</a>.</p>
<h4>Pushing an App</h4>
<p>There are a few avenues for standing up applications. If you have an application already, you'll need to verify that it will work under the runtimes our platform has installed. You can find this out by using the <code>af runtimes</code> command in the AF CLI tool or viewing our <a href="runtimes-and-available-jumpstarts-list-26jan2015.md">Runtimes and Available Jumpstarts List</a>.</p>
<p>If you want to start from scratch, you can use our jumpstart applications. For detailed instructions on this, you can visit our <a href="web-console-and-cli-introduction.md">Web Console and CLI Introduction</a> article.</p>
<h4>Non-Persistent Data Storage</h4>
<p>AppFog does not have a persistent data storage system. This means that any files created or updated while the application is running are volatile and will be lost if the application is restarted or crashes. The only files that are persisted between application (re)starts are those that are uploaded with the <code>af push</code> or <code>af update</code> commands. The best practice for persisting files created while an application is running is to store them in a native AppFog database or external storage system like CenturyLink Cloud or ClearDB. </p>
<p>The <a href="http://12factor.net">12 Factor App</a> website provides a helpful guide on how to build fault-tolerant, redundant cloud-based applications.</p>
<p> </p>
