{{{
  "title": "Account Specific: Can I change my AppFog account email address?",
  "date": "1-27-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Q. Can I change the email address I use to login to my AppFog account?</p>
<p>A. No. Due to how Cloud Foundry (the open-source PaaS underlying AppFog) was designed, each account is permanently associated with a single email address. So unfortunately, we are unable to change your account's email address. However, we have a work around solution: create a new (destination) account, and copy over the source code, environment variables, and database content from your existing (original) account.</p>
<p>To do so, follow these steps.</p>
<ol>
<li>First, you'll need to create the account with the email you want. Send us the email address you want to associate with the destination account.</li>
<li>You will need to complete the account verification steps and select a plan.</li>
<li>Via the command-line tool (CLI), login to the original account and download all of your applications. The command is <a href="https://docs.appfog.com/getting-started/af-cli#app-download">here</a>. Note: This will download a copy of each app's source code to your current system folder.</li>
<ol>
<li>Next, get a database dump of each database using the<a href="https://docs.appfog.com/getting-started/af-cli#services"> export services command</a>.</li>
<li>Finally, list the environment variables for each app using the $ af env &lt;appname&gt; command.</li>
</ol>
<li>Logout of the original account and login to the destination account via the CLI.</li>
<li>In the destination account, upload and deploy your applications using the upload/push commands.</li>
<li>Add each app's environment variables using the $ af env-add &lt;appname&gt; &lt;variable [=] value&gt; command.</li>
<li>Create and import your data using the<a href="https://docs.appfog.com/getting-started/af-cli#services"> import services command</a> to move your data into the new service.</li>
<li>Almost done! Test the newly created applications in the destination account and confirm they are functioning as expected.</li>
</ol>
<p>At this point, we recommend you leave the original account active for a few days while using the applications now running on the destination account. Once you are confident nothing was overlooked, you can log back into the original account and select the <a href="https://console.appfog.com/#account">cancel account option</a>. <strong>Note: Before cancelling, confirm your applications and services are functioning properly on the new account.</strong> Please let us know if you have questions regarding these instructions.</p>
<p> </p>
