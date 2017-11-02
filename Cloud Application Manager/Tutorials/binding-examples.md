{{{ "title": "Binding Examples",
"date": "11-02-2017",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

Bindings glue together different parts of a multi-tier application over the network. These components can be parts of an application stack, a load balancing pool, cluster, and more. Bindings enable services to auto-discover and connect dynamically at scale. They also reconfigure the instances that need it to keep their configuration up to date.

**In this article:**

* Brief recap on Bindings
* A Simple Example
  * Create the NFS Server script boxes
    * Install Script
    * Configure Script
  * NFS client box
* Three Tiers application


### Brief recap on Bindings

Bindings are [variables](./parameterizing-boxes-with-variables.md) that you can add to boxes. They represent a connection from the deployed box to other instances. The detail explanation of Bindings can be found at this [knowledge article](./managing-multi-tier-applications.md).

### A Simple Example

The easiest way to understanding the function of Bindings is to put it to use.  This portion of the article will use Binding to establish a simple client server relation between to instances.  This article to walk through setting up a pair NFS server and client boxes with Bindings.

#### Creating the NFS Server script boxes
  Create the NFS server box in your workspace
  ![Create a new script box](../../images/cloud-application-manager/binding-example/binding-example-new-script.png)

  ![New Script Box](../../images/cloud-application-manager/binding-example/binding-example-new-script-box.png)

  ![NFS demo server](../../images/cloud-application-manager/binding-example/binding-example-nfs-demo-server.png)

  ##### Install script
  ```
  #!/bin/bash -e
  if [[ -e /etc/redhat-release || -e /etc/system-release ]]; then
    yum -y install nfs-utils nfs-utils-lib
    else
    export DEBIAN_FRONTEND=noninteractive
    apt-get update
    apt-get -y install nfs-kernel-server
  fi
  ```
  ##### Configure script
  ```
  #!/bin/bash -e
  mkdir -p {{ EXPORT_DIRECTORY }}
  echo {{ netmask.private }}
  # Configure etc/hosts
  sed  -i '/# BEGIN NFS CONFIGURATION/,/# END NFS CONFIGURATION/d' /etc/exports
  cat >> /etc/exports << \
  EXPORTS_CONFIG
  # BEGIN NFS CONFIGURATION
  {{ EXPORT_DIRECTORY }}  {{ EXPORT_HOST }}(rw,sync,no_root_squash,no_subtree_check)
  # END NFS CONFIGURATION
  EXPORTS_CONFIG
  if [[ -e /etc/redhat-release || -e /etc/system-release ]]
  then
    service rpcbind start
    service nfs start
  else
    service nfs-kernel-server restart
  fi
  echo "NFS Test OK" > /data/export2/NFS_test
  ```
  Add two varibales to the NFS server box (screenshots below). EXPORT_HOST for the network of the NFS clients and EXPORT_DIRECTORY is the directory of the file share.

  ![EXPORT_HOST variable](../../images/cloud-application-manager/binding-example/binding-example-variable-1.png)
  ![EXPORT_DIRECTORY variable](../../images/cloud-application-manager/binding-example/binding-example-variable-2.png)

 #### NFS client box
  ![New Script Box](../../images/cloud-application-manager/binding-example/binding-example-nfs-demo-client.png)
  Use the script below for install script:
  ```
  if [[ -e /etc/redhat-release || -e /etc/system-release ]]; then
    yum update -y
    yum -y install nfs-utils nfs-utils-lib
  else
    export DEBIAN_FRONTEND=noninteractive
    apt-get -y install nfs-kernel-server
  fi
  ```
  The configure script is as follow:
  ```
  #!/bin/bash
  {% if server %}
  if mount | grep {{ LOCAL_PATH }} > /dev/null; then
    echo "Folder already mounted"
  else
    mkdir -p {{ LOCAL_PATH }}
    mount {{ server.address.private }}:{{ server.EXPORT_DIRECTORY }} {{ LOCAL_PATH }}
  fi
  {% endif %}
  exit 0;
  ```
  Configure two new variables for this box, one is LOCAL_PATH for the mount point of the NFS client and the other one is the Binding variable.
  ![LOCAL_PATH variable](../../images/cloud-application-manager/binding-example/binding-example-nfsclient-variable-1.png)
  ![Binding](../../images/cloud-application-manager/binding-example/binding-example-nfsclient-variable-1.png)

  #### Application Box with NFS server and client
  Once the two script boxes are created, creation of the an application box would be the next step.
  To create an application box, click on "New" -> "Application Box", Enter "NFS Demo"
  Edit the newly created Application Box in Code section of the portal, Click on "New" and type "NFS demo" in the search window

  ![Application Box](..images/binding-example-application.png)
  ![Edit Topology](../../images/cloud-application-manager/binding-example/binding-example-edit-topology.png)

  Click on "NFS Demo Server" and add "nfsserver" tag to the box

  ![Add tag](../../images/cloud-application-manager/binding-example/binding-example-edit-topology-tag.png)

  Tagging bindings allow services to discover each other automatically. At deploy time, for the bindings defined in the boxes, we need to apply tags of instances to which they can bind. In this example, we ask the NFS client to bind to instances tagged as nfsserver.
  Repeat the process to add the "NFS Demo Client", on the Edit Box Topology, there should be a suggestion to the nfsserver binding.  Select 'nfsserver' and "Save".
  On the Topology page of the Application Box, you should be able to see the connectivity between the two boxes.

  ![Add binding](../../images/cloud-application-manager/binding-example/binding-example-edit-topology-nfsclient-tag.png)

  ![Binding](../../images/cloud-application-manager/binding-example/binding-example-binding.png)

#### Use of Parameters in Binding
  (Parameters in binding)[../../images/cloud-application-manager/binding-example/binding-example-binding-parameters.png]
  From the configure script, the nfsserver.address.private and nfsserver.EXPORT_DIRECTORY are passed from the nfsserver box to nfsclient box.
  This is a simple example and this can be used in a more complex environment, like the JBoss example that will be covered in the next section.


### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
