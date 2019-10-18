{{{
  "title": "Getting Started with Managed Active Directory on CenturyLink Cloud",
  "date": "6-13-2016",
  "author": "Thomas Broadwell",
  "attachments": [],
  "contentIsHTML": true
}}}

<strong>NOTE: Managed Active Directory requires a Forest and at least two Domain Controllers be present within your domain.  Before you can deploy Managed Active Directory blueprints, you must have created Managed Windows servers on which to build them.  If a Forest does not already exist, the "CLC Managed Active Directory - New Forest" blueprint will deploy a new forest and a Domain Controller.  A secondary Domain Controller can be deployed using the "CLC Managed Active Directory - Add DC" blueprint.  Managed AD requires that two or more Domain Controllers have been built in your deployment, as this is necessary for servers to be added into your Domain. If this is not possible, all server builds will be added into the shared Active Directory Domain.</strong>
</p>

<p>Here's how to get started with Managed Active Directory in CenturyLink Cloud:</p>

<p>1. Log on to the Control Portal. Using the left side navigation bar, click on Orchestration > Blueprints Library. Search for "Active Directory". Click on the “CLC Managed Active Directory – Add DC” Blueprint.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/EyJnmscs4LOWcKiCl1J26abrq/?name=AD_DC.jpg" alt="AD_DC.jpg" />
</p>
<p>2. Click on the deploy blueprint button.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/uhTQznQMIepjAKdDmHDMGmcMP/?name=deploy.jpg" alt="deploy.jpg" />
</p>
<p>3.&nbsp;Fill out the appropriate details, as shown below.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/74OxavA9bA3kecHCHNFZXKa3h/?name=Screen+Shot+2014-06-19+at+12.24.32+PM.png" alt="Screen_Shot_2014-06-19_at_12.24.32_PM.png" />
</p>

<p>4. Click next, and then verify that the information is correct.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/6XGd05W36YINVRGd9QHouWRIj/?name=Verify.jpg" alt="Verify.jpg" />
</p>

<p>5.&nbsp;Once verified, please click on the deploy blueprint button. You will be presented with the deployment details along with an email stating the Blueprint has been queued.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/LJNTQK4qwNc3EPuVAwsA8QaSx/?name=Queue.jpg" alt="Queue.jpg" />
</p>

<p><strong>Q: How is Managed Active Directory on CenturyLink Cloud priced? </strong>
</p>
<p>A: CenturyLink Cloud Managed Active Directory is priced hourly.</p>
<p><strong>Q: What Versions of Managed Active Directory are supported? </strong>
</p>
<p>A: CenturyLink Cloud Supports Managed Windows 2008 R2 &amp; 2012</p>
<p><strong>Q: Does the Operating System Edition affect the supported version of Managed Active Directory? </strong>
</p>
<p>A: No.
</p>
<p><strong>Q: Can *un-managed* Microsoft Active Directory be converted to *Managed* (or vice versa)?</strong>
</p>
<p>A: This capability is not available at this time.</p>
<p><strong>Q: Why can't I order new instances of Managed Microsoft Active Directory from within the CenturyLink Cloud portal?</strong>
</p>
<p>A: We have discontinued the consumption of Managed Active Directory from within the CenturyLink Cloud control portal. Existing CenturyLink Cloud users of this service may continue to use provisioned instances, but new customers of Managed Active Directory must consume it as part of <a href="https://www.ctl.io/managed-services-anywhere/">Managed Services Anywhere</a>.</p>
<p><strong>Q: What if I'm looking for Managed Active Directory on other platforms? </strong>
</p>
<p>A: Managed Active Directory is just one of many services available with <a href="https://www.ctl.io/managed-services-anywhere/">Managed Services Anywhere</a>.</p>

