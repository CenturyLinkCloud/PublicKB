{{{
  "title": "Disabling a sub account and deleting associated resources",
  "date": "11-4-2013",
  "author": "Ade Miller",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The<a href="https://t3n.zendesk.com/entries/22511724-Cloud-Platform-Release-Notes-October-23-2013" target="_self"> October 23rd 2013 release</a> of the Cloud Platform supports users removing networks and servers associated with the sub account prior to
  disabling the account.&nbsp;</p>
<ol>
  <li>From the sub account dashboard select the SERVERS menu item.</li>
  <li>Delete all the servers associated with this account. From the account’s SERVERS menu remove the server group or servers within each group.</li>
  <li>Delete all the networks associated with the deleted servers. Select the NETWORKS menu and remove each network using the ‘X’ box on the right hand side of the networks list. You cannot delete a network that are still associated with a server.</li>
  <li>Now that you have removed all the resources associated with the sub account, you can now disable the account using the drop down menu on the account’s INFO menu.</li>
</ol>
<p>Explicitly removing network and server resources from the account prior to disabling it ensures that these resources can be reused.</p>