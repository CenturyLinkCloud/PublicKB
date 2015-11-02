#!/bin/bash

yum -y update
curl -O -sSL https://get.docker.com/rpm/1.7.1/centos-6/RPMS/x86_64/docker-engine-1.7.1-1.el6.x86_64.rpm
yum -y localinstall --nogpgcheck docker-engine-1.7.1-1.el6.x86_64.rpm
service docker start
docker run hello-world
chkconfig docker on
