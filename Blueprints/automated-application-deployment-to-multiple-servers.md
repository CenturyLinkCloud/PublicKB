{{{
  "title": "Automated Application Deployment to Multiple Servers",
  "date": "10-8-2014",
  "author": "Bryan Friedman",
  "attachments": [
    {
      "url": "../attachments/DKH2UpNYni9uEqvvZlTl0xsun-package.zip",
      "type": "application/zip",
      "file_name": "package.zip"
    }
  ],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>Most modern application architectures require the same code to be deployed to many servers. Whether you are running a load-balanced web app, a database cluster, a distributed set of batch jobs, or all of the above, you are faced with maintaining code
  parity across all nodes, ensuring you have the latest code at every available location. While there are a number of sophisticated deployment tools available (Octopus, Go, Packer, etc.), sometimes all that’s required is simply copying the code from a
  repository to a specific location on each server. On CenturyLink Cloud, we will see in the following example that no matter what the deployment model, Blueprint scripts can help you make this task easy, automated, and repeatable.</p>
<p>In this scenario, we have an app written in PHP with code maintained in a GitHub repository. This app is deployed to three web servers sitting behind a load balancer running RedHat with Apache and PHP already installed. In order to deploy updated code
  from the repo to all of the servers, we will create a script to pull the code from GitHub to a specified path on the server, and then use the control portal to run that script on all three servers. Although we are using a simple git script on Linux
  to deploy our application in this example, the pattern described below can be used to perform <em>any</em> scriptable deployment action across many servers with any OS.</p>
<h3>Steps</h3>
<ol>
  <li><strong><strong>Write a shell </strong></strong><strong>script to clone or pull from Git repository.</strong>
  </li>
  <ol>
    <li>Before creating any Blueprints or Scripts in the Control Portal, write a shell script that will run on a RedHat Linux server. It will need three command line parameters:
      <br />
      <pre># Take parameters from command line<br /> ACTION="$1"    # Either "clone" or "pull" depending on first time deployment or update<br /> GITREPO="$2"   # The URI for the repository<br /> APPPATH="$3"   # The path on the server to deploy to</pre>
    </li>
    <li> Next, ensure that git package is installed on server.
      <br />
      <pre># Ensure git is installed<br />yum -y install git</pre>
    </li>
    <li>Finally, depending on the defined parameters, either “clone” or “pull” the specified repository to the specified path.
      <br />
      <pre>if [ "$ACTION" = "clone" ] ; then

   git clone "$GITREPO" "$APPPATH"

elif [ "$ACTION" = "pull" ] ; then

   cd "$APPPATH"

   git pull

fi</pre>
    </li>
  </ol>
  <li><strong>Create the script package.</strong> (For details on creating script packages in general, refer to the article <a href="../Blueprints/blueprints-script-and-software-package-management.md">Blueprints Script and Software Package Management</a>.)</li>
  <ol>
    <li>Save the script from Step 1 as <code>install.sh</code>.</li>
    <li>Now, create the package manifest XML with all the information needed to upload the script to the control portal. This file contains the name and description of the package, along with the parameters needed and the command to execute. The three parameters
      defined above are passed to the command as Global parameters, so they will only be requested once and applied to all servers.
      <pre>&lt;Manifest&gt;

  &lt;Metadata&gt;

    &lt;UUID&gt;74b6ac7b-6848-4adc-9ecf-f1fc21b26561&lt;/UUID&gt;

    &lt;Name&gt;Clone or Pull a Git Repo&lt;/Name&gt;

    &lt;Description&gt;

    Clones or pulls the provided Git repository to the specified directory

    &lt;/Description&gt;

  &lt;/Metadata&gt;

  &lt;Parameters&gt;

    &lt;Parameter Name="Git Repo URL" Type="String" Variable="T3.GitRepo.URL" <strong>Prompt="Global"</strong> /&gt;

    &lt;Parameter Name="Local Repo Path" Type="String" Variable="T3.GitRepo.LocalPath" <strong>Prompt="Global"</strong> /&gt;

    &lt;Parameter Name="Clone or Pull" Type="Option" Variable="T3.GitRepo.CloneOrPull" <strong>Prompt="Global"</strong> Hint="If this is a first-time deployment, use Clone. If this is an update to an existing deployment, use Pull."&gt;

      &lt;Option Name="Clone" Value="clone" /&gt;

      &lt;Option Name="Pull" Value="pull" /&gt;

    &lt;/Parameter&gt;

  &lt;/Parameters&gt;

  &lt;Execution&gt;

    &lt;Mode&gt;Ssh&lt;/Mode&gt;

    &lt;Command&gt;install.sh ${T3.GitRepo.CloneOrPull} ${T3.GitRepo.URL} ${T3.GitRepo.LocalPath}&lt;/Command&gt;

    &lt;Persistent&gt;false&lt;/Persistent&gt;

  &lt;/Execution&gt;

&lt;/Manifest&gt;

</pre>
    </li>
    <li>Save this file as <code>package.manifest</code>.</li>
    <li>Create a ZIP file that contains the two files just created (<code>package.manifest</code> and <code>install.sh</code>) at the top level (not nested in a folder). Save this ZIP file as <code>package.zip</code>.</li>
  </ol>
  <li><strong>Upload the script to the control portal. </strong>(For details on creating script packages in general, refer to the article <a href="../Blueprints/blueprints-script-and-software-package-management.md">Blueprints Script and Software Package Management</a>.)</li>
  <ol>
    <li>Login to control portal and navigate to the Scripts page.
      <br /><img src="../images/blueprints-auto-app-deploy-2014-06-05-001-Scripts-Menu.png" alt="2014-06-05-001-Scripts-Menu.png" />
    </li>
    <li>Click on the "+ new script" button.
      <br /><img src="../images/blueprints-auto-app-deploy-2014-06-05-002-New-Script.png" alt="2014-06-05-002-New-Script.png" />
    </li>
    <li>Choose "Browser Upload" and then upload the <code>package.zip</code> file.
      <br /><img src="../images/blueprints-auto-app-deploy-2014-06-05-005-Upload-File.png" alt="2014-06-05-005-Upload-File.png" />
    </li>
    <li>Now publish the package by clicking the "publish" button next to the package name in the list of unpublished packages.
      <br /><img src="../images/blueprints-auto-app-deploy-2014-06-05-006-Publish.png" alt="2014-06-05-006-Publish.png" />
    </li>
    <li>Click the "next" button on the displayed information page and then select the desired attributes for the package. In this example, select "Scripts", "Linux" (selecting only RedHat Linux in this case) and finally "Private". Then click the "Publish"
      button.
      <br /><img src="../images/blueprints-auto-app-deploy-2014-06-05-008-Package-Details.png" alt="2014-06-05-008-Package-Details.png" />
    </li>
    <li>The package is queued for publishing. Once the publish operation is complete, it is a usable script. (You can click the "Details Page" link to check the status of the publish.)
      <br />
      <br /><img src="../images/blueprints-auto-app-deploy-publish-package.png" alt="publish-package.png" />
    </li>
  </ol>
  <li><strong>Execute script on [multiple] server(s) within a group. </strong>(Alternatively, you could create a Blueprint and use this Script as the last task of the build procedure.)</li>
  <ol>
    <li>From the group page, select "execute package" from the actions menu.</li>
    <li>Select the package you uploaded in the previous steps. It should be listed under "private" as seen here:
      <br /><img src="../images/blueprints-auto-app-deploy-exec-pkg-git.png" alt="exec-pkg-git.png" />
    </li>
    <li>Now enter the values for the parameters that were defined as the prompts indicate. First, the path to your Git repository, then the path to deploy the app to on the server, and finally whether you want to clone the repository, or just pull the latest
      code. The first time you deploy the app, you should choose "Clone" to set it up for the first time, but every time after, select "Pull" to simply update the code with the latest release.
      <br /><img src="../images/blueprints-auto-app-deploy-git-params.png" alt="git-params.png" />
      <br />
      <br />
    </li>
    <li>Finally, select the servers to execute the script on and click the "execute package" button.
      <br /><img src="../images/blueprints-auto-app-deploy-exec-pkg-git-select-servers.png" alt="exec-pkg-git-select-servers.png" />
    </li>
    <li>You will then be redirected to the Queue page to see the status of the running task. When it is completed, log on to one of the servers or load the application to confirm it has been updated.</li>
  </ol>
</ol>
