{{{
  "title": "Add Multiple Instances of a Software Package to a Blueprint",
  "date": "8-2-2012",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description:</strong>
</p>
<p>Users can set unique parameters for each instance of a software package in a blueprint. For instance, if a blueprint author wishes to add Microsoft SQL Server 2012 to two servers but with different credentials for each machine, that is possible within
  the Blueprint Designer. This article walks through the process of creating blueprints with multiple identical software packages and then setting unique parameters when that blueprint is deployed.</p>
<p><strong>Steps:</strong>
</p>
<p><strong>1a. Create blueprint with multiple servers, software added at “Tasks &amp; Order” phase.</strong>
</p>
<ul>
  <li>Locate the “Design Blueprint” option in the Control Portal navigation menu.
    <br /><img src="../images/blueprint-add-package-siblueprint01.png" alt="siblueprint01.png" />
  </li>
  <li>Provide a name, version number, privacy setting and description for the blueprint.
    <br /><img src="../images/blueprint-add-package-siblueprint02.png" alt="siblueprint02.png" />
  </li>
  <li>Add a pair of servers to the blueprint. In this example, the servers are Windows Server 2008 R2 machines with default memory and CPU configurations. Note that no software/tasks/scripts are applied at this point.
    <br /><img src="../images/blueprint-add-package-siblueprint03.png" alt="siblueprint03.png" />
  </li>
  <li>After clicking “Next”, click the “Add Task” button and choose a software package or script that is known to have installation parameters.
    <br /><img src="../images/blueprint-add-package-siblueprint04.png" alt="siblueprint04.png" />
  </li>
  <li>Click the “Add” button and then choose which server that this package applies to. Blueprint authors can select specific servers or choose the “Select During Deployment” option. In this example, the first server is selected.
    <br /><img src="../images/blueprint-add-package-siblueprint05.png" alt="siblueprint05.png" />
  </li>
  <li>After clicking the “Add Global Tasks” button, repeat this process and add the same software package to the second server in the blueprint. The final result should show two servers and two instances of the software package.
    <br /><img src="../images/blueprint-add-package-siblueprint06.png" alt="siblueprint06.png" />
  </li>
  <li>Finish the Blueprint Designer wizard and submit the blueprint for publishing.</li>
</ul>

<p><strong>1b. Create blueprint with multiple servers, software added as part of each server configuration.</strong>
</p>
<ul>
  <li>In this variation of step 1a, the software is selected at the same time as the server is configured. These two methods for installing software produce the same output even though the blueprint engine treats them slightly differently. The technique in
    step 1a is recommended when the server environment already exists and the blueprint is used to provision software onto that environment. The activities outlined here in Step 1b are recommended when building an entirely new environment.</li>
  <li>Locate the “Design Blueprint” option in the Control Portal navigation menu.
    <br /><img src="../images/blueprint-add-package-siblueprint01.png" alt="siblueprint01.png" />
  </li>
  <li>Provide a name, version number, privacy setting and description for the blueprint.
    <br /><img src="../images/blueprint-add-package-siblueprint07.png" alt="siblueprint07.png" />
  </li>
  <li>Add a pair of servers to the blueprint. In this example, the servers are Windows Server 2008 R2 machines with default memory and CPU configurations. On the server configuration page, click the “Install Software” button and select a software package.
    <br /><img src="../images/blueprint-add-package-siblueprint08.png" alt="siblueprint08.png" />
  </li>
  <li>Repeat the process and add a second server that has the same software package selected during the server configuration.</li>
  <li>After saving both server configurations, see the “Task &amp; Order” page where both servers, and their software packages, are listed in a slightly different way than demonstrated in step 1a.
    <br /><img src="../images/blueprint-add-package-siblueprint09.png" alt="siblueprint09.png" />
  </li>
  <li>Complete the blueprint and submit it for publishing.</li>
</ul>

<p><strong>2. Deploy blueprint and set unique software package settings</strong>
</p>
<ul>
  <li>Blueprints built using either the technique from Step 1a or 1b will follow the same deployment process.</li>
  <li>Locate the blueprints that have multiple servers with the same software package.
    <br /><img src="../images/blueprint-add-package-siblueprint10.png" alt="siblueprint10.png" />
  </li>
  <li>Select a blueprint for deployment.
    <br /><img src="../images/blueprint-add-package-siblueprint11.png" alt="siblueprint11.png" />
  </li>
  <li>Click “Deploy Blueprint” and see the deployment-level parameters that can be set including server passwords, network, server names and one section for EACH instance of the software package contained in the blueprint. This means that each software package
    could be deployed with parameter that are unique to the server its being installed on.
    <br /><img src="../images/blueprint-add-package-siblueprint12.png" alt="siblueprint12.png" />
  </li>
  <li>Review the settings of the blueprint and choose to deploy it.</li>
  <li>Upon completion, see that the software was installed on each server per the configured parameters.</li>
</ul>
