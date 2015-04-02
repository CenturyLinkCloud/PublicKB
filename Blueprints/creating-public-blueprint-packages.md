{{{
  "title": "Creating Public Blueprint Packages",
  "date": "10-20-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>CenturyLink Cloud offers users the ability to create&nbsp;packages as a way to consistently run specific scripts or executables on one or more servers. These packages also provide the user with a method of defining a given set of parameters that allow
  for the gathering of information at deployment time so that it may be passed to the script to be used during the execution. (Read about <a href="../Blueprints/blueprints-script-and-software-package-management.md">Blueprints Script and Software Package Management</a>  for more information on how to create packages in general.) These scripts can be executed directly against one or more servers, or they may be included
  as <a href="../Blueprints/how-to-execute-a-blueprint.md">tasks that are run as part of a Blueprint definition</a>.</p>
<p>These packages are very often specific to a function that may only be applicable to a particular set of users. As such, packages are generally created in the context of a single account and marked as either Private (only visible to users in the account
  where it was created) or Private Shared (visible to users in the account where it was created and all sub-accounts underneath it).&nbsp;However, if a package is created that could be useful for other users and accounts, it may be published as a Public
  package so all users are able to utilize it. In this case, there are some additional considerations to be addressed and steps to be followed.</p>
<h3>Public Package Considerations</h3>
<p>CenturyLink Cloud users are encouraged to submit packages as public if they feel they are appropriate for public consumption and potentially useful for other customers. When creating packages that are intended to be published as publicly available, be
  sure to take the following items into consideration:</p>
<ol>
  <li><strong>Naming</strong>&nbsp;-There is a preferred naming convention to follow for packages that will be made public. The following form should be used when naming packages intended to be public:
    <br />
    <br /><strong>&lt;Verb&gt; &lt;Name&gt;</strong> <strong>on &lt;Platform&gt; (x of #) [&lt;Description&gt;]</strong>
    <br /><strong>Example: Install Active Directory Domain Services on Windows (1 of 2) [Primary Node]</strong>
    <br />
    <br />&lt;Verb&gt; is usually "Install" or some other word that describes the primary action the package is doing.
    <br />&lt;Name&gt; is the name of the software.
    <br />&lt;Platform&gt; should generally be either "Linux" or "Windows" or in some cases, the specific version of Linux (RedHat, Ubuntu) or Windows (2008, 2012) if other similar packages exist for different versions.
    <br />(x of #) is optional but should be included if the package is used as part of a series of packages that should be run a specific order.
    <br />&lt;Description&gt; is also optional but can be included if there is a short piece of additional information that is helpful in describing better what the package does. It should be surrounded by square brackets [ ] and put at the end of the name.<strong><br /><br /></strong>
  </li>
  <li><strong>Parameters - </strong>Any time a package is created it should use parameters as much as possible to provide flexibility so that it may be used in many environments. This is particularly true for packages that will become public. Avoid using anything
    hardcoded (IP addresses, server names, passwords, etc.) and make things as configurable as possible through the use of parameters. Also, keep in mind that your package will be replicated to all CenturyLink Cloud DCs, so there also should be no DC-specific
    dependencies built in.
    <br />
    <br />
  </li>
  <li><strong>Licensing - </strong>Be aware of the licensing requirements for any software included in the package. Of course, using free or open source keeps this easy, but if you are using commercial software, be sure the package includes licensing validation.
    <br
    />
    <br />
  </li>
  <li><strong>Maintenance - </strong>If possible, the package script should be written in a way that it does not need to be updated frequently as new software versions become available. At the very least, every effort should be made to write it so it is as easy/trivial
    as possible to update it for new versions (or new OS templates) as needed.
    <br />
    <br />
  </li>
  <li><strong>Testing - </strong> Public packages are definitely not built for one-time use, so testing them should of course be more rigorous than quick throwaway packages. Consider all possible OS template versions that it will (or will not) work on and, if
    possible, write scripts in a way that they can be repeatedly deployed, even on the same server, and end up with the same result.</li>
</ol>
<h3>How to Publish a Public Package</h3>
<ol>
  <li>After creating the package and taking all of the above considerations into account, follow the instructions outlined in the article about <a href="../Blueprints/blueprints-script-and-software-package-management.md"
   >Blueprint Script and Software Package Management&nbsp;</a>to publish the package. For the final step, be sure to select "Public" as the visibility choice.&nbsp;After a package is published with public visibility, it is put into a "pending"
    state and must be approved by a CenturyLink Cloud Administrator before it is available for public use. (Users in the account where it was created will still be able to use it in existing Blueprints while it is in a pending state.)</li>
  <li>Send an e-mail to <a href="mailto:ecosystem@centurylinkcloud.com">ecosystem@centurylinkcloud.com</a>&nbsp;with the subject of "Package Approval" and be sure to include your account alias, the name of the package in the request, and a brief description
    of what it is and how to use it (if not clear from the package definition).</li>
  <li>After reviewing and testing the package, if there are no issues found, the package will be approved by a CenturyLink Cloud Administrator. Once approved, it will appear in the public packages library to be used on servers and in Blueprint definitions.</li>
</ol>
