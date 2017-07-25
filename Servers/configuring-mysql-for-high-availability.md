{{{
  "title": "Configuring MySQL for High Availability",
  "date": "10-2-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description</strong></p>

<p>Simple scalability and easy elasticity are key benefits of any cloud environment, and along with features like self-service load balancer configurations and autoscaling, CenturyLink Cloud enables users to easily deploy applications with high-availability
  architectures. While this is especially true for most web applications, the database tier, particularly when it is a traditional relational database like MySQL, can often become the performance bottleneck or the single point of failure for many workloads
  because it can sometimes be a challenge to scale it out. While a vertical autoscale can help handle peak usage for performance, it doesn't cut it when you're looking for high availability from your relational database.</p>

<p><a href="http://dev.mysql.com/doc/refman/5.7/en/ha-overview.html">MySQL offers a number of high-availability configurations</a>, but perhaps the two most commonly implemented are <a href="#replication">Replication</a> and <a href="#clustering">Clustering</a>.
  In this article, we will explore both types of MySQL high-availability options and walkthrough the steps for deploying them on the CenturyLink Cloud.</p>

<p>
  <a name="replication"></a>
</p>
Replication

<p><a href="http://dev.mysql.com/doc/refman/5.7/en/replication.html">MySQL Replication</a>&nbsp;allows for data to be asynchronously copied from a "master" database to one or more "slave" database servers automatically as data in the master
  is updated. This means you can read data from any slave database server, but should only ever write to the master. There are many potential <a href="http://dev.mysql.com/doc/refman/5.7/en/replication-solutions.html">solutions</a> that
  can take advantage of this type of configuration. Perhaps you want to use the slaves as <a href="http://dev.mysql.com/doc/refman/5.7/en/replication-solutions-backups.html">database backups</a>, distribute some data to more <a href="http://dev.mysql.com/doc/refman/5.7/en/replication-solutions-partitioning.html"
  target="_self">geographically desirable locations</a> for certain user queries, or even use them as the connection points for read-only analytics applications so as not to affect performance of the master (be careful though, too many slaves can result
  in <a href="http://dev.mysql.com/doc/refman/5.7/en/replication-solutions-performance.html">performance degradation</a> of the master). In the case of a failover situation, if your master goes down, you can (manually) <a href="http://dev.mysql.com/doc/refman/5.7/en/replication-solutions-switch.html"
 >turn any slave into the master</a> and have the system back up in less time than it might take to rebuild from backups. And, of course, you may simply want to use them to <a href="http://dev.mysql.com/doc/refman/5.7/en/replication-solutions-scaleout.html"
 >scale out </a>your environment and spread your load across multiple servers as you might do on the web tier as well (remember though, the app can read from any slave, but it must always write to the master). Whatever the scenario you
  plan to use replication for, the below steps will walk you through getting MySQL master and slave instances up and running on the CenturyLink Cloud.</p>

<h3>Steps to Configure MySQL <em>Replication</em> on CenturyLink Cloud</h3>

<p>These steps describe the process to bring up one master and one slave, but you can repeat the steps to create the slave and deploy multiple ones if you wish. While there are many possible MySQL replication options (including the ability to replicate all
  databases, a specific database, or specific tables), the following outlines a good baseline to configure replication for a single database. You should consult the <a href="http://dev.mysql.com/doc/refman/5.7/en/replication.html">MySQL documentation</a>  for more details.</p>
<p>In this example, we will use Ubuntu 12 servers, but with the exception of using a different package manager/installation in the first few steps, this MySQL configuration will work on any system that supports MySQL replication.</p>

<div>
  <ol>
    <li><strong>Create Server (Master).</strong> Here we will use the Ubuntu 12 64-bit template.
      <br /><img src="https://t3n.zendesk.com/attachments/token/Yrw7HiEbIwxfVnoqJsRQWe6hm/?name=create-master.png" alt="create-master.png" /><img src="https://t3n.zendesk.com/attachments/token/EsMuteRIDJIxubJ4Kz7sMGMdu/?name=master-server-details.png" alt="master-server-details.png"
      />
    </li>
    <li><strong>Install MySQL.</strong> This will become the "master" server.
      <br />We will use the following script to install the MySQL package using Ubuntu's package manager. You could also create a <a href="https://t3n.zendesk.com/entries/20348448-Blueprints-Script-and-Software-Package-Management">blueprint script</a>      to do this, but since we are only installing on one server for now, we will logon to the server and run the commands manually.
      <pre>apt-get update<br />apt-get -y install mysql-server mysql-client</pre>
      <p>During the installation, you will be prompted to enter a password for the MySQL admin user, which you should not leave blank.</p>
    </li>
    <li><strong>Clone Server (Slave).</strong> Since we have a basic vanilla install of MySQL now, we will clone the master server before configuring it. This clone will become the "slave".
      <br /><img src="https://t3n.zendesk.com/attachments/token/Wv2S0jYsBM0ObeuBqWSPAE7jZ/?name=clone-master.png" alt="clone-master.png" /><img src="https://t3n.zendesk.com/attachments/token/v5p7PGjPYpIVFXjOfm4c499tF/?name=clone-master-form.png" alt="clone-master-form.png"
      />
    </li>
    <li><strong>Configure Master.<br /></strong>Log into the master server with SSH and perform the following steps:</li>
    <ol>
      <li><strong>Create database.</strong>
        <br />Login to the mysql client and use the <code>create database</code> command to create a database. In this example, we will use the name <code>my_database</code>.
        <br /><img src="https://t3n.zendesk.com/attachments/token/3mcNUvu9PNSnD8VwhOylmaqol/?name=create-database.png" alt="create-database.png" />
        <br />After creating the database, you can <code>quit</code> the mysql client for now.</li>
      <li><strong>Update config file.</strong>
        <br />You will need to edit the MySQL config file located at <code>/etc/mysql/my.cnf</code>&nbsp;.
        <pre>vi /etc/mysql/my.cnf</pre>
        <p>First, you need to find the line that says <code>bind-address = 127.0.0.1</code>&nbsp;and replace it with the IP of this server, which you can get from the control portal or by using the <code>ifconfig</code> command. Here's what ours will look
          like in this example:</p>
        <pre>bind-address = 10.126.32.14</pre>
        <p>Next, find the line that has the <code>server-id</code>, which will probably be commented out and set to a value of 1. Uncomment this line (remove the # character at the beginning of the line) and set the number to anything you want as long as
          it is unique among all masters and slaves. Here, we will leave it set to 1:</p>
        <pre>server-id = 1</pre>
        <p>Now we'll uncomment one more line relating to the <code>log_bin</code> file where the details of the replication are kept on the master:</p>
        <pre>log_bin = /var/log/mysql/mysql-bin.log</pre>
        <p>Finally, we set the <code>binlog_do_db</code> parameter to the database that we want to replicate, in this case the database we created in the first step above:</p>
        <pre>binlog_do_db = my_database</pre>
        <p>Then, all we have to do is restart mysql from the command prompt with <code>service mysql restart</code>:
          <br /><img src="https://t3n.zendesk.com/attachments/token/kpQvLNdAT1v0pJ8BP1twDJ7fP/?name=mysql-restart.png" alt="mysql-restart.png" />
        </p>
      </li>
      <li><strong>Grant privileges and get status.<br /></strong>Back in the mysql command line client, you will use the following command to grant privileges on the database to a user that the slave servers will use to read the data from the master. Here,
        you can use any password you want, but for this example, we will just use <code>password</code>:
        <br />
        <pre>GRANT REPLICATION SLAVE ON *.* TO 'slave_user'@'%' IDENTIFIED BY 'password';<br />FLUSH PRIVILEGES;</pre>
        <img src="https://t3n.zendesk.com/attachments/token/48VrGoW2P0pzXDJFIJrVTYJz8/?name=grant-privs.png" alt="grant-privs.png" />
        <br />
        <br />Now we need to get some information about the master database with the following command:
        <br />
        <pre>SHOW MASTER STATUS;</pre> This will show us a table that includes the position from which the slave database will start replicating. Take note of this information as we will need it later to configure the slave:
        <br /><img src="https://t3n.zendesk.com/attachments/token/AakQM6fhmYUg92eXPKnOkBqoe/?name=show-master.png" alt="show-master.png" />
      </li>
      <li><strong>Export database.<br /></strong>Back at the shell prompt, we'll use the <code>mysqldump</code> command to export the database.&nbsp;<em><em>Note: Since we just created this database, we don't actually have any data in it yet, but if we did, this step would ensure the slave starts with the same data the master already has.<br /></em></em>
        <pre>mysqldump -u root -p --opt my_database &gt; my_database.sql</pre>
      </li>
    </ol>
    <li><strong>Configure Slave.<br /></strong>Now we'll log into the slave server with SSH and perform the following steps:</li>
    <ol>
      <li><strong>Create database.</strong>
        <br />Same as before, login to the mysql client and use the&nbsp;<code>create database</code>&nbsp;command to create a database called <code>my_database</code>.
        <br /><img src="https://t3n.zendesk.com/attachments/token/3mcNUvu9PNSnD8VwhOylmaqol/?name=create-database.png" alt="create-database.png" />
      </li>
      <li><strong>Import database.<br /></strong>First, we need to retrieve the export file from the master server. We can use <code>scp</code> to do this:
        <br />
        <pre>scp root@10.126.32.14:~/my_database.sql .</pre>
        <p>Then we will import the database:</p>
        <pre>mysql -u root -p my_database &lt; my_database.sql</pre>
        <img src="https://t3n.zendesk.com/attachments/token/6yVqZGjj6rSCweHA6Rmh6pKu1/?name=import-master-db.png" alt="import-master-db.png" />
      </li>
      <li><strong>Update config file.<br /></strong>Next we update the configuration file in a similar way as we did on the master. We don't need to worry about the IP address in this case, but we need to set the <code>server-id</code> (to something other
        than 1), uncomment the <code>log_bin</code> line, and uncomment and set the <code>binlog_do_db</code> value:
        <br />
        <pre>server-id = 2</pre>
        <pre>log_bin = /var/log/mysql/mysql-bin.log</pre>
        <pre>binlog_do_db = my_database</pre> We also need to add one more line that isn't in the file by default:
        <br />
        <pre>relay-log               = /var/log/mysql/mysql-relay-bin.log</pre> A MySQL restart is required to apply the changes:
        <br /><img src="https://t3n.zendesk.com/attachments/token/kpQvLNdAT1v0pJ8BP1twDJ7fP/?name=mysql-restart.png" alt="mysql-restart.png" />
      </li>
      <li><strong>Start slave.<br /></strong>Now we need that information from the master server that we took down. From the mysql client on the slave, we'll enter the following command based on the IP address of the master and the information we got from
        before, and then start the slave:
        <br />
        <pre>CHANGE MASTER TO MASTER_HOST='10.126.32.14',MASTER_USER='slave_user',MASTER_PASSWORD='password',MASTER_LOG_FILE='mysql-bin.000001',MASTER_LOG_POS=557;<br /><br />START SLAVE;</pre>
        <img src="https://t3n.zendesk.com/attachments/token/5VuLsu2FQ3FhT5ZHLOx8VlWBN/?name=start-slave.png" alt="start-slave.png" />
      </li>
    </ol>
    <li><strong>Confirm data replication.<br /></strong>You can test the setup by inserting data into a table on the master, then querying the slave to ensure the data is replicated correctly.</li>
    <li><em>(Optional)</em> Repeat steps 4 and 6 for each additional slave.</li>
  </ol>
  <a name="clustering"></a>
  Cluster
  <p><a href="http://dev.mysql.com/doc/refman/5.6/en/mysql-cluster-overview.html">MySQL Clustering</a> provides an option that is designed not to have any single point of failure. It enables clustering utilizing a shared-nothing architecture,
    meaning it works well with minimally specced hardware, each with its own memory and disk. MySQL Cluster combines the standard MySQL server with an in-memory clustered storage engine called NDB (Network DataBase), and so it sometimes referred to as
    an NDB cluster.&nbsp;A MySQL Cluster consists of multiple nodes of different types,&nbsp;including MySQL servers (for access to NDB data), data nodes (for storage of the data), and one or more management servers. All data in an NDB cluster&nbsp;is
    stored in the data nodes and the tables are directly accessible from all other SQL nodes in the cluster. This differs from the replication methodology in that there is no master-slave relationship - all data nodes contain copies of the data, but you
    can read or write to the tables using any of the SQL nodes in the cluster. The following steps will walk you through getting MySQL Cluster installed, configured, and started up on the CenturyLink Cloud.</p>
  <h3>Steps to Configure MySQL <em>Cluster</em> on CenturyLink Cloud</h3>
  <p>These steps describe the process to bring up one management (ndb_mgmd) node, one SQL (mysqld) node, and two data (ndbd) nodes. This is the absolute minimum required number of servers for a cluster to work. It is highly recommended to create multiple
    SQL nodes (following the same steps listed below for the SQL node), and additional data nodes as needed, and it is even possible to set up multiple management nodes (though this is less critical since a cluster can function for some time without the
    ndb_mgmd node being up). There are plenty of configuration options as well as <a href="http://dev.mysql.com/doc/refman/5.6/en/mysql-cluster-limitations.html">some limitations</a> to using clustering, so the <a href="http://dev.mysql.com/doc/refman/5.6/en/mysql-cluster.html"
   >MySQL documentation</a> can be consulted for more information.</p>
  <p>In this example, we will use RedHat Enterprise Linux 6 servers, but with the exception of using a different package manager/binary installation in the second step, this MySQL configuration will work on any system that supports MySQL clusters. (More
    information in the <a href="http://dev.mysql.com/doc/refman/5.6/en/mysql-cluster-installation.html">MySQL documentation</a>.)</p>
  <ol>
    <li><strong>Create Server (Management).</strong> Here we will use the RedHat Enterprise Linux 6 template.</li>
    <li><strong>Install MySQL cluster binary.</strong> This will become the "management node" (ndb_mgmd).
      <br />For clustered versions of MySQL, unfortunately we cannot use the regular binaries that come from our public Linux package manager libraries, so we'll have to download the binary from Oracle's site and then copy it on to our server for installation.
      We can find the binaries available at&nbsp;<a href="http://dev.mysql.com/downloads/cluster/">http://dev.mysql.com/downloads/cluster/</a>&nbsp;where for this example we will select and download the&nbsp;<em>MySQL-Cluster-server-gpl-7.3.6-2.el6.x86_64.rpm</em>      package for Red Hat Linux. (For instructions on other operating systems, refer to the <a href="http://dev.mysql.com/doc/refman/5.6/en/mysql-cluster-installation.html">MySQL manual</a>.) Once downloaded, we can use <code>scp</code>      (or another file transfer tool) to copy the file onto the server.
      <br /><img src="https://t3n.zendesk.com/attachments/token/491wL9Gleycg9Y7teloVDzm0M/?name=scp-mysql-binary.png" alt="scp-mysql-binary.png" />
      <br />
      <br />Once it's there, we'll login to the server with SSH, change to the directory where it's located, and run the following commands to get it installed. The first command ensures we won't have any version conflicts, and the second command installs the
      package.
      <br />
      <pre>yum -y remove mysql-libs</pre>
    </li>
    <li>
      <pre>rpm -Uhv MySQL-Cluster-server-gpl-7.3.6-2.el6.x86_64.rpm</pre>
    </li>
    <li><strong>Clone Server (Data 1).&nbsp;</strong>Since we have MySQL installed already, we will clone the server before configuring it. This clone will become a data (ndbd) node.</li>
    <li><strong>Clone Server (Data 2).&nbsp;</strong>This clone will become another data (ndbd) node.</li>
    <li><strong>Clone Server (SQL)</strong>.<strong>&nbsp;</strong>This clone will become the SQL (mysqld) node.</li>
    <li><strong>Configure SQL Node and Data Nodes.<br /></strong>Now that we have all of the servers we will use with the software installed, it's time to configure each one. We'll start with the SQL and data nodes, which will have identical configurations.
      Begin by editing the MySQL configuration file located at <code>/etc/my.cnf</code>&nbsp;(if it's not there it should be created). You can use <code>vi</code>&nbsp;(or any editor of your choice) and make sure it looks like the following:
      <br />
      <pre>[mysqld]

# Options for mysqld process:

ndbcluster                      # run NDB storage engine



[mysql_cluster]

# Options for MySQL Cluster processes:

ndb-connectstring=10.71.9.12  # location of management server</pre> This file should be the same for all data and SQL nodes, so be sure to edit and save the file as above on all three of these servers in our cluster.
      <br />Now, on the data nodes only, we will need to create the directory <code>/usr/local/mysql/data</code>, which we can do with the following commands:
      <br />
      <pre>mkdir /usr/local/mysql<br />mkdir /usr/local/mysql/data</pre>
      <p>Once this is complete, we're ready to move on to configuring the management node.</p>
    </li>
    <li><strong><strong>Configure Management Node.<br /></strong></strong>We will start by creating the directory <code>/var/lib/mysql-cluster</code> and then creating a <code>config.ini</code> file in it:
      <pre>mkdir /var/lib/mysql-cluster

cd /var/lib/mysql-cluster

vi config.ini

</pre>
      <p>(Again, you can use any editor you want, here we are using <code>vi</code>.) The file should contain the following:</p>
      <pre>[ndbd default]

# Options affecting ndbd processes on all data nodes:

NoOfReplicas=2    # Number of replicas

DataMemory=80M    # How much memory to allocate for data storage

IndexMemory=18M   # How much memory to allocate for index storage

                  # For DataMemory and IndexMemory, we have used the

                  # default values. Since the "world" database takes up

                  # only about 500KB, this should be more than enough for

                  # this example Cluster setup.



[tcp default]

# TCP/IP options:

portnumber=2202   # This the default; however, you can use any

                  # port that is free for all the hosts in the cluster

                  # Note: It is recommended that you do not specify the port

                  # number at all and simply allow the default value to be used

                  # instead



[ndb_mgmd]

# Management process options:

hostname=10.71.9.12             # Hostname or IP address of MGM node

datadir=/var/lib/mysql-cluster  # Directory for MGM node log files



[ndbd]

# Options for data node "A":

                                # (one [ndbd] section per data node)

hostname=10.71.9.13             # Hostname or IP address

datadir=/usr/local/mysql/data   # Directory for this data node's data files



[ndbd]

# Options for data node "B":

hostname=10.71.9.14             # Hostname or IP address

datadir=/usr/local/mysql/data   # Directory for this data node's data files



[mysqld]

# SQL node options:

hostname=10.71.9.15             # Hostname or IP address

                                # (additional mysqld connections can be

                                # specified for this node for various

                                # purposes such as running ndb_restore)</pre> (These are the minimum settings required for the cluster to work. For more options, you may consult the <a href="http://dev.mysql.com/doc/refman/5.6/en/mysql-cluster-config-file.html"
     >MySQL documentation</a>.) Once this file is saved, we're ready to startup the cluster.</li>
    <li><strong>Startup the Cluster.&nbsp;</strong>Order matters here, so follow these steps closely.</li>
    <ol>
      <li><strong>Start the management node.<br /></strong>Logon to the management node server and&nbsp;issue the following command to start the management node process:
        <pre>ndb_mgmd -f /var/lib/mysql-cluster/config.ini</pre>
      </li>
      <li><strong>Start the data nodes.<br /></strong>Logon to each of the data nodes and issue the following command to start them up:
        <pre>ndbd</pre>
      </li>
      <li><strong>Start the SQL node.<br /></strong>Logon to the SQL node and issue the following command to start the <code>mysqld</code> process:
        <br />
        <pre>service mysql start</pre>
      </li>
      <li><strong>Confirm successful startup.<br /></strong>From the management node server, you can issue the <code>ndb_mgm</code> command to start the management client. From this prompt, type <code>SHOW</code> to confirm all the nodes are up and running
        successfully. You can use this command at any time to investigate the health of the cluster.
        <br />
        <br /><img src="https://t3n.zendesk.com/attachments/token/4GMLUwPbdBvlIffrc93o1yr7O/?name=ndb_mgm_show.png" alt="ndb_mgm_show.png" />
      </li>
    </ol>
    <li><strong>Create database and tables.<br /></strong>Now that you have a cluster up and running, you can use it for high-availability databases. You can logon to the SQL node with any MySQL client and create a database. If you want the tables in this
      database to use clustering, you&nbsp;<em>must</em> use&nbsp;<code>engine=NDBCLUSTER</code>&nbsp;at the end of each create statement when creating tables. (Most SQL scripts exported from a MySQL database will use the InnoDB engine, so you can often
      to a find and replace of InnoDB with NDBCLUSTER to convert your scripts to be usable by a cluster.)</li>
    <li><strong>Confirm data access when one node goes down.</strong>&nbsp;
      <br />You can test your cluster by reading and writing data to a table while one of the data nodes is down.&nbsp;Of course, with this configuration, the one SQL node is a single point of failure. As such, it is recommended to setup additional SQL nodes
      to allow for failover or load balancing.</li>
    <li><em>(Optional)</em>&nbsp;Repeat above steps as needed to set up additional nodes of any type.</li>
  </ol>
  <p>Finally, if you want to get really fancy, you can even combine the above methods and use Cluster Replication to replicate a master cluster to slave clusters. Consult the <a href="http://dev.mysql.com/doc/refman/5.6/en/mysql-cluster-replication.html"
   >MySQL manual</a> for more on this.</p>
</div>