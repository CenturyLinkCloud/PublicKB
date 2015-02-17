{{{
  "title": "How To:  Create Customer Specific OS Templates",
  "date": "9-2-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Overview</h3>
<p>CenturyLink Cloud customers may choose to create their own baseline OS templates for deployment within the Control Portal. These templates may include customization, software packages, security templates or other components. Customers should
  take care to test and validate the packages or changes being applied to the OS instance function properly after the template process is complete. Customers are responsible for this validation and ongoing support of changes made to OS Templates.
  </p>
<h3>Important Notices</h3>
<p><em><strong>DO NOT RUN THE CONVERT TO TEMPLATE FUNCTION ON A PRODUCTION/LIVE VIRTUAL SERVER</strong></em>. Customers should create a virtual instance with their specific configurations on a non-production virtual instance. The convert to template
  function actually modifies and moves the virtual machine to the templates group. </p>
<p>Customers creating OS Templates for Windows Servers should carefully review the <a href="http://technet.microsoft.com/en-us/library/hh824835.aspx" target="_blank">Microsoft Sysprep for Server Roles technet article</a>. Sysprep is a component of
  creating an OS Template and as such certain OS Roles are not supported in both the template or clone process. <strong><em>For Windows Servers the CenturyLink Cloud Platform performs the sysprep function on behalf of customers when using the Convert To Template feature</em></strong>.</p>
<h3>Steps</h3>
<ol>
  <li>Use the Create Server Control Portal function to deploy a baseline operating system supported on the CenturyLink Cloud platform. Customers may elect to perform this task outside of the platform and wish to import into the Control Portal. CenturyLink
    Cloud provides <a href="http://www.centurylinkcloud.com/products/support/service-tasks" target="_blank">service tasks</a> to perform this import and customers should engage this group for fees. Preparation steps to import the VM can be found
    <a href="http://help.tier3.com/entries/22209635-Best-Practices-and-Preperation-for-a-Virtual-Machine-OVF-OVA-Import" target="_blank">Here</a>.</li>
  <li>Login to the newly created OS Instance and apply the customization or packages that should be part of the Template. We recommend after all changes are made a clean reboot of the OS prior to proceeding to step #3.</li>
  <li>Navigate to the Server Instance built in step #1 in the Control Portal. Select the Convert to Template button under the Action Menu.</li>

<p><img src="https://t3n.zendesk.com/attachments/token/6MuREq25V2GX8MZ2ngH8hXHPO/?name=01.png" alt="01.png" />
</p>
<li>Using the convert to template user interface input details about the template you wish to create. </li>
<ul>
  <ul>
    <ul>
      <li>Source Server Admin/Root Password:  The administrative password for the source VM</li>
      <li>Template Description: The description is how you will identify your template when creating new servers</li>
      <li>Privacy Settings: Allows customers to define where the template is displayed. Customers with sub accounts can choose to permit access to this template using the Private Shared function.</li>
    </ul>
  </ul>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/jUfTHvR7WbWP4iifNVqEryLCp/?name=02.png" alt="02.png" />
</p>
<li>The Convert to Template task can be tracked via the Queue</li>
<p><img src="https://t3n.zendesk.com/attachments/token/z3JiOR563C20cdbMPS9IbAW4U/?name=04.png" alt="04.png" />
</p>
<li>Once the Convert to Template job is complete customers can test the deployment of the new template by using the Create Server function. The Template Description defined previously should be visible in the Operating System pull down menu.
<p><img src="https://t3n.zendesk.com/attachments/token/VOpySqoalxhPyEIxLvwTa22v9/?name=03.png" alt="03.png" />
</p>

</ol>
<h3>FAQ</h3>
<p><strong>Question</strong>: I've created a custom template in Data Center A, but when I try to create a VM from template in Data Center B its not showing?</p>
<p><em><strong>Answer: Customer created templates do not replicate to all data centers out of the box today. If you need templates copied to other data centers please create a support ticket. Feature sets for global template replication are coming soon.</strong></em>
</p>
<p><strong>Question</strong>: What format should my virtual machine use if I choose to leverage the service task to import a VM as a template?</p>
<p><em><strong>Answer: We recommends OVF format for importing; Additional formats or services are available by speaking to a sales Representative</strong></em></p>
<p><strong>Question</strong>: Is there a way to automatically import VM's as templates to the CenturyLink Cloud platform?</p>
<p><em><strong>Answer: No, please contact a sales representative for import fees via service tasks</strong></em>
</p>
<p><strong>Question</strong>: What fees are associated with use of custom OS templates?</p>
<p><em><strong>Answer: Templates are stored in a group called 'Templates' within the server groups area of Control. Template storage is billed on a per GB basis as Standard Storage. Rates are available from your Sales Representative. </strong></em>
</p>
<p><strong>Last updated: TUES 07/31/2014 16:20 EST</strong>
</p>
