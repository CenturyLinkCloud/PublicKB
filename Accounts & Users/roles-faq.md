{{{
  "title": "Roles FAQ",
  "date": "11-6-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

CenturyLink Cloud uses role-based access control (RBAC) for restricting system access for specific areas of the platform to authorized users only. There are currently eight roles available to choose from with varying degrees of access. These roles were designed to align with job functions that are generally found in most organizations.

This FAQ addresses many commonly asked questions about roles. For more information about how these roles may best be used in the context of your organization, see the KB article titled [Practical Guide for Using Roles](../Accounts & Users/practical-guide-for-using-roles.md).

### General</strong>

**Q: What roles are available and how do I change a user's role?**

A: The list of roles available in the platform and instructions for setting a user's roles can be found in the [User Permissions](user-permissions.md) article.

**Q: Specifically what actions does each role allow a user to perform?**

A: For a complete list of actions that can be performed in the platform broken down by role, reference the [Role Permissions Matrix](../Accounts & Users/role-permissions-matrix.md).

**Q: How are these roles different from the previous ones that were available?**

A: Previously, CenturyLink Cloud offered a very small set of roles (called "area permissions") that allowed for broadly restricting large parts of the Control Portal for a few specialty users (such as a Billing Administrator). To perform the vast majority of activities in the platform, it was required to be an Account Administrator, which often meant opening up more permissions than were required for a user to complete their necessary tasks. The newer implementation supports more granularity of control as well as the ability for some users to have read-only access to some areas without the ability to change the configuration. Information on migrating existing users into the new roles model can be found in the [Roles Migration Guide](roles-migration-guide.md).

**Q: Can I change a user's role through the API?**

A: Yes, users may be assigned roles through the v1 API using the [UpdateUser](http://www.ctl.io/api-docs/v1#users-updateuser) method. API v2 does not yet support user or role management, but will eventually support it as well.

**Q: How long before a user's role changes take effect?**

A: Users should see the effect of role assignment immediately, but may be required to logout and back in first if the affected user is logged in at the time of the changes.

**Q: Can a user have multiple roles assigned?**

A: Yes, a user may be a member of more than one role. In these cases, the superset of permissions are applied for the user. In other words, the role with the highest level of privilege for a specific action will take precedence. For example, if a user is in a role that has only read access to networks (like Account Viewer) as well as a role that has update access to networks (like Network Manager), the user will be able to update networks.

**Q: Do individual roles inherit permissions from other roles or relate to each other at all?**

A: Each role defines a unique and specific set of actions that a user may perform in the system. While one role may include a similar set of actions as another, they in no way inherit from each other. All roles definitions are separate from each other and not related in any way.

**Q: Do these roles apply for API users?**

A: The short answer is: yes for API v2, no for API v1. When using API v2, authentication is performed using Control Portal user credentials. In this case, the permissions for the roles assigned to the user authenticating against v2 will be respected. In the case of API v1, authentication is done using a separate set of API users (as described in the API v1 <a href="http://www.ctl.io/api-docs/v1#authentication-authentication-overview">Authentication Overview</a>). These users effectively act as Account Administrators and do not have restricted access to any account resources.

**Q: These roles don't exactly fit my security requirements. Do you support custom roles? What about entity-level permissions?**
A: Custom roles are not currently supported, however the new underlying roles architecture may allow for this to be considered in the future. While entity-level permissions, or ACLs, are not explicitly available, the ability to control access at this level can be achieved by using parent and/or sibling accounts to separate resources. For more information on best practices around setting up an account hierarchy, you may reference the [Practical Guide for Using Roles](practical-guide-for-using-roles.md).

**Q: My organization doesn't have job titles that map to these role names. How do I apply these existing roles to my organization?**
A: Some tips for applying this role model to your organization may be found in the [Practical Guide for Using Roles](practical-guide-for-using-roles.md). You may also get a better idea of the complete list of actions that each role can perform by reviewing the [Role Permissions Matrix](role-permissions-matrix.md).

**Q: Some roles seem really similar to each other. When would I use one role as opposed to another?**

A: In some cases, there are definitely only small differences between two roles. For example, Server Administrators only have a few more permissions than Server Operators, and DNS Managers have a subset of the permissions that a Network Manager has. It is important to understand the specific distinctions between these roles. To see the complete list of actions that each role can perform, check out the [Role Permissions Matrix](../Accounts & Users/role-permissions-matrix.md), and for more help on applying this role model to your organization, some tips may be found in the [Practical Guide for Using Roles](practical-guide-for-using-roles.md).
