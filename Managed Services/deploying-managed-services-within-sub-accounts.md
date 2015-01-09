{{{
  "title": "Deploying Managed Services within Sub-Accounts",
  "date": "10-24-2014",
  "author": "Jared Ruckle",
  "attachments": []
}}}

<p>For many customers, the ability to create and maintain sub-accounts with within your primary CenturyLink Cloud Control account is one of the appeals of our platform.&nbsp; It is important to note, however, that if you plan to create VMs with Managed Services
  such as Managed OS and Applications within those Sub-Accounts, you must be logged in at the Sub-Account level to build the servers within that Sub-Account.</p>
<p>As a managed VM is created, our system automation will attempt to confirm that you are in fact a valid user at the account level at which you are creating a VM.&nbsp; At this time, this check <em>only applies</em> when you are attempting to make a VM
  <em>‘managed’</em> by CenturyLink.&nbsp; <em>This check does not take place when building standard unmanaged VMs</em>.</p>
<p>To avoid unnecessary build failures, please make certain that you log into the appropriate Parent or Sub-account in which you plan to build the managed VM.&nbsp; Please contact your internal Account Administrator if you do not have log-in access to a
  given Parent or Sub-account level.</p>
<p><strong>NEED ADDITIONAL ASSISTANCE?</strong>
</p>
<p>Refer to this related KB, "<a href="https://t3n.zendesk.com/entries/46750410-Troubleshooting-a-Failed-Managed-Services-Blueprint" target="_blank">Troubleshooting a Failed Managed Services Blueprint</a>."</p>