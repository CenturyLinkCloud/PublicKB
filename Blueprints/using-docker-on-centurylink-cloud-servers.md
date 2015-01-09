{{{
  "title": "Using Docker on CenturyLink Cloud Servers",
  "date": "10-14-2014",
  "author": "Bryan Friedman",
  "attachments": []
}}}

<h3>Description</h3>
<p><a href="http://www.docker.com" target="_blank">Docker</a> is open-source software for Linux that is used to deploy of applications inside software containers by providing an additional layer of abstraction of operating system–level virtualization. CenturyLink
  Cloud supports Docker on two traditional Linux distributions as well as on the newer, lightweight <a href="http://www.coreos.com" target="_blank">CoreOS</a> that is used specifically for deploying applications in Docker containers.&nbsp;CenturyLink
  Cloud also supports <a href="http://www.panamax.io" target="_blank">Panamax</a>, a web-based tool that makes it easy to deploy complex Docker applications through a drag-and-drop interface. (Read about <a href="https://t3n.zendesk.com/forums/20510978-Drafts/entries/%20https://t3n.zendesk.com/entries/47064274-Building-CoreOS-Server-Cluster-on-the-CenturyLink-Cloud"
  target="_blank">installing CoreOS or Panamax on CenturyLink Cloud</a>.)</p>
<h3>Steps</h3>
<p>The quickest way to get a single Linux server up and running with Docker is to use one of the provided Blueprints, either "Install Docker on CentOS" or "Install Docker on Ubuntu". Clicking on either of these blueprints and then clicking "deploy blueprint"
  will provision a server and install Docker for you. This process is outlined below. Alternatively, you could also provision your own Ubuntu 14 or CentOS 6 server and follow the steps for <a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups"
  target="_blank">executing a package on a server</a>, selecting&nbsp;the "Install Docker on Ubuntu" or "Install Docker on CentOS" package depending on your server type.</p>
<p>The steps provided below will work with either Ubuntu 14 or CentOS 6 versions of Linux. The example below shows Ubuntu 14, but the process is the same for CentOS 6. (Just replace the package or Blueprint name with "CentOS" instead of "Ubuntu".)</p>
<ol>
  <li>In the Control Portal, navigate to the Blueprints Library and search for "docker" to find the two available Blueprints.
    <br /><img src="https://t3n.zendesk.com/attachments/token/ikCg75nvFxom1Lw4TW8okDQGh/?name=docker-blueprints.png" alt="docker-blueprints.png" />
  </li>
  <li>Click on "Install Docker on Ubuntu", then click "deploy blueprint" to begin the installation.
    <br />
    <br />
  </li>
  <li>Now you will be presented with a page to input parameter values to specify details of the installation. Enter the required values for the server build (password, group, network, DNS, service level, and name). For the "Install Hello World Node Container"
    option, you may leave the default as "No" which will install Docker on the server but will not include any containers. If you select "Yes", the package will also install a sample container running a Node.js "Hello World" application on port 49160
    as an example container.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/jFvp5X8kjIJa9o3aHIZjyB8BX/?name=docker-params.png" alt="docker-params.png" />
  </li>
  <li>Click the "next: step 2" button, then "deploy blueprint" after reviewing the values. This should kick off a deployment job in your queue. Once the job has completed, the server will be created.
    <br /><img src="https://t3n.zendesk.com/attachments/token/LWkdbQ6qVERmdR6AvziasSFAP/?name=docker-queue-complete.png" alt="docker-queue-complete.png" />
    <br />
    <br />
  </li>
  <li>You should see the new server under the group you chose when deploying the blueprint. Here, we use our VPN connection and IP address to confirm the example container application is deployed.&nbsp;
    <br /><img src="https://t3n.zendesk.com/attachments/token/DK1k8B0hgZ7UFayDa0mYg22mO/?name=docker-server.png" alt="docker-server.png" /><img src="https://t3n.zendesk.com/attachments/token/ahnBnyo9ROmlE2ikBoGCuDgNf/?name=docker-hello-world.png" alt="docker-hello-world.png"
    />
  </li>
</ol>
