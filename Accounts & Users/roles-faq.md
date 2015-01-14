{{{
  "title": "Roles FAQ",
  "date": "11-6-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3><strong>Description</strong></h3>
<p>CenturyLink Cloud uses role-based access control (RBAC) for restricting&nbsp;system access for specific areas of the platform to authorized users only. There are currently eight roles available to choose from with varying degrees of access. These roles
  were designed to align with job functions that are generally found in most organizations.</p>
<p>This FAQ addresses many commonly asked questions about roles. For more information about how these roles may best be used in the context of your organization, see&nbsp;the KB article titled <a href="https://t3n.zendesk.com/entries/58057320-Practical-Guide-for-Using-Roles"
  target="_blank">Practical Guide for Using Roles</a>.</p>
<h3><strong>General</strong></h3>
<p><strong>Q: <strong>What roles are available and ho</strong>w do I change a user's role?</strong>
</p>
<p>A: The list of roles available in the platform and instructions for setting a user's roles&nbsp;can be found in the <a href="https://t3n.zendesk.com/entries/57972900-User-Permissions" target="_blank">User Permissions</a>&nbsp;article.</p>

<p><strong>Q: Specifically what actions does each role allow a user to perform?</strong>
</p>
<p>A: For a complete list of actions that can be performed in the platform broken down by role, reference the <a href="https://t3n.zendesk.com/entries/57974910-Role-Permissions-Matrix" target="_blank">Role Permissions Matrix</a>.&nbsp;</p>

<p><strong>Q: How are these roles different from the previous ones that were available?</strong>
</p>
<p>A: Previously, CenturyLink Cloud offered a very small set of roles (called "area permissions") that allowed for broadly restricting large parts of the Control Portal for a few specialty users (such as a Billing Administrator). To perform the vast majority
  of activities in the platform, it was required to be an Account Administrator, which often meant opening up more permissions than were required for a user to complete their necessary tasks. The newer implementation supports more granularity of control
  as well as the ability for some users to have read-only access to some areas without the ability to change the configuration. Information on migrating existing users into the new roles model can be found in the <a href="https://t3n.zendesk.com/entries/58057670-Roles-Migration-Guide"
  target="_blank">Roles Migration Guide</a>.&nbsp;</p>

<p><strong>Q: Can I change a user's role through the API?</strong>
</p>
<p>A: Yes, users may be assigned roles through the v1 API using the <a href="https://t3n.zendesk.com/entries/22454018-UpdateUser" target="_blank">UpdateUser</a>&nbsp;method. API v2 does not yet support user or role management, but will eventually support
  it as well.<em><br /></em>
</p>

<p><strong>Q: How long before a user's role changes take effect?</strong>
</p>
<p>A: Users should see the effect of role assignment immediately, but may be required to logout and back in first if the affected user is logged in at the time of the changes.</p>

<p><strong>Q: Can a user have multiple roles assigned?</strong>
</p>
<p>A: Yes, a user may be a member of more than one role. In these cases, the superset of permissions are applied for the user. In other words, the role with the highest level of privilege for a specific action will take precedence. For example, if a user
  is in a role that has only read access to networks (like Account Viewer) as well as a role that has update access to networks (like Network Manager), the user will be able to update networks.</p>

<p><strong>Q: Do individual roles inherit permissions from other roles or relate to each other at all?</strong>
</p>
<p>A: Each role defines a unique and specific set of actions that a user may perform in the system. While one role may include a similar set of actions as another, they in no way inherit from each other. All roles definitions are separate from each other
  and not&nbsp;related in any way.</p>

<p><strong>Q: Do these roles apply for API users?</strong>
</p>
<p>A: The short answer is: yes for API v2, no for API v1. When using API v2, authentication is performed using Control Portal user credentials. In this case, the permissions for the roles assigned to the user authenticating against v2 will be respected.
  In the case of API v1, authentication is done using a separate set of API users (as described in the API v1&nbsp;<a href="https://t3n.zendesk.com/entries/20345423-Authentication-Overview" target="_blank">Authentication Overview</a>). These users effectively
  act as Account Administrators and do not have restricted access to any account resources.</p>

<p><strong>Q: These roles don't exactly fit my security requirements. Do you support custom roles? What about entity-level permissions?</strong>
</p>
<p>A: Custom roles are not currently supported, however the new underlying roles architecture may allow for this to be considered in the future. While entity-level permissions, or ACLs, are not explicitly available, the ability to control access at this
  level can be achieved by using parent and/or sibling accounts to separate resources. For more information on best practices around setting up an account hierarchy, you may reference&nbsp;the&nbsp;<a href="https://t3n.zendesk.com/entries/58057320-Practical-Guide-for-Using-Roles"
  target="_blank">Practical Guide for Using Roles</a>.</p>

<p><strong>Q: My organization doesn't have job titles that map to these role names. How do I apply these existing roles to my organization?</strong>
</p>
<p>A: Some tips&nbsp;for applying this role model to your organization may be found in the&nbsp;<a href="https://t3n.zendesk.com/entries/58057320-Practical-Guide-for-Using-Roles" target="_blank">Practical Guide for Using Roles</a>. You may also get a better
  idea of the&nbsp;complete list of actions that each role can perform by reviewing the&nbsp;<a href="https://t3n.zendesk.com/entries/57974910-Role-Permissions-Matrix" target="_blank">Role Permissions Matrix</a>.</p>


<p><strong>Q: Some roles seem really similar to each other. When would I use one role as opposed to another?</strong>
</p>
<p>A: In some cases, there are definitely only small differences between two roles. For example, Server Administrators only have a few more permissions than Server Operators, and DNS Managers have a subset of the permissions that a Network Manager has. It
  is important to understand the specific distinctions between these roles. To see the complete list of actions that each role can perform, check out the&nbsp;<a href="https://t3n.zendesk.com/entries/57974910-Role-Permissions-Matrix" target="_blank">Role Permissions Matrix</a>,
  and for more help on applying this role model to your organization, some tips may be found in the&nbsp;<a href="https://t3n.zendesk.com/entries/58057320-Practical-Guide-for-Using-Roles" target="_blank">Practical Guide for Using Roles</a>.</p>