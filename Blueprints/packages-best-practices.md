{{{
  "title": "Packages Best Practices",
  "date": "6-17-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Packages are an invoked piece of software, uploaded to the cloud platform, which customizes a server template.  Packages should adhere to the following best practices for increase maintainability and a consistent user deployment experience.

Related:

* [Template best practices](templates-best-practices.md)
* [Blueprint best practices](blueprints-best-practices.md)
* [Understanding the Difference Between Templates, Blueprints and Packages](understanding-the-difference-between-templates-blueprints-and-packages.md)


### Adhere to published Package maximums

See the published [Package maximums and limits](blueprint-package-and-template-maximum-limits.md). While there are no size limitations note that the maximum execution time for a package is five minutes.  This means large network transfers may exceed this limit and should be redesigned.

Mitigate this by:

* Executing long-running tasks in the background so the primary task can exist.  
* On Linux background tasks also need to close or redirect the stdout/stderr file descriptors (e.g. >/dev/null 2>&1).  
* If errors are encountered send an email to notify


### Changes to Existing Package Parameters

If your package is part of a Blueprint and the parameters change this will not be reflected in the Blueprint itself until the Blueprint has been opened for editing then resaved.


### Parameter Visibility

Global parameters are shown towards the top of the wizard before any platform-level parameters (such as server password, group, etc.).  Keeping all of your package parameters with a global scope keeps them in the same location.

Script specific parameters are relegated to the bottom of the page and if not required may be missed.


### Packages and Blueprint Visibility

Any packages that will be included in a Blueprint with a **Shared** or **Public** visiblity level must have the same visibility.  For example, Public Blueprints must reference only packages that are also public.


### Software vs. Scripts

CenturyLink Cloud includes the concepts of grouping packages into classes of either Software or Scripts.  *All new package deployments should be classified as Scripts* - we anticipate deprecating the Software class and many third party tools have been created to support Scripts rather than software.  There is zero functionality differentiation between the two classification types.

