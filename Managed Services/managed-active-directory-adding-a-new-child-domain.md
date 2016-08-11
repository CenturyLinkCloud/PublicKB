{{{
  "title": "Managed Active Directory - Adding a New Child Domain",
  "date": "10-14-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>As your Active Directory environment grows, you may need add new "child" domains. <strong>NOTE: Before you can deploy a new child, you need to have Managed Active Directory and Managed Windows server in place. <strong>Also, please ensure that two or more Domain Controllers have been built in your deployment, as this is a necessary component for servers to be added into your Domain. If this is not possible, all server builds will be added into the shared Active Directory Domain.</strong></strong>
</p>
<p>1. Log on to the [Control Portal](https://control.ctl.io/). Using the left side navigation bar, click on **Orchestration** > **Blueprints Library**. Search for "Active Directory". Click on the “<strong>CLC Managed Active Directory – New Child</strong>" Blueprint. Click on the **deploy blueprint** button.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/XOGsQO84SHAiWnaZq7DAgga5Z/?name=Child.jpg" alt="Child.jpg" />
</p>
<p>2.&nbsp;Fill out the appropriate details, as shown below.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/uTdbFfjWX4bZnF2IeG0xVGqFT/?name=Screen+Shot+2014-06-19+at+1.54.46+PM.png" alt="Screen_Shot_2014-06-19_at_1.54.46_PM.png" />
</p>

<p>3. Click next, and then verify that the information is correct.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/FTwAOi5yuja5DsEP8Scb3xyS9/?name=Child-Verify.jpg" alt="Child-Verify.jpg" />
</p>

<p>4.&nbsp;Once verified, please click on the deploy blueprint button. You will be presented with the deployment details along with an email stating the Blueprint has been queued.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/c5pOtXGVNHprMzE2GGrSbbuPw/?name=Queue_Child.jpg" alt="Queue_Child.jpg" />
</p>
