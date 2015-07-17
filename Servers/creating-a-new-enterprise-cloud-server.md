{{{
  "title": "Creating a New Enterprise Cloud Server",
  "date": "11-13-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description:</strong>
</p>
<p>The heart of the CenturyLink Cloud Enterprise Cloud Platform is the ability to create and manage virtual infrastructure. In this KB article, we demonstrate how to provision new virtual machines in the CenturyLink Cloud.</p>
<p><strong>Steps:</strong>
</p>
<div><strong>1. Start "Create Server" Process.</strong>
</div>
<ul>
  <li>There are two places to initiate this process. The first is from the top-most navigation menu under the <strong>Servers</strong> section.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/4nWmChpcg7AfDt5QDcGoLyuoN/?name=createserver16.png" alt="createserver16.png" />
  </li>
  <li>The second place to trigger this process is from within the Servers UI. From the Servers page, select the <strong>New Server (+) </strong>icon<strong>. </strong>
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/J17PuvEMgJSePQgWApGEtscTj/?name=01.png" alt="01.png" /><img src="https://t3n.zendesk.com/attachments/token/65AvXyfs7BQLgQ7vgpkIke2Ed/?name=02.png" alt="02.png" />
  </li>
</ul>
<div><strong>2. Provide Basic Server Information</strong>
</div>
<ul>
  <li>Choose a Data Center to deploy this virtual server into.
    <br /><img src="https://t3n.zendesk.com/attachments/token/toRhTjyzqx3BUzQffdF8aBoni/?name=03.png" alt="03.png" />
  </li>
  <li>Set the following parameters:</li>
</ul>
<ol>
  <ol>
    <li><a href="http://www.ctl.io/products/management/groups">Group membership</a>&nbsp;</li>
    <li><a href="http://www.ctl.io/managed-services/operating-system">Managed Server</a>
    </li>
    <li><a href="http://www.ctl.io/servers">Standard </a>or <a href="http://www.ctl.io/products/compute/hyperscale">Hyperscale</a>&nbsp;Server Type</li>
  </ol>
</ol>
<p><img src="https://t3n.zendesk.com/attachments/token/Ij5TseHU3xH1OVaAxqAny7Y9h/?name=04.png" alt="04.png" />
</p>
<ul>
  <li>Choose the operating system template for this server. This can use any of the 20+ Windows and Linux templates offered by CenturyLink Cloud or a custom template created by a user within the account.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/3LqcoKLBAueWJw5lnzNsXwpwI/?name=05.png" alt="05.png" />
</p>
<ul>
  <li>Set the server name. The name entered by the user is part of a formatted name that is arranged as: <strong>&lt;data center name&gt;</strong> + <strong>&lt;account alias&gt;</strong> + <strong>&lt;user-provided server name&gt;</strong> +<strong> &lt;counter index&gt;</strong>.
    Server names can only be changed after the fact by contacting the CenturyLink Cloud NOC.</li>
  <li>Set a description for the server. This field is mandatory.</li>
  <li>Set the Administrator password for the server. This is the "Administrator" password for Windows, or "root" password for Linux.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/dl0uRYAhAamj2ioQQcXxo1aeg/?name=06.png" alt="06.png" />
</p>
<div><strong>3. Define Server Resources</strong>
</div>
<ul>
  <li>Specify CPU, memory and storage allocation for the server. Provision up to <a href="https://t3n.zendesk.com/entries/21819996-Cloud-Server-Instance-Size-and-Performance">platform maximums</a>. These values can be changed by the user after
    provisioning the server.</li>
  <li>Add storage disks to the server up to <a href="https://t3n.zendesk.com/entries/21819996-Cloud-Server-Instance-Size-and-Performance">platform maximums</a> based on server type. Storage disks can be expanded, added, and removed after
    the server is built. Choosing a Partition results in a formatted disk in the operating system. Raw Disk provides an unformatted volume. </li>
  <li>Select a <a href="https://t3n.zendesk.com/entries/22032834-Creating-and-Applying-Autoscale-Policies">CPU Autoscale Policy</a>&nbsp;making it possible to scale servers up and down based on utilization ensuring optimal deployment of resources
    for cloud environments under a variety of conditions</li>
  <li>Select an appropriate <a href="https://t3n.zendesk.com/entries/21861680-CenturyLink-Cloud-Backup-and-Recovery-Services">backup level</a> for your new virtual machine. (<strong>Quick Tip</strong>: &nbsp;This is only available for
    Standard Server Type)</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/Jx5riABL8L9GajDwO14hzgQlK/?name=07.png" alt="07.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/jvqizpp8svKZQ27jfng78KHuN/?name=09.png" alt="09.png" />
</p>
<div><strong>4. Network</strong>
</div>
<ul>
  <li>Select the account network, primary DNS and secondary DNS for this server. Accounts can have multiple networks within a particular data center. If the user wishes to change their network settings after the server has been provisioned, they must contact
    the CenturyLink Cloud NOC who can, <strong>for a fee</strong>, change the vlan and re-IP the server.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/23gQG2zXrcfIpYWPx6DAQ2SmN/?name=08.png" alt="08.png" />
</p>

<p><strong>5. Time to Live</strong>
</p>
<ul>
  <li>Set a Time to Live. Choose whether you want to manually delete this server at some point in the future, or whether the system should delete this server on a set date. Setting a time to live results in a new "Scheduled Task" added to the server. This
    Scheduled Task can be changed by the user after the server is provisioned.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/MI04DqkHMP4JKaq6H9uNfbdcb/?name=10.png" alt="10.png" />
</p>
<ul>
  <li>Click the <strong>Create Server </strong>button to queue the server build.</li>
</ul>
<div><strong>6. Confirm server settings</strong>
</div>
<ul>
  <li>Once the CenturyLink Cloud build engine has provisioned the virtual server, you can see the details of the server.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/kuFwSYjYAE4DtzWnMjop5ywOH/?name=11.png" alt="11.png" />
  </li>
  <li>View and change its resource allocations by clicking the CPU, Memory or Storage icons and sliding resources up or down.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/prswQ5VFYhytgdVXjDIqerRSv/?name=12.png" alt="12.png" />
</p>