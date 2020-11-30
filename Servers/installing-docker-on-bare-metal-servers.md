{{{
  "title": "Installing Docker on Bare Metal Servers",
  "date": "8-12-2015",
  "author": "Bryan Friedman",
  "attachments": [
    {
      "file_name": "Install Docker on Bare Metal - RHEL/CentOS 6",
      "url": "../attachments/install-docker-centos6.sh",
      "type": "application/x-sh"
    }
  ],
  "contentIsHTML": false
}}}

### Description

[Docker](//www.docker.com) is open-source software for Linux that is used to deploy applications inside software containers by providing an additional layer of abstraction within the operating system–level virtualization. Lumen Cloud supports [Docker on virtual cloud servers](../Blueprints/using-docker-on-centurylink-cloud-servers.md) as well as on bare metal servers. The instructions for installing Docker on bare metal servers are listed below. A shell script that runs all the commands below is also attached for reference.

### Prerequisite

- Follow the instructions for [creating a new bare metal server](../Servers/creating-a-new-bare-metal-server.md) if you don't already have one. Make sure to select CentOS 6, RedHat Enterprise Linux 6, or Ubuntu 14 from the OS list. Any of these operating systems support Docker. Depending on the OS you choose, follow the instructions below for installing Docker on CentOS 6/Red Hat 6 or on Ubuntu 14.

### Steps

#### Ubuntu 14

1. Run the following command to install Docker. This will download and install the latest version and configure it to start during system boot.

        curl -sSL https://get.docker.com/ | sh  

2. Run the `hello-world` container to test the `docker` command and confirm the installation was successful.

        docker run hello-world

#### CentOS 6 and Red Hat 6

1. Log into the machine via SSH as the `root` user. (Make sure you are logged into your [VPN](../Network/CenturyLink Cloud/how-to-configure-client-vpn.md) and connecting to the machine's private IP as it is not recommended to allow SSH over a public IP.)

        ssh root@{ip_address}

2. It is recommended to run a full update on the system to ensure that it is fully patched.

        yum -y update

3. Download the Docker RPM using `curl`.

        curl -O -sSL https://get.docker.com/rpm/1.7.1/centos-6/RPMS/x86_64/docker-engine-1.7.1-1.el6.x86_64.rpm

4. Install the package with `yum`.

        yum -y localinstall --nogpgcheck docker-engine-1.7.1-1.el6.x86_64.rpm

5. Start the Docker daemon with this command:

        service docker start

6. Run the `hello-world` container to test the `docker` command and confirm the installation was successful.

        docker run hello-world

7. To set Docker to start during system boot, run the following command:

        chkconfig docker on
