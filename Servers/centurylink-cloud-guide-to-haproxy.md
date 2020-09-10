{{{
  "title": "CenturyLink Cloud Guide to HAProxy",
  "date": "12-17-2015",
  "author": "Gavin Lai",
  "attachments": [],
  "contentIsHTML": false
}}}

### Table of contents

* [Overview](#overview)
* [Prerequisites](#prerequisites)
* [Use Case Scenarios](#use-case-scenarios)
* [Preparation](#preparation)
* [Deployment](#deployment)
* [HAProxy configuration differences](#haproxy-configuration-differences)
* [Testing](#testing)
* [Troubleshooting](#troubleshooting)
* [Support](#support)

### Overview

HAProxy is a free, open source solution offering high availability load
balancing and proxy for TCP and HTTP-based applications. HAProxy can
provide a feature rich alternative to the built-in load balancing
offering from CenturyLink Cloud. HAProxy and Keepalive can be used
together to create a high availability load balancing solution.

### Prerequisites

-   Access to the CenturyLink Cloud platform as an authorized user

-   Identify a Network VLAN you want the HAProxy to reside on

-   Understanding the functions of load balancer (beyond the scope of this article) and CenturyLink Cloud load balancing  offerings, to learn more, please see this [KB](../Network/CenturyLink Cloud/self-service-load-balancing-faq.md),
    [general knowledge](//en.wikipedia.org/wiki/Load_balancing_%28computing%29)
     and [HAProxy documentations](//www.haproxy.org/#docs)

-   Existing web servers or application servers to be load balanced

- High Availability HAProxy nodes have to reside on the same VLAN as multicast is used for heartbeats

### Use Case Scenarios

HAProxy can be used as dedicated applications (layer 7) or TCP (layer 4) load balancer to create a high availability environment for any internal and external web or applications environment. In this use case, two web servers are load balanced by a pair of HAProxy to create a high availability environment.
HAProxy can be configured to handle both internal and external network traffic and used to perform the following functions:

-   Dedicated web services load balancing

-   Dedicated Application load balancing

-   Dedicated Work load distribution

-   SSL offloading

![HAProxy Network Diagram](../images/haproxy/HAProxy-blockdiagram.png)

Web traffic can come through a public/private Virtual IP (VIP)  and reach the HAProxy pair. HAProxy would redirect the
traffic based on the algorithm chosen in the configuration.
In this scenario, port 80 and 443 are being load balanced with round-robin algorithm.  A complete list of algorithm can be found [here](//cbonte.github.io/haproxy-dconv/configuration-1.6.html)

### Preparation

In preparation. There are several factors need to be considered:

-   Network ports required for the load balance application

-   Firewall rules required

-   SSL certificate if the application is SSL based

-   Configure the Virtual IP for the HAProxy servers with Public IP address:
 - [Assign a public IP address](../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) to one of the HAProxy servers and bind it to a new IP address
 ![Adding Public IP with new Privte IP](../images/haproxy/HAProxy-add-publicip.png)
 - From that server, run `ifconfig ens160:1 down` and `remove /etc/sysconfig/network-scripts/ifcfg-ens160:1` file; verify this step by pinging the new public and private IP addresses, there should be no reply from these addresses (assuming ens160 is the network interface)

 - In this example, 10.100.96.28 is the new private IP assigned along with the public IP addresses

- If only Private IP address is required:
 - Please following this [KB](../Network/CenturyLink Cloud/how-to-reserve-ip-addresses.md) to reserve the Private IP address required for HAProxy


### Deployment

HAProxy can be deployed in a single or HA configuration. This
walk-through cover both single and HA configuration. HAProxy can be
configured with a single network interface or 2 (or more) network
interfaces, depending on the security and infrastructure requirement,
both can be implemented in CenturyLink Cloud.

-   Deploy a CentOS 7 server using either the [Control
    Portal](//control.ctl.io), [CLI](//github.com/CenturyLinkCloud/clc-go-cli) or [API](//www.ctl.io/developers/)

-   Once deployed, connect to [Client
    VPN](../Network/CenturyLink Cloud/how-to-configure-client-vpn.md)
    and secure shell to the server and start implementation:

-  As the applications use 'GetHostByName' system calls, `hostname -s` output should match the real hostname and not localhost.  In order to change hostname, run the first two commands below and update the repository with `yum update`

    a.  `grep HOSTNAME /etc/sysconfig/network | awk -F= '{print \$2}' | tee /etc/hostname`

    b.  `` hostname \`grep HOSTNAME /etc/sysconfig/network | awk -F= '{print \$2}'\` ``

    c.  `yum update`

-  Install HAproxy (and Keepalive only for HA)

    a.  `yum install haproxy -y`

    b.  `yum install keepalived –y`

-  Depending on the application or network ports required to be
    balanced, both the OS, haproxy configuration and firewall need to be
    configured:

    a.  For the OS:
      -   Enable Packet forwarding
      -   Enable reverse path filtering
      -   Bind to non-local address needs to be enabled

    ```
          systctl –w net.ipv4.ip\_forward=1
          systctl –w net.ipv4.conf.default.rp\_filter=1
          systctl –w net.ipv4.ip\_nonlocal\_bind=1
    ```

  b.  For HAProxy configuration (/etc/haproxy/haproxy.cfg)
      -   Enable the application(s) to be load balanced by editing the /etc/haproxy/haproxy.cfg.  The file content would look similar to below:

  ```           
  global
     log         127.0.0.1 local2 info
     chroot      /var/lib/haproxy
     pidfile     /var/run/haproxy.pid
     maxconn     4000
     user        haproxy
     group       haproxy
  daemon
     stats socket /var/lib/haproxy/stats
  defaults
     mode                    http
     log                     global
     option                  httplog
     option                  dontlognull
     option http-server-close
     option forwardfor       except 127.0.0.0/8
     option                  redispatch
     retries                 3
     timeout http-request    10s
     timeout queue           1m
     timeout connect         10s
     timeout client          1m
     timeout server          1m
     timeout http-keep-alive 10s
     timeout check           10s
     maxconn                 3000
  frontend  https-in *:443
     mode tcp
     option tcplog
     default_backend             backend_server
  frontend  http-in *:80
     mode http
     default_backend http_server
  backend backend_server
     mode tcp
     balance     roundrobin
     option ssl-hello-chk
     server      wwws01 10.100.96.21:443 check
     server      wwws02 10.100.96.27:443 check
     http-request set-header X-Forwarded-Port %[dst_port]
     http-request add-header X-Forwarded-Proto https if { ssl_fc }
  backend http_server
     mode http
     balance     roundrobin
     server      www01 10.100.96.21:80 check
     server      www02 10.100.96.27:80 check
 ```

   - options in haproxy.cfg like balance algorithm Round-robin (other options are [available](//cbonte.github.io/haproxy-dconv/configuration-1.5.html#4.2-balance)) and options can be found at [HAProxy site](//www.haproxy.org/#docs)

  -   Setting up proper logging (optional, if not set, HAProxy logs might not be reliability populated in /var/log/messages); To do this, UDP syslog reception needs to be enabled as HAProxy is running with chroot by changing the following in /etc/rsyslog.conf:

 ```
    \$ModLoad imudp
    \$UDPServerRun 514
    \$AllowedSender UDP, 127.0.0.1
    \*.info;mail.none;authpriv.none;cron.none;local2.none   /var/log/messages
    local2.\* /var/log/haproxy.log
 ```

  c. Keepalive parameters (in /etc/keepalived/keepalived.conf)

 ```
   global_defs {
     notification_email {
     your@email
   }
   notification_email_from your@email
   smtp_server  your_smtp_server
   smtp_connect_timeout 30
   router_id CA3CCVAHAPROX02
   }

   vrrp_script chk_haproxy {
        script "killall -0 haproxy"
        interval 2
        weigth 2
   }
   vrrp_instance VI_1 {
    state MASTER
    interface ens160
    virtual_router_id 51
    priority 101
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 57924680
    }
    virtual_ipaddress {
        10.100.96.28 dev ens160
    }
    track_interface {
                ens160
        }
    track_script {
                chk_haproxy
        }
   }
 ```

d.  Firewall rules (this varies as application ports and security policy
    can be different, please use the following as references):

  -   HAProxy and Keepalive

 ```
    firewall-cmd --permanent --zone=internal --add-service=http
    firewall-cmd --permanent --zone=internal --add-service=https
    firewall-cmd --zone=internal --add-port=443/tcp
    firewall-cmd --zone=internal --add-port=80/tcp
 ```
  -   Keepalive

 ```
    firewall-cmd --direct --add-rule ipv4 filter INPUT 0 -i ens160 -d 224.0.0.0/8 -j ACCEPT
    firewall-cmd --direct --perm --add-rule ipv4 filter INPUT 0 -i ens160 -d 224.0.0.0/8 -j ACCEPT
    firewall-cmd --direct --add-rule ipv4 filter INPUT 0 -p vrrp -i ens160 -j ACCEPT
    firewall-cmd --direct --perm --add-rule ipv4 filter INPUT 0 -p vrrp -i ens160 -j ACCEPT
    firewall-cmd --direct --add-rule ipv4 filter OUTPUT 0 -p vrrp -o ens160 -j ACCEPT
    firewall-cmd --direct --perm --add-rule ipv4 filter OUTPUT 0 -p vrrp -o ens160 -j ACCEPT
    firewall-cmd --reload
 ```
#### HAProxy configuration differences
The difference in configuration (haproxy.cfg) between the two HAProxy nodes:

| HXPRoxy       | haproxy1        | haproxy2  |
|-------------|---------------|---------|
| state         | MASTER          | BACKUP    |
| priority      | 101             |   100     |
| router_id     | SeverName1      |ServerName2|


### Testing
The environment can be tested by disabling httpd (or the load balanced application) and haproxy.  In this example, `systemctl stop httpd` and `systemctl stop haproxy` are used to perform testing.  From the demo below, the screen on the left shows the output of a https request to the VIP.  On the right, the commands are run to show the effect of the https requests.  There is minimal delay for the fail over to take place.
![Demo failover](../images/haproxy/haproxy-demo-failover.gif)

### Troubleshooting
- The most common issue is firewall ports are not configured properly, firewall can be disabled for testing purpose

- If the HAProxy load balancers are on different VLANs, please make sure the firewall ports are configured between the two VLANs (for details, please see this [KB](../Network/CenturyLink Cloud/connecting-data-center-networks-through-firewall-policies.md))

- Keepalive uses VRRP for heatbeat, the following command would help identify if VRRP is working:

    ```
    netstat -g
    netstat -ng
    ip maddr show
    ```

- As for the virtual IP on the HAProxy server, the Master HAProxy should own the Virtual IP address, `ip a` command will show if that node has the VIP address, the sample output:

 ```
 2: ens160: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 00:0c:29:6e:bd:96 brd ff:ff:ff:ff:ff:ff
    inet 10.100.96.26/24 brd 10.100.96.255 scope global ens160
       valid_lft forever preferred_lft forever
    inet 10.100.96.28/32 scope global ens160
       valid_lft forever preferred_lft forever
    inet6 fe80::20c:29ff:fe6e:bd96/64 scope link
 ```

### Support
* For issues related to deploying HAProxy, accessing the deployed software, please visit the [HAProxy Website](//www.haproxy.org/#supp)
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying any Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](//t3n.zendesk.com/tickets/new).
