{{{
  "title": "Blueprints Best Practices",
  "date": "1-19-2015",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": false
}}}

Blueprints are a saved and repeatable workflow that bundles components like Templates, Packages, and other Blueprints together. Blueprints should adhere to the following best practices for increased maintainability and a consistent user deployment experience.

See also the KB articles on

* [Templates Best Practices](templates-best-practices.md)
* [Packages Best Practices](packages-best-practices.md)
* [Differentiating the Template, Package and Blueprint components](understanding-the-difference-between-templates-blueprints-and-packages.md)

### Workflow Components to Consider

When deploying new servers as part of a Blueprint make careful consideration of the following components:

* Always patch servers to the latest patch level (include the Linux Update or Perform Windows Update)
* If you have a demo mode or application available include a parameter to optionally install and configure as part of your Blueprint (as opposed to handling this out of band or of creating multiple Blueprints with largely matching functionality)
* Attach public IP addresses only on services that will receive inbound Internet traffic.  Most customers access the cloud environment via secured private connectivity and don't see the public addresses.  If your Blueprint is an Internet connected service that should be accessible to the Internet at large then skip this step

### When to use Packages versus Blueprints

Simple Blueprints can be built that include only a package with no other components.  Comparing the two deployment steps side by side we see the following experiences:

#### Packages

1. Navigate to Server Group
2. Select Package to execute and server(s) on which to execute
3. Complete deploy data collector

Considerations:

* Can execute the same package on multiple servers within a single execution stream
* Easiest approach for adding capabilities to an existing server
* Always immediately clear this package will add capabilities to an existing server (vs. building a new server with the specified capabilities)

#### Blueprints

1. Select Blueprint from library and click deploy button
2. Select existing server on which to execute
3. Complete deploy data collector

### Blueprints Are Stateless

If your deployment workflow involves multiple servers, such as deploying a new cluster, some mechanism external to Blueprints is needed to facilitate connection and initiation activities across the different servers.  Common patterns for resolving this:

### Deploying a "cluster"
If you only need to define a "master" server - see the [Master and Slave Node Blueprint Example Package](https://github.com/CenturyLinkCloud/Ecosystem/tree/master/Blueprints/Reference%20Templates/Master%20and%20Slave%20Node%20Blueprint%20Example%20Package%20-%20Linux) on Github.  In this pattern the "master" is selected by the deploying user at deploy time from a drop down menu. Make careful use of the "Global" variable type as referenced in [Blueprints Script and Software Package Management](blueprints-script-and-software-package-management.md).

### Adding to Existing Environment
If you are adding capacity to an existing environment the most common pattern is a drop down where you can select an existing asset which the new server is able register with.

### Caching Package Parameters
The parameter types and other metadata is embedded within the Blueprint definition.  Changes to parameter names, types, etc. in an included package will not be reflected until the blueprint is edited and republished.

### Advanced Needs
If your state needs are more advanced, such as requiring key exchange, automated registering of new assets, self-discovery, etc. we recommend investigating the [bpbroker](https://github.com/CenturyLinkCloud/bpbroker) toolset which was specifically created to support this workflow.

### Adding a Public IP Address
CenturyLink Cloud includes an operation to add a public IP address to any server as part of the Blueprint deployment.  Take note that this operation adds both an additional private IP address then NATs a new public IP to the server.

 * Inbound requests to the public IP will always function as expected
 * Egress traffic sourcing from the server will **not** come from the new public IP address.  Egress traffic will appear to source from the public IP associated with the primary server IP address (this can only be configured via the control portal).  If no public IP is associated with the primary server IP address then the traffic will be NATed behind a shared public IP address associated with a number of hosts in the datacenter.


| Scenario   	| Ingress Public IP  	| Egress Public IP  	|
|---	|---	|---	|
| Default Deployment - No public IP, single default private IP  	| -   	| Shared public IP  	|
 | Add public IP from control - Server has one private IP and a static NAT to the primary private IP | Static NAT to private IP address | Static NAT to private IP address |
 | Add public IP from Blueprint - Server has two private IPs and a static NAT to the secondary IP | Static NAT to secondary private IP address | Shared public IP |
