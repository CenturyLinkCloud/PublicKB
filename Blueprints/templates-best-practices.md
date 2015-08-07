{{{
  "title": "Templates Best Practices",
  "date": "1-19-2015",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Templates are defined virtual images and are the basis from which new servers are build.  Templates should adhere to the following best practices.

Blueprints are a saved and repeatable workflow that bundles components like Templates, Packages and other Blueprints together.  Blueprints should adhere to the following best practices for increased maintainability and a consistent user deployment experience.

### Additional References

See also the KB articles on

- [Blueprint Best Practices](blueprints-best-practices.md)
- [Packages Best Practices](packages-best-practices.md)
- [Differentiating the Template, Package and Blueprint components](understanding-the-difference-between-templates-blueprints-and-packages.md)
- [Best Practices and Preparation for a Virtual Machine/OVF/OVA Import ](../Service Tasks/best-practices-and-preparation-for-a-virtual-machineovfova-import.md)

### Using Templates versus Integrating with Blueprints

Templates appear easier for a successful integration but in actual experience many caveats surface making Blueprints the preferred mechanism for defining server/application end-state.

#### Templates

- If designed according to a minimum supported feature set will be compatible across multiple Private/Public cloud platforms
- Consistent day 0 deployment but less consistency with ongoing run state if patches or other changes are required on the underlying server or software components
- Importing Templates from outside of the cloud process is a non-zero time commitment to cover both a large data transfer and the engineering required for successful deployment
- Importing Templates is considered a billable service task, whereas Blueprints are not

#### Blueprints

- Configuration driven design moves us away from the legacy "golden image" mindset
- Supports flexible underlying operating system versioning (multiple versions of Windows or multiple versions/distributions of Linux) for easy customer deployment
- Changes to underlying OS (including patching) and foundational hardware can be accomplished without rebuilding the entire solution workflow (e.g. replace just a patch or just a configuration step without disrupting the rest of the workflow)
- Requires some engineering expertise to correctly define and package the desired end state
