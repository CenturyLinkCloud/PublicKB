{{{
  "title": "Roles Migration Guide",
  "date": "11-6-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false
}}}

<h3>Description</h3>
<p>CenturyLink Cloud uses role-based access control (RBAC) for restricting system access for specific areas of the platform to authorized users only. Prior to the release of the currently available eight roles that are designed to align with job functions generally found in most organizations, there was a much smaller and less scalable role set that resulted in a number of users being given more access than they needed to perform their job duties. The guidelines below will help customers migrate from using the four legacy roles to leveraging the eight new more granular ones.</p>
<h3>Existing Roles Mapping</h3>
<p>In the past the only roles available in the Control Portal were Account Administrator, Domain Administrator, Premium Server Administrator, and Billing Administrator. Unfortunately, the provided level of access for these roles, particularly the Premium Server Admin role, was typically not enough for most organizations to effectively use them, forcing the majority of users to be given full Account Administrator access in order to accomplish what they needed.</p>
<p>In the new model, these four roles are "mapped" to new, more usable versions of themselves, and four new roles are introduced to allow for more granular access of areas within Control. Users who were members of the legacy role are now members of the new version of that role, per the table below. </p>
<table>
<thead>
<tr>
  <td>Legacy Role</td>
  <td>New Role
  </td>
</tr>
</thead>
  <tbody>

    <tr>
      <td>Account Administrator</td>
      <td>Account Administrator</td>
    </tr>
    <tr>
      <td>Billing Administrator</td>
      <td>Billing Manager</td>
    </tr>
    <tr>
      <td>Domain Administrator</td>
      <td>DNS Manager</td>
    </tr>
    <tr>
      <td>Premium Server Administrator</td>
      <td>Server Administrator</td>
    </tr>
  </tbody>
</table>

You should find that for Account Administrators and Billing Managers, their access is virtually identical to what it was before, with Billing Managers now able to simply view some additional account settings (but not change them). Domain Administrators similarly now have read-only access to account settings, as well as to other areas such as load balancers, SMTP relay, VPN, and network configuration, in addition to the existing DNS and Site Redirect access they had before. Perhaps the biggest change to the previous role set happens for Server Administrator. This role was frequently the culprit for not providing sufficient access to users and leading many to become full blown Account Administrators without the need for access to all things. Server Administrators now have full access to all server-related functions as well as other tangential areas such as load balancers, networks, policies, etc. You can view a complete list of actions that can be performed by each role in the
[Role Permissions Matrix](../Accounts & Users/role-permissions-matrix.md).

<h3>Migrating Users to New Roles</h3>
<p>If almost all users in your account are Account Administrators, you will likely want to move some of them into one of the four new roles: Server Operator, Network Manager, Security Manager, or Account Viewer.</p>
<p>Many customers will find the Account Viewer role to be very helpful for giving users of the Control Portal read-only access to all account resources. This is a brand new concept introduced into the interface that did not exist for the previous role set. Any users who wanted to peruse through servers, networks, or account resources before had to be given access to change or delete them as well. Now with roles like the Account Viewer and Security Manager role, any users who you want to "look but not touch" can be moved out of the Account Administrator role into a role more suitable for viewing only. </p>
<p>Additionally, the Server Operator role was introduced to enable the management of servers only, without the additional access to other related items like alert or autoscale policies and Blueprints. The majority of users in an organization will probably be members of this role, or at least Server Administrators, since it is likely that most users will be interacting only with the servers and groups interface on a daily basis.</p>
<p>Finally, the Network Manager role as was added to segregate the network-specific functionality from other areas of the Control Portal. Since many organizations have separate resources who manage only the network portion of their infrastructure, this role was designed for this purpose. If your organization has server administrators who need access to all network areas as well, you may choose to have these users be members of both roles if it makes sense.</p>
<p>For other tips on applying these roles to your organization along with a suggested breakdown of how many users might be in each role in your account, check out the [Practical Guide for Using Roles](../Accounts & Users/practical-guide-for-using-roles.md). </p>
