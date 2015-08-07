{{{
  "title": "Troubleshooting a Failed Managed Services Blueprint",
  "date": "10-24-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>If a Managed Services Blueprint does not complete as expected, please note the OS and the time the Blueprint was attempted. RHEL Managed Services Blueprints will fail from 9am to 10am UTC as a result of regular maintenance in our managed services infrastructure. Please wait one hour before attempting again.</p>

<p>If that is not the issue, follow these steps to expedite troubleshooting.</p>
<p><strong>1. From within the Control Portal, hover over the green bar at the top of the page.</strong>
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/U8DbQ8GQAPbqUUC5iz66CKzfe/?name=Menu.png" alt="Menu.png" />
</p>

<p><strong>2. Select Queue beneath Blueprints</strong>
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/9H29B48xmszIFEY7lO1hpGiK4/?name=Queue.png" alt="Queue.png" />
</p>

<p><strong>3. On the Deployment Queue page, click the pull-down list and select the correct data center.</strong>
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/HGRaSjuSNpR79phiQH7UVmJOx/?name=Context.png" alt="Context.png" />
</p>
<p><strong>4. Click on the radio buttons to find the relevant job and status.</strong>
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/COvAYHehl5K2B1wFKqeBsfkG3/?name=Deployment.png" alt="Deployment.png" />
</p>
<p><strong>5. If your request is in failed status, click on the request to see additional details.&nbsp;</strong>
</p>
<p><strong>6. Click Resume to try to run the request from the point of failure.</strong>
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/AS0hlgmJ5GDtwjovfrorTGZ1z/?name=Details.png" alt="Details.png" /></p>
<p><strong>7. If the issue occurs while running a CLC Blueprint for a Managed Application and the Blueprint fails again after Resuming:&nbsp;</strong>
</p>

<ul>
  <li>If the Blueprint failed at either the step of “Validate Blueprint” or “Reserve Blueprint” call Support at 1-888-638-6771 and notify us about the ≈step the Blueprint failed (such as “Install Managed MS SQL”) and approximate dates and times when you attempted
    to resume it.</li>
  <li>If the Blueprint failed after “Reserve Blueprint,” expand the step where the error failed by clicking on it.</li>
</ul>
<ol>
  <ul>
    <li>You may be able to further expand the errant step to see details of the error:</li>
  </ul>
</ol>
<p><img src="https://t3n.zendesk.com/attachments/token/8L7RLq5vFql23Ai1M2rWlKRdi/?name=Error_Details.png" alt="Error_Details.png" />
</p>
<ul>
  <li>Call Support at 1-888-638-6771. Please notify us about the step the Blueprint failed (such as “Install Managed MSSQL”) and approximate dates and times when you attempted to resume it.</li>
</ul>
<p><strong>8. If the issue occurs during Server Creation for a VM you are attempting to “Make Managed” and the job fails at the same point a second time, continue to troubleshoot by:</strong>
</p>
<ul>
  <li>Checking to see if Blueprint failed prior to a step called "Apply CTS customizations to ______." (The blank would be specific to an Operating System) If so, it is possibly a resource issue.</li>
  <ul>
    <li>Please check the main dashboard to determine if you have exceeded resource limits.</li>
  </ul>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/8Zk9V4VvIYIhGI2ZcUAbvXRax/?name=Resource_Check.png" alt="Resource_Check.png" />
</p>
<ul>
  <ul>
    <li>If it is a resource issue and you require more resources, please adjust accordingly or request limit increases from your account administrator.</li>
    <li>If it is not a resource issue, please contact Support at 1-888-638-6771. Please also note the step the Blueprint failed and approximate dates and times you attempted to Resume it.</li>
  </ul>
</ul>
<ul>
  <li>Check to see if the Blueprint failed at the step called "Apply CTS customizations to ______." (The blank would be specific to the OS.) &nbsp;If this is the case call Support at 1-888-638-6771.Please also note what step the Blueprint failed and approximate
    dates and times when you attempted to Resume it.</li>
</ul>
<p><strong>NEED ADDITIONAL ASSISTANCE?</strong>
</p>
<p>Refer to this related KB, "<a href="https://t3n.zendesk.com/entries/46770424-Deploying-Managed-Services-within-Sub-Accounts">Deploying Managed Services with Sub-accounts</a>."</p>
