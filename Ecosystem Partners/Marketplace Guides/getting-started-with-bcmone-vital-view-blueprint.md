{{{
  "title": "Getting Started with BCMOne Vital View - Blueprint",
  "date": "1-5-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Partner Profile</strong>
</p>
<ul>
  <ul>
    <li>BCMOne Vital View - Intelligent monitoring platform</li>
    <li><a href="http://www.bcmone.com/vitalview">http://www.bcmone.com/vitalview</a>
    </li>
    <li>CenturyLink Cloud Account Alias: BCM</li>
  </ul>
</ul>
<ul>
  <ul>
    <li>Customer Support:</li>
    <ul>
      <li>24x7 Email Support -&nbsp;<a href="mailto:support@bcmone.com">support@bcmone.com</a>
      </li>
      <li>24x7 Telephone Support - (888) 543-2000</li>
      <li>Sales and Marketing -&nbsp;<a href="mailto:VitalViewNewReg@BCMOne.com">VitalViewNewReg@BCMOne.com</a>
      </li>
    </ul>
  </ul>
</ul>
<strong>Description</strong>
<p>Vital View has integrated their technology with the CenturyLink Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this intelligent monitoring solution.</p>
<strong>Audience</strong>
<ul>
  <li>CenturyLink Cloud Users</li>
</ul>
<strong>Impact</strong>
<p>After reading this article, the user should feel comfortable getting started using the Vital View technology on CenturyLink Cloud.</p>
<strong>Prerequisite</strong>&nbsp;
<ul>
  <li>Access to the CenturyLink Cloud platform as an authorized user.</li>
  <li>Note: &nbsp;If you want to access Vital View from the internet or a Mobile Device, you will need to manually add a Public IP address to the VitalView server. To add a public IP please follow <a href="https://t3n.zendesk.com/entries/49195400-How-To-Add-Public-IP-to-Virtual-Machine">these instructions</a>
  </li>
</ul>
<strong>Detailed Steps</strong>
<p>Follow these step by step instructions to get started with a single-server Vital View deployment. </p>
<ol>
  <li><em>Locate the Blueprint in the Blueprint Library</em>.&nbsp;
    <ul>
      <li>Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.</li>
      <li>Search for “Vital View” in the keyword search on the right side of the page.</li>
      <li>Click the “Install Vital View” blueprint.</li>
    </ul>
  </li>
  <li><em>Choose the Blueprint</em>.&nbsp;
    <ul>
      <li>Click on the "Deploy Blueprint" button.</li>
      <ul>
        <li><img src="https://t3n.zendesk.com/attachments/token/Qke8IWcvrif1WlC52E3aJ4cWI/?name=bc1.jpg" alt="bc1.jpg" />
        </li>
      </ul>
    </ul>
  </li>
  <li><em>Configure the Blueprint</em>.&nbsp;
    <ul>
      <li>Complete the information/fields required by the Blueprint wizard.</li>
      <li>On the first page, “Customize Blueprint”, ensure the following options are configured.</li>
      <ul>
        <li>Password/Confirm Password (This is the root password for the server. Keep this in a secure place).</li>
        <li>Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).</li>
        <li>Optionally set the server name prefix.</li>
        <li>Provide information in additional fields.</li>
        <ul>
          <li><img src="https://t3n.zendesk.com/attachments/token/I85DkZg5WwEhR96AwNEoh2ShT/?name=bc2.jpg" alt="bc2.jpg" />
          </li>
        </ul>
      </ul>
    </ul>
  </li>
  <li><em>Review and Confirm the Blueprint</em>.&nbsp;
    <ul>
      <li>Click “next: step 2”</li>
      <li>Verify your configuration details.</li>
      <ul>
        <li><img src="https://t3n.zendesk.com/attachments/token/UFbUUkux0Vl97jwBUO1SXGlag/?name=bc3.jpg" alt="bc3.jpg" />
        </li>
      </ul>
    </ul>
  </li>
  <li><em>Deploy the Blueprint</em>.&nbsp;
    <ul>
      <li>Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.</li>
      <li>This will kick off the blueprint deploy process and load a queue page to allow you to track the progress of the deployment. </li>
      <li>You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.</li>
      <li>Below is what a successful deployment looks like when completed.</li>
      <ul>
        <li><img src="https://t3n.zendesk.com/attachments/token/sJE1g3Q6En2r4V6cWp54D22M3/?name=bc4.jpg" alt="bc4.jpg" />
        </li>
      </ul>
    </ul>
  </li>
  <li><em>Get Busy!</em>&nbsp;</li>
  <ul>
    <li>Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.&nbsp;</li>
    <li>
      <p>Once the process has completed ­ you will need to determine the your IP address for the newly deployed host. If you navigate to the “Servers” panel and look for the IP addresses. Note the IP address, it will be required in future steps. See
        the image below for help.</p>
    </li>
    <li><strong>Important</strong>: &nbsp;&nbsp;If you want to access Vital View from the internet you will need to manually add a Public IP address to the Vital View server via the CenturyLink Cloud control portal. To add a public IP please follow <a href="https://t3n.zendesk.com/entries/49195400-How-To-Add-Public-IP-to-Virtual-Machine">these instructions</a>.
      &nbsp;You will need to copy the IP address,&nbsp;it will be required in future steps.</li>
    <ul>
      <li><img src="https://t3n.zendesk.com/attachments/token/Tnb7YdVpx022zbbZg66t7pIvy/?name=bcm6.jpg" alt="bcm6.jpg" />
      </li>
    </ul>
  </ul>
  <li><em>Access The Vital View dashboard Interface</em></li>
  <ul>
    <li>The Vital View web interface is accessible via https on port 443 of the server’s public or private IP address.&nbsp;Go ahead and navigate to the dashboard now. Ignore the warning about SSL certificate and continue.</li>
    <ul>
      <li>https://IPADDRESS/vitalview/check_mk/login.py&nbsp;</li>
      <li>
        <p>Mobile Devices can access the service by connecting to the Public IP address on the VitalView server </p>
      </li>
    </ul>
    <li>Create An Account - Once you’ve loaded the web interface, go ahead and create the account, you will automatically be logged in.<img src="https://t3n.zendesk.com/attachments/token/9pCReKVQehzAtw2vfyx90NiTA/?name=bc5.jpg" alt="bc5.jpg" />
    </li>
  </ul>
</ol>

<p><strong>Pricing</strong></p>
<p>The costs listed above in Steps 1 and 2 are for the CenturyLink Cloud infrastructure only. There are no Vital View license costs or additional fees bundled in.</p>
<p>After deploying this Blueprint, the user can secure entitlements to the Vital View technology by using the following steps:</p>
<ul>
  <li>Contact BCMOne Vital View Support via telephone: (855) 662-7722</li>
  <li>Contact Vital View via&nbsp;<a href="https://cloudmine.me/contact/">contact page one their website</a>
  </li>
</ul>

<p><strong>Frequently Asked Questions</strong></p>
<p>Where do I obtain my&nbsp;Vital View License?</p>
<ul>
  <li>Contact BCMOne Vital View via telephone: (855) 543-2000</li>
  <li>Contact BCMOne Vital View via&nbsp;Email Support -&nbsp;<a href="mailto:support@bcmone.com">support@bcmone.com</a>
  </li>
  <li>Contact BCMOne Vital View via their website,&nbsp;<a href="http://www.bcmone.com/vitalview">http://www.bcmone.com/vitalview</a>
  </li>
</ul>
<p>&nbsp;Who should I contact for support?</p>
<ul>
  <li>For issues related to deploying the&nbsp;Vital View Blueprint on CenturyLink Cloud, please contact&nbsp;<a href="mailto:support@bcmone.com">support@bcmone.com</a>
  </li>
  <li>For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud&nbsp;<a href="https://t3n.zendesk.com/entries/23610702-How-do-I-report-a-support-issue-">Support Process</a>.</li>
</ul>