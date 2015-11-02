{{{
  "title": "How to use Control DNS",
  "date": "10-13-2014",
  "author": "Russ Malloy",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description&nbsp;</h3>
<p>CenturyLink Cloud supports the ability to host and manage your DNS zone within the portal.</p>
<h3>Audience</h3>
<ul>
  <li>Everyone</li>
</ul>
<h3>Prerequisites</h3>
<p>Must have Account Admin permissions</p>
<p>In order for this DNS zone to be utilized, you must update your Name Server records with your Domain Registrar. See&nbsp;<a href="#ComRef">Name Servers</a>
</p>

<h3>Creating a DNS Zone</h3>
<p>Navigate to Domains -&gt; DNS. </p>
<p>Click “new dns zone”. Fill out the below information.</p>
<p>Zone: Input the name of the zone. Example: mydnszone9.com</p>
<p>TTL: 1 hour (Leave as is or modify if needed)</p>
<p>Email: Administrators email for the zone. Example: <a href="mailto:admin@mydnszone9.com">admin@mydnszone9.com</a>
</p>
<p>Google Apps- Leave blank unless you use this.</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/g6pf6kex9y6y6n7/?name=CreateZone.png" alt="CreateZone.png" />
</p>

<p>Wait approximately 30 seconds for the zone to create. Hit F5 to refresh your browser and the domain will appear. Click on your domain to start configuring it.</p>

<h3>Creating Records</h3>
<p>To add your first record, click DNS Tasks and select Add New Record. Below are a few examples.</p>
<p>Creating an A record:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/abxiu0k0skztrz3/?name=CreateA.png" alt="CreateA.png" />
</p>

<p>Hitting ok will create an A record. This would direct any traffic to ftp.mydnszone9.com to 5.5.5.5</p>
<p>Creating a CNAME record:</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/5vdqo5wz0sqzzfq/?name=CreateCNAME.png" alt="CreateCNAME.png" />
</p>
<p>Hitting ok will create a CNAME record. </p>

<p><strong>Deleting records</strong>
</p>
<p>You can delete a record by hitting the Red X on the right side to delete it permanently. You will get a confirmation prompt before the Delete takes place. This applies to individual records and entire zones.</p>

<h3><a name="ComRef"></a>Name Servers</h3>
<p>When you are viewing a DNS zone in Control, you will notice the “Name Server Records” at the top right. These are the records that need to be configured with your domain registrar so that DNS requests are sent to the correct location. </p>

<h3>Notes</h3>
<p>Updating DNS records can take up to 24 hours to propagate throughout the internet. Some providers and ISP’s are much faster than others, but at most it should only take 24 hours.</p>
<p>At the bottom of the DNS page there is a Notes section. This will log any changes made by users. You can also select “New note” to leave an informational note to other users in your environment.</p>
