{{{
"title": "Using a STONITH Fencing Agent with CenturyLink Cloud",
"date": "04-30-2020",
"author": "Clinton Popovich",
"keywords": ["High availability", "Pacemaker", "Apache", "Postgres"],
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* [Audience](#audience)
* [Technical Level](#technical-level)
* [Overview](#overview)
* [Requirements](#requirements)
* [Adding a Fence to Pacemaker and Corosync](#adding-a-fence-to-pacemaker-and-corosync)

### Audience

System Admins and highly technical users of CenturyLink Cloud.

### Technical Level

Highly technical. Targeted at a systems administrator or advanced developer.

### Overview

STONITH ("Shoot The Other Node In The Head" or "Shoot The Offending Node In The Head”) is a technique for node level fencing in computer clusters.

Fencing isolates a failed node so that it doesn’t disrupt a cluster. STONITH maintains the integrity of nodes in a high-availability (HA) cluster by resetting or powering down the failed node. An unresponsive node can still access your data, so the only way to be 100% certain data is safe is to fence the failed node so it's completely offline.

An administrator might employ STONITH if one of the nodes in a cluster can’t be reached by the other node(s) in the cluster, or if two nodes try to write to a shared storage resource. STONITH provides effective protection against multi-node error-prone contention, which can create catastrophic problems.

Single node systems use a comparable mechanism called a watchdog timer. A watchdog timer will reset the node if the node does not tell the watchdog circuit it is operating well. A STONITH decision can be based on various decisions which can be customer specific plugins.

This article outlines the steps taken to implement STONITH and provide node level fencing.

### Requirements

The following must be installed in order for this process to work:

•	[PyCurl](http://pycurl.io/) for Python

•	[Pacemaker 1.1.18](https://clusterlabs.org/pacemaker/) (or higher)

•	[Corosync Cluster Engine](http://corosync.github.io/corosync/), version '1.4.7' (or higher)

•	[fence-agents.x86_64](https://access.redhat.com/solutions/917833): Fence Agents for Red Hat Cluster (our agent builds off the libraries found in this RPM)

It has onboard help if you use the -h argument:

``[ab77613@uc1ctovipgsql01 ~]$ /usr/sbin/fence_clc -h``

**Usage: fence_clc [options]**

**Options:**

-l, --username=[name]          Login name

-p, --password=[password]      Login password or passphrase

-y, --account=<CLC account>    CLC account

-x, --proxy=http://<ip>:<port> Proxy URL

-s, --switch=[id]              Physical switch number on device

-o, --action=[action]          Action: status, reboot (default), off or on

-S, --password-script=[script] Script to run to retrieve password

-v, --verbose                  Verbose mode

-D, --debug-file=[debugfile]   Debugging to output file

-V, --version                  Output version information and exit

-h, --help                     Display this help and exit

--shell-timeout=[seconds]      Wait X seconds for cmd prompt after issuing command

--power-wait=[seconds]         Wait X seconds after issuing ON/OFF

--power-timeout=[seconds]      Test X seconds for status change after ON/OFF

--delay=[seconds]              Wait X seconds before fencing is started

--login-timeout=[seconds]      Wait X seconds for cmd prompt after login

--retry-on=[attempts]          Count of attempts to retry power on

The STONITH and fencing terms are often used interchangeably here as well as in other texts.

The STONITH subsystem consists of two components:

•	Pacemaker-fenced

•	STONITH plugins

This STONITH agent can be used with anything [Pacemaker/Corosync](https://clusterlabs.org/pacemaker/doc/) can provide high-availability.

Pacemaker-fenced is a daemon that runs on every node in the cluster and can be accessed by the local processes or over the network. It accepts commands which correspond to fencing operations: ``reset``, ``power-off``, and ``power-on``. It may also check the status of the fencing device. When the pacemaker-fenced instance receives a fencing request, it's up to this and other pacemaker-fenced programs to carry out the desired fencing operation.

For every supported fencing device there is a STONITH plugin that's capable of controlling that device. A STONITH plugin is the interface to the fencing device. All STONITH plugins look the same to pacemaker-fenced, but are very different on the other side reflecting the nature of the fencing device.

Some plugins can support more than one device. For example, [ipmilan](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/fence_configuration_guide/s1-software-fence-ipmi-ca) (or external/ipmi) implements the IPMI protocol and can control any device that supports it.

### Adding a Fence to Pacemaker and Corosync

1)	Install Pacemaker/Corosync & other dependencies (for HA setup)

    ``yum install -y corosync pacemaker resource-agents pcs pcsd cman fence-agents-virsh``

2)	Make sure fence-agents.x86_64 is installed from CentOS yum repo (this is the only real dependency for fence_clc)

    ``yum install fence-agents``

3)	Install PyCurl

    ``yum install python-pycurl``

4)	Copy fence_clc to /usr/sbin/

    ``#cp fence_clc /usr/sbin/``

If this has been correctly installed, running ``pcs stonith list`` will show ``fence_clc``

5)	Create the fence

    ``pcs stonith create <name of fence>  fence_clc pcmk_host_check="static-list" pcmk_host_list="<SINGLE VM NAME HERE>" account="<CLC ACCOUNT>" login="<USER IN YOUR CLC ACCOUNT>" passwd="<PASSWORD FOR LOGIN USER>" proxy="<PROXY IF NEEDED>" switch="<VM YOU ARE CONTROLING IN CLC>"``

This fencing agent was tested using [Red Hat High Availability Add-On Configuration and Management Reference Overview](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/high_availability_add-on_reference/ch-overview-haar) for reference.

**The following agent has been tested on CLC:**

  ```
  import sys, re
  import time
  import atexit
  import pycurl, json, StringIO
  sys.path.append("/usr/share/fence")
  from fencing import *
  from fencing import fail_usage

  #BEGIN_VERSION_GENERATION
  RELEASE_VERSION="0.0.02"
  BUILD_DATE="(built Wed Mar 09 04:41:47 EST 2020)"
  #END_VERSION_GENERATION

  def curl(URL, data, options, token):
    ret = StringIO.StringIO()
    crl = pycurl.Curl()
    crl.setopt(pycurl.URL, URL)
    if (len(options["--proxy"]) > 0):
      crl.setopt(pycurl.PROXY, options["--proxy"])
    crl.setopt(pycurl.HTTPHEADER, ['Authorization:Bearer ' + token ,'Content-Type: application/json'])
    if (len(data) > 0):
      crl.setopt(pycurl.POST, 1)
      crl.setopt(pycurl.POSTFIELDS, data)
    crl.setopt(pycurl.WRITEFUNCTION, ret.write)
    crl.perform()
    crl.close()
    return ret.getvalue()

  def define_new_opts():
    all_opt["account"] = {
                "getopt" : "y:",
                "longopt" : "account",
                "help":"-y, --account=<CLC account>    CLC account",
                "required" : "0",
                "shortdesc" : "CLC Account",
                "default" : "",
                "order": 1
                }

  all_opt["proxy"] = {
                "getopt" : "x:",
                "longopt" : "proxy",
                "help":"-x, --proxy=http://<ip>:<port> Proxy URL",
                "required" : "0",
                "shortdesc" : "Proxy URL",
                "default" : "",
                "order": 1
                }

  def fetch_token(options):
    token = ""
    data = json.dumps({"username": options["--username"], "password": options["--password"]})
    token = (json.loads(curl('https://api.ctl.io/v2/authentication/login', data, options, token))['bearerToken'])
    return token

  def get_power_status(conn, options):
    token = str(fetch_token(options))
    returned = curl('https://api.ctl.io/v2/servers/' + options["--account"] + '/' + options["--switch"], "", options, token)
    details = json.dumps(json.loads(returned)['details'])
    if json.loads(details)['powerState'] == "started":
      return "on"
    else:
      return "off"

  def set_power_status(conn, options):
    del conn
    token = str(fetch_token(options))
    if options["--action"] == "on":
      returned = curl('https://api.ctl.io/v2/operations/' + options["--account"] + '/servers/powerOn', "[\"" + options["--switch"] + "\"]", options, token)
    else:
      returned = curl('https://api.ctl.io/v2/operations/' + options["--account"] + '/servers/powerOff', "[\"" + options["--switch"] + "\"]", options, token)

  time.sleep(int(options["--power-wait"]))```

  def main():
    device_opt = ["login", "passwd", "account", "proxy", "switch"]
    atexit.register(atexit_handler)
    define_new_opts()
    options = check_input(device_opt, process_input(device_opt))
    docs = {}
    docs["shortdesc"] = "Fence agent for CLC"
    docs["longdesc"] = "fence_CLC is an I/O Fencing agent \
  which can be used with the Centurylink Cloud API. \
  It logs via ssh to api.ctl.io where it does all the work. "
    docs["vendorurl"] = "http://clc.io"
    show_docs(options, docs)

  result = fence_action(None, options, set_power_status, get_power_status)
    sys.exit(result)```

  if __name__ == "__main__":
	main()
  ```

There are two more ways to check whether a cluster fencing configuration is fully operational:

•	Use the command ``pcs stonith`` fence hostname. This will attempt to fence the requested node. If successful, the cluster can fence this node.

•	Disable the network on a node  by unplugging the network cable(s), closing the cluster ports on the firewall, or disabling the entire network stack. The other nodes in the cluster should detect that the machine has failed, and fence it. This also tests the cluster’s ability to detect a failed node.
