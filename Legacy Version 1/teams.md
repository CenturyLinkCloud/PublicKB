{{{
  "title": "Customize: Teams",
  "date": "1-28-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The Teams feature allows paid account owners to create Teams and give Team Members permission to manage applications on behalf of the Team Leader using the Command-line Tool.</p>
<p><strong>NOTE: Team Members do not have acess to the Team Leader's account using the Web Console, but they can execute commands to manage apps and services in the Team Leader's account using the '<code>af</code>' command-line tool.</strong></p>
<h3>Requirements:</h3>
<p>The Team Leader's account must be on a Silver, Gold or Platinum plan to create and administer teams. An account can only be a Team Leader for one team, but an account can be a Team Member of multiple teams.</p>
<p>A Team Member's account can be any of these types:</p>
<ul>
<li><strong>Free:</strong> Free accounts were grandfathered in on Feb 28, 2013 with the following resources: 512MB Ram, 10 app instances, and 2 service instances.</li>
<li><strong>Verified Default:</strong> A verified default account can be created by completing the <a href="https://console.appfog.com/signup">sign-up</a> and verification process. A verified default account has 0 resources to deploy apps or services, but can manage apps and services on a Team Leader's account to which they have been invited.</li>
<li><strong>Paid:</strong> Any account belonging to a Basic, Developer, Silver, Gold, or Platinum plan can also be a member of a team, although typically Team Leader accounts are composed of Team Members with Free or Verified Default accounts.</li>
</ul>
<p>The Team Leader has administrative control over the members of their team. Only the Team Leader can invite or remove team members. The Team management functions are listed below.</p>
<p>To get started, go to the <a href="https://console.appfog.com/">Web Console</a> and select the "Teams" tab from the nav menu. The "Teams" page lists Team Members with access to your account, pending invitations, and accounts you are a Team Member of.</p>
<h3>Invite a Team Member</h3>
<p>To invite a new team member, enter their email address in the "Add Members to your team!" box in the "Members in your Team" section.</p>
<h3>Accept an invitation to join a Team</h3>
<p>In the "Your team memberships" section, an invitation from the Team Leader will be displayed with a message: " INVITED on &lt;MM/DD Thh:mm:ss+00:00/YYYY&gt;". Mouse-over the box and click either the "Accept" or "Decline" button. Within a few minutes, the Team Leader's invitation status will update and display the invitation as accepted.</p>
<h3>Managing a Team Leader's account</h3>
<p>Once you've accepted an invitation to a Team, you can interact with the apps on the Team account from the command line tool. Simply use the "<code>-u</code>" flag:</p>
<pre>$ af -u team@appfog.com update example-app</pre>
<p>This command simply does an "<code>af update</code>", but acts on the "team@appfog.com" account.</p>
<p>You can also stop, start, and restart apps, add services, modify environment variables, etc. The only command Team members don't have access to is <code>af passwd</code>. To see the full list of commands, check out the <a href="https://docs.appfog.com/getting-started/af-cli">af cli doc</a>.</p>
