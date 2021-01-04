{{{
  "title": "Rolling Back WordPress Sites",
  "date": "10-08-2015",
  "author": "Matt Wittmann",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT NOTE

Lumen WordPress hosting is currently in a Limited Beta program with specific customers by invitation only
and is not intended for production usage.

During the Limited Beta there is no production Service Level Agreement.

### Overview

Rollback is the complement to [site update with git](wordPress-site-updates-with-git.md).
It is important to [test plug-in and theme changes locally](wordpress-local-development.md)
with Vagrant, but if a bad change has been pushed to the live site, it is possible
to roll back without dealing with git commit history and reverts.

The rollback feature is intended as a quick fix until the site's git repository is
fixed. After a rollback is performed, further rollbacks are disabled until the next
push to Lumen Git Hosting; in other words, it is **not** possible to roll back
the rollback. The code in the Lumen Git Hosting repository is not modified.

### Prerequisites

* A WordPress site has been created using the Lumen WordPress hosting platform.
* A change to the site has been committed and pushed to Lumen Git Hosting.
* The change is undesired and needs to be rolled back.

### Rollback Process

1. [Log in](https://wordpress.ctl.io/) to the Lumen WordPress hosting platform.
2. Find the site that needs to be rolled back in the list of sites.
3. The "Roll Back" button is on the right side of the row. If no "Roll Back" button
   is visible for a given site, that site cannot be rolled back—either because it is
   a newly created site with no changes or because it has already been rolled back
   without further git pushes.
4. Click the "Roll Back" button. You will be prompted to confirm your choice.
5. The rollback process is initiated. This can take a couple of minutes. As with
   the initial blue/green deployment of updates from git, there may be a brief window
   when your site resolves to both the erroneous version and the version you are
   rolling back to.
6. The rollback process can take a few minutes to complete. If your site is still
   not rolled back after several minutes, you may consider opening a support ticket.
   Note that rollback will go two pushes back only. If you have committed and pushed
   several times without verifying your changes, the only way to recover will be
   manually reverting all the bad commits in your git history.

### After the Rollback

The rollback takes a site two git pushes back. If this version is also bad, a [git
revert](http://git-scm.com/docs/git-revert) will need to be performed. Performing a
git revert is also useful to fix the last bad push in the git repository.
Regardless, it is important to bring the `refs/HEAD/master` of the repository
back to a non-broken state. Once the fixing commits are pushed back up,
the normal blue/green deployment process of the site update will begin.

**Because of the rollback, until further commits are pushed to the site's repository,
the git repository will no longer be synchronized with the live site!**
