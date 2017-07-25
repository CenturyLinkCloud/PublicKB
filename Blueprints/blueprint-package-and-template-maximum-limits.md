{{{
  "title": "Blueprint, Package, and Template Maximums and Limits",
  "date": "1-19-2015",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
Below are a few notes on the defined maximums or limits associated with usage of the Blueprint engine.  Workflows that exceed these limits will fail with varying error messages.

### Packages
Packages are individually composable tasks which can be executed on an ad-hoc basis at the server group level or can be defined as a group as part of a Blueprint.

* Maximum execution time for a single package is 5 minutes
* Packages do not share state with other packages or a Blueprint in which they reside
* Packages have access to all set environment variables. Some of these can be specified within the package definition itself including system variables (user, hostname, IP address) and user defined variables.

### Blueprints
Blueprints are composed of a multi-task workflow which may involve one or more distinct packages.
* Maximum execution time for a single Blueprint is 20 minutes
