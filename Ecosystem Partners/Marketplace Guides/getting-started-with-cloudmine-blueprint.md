{{{
  "title": "Getting Started With CloudMine - Blueprint",
  "date": "12-4-2014",
  "author": "David Shacochis",
  "attachments": [],
  "contentIsHTML": false
}}}

###Partner Profile
</p>
<ul>
  <li>CloudMine - "Blend public cloud with private data to accelerate the next generation of enterprise mobility"</li>
  <li><a href="https://cloudmine.me">www.cloudmine.me</a>
  </li>
  <li>Customer Support:
    <ul>
      <li>CenturyLinksupport@cloudmine.me</li>
      <li>CenturyLink Cloud Account Alias: CMNE</li>
      <li>All support requests can be sent to CenturyLinksupport@cloudmine.me. Please include as much detail as possible regarding your issue and list pertinent contact information so that our team may address your question quickly.</li>
    </ul>
  </li>
</ul>

####Description
<p>CloudMine has integrated their technology with the CenturyLink Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Mobile Backend solution.</p>

####Audience####
<ul>
  <li>CenturyLink Cloud Users</li>
</ul>

####Impact
<p>After reading this article, the user should feel comfortable getting started using the partner technology on CenturyLink Cloud.</p>

####Prerequisite
<ul>
  <li>Access to the CenturyLink Cloud platform as an authorized user.</li>
</ul>

###Detailed Steps
<p>Follow these step by step instructions to get started with a single-server CloudMine deployment. </p>
<ol>
  <li><em>Locate the Blueprint in the Blueprint Library</em>.
    <ul>
      <li>Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.</li>
      <li>Search for “CloudMine” in the keyword search on the right side of the page.</li>
      <li><img src="https://t3n.zendesk.com/attachments/token/7vDSADKzNuwRiIofjep8zusIs/?name=CM1.png" alt="CM1.png" />
      </li>
      <li>Click the “CloudMine Single Server” blueprint.</li>
      <li><img src="https://t3n.zendesk.com/attachments/token/bwYULRqYHsobb5jyg1jPtOS8W/?name=CM2.png" alt="CM2.png" />
      </li>
    </ul>
  </li>
  <li><em>Choose the Blueprint</em>.
    <ul>
      <li>Click on the "Deploy Blueprint" button.</li>
      <li><img src="https://t3n.zendesk.com/attachments/token/7w7WQEjwMFz4HocjlmwncK5zD/?name=CM3.png" alt="CM3.png" />
      </li>
    </ul>
  </li>
  <li><em>Configure the Blueprint</em>.
    <ul>
      <li>Complete the information/fields required by the Blueprint wizard.</li>
      <li>On the first page, “Customize Blueprint”, ensure the following options are configured.</li>
      <ul>
        <li>Password/Confirm Password (This is the root password for the server. Keep this in a secure place).</li>
        <li>Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).</li>
        <li>Optionally set the server name prefix.</li>
        <li>Read and accept the CloudMine terms of service (https://cloudmine.me/eula/centurylink).</li>
        <li>The default values are fine for every other option.</li>
      </ul>
      <li><img src="https://t3n.zendesk.com/attachments/token/ZXYoYubqKeri9E4zQVk6zjZtd/?name=CM4.png" alt="CM4.png" />
      </li>
    </ul>
  </li>
  <li><em>Review and Confirm the Blueprint</em>.
    <ul>
      <li>Click “next: step 2”</li>
      <li>Verify your configuration details.</li>
    </ul>
  </li>
  <li><em>Deploy the Blueprint</em>.
    <ul>
      <li>Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.</li>
      <li>This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment. Generally, it will take 15 to 20 minutes to configure all of the components.</li>
    </ul>
  </li>
  <li><em>Monitor the Activity Queue</em>.
    <ul>
      <li>Monitor the Deployment Queue to view the progress of the blueprint.</li>
      <li>You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.</li>
    </ul>
  </li>
  <li><em>Get Busy!</em></li>
  <ul>
    <li>Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.&nbsp;</li>
    <li>
      <p>Once the process has completed ­ you will need to determine the public IP address for the newly deployed host. If you navigate to the “Servers” panel and look under “recent activity” you should see a status about “Mapping a Public IP”. Note this
        public IP, it will be required in future steps.</p>
    </li>
    <li>
      <p>Before navigating to the web interface, you will need to run a script on the server to let the server know what public IP address it was assigned. To do this, ssh into the public IP address as root, using the password set in step 5.</p>
    </li>
    <li><img src="https://t3n.zendesk.com/attachments/token/sfFfNITb1wPq7Zg1hvFmtWxfw/?name=cm7.png" alt="cm7.png" />
    </li>
    <li>Once in the server, you will need to run a script in root’s home directory like so:</li>
    <li><img src="https://t3n.zendesk.com/attachments/token/7UnKb2QnZVFmsmhdTVbJKm9q2/?name=cm8.png" alt="cm8.png" />
    </li>
    <li>After a couple seconds, the script should complete. You are now ready to use CloudMine!</li>
  </ul>
  <li><em>Access The CloudMine Interface</em></li>
  <ul>
    <li>The CloudMine web interface is accessible on port 8080 of the server’s public IP address (eg. http://123.45.67.89:8080). Go ahead and navigate to the dashboard now.</li>
    <li>Create An Account - Once you’ve loaded the web interface, go ahead and click the orange “Sign up for a new account” button and enter a name, email and password. Your email address will be the account name for future logins. Once you create the account,
      you will automatically be logged in.</li>
    <li><img src="https://t3n.zendesk.com/attachments/token/5gK7MkQEhvQ5Lkl0jbvbiLCGw/?name=cm9.png" alt="cm9.png" />
    </li>
    <li>Create An App -&nbsp;After logging into the dashboard for the first time, create a new app from the top of the screen. Simply give your app a name and click on “Create Application”. There’s no need to pick a mobile platform ‐ the app will be accessible
      from all platforms ‐ REST, iOS, Android, JavaScript, and others.</li>
    <li><img src="https://t3n.zendesk.com/attachments/token/TMq9e3Ui0E5rk4Xf4UdFUbJnS/?name=cm10.png" alt="cm10.png" />
    </li>
  </ul>
</ol>
<p><strong>Pricing</strong></p>
<p>The costs listed above in Steps 1 and 2 are for the CenturyLink Cloud infrastructure only. There are no CloudMine license costs or additional fees bundled in.</p>
<p>After deploying this Blueprint, the user can secure entitlements to the CloudMine technology by using the following steps:</p>
<ul>
  <li>Contact CloudMine via telephone: (855) 662-7722</li>
  <li>Contact Cloudmine via <a href="https://cloudmine.me/contact/">contact page one their website</a>
  </li>
</ul>

###Frequently Asked Questions

<p>Where do I obtain my CloudMine License?</p>
<ul>
  <li>Contact CloudMine via telephone: (855) 662-7722</li>
  <li>Contact Cloudmine via <a href="https://cloudmine.me/contact/">contact page one their website</a>
  </li>
</ul>
<p>Who should I contact for support?</p>
<ul>
  <li>For issues related to deploying the CloudMine& Blueprint on CenturyLink Cloud, please contact <a href="mailto:CenturyLinksupport@cloudmine.me">CenturyLinksupport@cloudmine.me</a>
  </li>
  <li>For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud <a href="https://t3n.zendesk.com/entries/23610702-How-do-I-report-a-support-issue-">Support Process</a>.</li>
</ul>
