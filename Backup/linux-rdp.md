{{{
  "title": "Install RDP on Linux for SBS",
  "date": "11-4-2019",
  "author":  "John Gerger",
  "keywords": ["api", "backup", "clc", "cloud", "install", "sbs", "server"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

The new Simple Backup Service (SBS) currently requires a web browser to perform restore operations. If you do not want to [allow remote web based connections to the Backup Agent](sbs-agent-security.md), you may want to connect directly to the machine via RDP and use a web browser and connect to the local server’s SBS web interface. It is relatively simple to add a desktop with RDP capability to a Linux server to be able to easily establish a typical RDP session to a remote Linux server and get a desktop complete with browser etc.

### Steps  
Here are the commands to install RDP services on a remote RHEL6x, RHEL7x, CentOS6x, and CentOS7x servers.
Other OSes and versions may have similar procedures.
```
# RHEL6x
#######
# Establish a remote SSH session as root and install and configure a desktop with RDP on RHEL6x
# Install a full desktop
yum -y groupinstall "Desktop Platform"

# Install RDP services
yum -y install xrdp tigervnc-server

# Start the RDP service manually now
/etc/init.d/xrdp start

# Install a web browser
yum -y install firefox

# You may now RDP to Linux from Windows
# NOTE1: Set mstsc to use 16bit High Color (24bit / 32bit will NOT work)
# NOTE2: You may want to login as a non-root user to get access to normal icons and programs
```
```
# RHEL7x
#######
# Establish a remote SSH session as root and install and configure a desktop with RDP on RHEL7x
# Install a full desktop
yum -y groups install "Server with GUI"

# Install RDP services
yum -y install xrdp tigervnc-server

# Allow a rule to allow RDP through the OS firewall
firewall-cmd --permanent --zone=public --add-port=3389/tcp

# Restart the firewall so the new RDP rule becomes effective
firewall-cmd --reload

# Set the RDP service to auto-start at boot-time
systemctl enable xrdp.service

# Start the RDP service manually now
systemctl start xrdp.service

# You may now RDP to Linux from Windows
# NOTE: Set mstsc to use 16bit High Color (24bit / 32bit will NOT work)
```
```
# CentOS6x
#########
# Establish a remote SSH session as root and install and configure a desktop with RDP on CentOS6x
# Install a full desktop
yum -y groupinstall desktop

# Install RDP services
yum -y install xrdp tigervnc-server

# Start the RDP service manually now
/etc/init.d/xrdp start

# Install a web browser
yum -y install firefox

# You may now RDP to Linux from Windows
# NOTE1: Set mstsc to use 16bit High Color (24bit / 32bit will NOT work)
# NOTE2: You may want to login as a non-root user to get access to normal icons and programs
```
```
# CentOS7x
##########
# Establish a remote SSH session as root and install and configure a desktop with RDP on CentOS7x
# Install a full desktop
yum -y groups install "Server with GUI"

# Install RDP services
yum -y install xrdp tigervnc-server

# Allow a rule to allow RDP through the OS firewall
firewall-cmd --permanent --zone=public --add-port=3389/tcp

# Restart the firewall so the new RDP rule becomes effective
firewall-cmd --reload

# Set the RDP service to auto-start at boot-time
systemctl enable xrdp.service

# Start the RDP service manually now
systemctl start xrdp.service

# You may now RDP to Linux from Windows
# NOTE: Set mstsc to use 16bit High Color (24bit / 32bit will NOT work)
```

![](../images/backup/rdp/RHEL7x_RDP_SBS_example.png)
