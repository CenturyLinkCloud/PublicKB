{{{
  "title": "Getting Started with Kubernetes - Ansible",
  "date": "2-01-2016",
  "author": "Chris Kleban",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](http://kubernetes.io/img/desktop/nav_logo.svg)

### Technology Profile
Kubernetes is an open source orchestration system for Docker containers. It handles scheduling onto nodes in a compute cluster and actively manages workloads to ensure that their state matches the users declared intentions. Using the concepts of "labels" and "pods", it groups the containers which make up an application into logical units for easy management and discovery. Source: Kubernetes.io

For more information, please view http://www.kubernetes.io


### Description
By using our Ansible scripts, customers can create a Kubernetes cluster on CenturyLink Cloud infrastruture by running a single script. 

To see the source code of our Kubernetes Cluster Creation Ansible scripts, please visit our github repo: https://github.com/CenturyLinkCloud/adm-kubernetes-on-clc


### Audience
CenturyLink Cloud Users, Developers, Operations, System Engineers, Architects 

### Impact
After following the instructions this article, the user should have a working kubernetes cluster on CenturyLink. 

### Clusters of VMs or Physical Servers, your choice.

- We support Kubernetes clusters on both Virtual Machines or Physical Servers. If you want to use physical servers for the worker nodes (minions), simple use the --minion_type=bareMetal flag.
- For more information on pyhsical servers, visit: https://www.ctl.io/bare-metal/)
- Physical serves are only available in the VA1 and GB3 data centers.
- VMs are available in all 13 of our public cloud locations


### Requirements

The following requirements are needed in order to use these scripts to install Kubernetes on CenturyLink Cloud. 

- A CenturyLink Cloud account 
- VPN access established to your Centurylink data-center

And 

- A linux host with the following items installed:
- ansible _version 2.0_ or newer.  
- python 
- pip
- git

### Script Installation

After you have all the requirements met, please follow these instructions to install this script. 

1) Clone this repository and cd into it.
``` 
git clone https://github.com/CenturyLinkCloud/adm-kubernetes-on-clc 
```

2) Install the CenturyLink Cloud SDK and Ansible Modules
```
sudo pip install -r requirements.txt
```

3) Create the credentials file from the template and use it to set your ENV variables

``` 
cp ansible/credentials.sh.template ansible/credentials.sh
vi ansible/credentials.sh
source ansible/credentials.sh
```

#### Ubuntu 14  Walkthrough: Installation of Requirements and Scripts

If you use ubuntu 14, for your convenouce we have provided a step by step guide to install the requirements and install the script.

```
  # system
  apt-get update
  apt-get install -y git python python-crypto
  curl -O https://bootstrap.pypa.io/get-pip.py
  python get-pip.py

  # installing this repository
  mkdir -p ~home/k8s-on-clc
  cd ~home/k8s-on-clc
  git clone https://github.com/CenturyLinkCloud/adm-kubernetes-on-clc.git
  cd adm-kubernetes-on-clc/
  pip install -r requirements.txt

  # getting started
  cd ansible
  cp credentials.sh.template credentials.sh; vi credentials.sh
  source credentials.sh
```

### Cluster Creation 

To create a new Kubernetes cluster, simply run the kube-up.sh script. A complete list of script options and some examples are listed below.

``` 
cd ./adm-kubernetes-on-clc/ansible
bash kube-up.sh
```

#### Script Options
```
Usage: kube-up.sh [OPTIONS]
Create servers in the CenturyLinkCloud environment and initialize a Kubernetes cluster
Environment variables CLC_V2_API_USERNAME and CLC_V2_API_PASSWD must be set in
order to access the CenturyLinkCloud API

All options (both short and long form) require arguments, and must include "="
between option name and option value.

     -h (--help)                   display this help and exit
     -c= (--clc_cluster_name=)     set the name of the cluster, as used in CLC group names
     -t= (--minion_type=)          standard -> VM (default), bareMetal -> physical]
     -d= (--datacenter=)           VA1 (default)
     -m= (--minion_count=)         number of kubernetes minion nodes
     -mem= (--vm_memory=)          number of GB ram for each minion
     -cpu= (--vm_cpu=)             number of virtual cps for each minion node
     -phyid= (--server_conf_id=)   physical server configuration id, one of
                                      physical_server_20_core_conf_id
                                      physical_server_12_core_conf_id
                                      physical_server_4_core_conf_id (default)
     -etcd_separate_cluster=yes    create a separate cluster of three etcd nodes,
                                   otherwise run etcd on the master node
```
#### Script Examples

Create a cluster with name of k8s_1, 1 master node and 3 worker minions (on physical machines), in VA1

```
 bash kube-up.sh --clc_cluster_name=k8s_1 --minion_type=bareMetal --minion_count=3 --datacenter=VA1
```
Create a cluster with name of k8s_2, an ha etcd cluster on 3 VMs and 6 worker minions (on VMs), in VA1

```
 bash kube-up.sh --clc_cluster_name=k8s_2 --minion_type=standard --minion_count=6 --datacenter=VA1 --etcd_separate_cluster=yes
```
Create a cluster with name of k8s_3, 1 master node, and 10 worker minions (on VMs) with higher mem/cpu, in UC1:


```
  bash kube-up.sh --clc_cluster_name=k8s_3 --minion_type=standard --minion_count=10 --datacenter=VA1 -mem=6 -cpu=4
```

### Cluster Deletion

To delete a cluster, log into the CenturyLink Cloud control portal and delete the parent server group that contains the Kubernetes Cluster. We hope to add a scripted option to do this soon. 


### What Kubernetes features do not work on CenturyLink Cloud

- At this time, there is no support services of the type 'loadbalancer'. We are actively working on this and hope to publish the changes soon. 
- At this time, there is no support for persistent storage volumes provided by CenturyLink Cloud. However, customers can bring their pwn persistent storage offering.



### Postrequisite

#### Kubernetes  Access
You will need the kubectl client program to manage your kubernetes cluster. You can access this by one of two ways:

- The master server has this installed. SSH to the master server and run kubectl from there. 
- Use your local machine (or some remote machine to the cluster)

#### Network access to the cluster
- Network access from a remote box to the master can be achieved by using the VPN access that you needed in the previous step or by adding a public IP address to the master server. 


### Kubernetes Usage

#### How to access the kubernetes UI 

Goto the following url in a web browser that has access to the master server:

http://(IP-ADDRESS-OF-MASTER-SERVER):8080/api/v1/proxy/namespaces/kube-system/services/kube-ui

#### How to use the kubectl client

To get your Kubernetes cluster's information:

``` 
kubectl -s http://(IP-ADDRESS-OF-MASTER-SERVER):8080 cluster-info 
```

To get the list of nodes in your Kubernetes clusters :

``` 
kubectl -s http://(IP-ADDRESS-OF-MASTER-SERVER):8080 get nodes 
```

To run 2 copies of nginx on your cluster:

``` 
kubectl -s http://(IP-ADDRESS-OF-MASTER-SERVER):8080 run my-nginx --image=nginx --replicas=2 --port=80 
```


For more information on how to use the kubectl client, please visit: 

### Pricing
The costs associated with running Kubernetes from the ansible scripts are for the CenturyLink Cloud infrastructure only.  There are no Kubernetes  license costs or additional fees bundled in.



### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to creating the Kubernetes cluster, please email kubernetes@ctl.io or create a support ticket. 
* For issues related to cloud infrastructure (VM’s, network, etc), please open a CenturyLink Cloud Support ticket: https://t3n.zendesk.com/tickets/new
* For more information on using Kubernetes, please visit http://kubernetes.io/v1.1/

