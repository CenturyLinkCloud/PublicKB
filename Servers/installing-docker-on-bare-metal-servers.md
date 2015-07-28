{{{
  "title": "Installing Docker on Bare Metal Servers",
  "date": "7-21-2015",
  "author": "Bryan Friedman",
  "attachments": [
    {
      "file_name": "Install Docker on RHEL/CentOS 6",
      "url": "../attachments/install-docker-centos6.sh",
      "type": "application/x-sh"
    }
  ],
  "contentIsHTML": false
}}}

### Description

[Docker](//www.docker.com) is open-source software for Linux that is used to deploy of applications inside software containers by providing an additional layer of abstraction of operating system–level virtualization. CenturyLink Cloud supports [Docker on virtual cloud servers](../Blueprints/using-docker-on-centurylink-cloud-servers.md) as well as on bare metal servers. The instructions for installing Docker on bare metal servers are listed below. A shell script that runs all the commands below is also attached for reference.

### Steps

1. Follow the instructions for [creating a new bare metal server](../Servers/creating-a-new-bare-metal-server.md) if you don't already have one. Make sure to select either CentOS 6 or RedHat Enterprise Linux 6 from the OS list. Both of these operating systems support Docker and all of the following steps will work the same on both distributions.

2. Log into the machine via SSH as the `root` user. (Make sure you are logged into your [VPN](../Network/how-to-configure-client-vpn.md) and connecting to the machine's private IP as it is not recommended to allow SSH over a public IP.)

        ssh root@{ip_address}

3. It is recommended to run a full update on the system to ensure that it is fully patched.

        yum -y update

4. Download the Docker RPM using `curl`.

        curl -O -sSL https://get.docker.com/rpm/1.7.1/centos-6/RPMS/x86_64/docker-engine-1.7.1-1.el6.x86_64.rpm

5. Install the package with `yum`.

        yum -y localinstall --nogpgcheck docker-engine-1.7.1-1.el6.x86_64.rpm

6. Start the Docker daemon with this command:

        service docker start

7. Run the `hello-world` container to test the `docker` command and confirm the installation was successful.

        docker run hello-world

8. To set Docker to start during system boot, run the following command:

        chkconfig docker on
