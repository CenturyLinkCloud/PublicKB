{{{
  "title": "Getting started with Minecraft Server Blueprint",
  "date": "3-31-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![Mojang logo](https://bugs.mojang.com/secure/attachment/50315/cnJMfJh.png)
### Technology Profile
Mojang is a Microsoft owned game developer studio based in Stockholm, Sweden. They develop a game called Minecraft.  

Minecraft is a sandbox construction game where you can build anything you can imagine. Minecraft is a game about breaking and placing blocks. In "Survival Mode", people built structures to protect against nocturnal monsters, but also offers "Creative Mode" allowing players to work together to create wonderful, imaginative things.

For more information, please view http://www.Minecraft.com

### Description
CenturyLink has created a Blueprint that makes it extremely easy to spin up a private Minecraft Server in minutes.  You can start using your Minecraft server immediately after the Blueprint completes.  The Blueprint will automatically install and configure Minecraft Server 1.8.3.  

Advantages of running Minecraft Server in CenturyLink Cloud:
* Fast provisioning - get a Minecraft server running within minutes- No long term server commitment - pay as you go each month
* On-demand Scalability - Add more CPU, Disk or Memory resources on the fly as your worlds grow
* Save money - Run your Minecraft server only when you use it.  You can host a server just in the evenings or weekends with your friends and not have to pay to run it 24/7 unless you chose to.  You can use the CenturyLink Cloud mobile app to start and stop your Minecraft server any time, any where.  
* Fast Bandwidth - Your Minecraft server has a 2GB inbound network throughput ensuring low latency game play.
* Easy backups - You can easily save your worlds anytime you choose, but we've also included an automatic backup in the configuration
* Customizable - Customize your Minecraft server by installing any mods you want!
* No technical experience required - Don't worry about setting up the VM and software dependencies, we did that for you.  Just run the blueprint and start playing.
* Parental Control - Control where your family plays and who they play with by having ownership of the server.
* Secure - CenturyLink Cloud includes network security and allows you to block users from connecting to your server at a network level in addition to game whitelists.

### Audience
CenturyLink Cloud Users, Creepers and Minecrafters

### Impact
After reading this article, the user should feel comfortable getting started using the Minecraft Server Blueprint technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
- Allow incoming traffic for ports 25565 so users can play on your Minecraft server.  To open the firewall port, Navigate to the server in Control and click on the Public IP address.  Then add a new rule for a specific port and enter 25565.  Hit Add when done so the changes are saved.  

- Customize your Minecraft Server by editing the Minecraft server.properties file in /minecraft-server

### Install Minecraft Server on Linux Blueprint
1. Locate the Mojang Minecraft Server Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Minecraft” in the keyword search on the right side of the page.
  3. Locate the 'Install Minecraft Server on Linux' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Minecraft Server on Linux” Blueprint.

3. Configure the Blueprint using the standard information.  There is nothing special required.

4. Review and Confirm the Blueprint.
  1. Click “next: step 2”
  2. Verify your configuration details.

5. Deploy the Blueprint.
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the Minecraft Server until you have received this email notification.

### Access your Minecraft server
After your Blueprint deploys successfully, please follow these instructions to access your server:
  1. Check your email to obtain Server Name and IP Address Login information
  2. Click on the link to the server and then add a firewall port as referenced in the postrequisite section
  3. SSH to your Minecraft Server's Public IP and login as the user minecraft with password Minecraft123 to customize your Minecraft server.
  4. Connect to your Minecraft Java console by running this command as the minecraft user: screen -r
  5. To disconnect from the java console: press "CTRL A + Z" (A then Z).
  6. To stop the server, login to the console and shut it down.  If you are not sure how to do that, consult the Minecraft documentation.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Mojang or Microsoft license costs or additional fees bundled in.

### Frequently Asked Questions

#### What does the Blueprint do?
1. Provision a VM with 2CPU and 8GB of RAM
2. Install Ubuntu 14 Linux x64
3. Add 20GB of Storage and mount it as /minecraft-server.  Note: You can grow storage on-demand.
4. Add a Public IP and open firewall ports 22
5. Run the 'Install Minecraft Server on Linux x64' Script Package

#### What does the 'Install Minecraft Server on Linux x64' Script Package do?
1. Add a user called minecraft intended to run the Minecraft Server java software
2. Create the necessary directories in /minecraft-server  (This is where all of the Minecraft Server software resides)
3. Install the Minecraft Server startup scripts: /etc/init.d/mincraft and /minecraft-server/minecraft-init/config
4. Install entries to the minecraft users crontab to schedule Minecraft backups 
5. Install JAVA 7 and all the dependencies
6. Downloading Minecraft Server 1.8.3 jar from Mojang
7. Accept the Minecraft Server EULA
8. Set permissions for Minecraft Server to run as minecraft user
9. Start Minecraft Server as minecraft user.  By default the Minecraft server is set to run with a minimum memory usage of 2GB and maximum of 7GB and will start a Survival Mode game.

#### Where can I get more information on the minecraft-init?
* For more information view https://github.com/Ahtenus/minecraft-init

#### How do I customize my Minecraft server?
* Please view this documentation: http://minecraft.gamepedia.com/Server.properties

#### Who should I contact for support?
* CenturyLink Cloud does not support the Minecraft Server software.  Please contact Mojang for any support around Minecraft.
* For issues related to cloud infrastructure (VM’s, network, etc), or is you experience a problem deploying the Blueprint, please open a CenturyLink Cloud Support ticket: https://t3n.zendesk.com/tickets/new
