{{{
  "title": "SafeHaven 3.0 and 3.1: Add New SRNs to a Pre-Existing Cluster",
  "date": "9-1-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview:
This document will walk you through manually adding additional SRN appliances to a pre-existing cluster, and then pairing the SRNs with their DR replication partners within the Recovery Data Center. Note that SRNs can replicate to multiple other SRNs in different groups, vlans or data centers using the procedure below. This document covers the procedure for 3.0 and 3.1.

#### Add New SRNs to a Pre-Existing Cluster on 3.0
1. Deploy the SRN and match its code to the cluster code.

2. In the SafeHaven Console, Right Click on the Site and Add click on “Register SRN”.

3. Enter the Information asked and register the SRN from the GUI.

4. SSH as “Administrator” into the CMS (Administrator password is the SafeHaven Cluster password).

5. cd /usr/lib/datagardens/BaseImageConfigurators.

6. CMS: Run ./addSRN script like below for each SRN that is added:
   For example:

   ```
   Administrator@VA1XXXXCMS01:cd /usr/lib/datagardens/BaseImageConfigurators/
   BaseImageConfigurators$: ./addSRN VA1RXXXXSRN02 10.135.25.20 10.135.25.20 10.135.25.20 CLC 20082

   ```

   The command syntax is ./addSRN SRNHOSTNAME "Service_IP" "Storage_IP" "WAN_Sync_IP" "Type of Connection" "Connection_Port"

   The connection port default is 20082. The options for "Type of connection" can be CLC, VMWARE, VPDC, VCLOUD, MANUAL or CUSTOM. Most cases will either be CLC or VMWARE/VCLOUD (if using vCD).

7. Test password-less ssh access from Administrator@CMS to root@SRN.

#### Pairing SRNs (Create Peers)
1. CMS: Run ./pair2SRNs.sh script once for each SRN pair:
   For example:
   ```
   Administrator@VA1XXXXCMS01:/usr/lib/datagardens/BaseImageConfigurators$ ./pair2SRNs.sh

   syntax: ./pair2SRNs.sh <SRN1 Service IP> <SRN1 Storage IP> <SRN1 Root Password> <SRN2 Service IP> <SRN2 Storage IP> <SRN2 Root Password>

   Note: this should be run as Administrator and the SRNs should already have been added to the cluster

   Exit

   Administrator@VA1CA6SHCMS01:/usr/lib/datagardens/BaseImageConfigurators$ ./pair2SRNs.sh 10.230.102.192 10.230.102.192 ABC123!! 10.135.25.20 10.135.25.20 ABC123!!

   Script will automatically exchange key as below:
   + SRN1_SERVICE_IP=10.230.102.192
   + SRN1_STORAGE_IP=10.230.102.192
   + RootPass1='ABC123!!'
   + SRN2_SERVICE_IP=10.135.25.20
   + SRN2_STORAGE_IP=10.135.25.20
   + RootPass2='ABC123!!'
   + AUTOSSHEX=/usr/lib/datagardens/BaseImageConfigurators/autoSSHKeyExchange.exp
   +ssh root@10.230.102.192 '/usr/lib/datagardens/BaseImageConfigurators/autoSSHKeyExchange.exp 10.135.25.20 root '\''ABC123!!'\'' root'
   spawn /usr/bin/ssh-keygen -R 10.135.25.20 #remove existing entries for 10.135.25.20
   spawn /usr/bin/ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.135.25.20
   The authenticity of host '10.135.25.20 (10.135.25.20)' can't be established.
   ECDSA key fingerprint is e4:11:ff:c0:cf:8d:74:cf:88:62:f5:7f:d3:de:5e:d9.
   Are you sure you want to continue connecting (yes/no)? yes
   /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
   /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
   root@10.135.25.20's password:
   Number of key(s) added: 1
   Now try logging into the machine, with: "ssh 'root@10.135.25.20'"
   + ssh root@10.135.25.20 '/usr/lib/datagardens/BaseImageConfigurators/autoSSHKeyExchange.exp 10.230.102.192 root '\''ABC123!!'\'' root'
   spawn /usr/bin/ssh-keygen -R 10.230.102.192 #remove existing entries for 10.230.102.192
   spawn /usr/bin/ssh-copy-id -i /root/.ssh/id_rsa.pub root@10.230.102.192
   The authenticity of host '10.230.102.192 (10.230.102.192)' can't be established.
   ECDSA key fingerprint is 3b:85:e0:16:cc:40:d3:b4:8c:3e:6b:46:6b:e7:a4:a2.
   Are you sure you want to continue connecting (yes/no)? yes
   /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
   /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
   root@10.230.102.192's password:
   Number of key(s) added: 1
   Now try logging into the machine, with: "ssh 'root@10.230.102.192'"
   and check to make sure that only the key(s) you wanted were added.
   + ssh root@10.230.102.192 ssh 10.135.25.20 hostname
   VA1RXXXXSRN02
   + suc1=0
   + ssh root@10.135.25.20 ssh 10.230.102.192 hostname
   PSRNMID02
   + suc2=0
   + set +x
   finish with success
   Administrator@VA1XXXXCMS01:/usr/lib/datagardens/BaseImageConfigurators$
   ```

Finally, test password-less root ssh access between all the SRN pairs.

#### ADD New SRNs to a Pre-Existing Cluster in 3.1
1. Right-click your Data Center and choose "Register SRN" and fill out the IP address/password fields.

2. Once the SRN has been registered, highlight the partner SRN and navigate to the "Peers" tab.

3. Click "Add Peer".

4. Choose the appropriate peers from the dropdown menu and enter the passwords, and click "Register".
