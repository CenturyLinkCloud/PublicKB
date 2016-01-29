{{{
  "title": "VPN Client Connection Troubleshooting",
  "date": "4-3-2014",
  "author": "jw@tier3.com",
  "attachments": []
}}}

Below are some common issues and resolutions around connecting to your VPN.

### I am having trouble even connecting

If you are having trouble connecting, it often has something to do with the firewall. Here is an example of a log that shows this error. To resolve this you can either change your firewall settings to allow the port or contact support to change the port that your VPN uses.

```
Tue Nov 09 18:06:12 2010 us=818000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 18:06:12 2010 us=818000 TLS Error: TLS handshake failed
Tue Nov 09 18:06:12 2010 us=818000 TCP/UDP: Closing socket
Tue Nov 09 18:06:12 2010 us=818000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 18:06:12 2010 us=818000 Restart pause, 2 second(s)
Tue Nov 09 18:06:14 2010 us=815000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 18:06:14 2010 us=815000 Re-using SSL/TLS context
Tue Nov 09 18:06:14 2010 us=815000 LZO compression initialized
Tue Nov 09 18:06:14 2010 us=815000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 18:06:14 2010 us=815000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 18:06:14 2010 us=815000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 18:06:14 2010 us=815000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 18:06:14 2010 us=815000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 18:06:14 2010 us=815000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 18:06:14 2010 us=815000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 18:06:14 2010 us=815000 UDPv4 link local: [undef]
Tue Nov 09 18:06:14 2010 us=815000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 18:07:14 2010 us=360000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 18:07:14 2010 us=360000 TLS Error: TLS handshake failed
Tue Nov 09 18:07:14 2010 us=360000 TCP/UDP: Closing socket
Tue Nov 09 18:07:14 2010 us=360000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 18:07:14 2010 us=360000 Restart pause, 2 second(s)
Tue Nov 09 18:07:16 2010 us=357000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 18:07:16 2010 us=357000 Re-using SSL/TLS context
Tue Nov 09 18:07:16 2010 us=357000 LZO compression initialized
Tue Nov 09 18:07:16 2010 us=357000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 18:07:16 2010 us=357000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 18:07:16 2010 us=357000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 18:07:16 2010 us=357000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 18:07:16 2010 us=357000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 18:07:16 2010 us=357000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 18:07:16 2010 us=357000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 18:07:16 2010 us=357000 UDPv4 link local: [undef]
Tue Nov 09 18:07:16 2010 us=357000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 18:08:17 2010 us=26000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 18:08:17 2010 us=26000 TLS Error: TLS handshake failed
Tue Nov 09 18:08:17 2010 us=26000 TCP/UDP: Closing socket
Tue Nov 09 18:08:17 2010 us=26000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 18:08:17 2010 us=26000 Restart pause, 2 second(s)
Tue Nov 09 18:08:19 2010 us=23000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 18:08:19 2010 us=23000 Re-using SSL/TLS context
Tue Nov 09 18:08:19 2010 us=23000 LZO compression initialized
Tue Nov 09 18:08:19 2010 us=23000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 18:08:19 2010 us=23000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 18:08:19 2010 us=23000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 18:08:19 2010 us=23000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 18:08:19 2010 us=38000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 18:08:19 2010 us=38000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 18:08:19 2010 us=38000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 18:08:19 2010 us=38000 UDPv4 link local: [undef]
Tue Nov 09 18:08:19 2010 us=38000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 18:09:19 2010 us=270000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 18:09:19 2010 us=270000 TLS Error: TLS handshake failed
Tue Nov 09 18:09:19 2010 us=270000 TCP/UDP: Closing socket
Tue Nov 09 18:09:19 2010 us=270000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 18:09:19 2010 us=270000 Restart pause, 2 second(s)
Tue Nov 09 18:09:21 2010 us=267000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 18:09:21 2010 us=267000 Re-using SSL/TLS context
Tue Nov 09 18:09:21 2010 us=267000 LZO compression initialized
Tue Nov 09 18:09:21 2010 us=267000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 18:09:21 2010 us=267000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 18:09:21 2010 us=267000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 18:09:21 2010 us=267000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 18:09:21 2010 us=283000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 18:09:21 2010 us=283000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 18:09:21 2010 us=283000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 18:09:21 2010 us=283000 UDPv4 link local: [undef]
Tue Nov 09 18:09:21 2010 us=283000 UDPv4 link remote: 64.94.142.10:1249
```

### I cannot access my server via ping or other methods

This usually happens in Windows when the OpenVPN client was not run using the "Run as Administator" option. Here is an example of the log for this case:

```
Tue Nov 09 17:40:27 2010 us=99000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 17:40:27 2010 us=99000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 17:40:27 2010 us=99000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link local: [undef]
Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS handshake failed
Tue Nov 09 17:41:27 2010 us=799000 TCP/UDP: Closing socket
Tue Nov 09 17:41:27 2010 us=799000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 17:41:27 2010 us=799000 Restart pause, 2 second(s)
Tue Nov 09 17:41:29 2010 us=812000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 17:41:29 2010 us=812000 Re-using SSL/TLS context
Tue Nov 09 17:41:29 2010 us=812000 LZO compression initialized
Tue Nov 09 17:41:29 2010 us=812000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 17:41:29 2010 us=812000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 17:41:29 2010 us=812000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 17:41:29 2010 us=812000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 17:41:29 2010 us=812000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link local: [undef]
Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 17:42:08 2010 us=266000 TLS: Initial packet from 64.94.142.10:1249, sid=220a1870 10cc7c8c
Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=1, /C=US/ST=WA/L=Seattle/O=Tier3LLC/CN=WA1RussVPN01-CA/emailAddress=noc@tier3.com
Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: nsCertType=SERVER
Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=0, /C=US/ST=WA/O=Tier3LLC/CN=WA1RussVPN01/emailAddress=noc@tier3.com
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
Tue Nov 09 17:42:08 2010 us=750000 Control Channel: TLSv1, cipher TLSv1/SSLv3 DHE-RSA-AES256-SHA, 1024 bit RSA
Tue Nov 09 17:42:08 2010 us=750000 [WA1RussVPN01] Peer Connection Initiated with 64.94.142.10:1249
Tue Nov 09 17:42:10 2010 us=403000 SENT CONTROL [WA1RussVPN01]: 'PUSH_REQUEST' (status=1)
Tue Nov 09 17:42:10 2010 us=434000 PUSH: Received control message: 'PUSH_REPLY,route 10.80.113.0 255.255.255.0 10.80.134.1,route-gateway 10.80.134.230,ping 10,ping-restart 120,ifconfig 10.80.134.231 255.255.255.0'
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: timers and/or timeouts modified
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: --ifconfig/up options modified
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route options modified
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route-related options modified
Tue Nov 09 17:42:10 2010 us=466000 ROUTE default_gateway=192.168.0.1
Tue Nov 09 17:42:10 2010 us=481000 TAP-WIN32 device [Local Area Connection 5] opened: \\.\Global\{E026A80A-7CB5-41F7-8ADA-EA136D0C7957}.tap
Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 Driver Version 9.6
Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 MTU=1500
Tue Nov 09 17:42:10 2010 us=497000 Notified TAP-Win32 driver to set a DHCP IP/netmask of 10.80.134.231/255.255.255.0 on interface {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} [DHCP-serv: 10.80.134.0, lease-time: 31536000]
Tue Nov 09 17:42:10 2010 us=497000 NOTE: FlushIpNetTable failed on interface [101] {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} (status=5) : Access is denied.
Tue Nov 09 17:42:15 2010 us=317000 TEST ROUTES: 1/1 succeeded len=1 ret=1 a=0 u/d=up
Tue Nov 09 17:42:15 2010 us=333000 C:\WINDOWS\system32\route.exe ADD 10.80.113.0 MASK 255.255.255.0 10.80.134.1
Tue Nov 09 17:42:15 2010 us=348000 ROUTE: route addition failed using CreateIpForwardEntry: Access is denied. [status=5 if_index=101]
Tue Nov 09 17:42:15 2010 us=348000 Route addition via IPAPI failed [adaptive]
Tue Nov 09 17:42:15 2010 us=348000 Route addition fallback to route.exe
Tue Nov 09 17:42:15 2010 us=411000 ERROR: Windows route add command failed [adaptive]: returned error code 1
Tue Nov 09 17:42:15 2010 us=411000 Initialization Sequence Completed
```

### I am getting a "TLS" error

```
TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
TLS Error: TLS handshake failed
TCP/UDP: Closing socket
SIGUSR1[soft,tls-error] received, process restarting
Restart pause, 2 second(s)
```

Your OpenVPN will also pause for 60 seconds at a time on this line (or one very similar):

```
Wed Nov 10 14:41:44 2010 us=378000 UDPv4 link remote: 64.94.142.10: (Your OpenVPN port)
```

If you see the above error message in your OpenVPN log, it can mean a few things:

1. You may have reached the maximum concurrent sessions available for your OpenVPN connection. Go to https://control.ctl.io/Network/vpn and click "edit settings" to increase your max connections, then try again.

2. Your Windows firewall is blocking the required port. Try to disable your firewall and connect again. If you don't want to disable your firewall, you can open the required Inbound/Outbound ports. Your remote ports are unique. You can find the port numbers by following the instructions below or by contacting support.

3. Your physical firewall is blocking the required port. Check with your network administrator and let them know that you need a specific Outbound TCP and UDP port number to be opened in order for OpenVPN to be able to connect to CenturyLink Cloud. You can find the port number by following the instructions below or by contacting support.

To find your OpenVPN port, open the configuration folder for your VPN connection (`C:\Program Files (x86)/OpenVPN/config/[VpnName]` in Windows, or inside the TBLK file using Tunnelblick on a Mac). In this folder, find the `ovpn` file and open it with Notepad or a similar text editor. Under the `proto tcp` or `proto udp` line, there is a line `remote [IPHOST] [PORT]`. The last number on this line is the port number.

### It says my credentials are not correct

Some users authenticate their OpenVPN with Active Directory (LDAP). You can disable/enable this with the "edit settings" button as described in [Configure Two-Factor Authentication for Client VPN](configure-two-factor-authentication-for-client-vpn.md).

If you have authentication enabled and you are unable to connect with your username/password, you will see this in your OpenVPN log:

```
Wed Nov 10 15:14:56 2010 us=515000 SIGUSR1[soft,auth-failure] received, process restarting
Wed Nov 10 15:14:56 2010 us=515000 Restart pause, 2 second(s)
```

You need to verify with CenturyLink Cloud or your Administrator that you are using the right credentials.

#### An example of a successful login log

```
Tue Nov 09 17:38:22 2010 us=766000 OpenVPN 2.1.1 i686-pc-mingw32 [SSL] [LZO2] [PKCS11] built on Dec 11 2009
Tue Nov 09 17:38:22 2010 us=766000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 17:38:23 2010 us=297000 Control Channel Authentication: using 'tlsauth.key' as a OpenVPN static key file
Tue Nov 09 17:38:23 2010 us=297000 Outgoing Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
Tue Nov 09 17:38:23 2010 us=297000 Incoming Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
Tue Nov 09 17:38:23 2010 us=297000 LZO compression initialized
Tue Nov 09 17:38:23 2010 us=297000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 17:38:23 2010 us=297000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 17:38:23 2010 us=297000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 17:38:23 2010 us=297000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 17:38:23 2010 us=297000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 17:38:23 2010 us=297000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 17:38:23 2010 us=297000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 17:38:23 2010 us=297000 UDPv4 link local: [undef]
Tue Nov 09 17:38:23 2010 us=297000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 17:39:23 2010 us=966000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 17:39:23 2010 us=966000 TLS Error: TLS handshake failed
Tue Nov 09 17:39:23 2010 us=966000 TCP/UDP: Closing socket
Tue Nov 09 17:39:23 2010 us=966000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 17:39:23 2010 us=966000 Restart pause, 2 second(s)
Tue Nov 09 17:39:25 2010 us=962000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 17:39:25 2010 us=962000 Re-using SSL/TLS context
Tue Nov 09 17:39:25 2010 us=962000 LZO compression initialized
Tue Nov 09 17:39:25 2010 us=962000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 17:39:25 2010 us=962000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 17:39:25 2010 us=962000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 17:39:25 2010 us=962000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 17:39:25 2010 us=962000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 17:39:25 2010 us=962000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 17:39:25 2010 us=962000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 17:39:25 2010 us=962000 UDPv4 link local: [undef]
Tue Nov 09 17:39:25 2010 us=962000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 17:40:25 2010 us=87000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 17:40:25 2010 us=87000 TLS Error: TLS handshake failed
Tue Nov 09 17:40:25 2010 us=87000 TCP/UDP: Closing socket
Tue Nov 09 17:40:25 2010 us=87000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 17:40:25 2010 us=87000 Restart pause, 2 second(s)
Tue Nov 09 17:40:27 2010 us=99000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 17:40:27 2010 us=99000 Re-using SSL/TLS context
Tue Nov 09 17:40:27 2010 us=99000 LZO compression initialized
Tue Nov 09 17:40:27 2010 us=99000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 17:40:27 2010 us=99000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 17:40:27 2010 us=99000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 17:40:27 2010 us=99000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 17:40:27 2010 us=99000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link local: [undef]
Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS handshake failed
Tue Nov 09 17:41:27 2010 us=799000 TCP/UDP: Closing socket
Tue Nov 09 17:41:27 2010 us=799000 SIGUSR1[soft,tls-error] received, process restarting
Tue Nov 09 17:41:27 2010 us=799000 Restart pause, 2 second(s)
Tue Nov 09 17:41:29 2010 us=812000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
Tue Nov 09 17:41:29 2010 us=812000 Re-using SSL/TLS context
Tue Nov 09 17:41:29 2010 us=812000 LZO compression initialized
Tue Nov 09 17:41:29 2010 us=812000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
Tue Nov 09 17:41:29 2010 us=812000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
Tue Nov 09 17:41:29 2010 us=812000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
Tue Nov 09 17:41:29 2010 us=812000 Local Options hash (VER=V4): 'a7133b47'
Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options hash (VER=V4): 'c5677ab3'
Tue Nov 09 17:41:29 2010 us=812000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link local: [undef]
Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link remote: 64.94.142.10:1249
Tue Nov 09 17:42:08 2010 us=266000 TLS: Initial packet from 64.94.142.10:1249, sid=220a1870 10cc7c8c
Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=1, /C=US/ST=WA/L=Seattle/O=Tier3LLC/CN=WA1RussVPN01-CA/emailAddress=noc@tier3.com
Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: nsCertType=SERVER
Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=0, /C=US/ST=WA/O=Tier3LLC/CN=WA1RussVPN01/emailAddress=noc@tier3.com
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
Tue Nov 09 17:42:08 2010 us=750000 Control Channel: TLSv1, cipher TLSv1/SSLv3 DHE-RSA-AES256-SHA, 1024 bit RSA
Tue Nov 09 17:42:08 2010 us=750000 [WA1RussVPN01] Peer Connection Initiated with 64.94.142.10:1249
Tue Nov 09 17:42:10 2010 us=403000 SENT CONTROL [WA1RussVPN01]: 'PUSH_REQUEST' (status=1)
Tue Nov 09 17:42:10 2010 us=434000 PUSH: Received control message: 'PUSH_REPLY,route 10.80.113.0 255.255.255.0 10.80.134.1,route-gateway 10.80.134.230,ping 10,ping-restart 120,ifconfig 10.80.134.231 255.255.255.0'
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: timers and/or timeouts modified
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: --ifconfig/up options modified
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route options modified
Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route-related options modified
Tue Nov 09 17:42:10 2010 us=466000 ROUTE default_gateway=192.168.0.1
Tue Nov 09 17:42:10 2010 us=481000 TAP-WIN32 device [Local Area Connection 5] opened: \\.\Global\{E026A80A-7CB5-41F7-8ADA-EA136D0C7957}.tap
Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 Driver Version 9.6
Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 MTU=1500
Tue Nov 09 17:42:10 2010 us=497000 Notified TAP-Win32 driver to set a DHCP IP/netmask of 10.80.134.231/255.255.255.0 on interface {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} [DHCP-serv: 10.80.134.0, lease-time: 31536000]
Tue Nov 09 17:42:10 2010 us=497000 NOTE: FlushIpNetTable failed on interface [101] {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} (status=5) : Access is denied.
Tue Nov 09 17:42:15 2010 us=317000 TEST ROUTES: 1/1 succeeded len=1 ret=1 a=0 u/d=up
Tue Nov 09 17:42:15 2010 us=333000 C:\WINDOWS\system32\route.exe ADD 10.80.113.0 MASK 255.255.255.0 10.80.134.1
Tue Nov 09 17:42:15 2010 us=348000 ROUTE: route addition failed using CreateIpForwardEntry: Access is denied. [status=5 if_index=101]
Tue Nov 09 17:42:15 2010 us=348000 Route addition via IPAPI failed [adaptive]
Tue Nov 09 17:42:15 2010 us=348000 Route addition fallback to route.exe
Tue Nov 09 17:42:15 2010 us=411000 ERROR: Windows route add command failed [adaptive]: returned error code 1
Tue Nov 09 17:42:15 2010 us=411000 Initialization Sequence Completed
```
