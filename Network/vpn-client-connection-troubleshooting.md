{{{
  "title": "VPN Client Connection Troubleshooting",
  "date": "4-3-2014",
  "author": "jw@tier3.com",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Here are some of the common issues and resolution:</p>
<ul>
  <li><a href="#1">I&nbsp;am having trouble even connecting</a>
  </li>
  <li><a href="#2">I cannot access my server via ping or other methods</a>
  </li>
  <li><a href="#3">I am getting a "TLS" error</a>
  </li>
  <li><a href="#4">It says my credentials are not correct</a>
  </li>
  <li><a href="#5">An example of a successful login</a>
  </li>
</ul>
<p>
  <a name="1"></a>
</p>
<h3>I am having trouble even connecting</h3>
<p>Many times if you are having trouble even connecting this is usually something that has to do with the firewall. Here is an example of a log that shows this error. To resolve this you can either change your firewall settings to allow the port or contact
  the NOC team to change the port.</p>
<p>Tue Nov 09 18:06:12 2010 us=818000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 18:06:12 2010 us=818000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 18:06:12 2010 us=818000 TCP/UDP: Closing socket
  <br />Tue Nov 09 18:06:12 2010 us=818000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 18:06:12 2010 us=818000 Restart pause, 2 second(s)
  <br />Tue Nov 09 18:06:14 2010 us=815000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 18:06:14 2010 us=815000 Re-using SSL/TLS context
  <br />Tue Nov 09 18:06:14 2010 us=815000 LZO compression initialized
  <br />Tue Nov 09 18:06:14 2010 us=815000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 18:06:14 2010 us=815000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 18:06:14 2010 us=815000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 18:06:14 2010 us=815000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 18:06:14 2010 us=815000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 18:06:14 2010 us=815000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 18:06:14 2010 us=815000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 18:06:14 2010 us=815000 UDPv4 link local: [undef]
  <br />Tue Nov 09 18:06:14 2010 us=815000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 18:07:14 2010 us=360000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 18:07:14 2010 us=360000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 18:07:14 2010 us=360000 TCP/UDP: Closing socket
  <br />Tue Nov 09 18:07:14 2010 us=360000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 18:07:14 2010 us=360000 Restart pause, 2 second(s)
  <br />Tue Nov 09 18:07:16 2010 us=357000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 18:07:16 2010 us=357000 Re-using SSL/TLS context
  <br />Tue Nov 09 18:07:16 2010 us=357000 LZO compression initialized
  <br />Tue Nov 09 18:07:16 2010 us=357000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 18:07:16 2010 us=357000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 18:07:16 2010 us=357000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 18:07:16 2010 us=357000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 18:07:16 2010 us=357000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 18:07:16 2010 us=357000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 18:07:16 2010 us=357000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 18:07:16 2010 us=357000 UDPv4 link local: [undef]
  <br />Tue Nov 09 18:07:16 2010 us=357000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 18:08:17 2010 us=26000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 18:08:17 2010 us=26000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 18:08:17 2010 us=26000 TCP/UDP: Closing socket
  <br />Tue Nov 09 18:08:17 2010 us=26000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 18:08:17 2010 us=26000 Restart pause, 2 second(s)
  <br />Tue Nov 09 18:08:19 2010 us=23000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 18:08:19 2010 us=23000 Re-using SSL/TLS context
  <br />Tue Nov 09 18:08:19 2010 us=23000 LZO compression initialized
  <br />Tue Nov 09 18:08:19 2010 us=23000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 18:08:19 2010 us=23000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 18:08:19 2010 us=23000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 18:08:19 2010 us=23000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 18:08:19 2010 us=38000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 18:08:19 2010 us=38000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 18:08:19 2010 us=38000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 18:08:19 2010 us=38000 UDPv4 link local: [undef]
  <br />Tue Nov 09 18:08:19 2010 us=38000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 18:09:19 2010 us=270000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 18:09:19 2010 us=270000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 18:09:19 2010 us=270000 TCP/UDP: Closing socket
  <br />Tue Nov 09 18:09:19 2010 us=270000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 18:09:19 2010 us=270000 Restart pause, 2 second(s)
  <br />Tue Nov 09 18:09:21 2010 us=267000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 18:09:21 2010 us=267000 Re-using SSL/TLS context
  <br />Tue Nov 09 18:09:21 2010 us=267000 LZO compression initialized
  <br />Tue Nov 09 18:09:21 2010 us=267000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 18:09:21 2010 us=267000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 18:09:21 2010 us=267000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 18:09:21 2010 us=267000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 18:09:21 2010 us=283000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 18:09:21 2010 us=283000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 18:09:21 2010 us=283000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 18:09:21 2010 us=283000 UDPv4 link local: [undef]
  <br />Tue Nov 09 18:09:21 2010 us=283000 UDPv4 link remote: 64.94.142.10:1249</p>
<p>
  <a name="2"></a>
</p>
<h3>I cannot access my server via ping or other methods</h3>
<p>This usually happens when using the Windows operating system and you did not perform a Run as Administrator on the open VPN client. Here is an example of the log:</p>
<p>Tue Nov 09 17:40:27 2010 us=99000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link local: [undef]
  <br />Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 17:41:27 2010 us=799000 TCP/UDP: Closing socket
  <br />Tue Nov 09 17:41:27 2010 us=799000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 17:41:27 2010 us=799000 Restart pause, 2 second(s)
  <br />Tue Nov 09 17:41:29 2010 us=812000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 17:41:29 2010 us=812000 Re-using SSL/TLS context
  <br />Tue Nov 09 17:41:29 2010 us=812000 LZO compression initialized
  <br />Tue Nov 09 17:41:29 2010 us=812000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 17:41:29 2010 us=812000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 17:41:29 2010 us=812000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link local: [undef]
  <br />Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 17:42:08 2010 us=266000 TLS: Initial packet from 64.94.142.10:1249, sid=220a1870 10cc7c8c
  <br />Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=1, /C=US/ST=WA/L=Seattle/O=Tier3LLC/CN=WA1RussVPN01-CA/emailAddress=noc@tier3.com
  <br />Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: nsCertType=SERVER
  <br />Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=0, /C=US/ST=WA/O=Tier3LLC/CN=WA1RussVPN01/emailAddress=noc@tier3.com
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
  <br />Tue Nov 09 17:42:08 2010 us=750000 Control Channel: TLSv1, cipher TLSv1/SSLv3 DHE-RSA-AES256-SHA, 1024 bit RSA
  <br />Tue Nov 09 17:42:08 2010 us=750000 [WA1RussVPN01] Peer Connection Initiated with 64.94.142.10:1249
  <br />Tue Nov 09 17:42:10 2010 us=403000 SENT CONTROL [WA1RussVPN01]: 'PUSH_REQUEST' (status=1)
  <br />Tue Nov 09 17:42:10 2010 us=434000 PUSH: Received control message: 'PUSH_REPLY,route 10.80.113.0 255.255.255.0 10.80.134.1,route-gateway 10.80.134.230,ping 10,ping-restart 120,ifconfig 10.80.134.231 255.255.255.0'
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: timers and/or timeouts modified
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: --ifconfig/up options modified
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route options modified
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route-related options modified
  <br />Tue Nov 09 17:42:10 2010 us=466000 ROUTE default_gateway=192.168.0.1
  <br />Tue Nov 09 17:42:10 2010 us=481000 TAP-WIN32 device [Local Area Connection 5] opened: \\.\Global\{E026A80A-7CB5-41F7-8ADA-EA136D0C7957}.tap
  <br />Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 Driver Version 9.6
  <br />Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 MTU=1500
  <br />Tue Nov 09 17:42:10 2010 us=497000 Notified TAP-Win32 driver to set a DHCP IP/netmask of 10.80.134.231/255.255.255.0 on interface {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} [DHCP-serv: 10.80.134.0, lease-time: 31536000]
  <br />Tue Nov 09 17:42:10 2010 us=497000 NOTE: FlushIpNetTable failed on interface [101] {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} (status=5) : Access is denied.
  <br />Tue Nov 09 17:42:15 2010 us=317000 TEST ROUTES: 1/1 succeeded len=1 ret=1 a=0 u/d=up
  <br />Tue Nov 09 17:42:15 2010 us=333000 C:\WINDOWS\system32\route.exe ADD 10.80.113.0 MASK 255.255.255.0 10.80.134.1
  <br />Tue Nov 09 17:42:15 2010 us=348000 ROUTE: route addition failed using CreateIpForwardEntry: Access is denied. [status=5 if_index=101]
  <br />Tue Nov 09 17:42:15 2010 us=348000 Route addition via IPAPI failed [adaptive]
  <br />Tue Nov 09 17:42:15 2010 us=348000 Route addition fallback to route.exe
  <br />Tue Nov 09 17:42:15 2010 us=411000 ERROR: Windows route add command failed [adaptive]: returned error code 1
  <br />Tue Nov 09 17:42:15 2010 us=411000 Initialization Sequence Completed</p>
<p>
  <a name="3"></a>
</p>
<h3>I am getting a "TLS" error</h3>

<p><strong>TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)</strong>
</p>

<p><strong>TLS Error: TLS handshake failed</strong>
</p>

<p><strong>TCP/UDP: Closing socket</strong>
</p>

<p><strong>SIGUSR1[soft,tls-error] received, process restarting</strong>
</p>

<div>
  <p><strong>Restart pause, 2 second(s)”</strong>
  </p>
  <p>Your OpenVPN will also pause for 60 seconds at a time on this line(or one very similar):</p>
  <p><strong>Wed Nov 10 14:41:44 2010 us=378000 UDPv4 link remote: 64.94.142.10: (Your OpenVPN port)</strong>
  </p>
</div>

<p>If you see the above error message in your OpenVPN log, it can mean a couple of things:</p>

<ol>
  <li>You have reached your max concurrent sessions available for your OpenVPN connection. Go to: <a href="https://control.tier3.com/Net/Vpn">https://control.tier3.com/Net/Vpn</a> and select Edit VPN Settings. Increase the Max connections and
    try again.</li>
  <li>Your Windows Firewall is blocking the required port. Try to disable your firewall and connect again. If you don’t want to disable your firewall, you can open the required Inbound/Outbound ports. Your remote ports are unique.&nbsp;
    You will need to email <a href="mailto:noc@tier3.com">noc@tier3.com</a> and ask what ports your OpenVPN uses or see the bullet below.&nbsp;</li>
  <li>Your physical Firewall is blocking the required port. (Firewall, Router, etc)&nbsp; Check with your network administrator.&nbsp;&nbsp; You can tell him/her this:&nbsp; “In order for OpenVPN to be able to connect to CenturyLink Cloud, Outbound TCP and UDP
    port xyz to be opened(email&nbsp; <a href="mailto:noc@tier3.com">noc@tier3.com</a> for your OpenVPN port or see the bullet below)”
    <br />
    <br />
  </li>
</ol>
<ul>
  <li>You can find your OpenVPN port by going to your Program Files(x86)/OpenVPN/config/VpnName and opening your VpnName.ovpn file with notepad or a similar editor. The proto = protocol (tcp or udp), and the last number on the remote line is the port
    it uses) &nbsp;Example UDP 1194</li>
</ul>

<p>
  <a name="4"></a>
</p>
<h3>It says my credentials are not correct</h3>

<p>Invalid Username/Password:</p>

<p>Some users authenticate their OpenVPN with Active Directory(LDAP). You disable/enable this on the “edit vpn settings” button at: <a href="https://control.tier3.com/Net/Vpn">https://control.tier3.com/Net/Vpn</a>
</p>

<p>If you have authentication enabled and you are unable to connect with your username/password, you will see this in your OpenVPN log:</p>

<p>“<strong>Wed Nov 10 15:14:56 2010 us=515000 SIGUSR1[soft,auth-failure] received, process restarting</strong>
</p>

<p><strong>Wed Nov 10 15:14:56 2010 us=515000 Restart pause, 2 second(s)”</strong>
</p>



<p>You need to verify with CenturyLink Cloud or your Administrator that you are using the right credentials. Your account must also be a member of: ManagedVPN</p>

<p>
  <a name="5"></a>
</p>
<h3>An example of a successful login log</h3>
<p>Tue Nov 09 17:38:22 2010 us=766000 OpenVPN 2.1.1 i686-pc-mingw32 [SSL] [LZO2] [PKCS11] built on Dec 11 2009
  <br />Tue Nov 09 17:38:22 2010 us=766000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 17:38:23 2010 us=297000 Control Channel Authentication: using 'tlsauth.key' as a OpenVPN static key file
  <br />Tue Nov 09 17:38:23 2010 us=297000 Outgoing Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
  <br />Tue Nov 09 17:38:23 2010 us=297000 Incoming Control Channel Authentication: Using 160 bit message hash 'SHA1' for HMAC authentication
  <br />Tue Nov 09 17:38:23 2010 us=297000 LZO compression initialized
  <br />Tue Nov 09 17:38:23 2010 us=297000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 17:38:23 2010 us=297000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 17:38:23 2010 us=297000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 17:38:23 2010 us=297000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 17:38:23 2010 us=297000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 17:38:23 2010 us=297000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 17:38:23 2010 us=297000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 17:38:23 2010 us=297000 UDPv4 link local: [undef]
  <br />Tue Nov 09 17:38:23 2010 us=297000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 17:39:23 2010 us=966000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 17:39:23 2010 us=966000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 17:39:23 2010 us=966000 TCP/UDP: Closing socket
  <br />Tue Nov 09 17:39:23 2010 us=966000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 17:39:23 2010 us=966000 Restart pause, 2 second(s)
  <br />Tue Nov 09 17:39:25 2010 us=962000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 17:39:25 2010 us=962000 Re-using SSL/TLS context
  <br />Tue Nov 09 17:39:25 2010 us=962000 LZO compression initialized
  <br />Tue Nov 09 17:39:25 2010 us=962000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 17:39:25 2010 us=962000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 17:39:25 2010 us=962000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 17:39:25 2010 us=962000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 17:39:25 2010 us=962000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 17:39:25 2010 us=962000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 17:39:25 2010 us=962000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 17:39:25 2010 us=962000 UDPv4 link local: [undef]
  <br />Tue Nov 09 17:39:25 2010 us=962000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 17:40:25 2010 us=87000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 17:40:25 2010 us=87000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 17:40:25 2010 us=87000 TCP/UDP: Closing socket
  <br />Tue Nov 09 17:40:25 2010 us=87000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 17:40:25 2010 us=87000 Restart pause, 2 second(s)
  <br />Tue Nov 09 17:40:27 2010 us=99000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 17:40:27 2010 us=99000 Re-using SSL/TLS context
  <br />Tue Nov 09 17:40:27 2010 us=99000 LZO compression initialized
  <br />Tue Nov 09 17:40:27 2010 us=99000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 17:40:27 2010 us=99000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 17:40:27 2010 us=99000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 17:40:27 2010 us=99000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link local: [undef]
  <br />Tue Nov 09 17:40:27 2010 us=99000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)
  <br />Tue Nov 09 17:41:27 2010 us=799000 TLS Error: TLS handshake failed
  <br />Tue Nov 09 17:41:27 2010 us=799000 TCP/UDP: Closing socket
  <br />Tue Nov 09 17:41:27 2010 us=799000 SIGUSR1[soft,tls-error] received, process restarting
  <br />Tue Nov 09 17:41:27 2010 us=799000 Restart pause, 2 second(s)
  <br />Tue Nov 09 17:41:29 2010 us=812000 NOTE: the current --script-security setting may allow this configuration to call user-defined scripts
  <br />Tue Nov 09 17:41:29 2010 us=812000 Re-using SSL/TLS context
  <br />Tue Nov 09 17:41:29 2010 us=812000 LZO compression initialized
  <br />Tue Nov 09 17:41:29 2010 us=812000 Control Channel MTU parms [ L:1590 D:166 EF:66 EB:0 ET:0 EL:0 ]
  <br />Tue Nov 09 17:41:29 2010 us=812000 Data Channel MTU parms [ L:1590 D:1450 EF:58 EB:135 ET:32 EL:0 AF:3/1 ]
  <br />Tue Nov 09 17:41:29 2010 us=812000 Local Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 1,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-client'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options String: 'V4,dev-type tap,link-mtu 1590,tun-mtu 1532,proto UDPv4,comp-lzo,keydir 0,cipher AES-128-CBC,auth SHA1,keysize 128,tls-auth,key-method 2,tls-server'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Local Options hash (VER=V4): 'a7133b47'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Expected Remote Options hash (VER=V4): 'c5677ab3'
  <br />Tue Nov 09 17:41:29 2010 us=812000 Socket Buffers: R=[8192-&gt;8192] S=[8192-&gt;8192]
  <br />Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link local: [undef]
  <br />Tue Nov 09 17:41:29 2010 us=812000 UDPv4 link remote: 64.94.142.10:1249
  <br />Tue Nov 09 17:42:08 2010 us=266000 TLS: Initial packet from 64.94.142.10:1249, sid=220a1870 10cc7c8c
  <br />Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=1, /C=US/ST=WA/L=Seattle/O=Tier3LLC/CN=WA1RussVPN01-CA/emailAddress=noc@tier3.com
  <br />Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: nsCertType=SERVER
  <br />Tue Nov 09 17:42:08 2010 us=422000 VERIFY OK: depth=0, /C=US/ST=WA/O=Tier3LLC/CN=WA1RussVPN01/emailAddress=noc@tier3.com
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Encrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Cipher 'AES-128-CBC' initialized with 128 bit key
  <br />Tue Nov 09 17:42:08 2010 us=750000 Data Channel Decrypt: Using 160 bit message hash 'SHA1' for HMAC authentication
  <br />Tue Nov 09 17:42:08 2010 us=750000 Control Channel: TLSv1, cipher TLSv1/SSLv3 DHE-RSA-AES256-SHA, 1024 bit RSA
  <br />Tue Nov 09 17:42:08 2010 us=750000 [WA1RussVPN01] Peer Connection Initiated with 64.94.142.10:1249
  <br />Tue Nov 09 17:42:10 2010 us=403000 SENT CONTROL [WA1RussVPN01]: 'PUSH_REQUEST' (status=1)
  <br />Tue Nov 09 17:42:10 2010 us=434000 PUSH: Received control message: 'PUSH_REPLY,route 10.80.113.0 255.255.255.0 10.80.134.1,route-gateway 10.80.134.230,ping 10,ping-restart 120,ifconfig 10.80.134.231 255.255.255.0'
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: timers and/or timeouts modified
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: --ifconfig/up options modified
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route options modified
  <br />Tue Nov 09 17:42:10 2010 us=434000 OPTIONS IMPORT: route-related options modified
  <br />Tue Nov 09 17:42:10 2010 us=466000 ROUTE default_gateway=192.168.0.1
  <br />Tue Nov 09 17:42:10 2010 us=481000 TAP-WIN32 device [Local Area Connection 5] opened: \\.\Global\{E026A80A-7CB5-41F7-8ADA-EA136D0C7957}.tap
  <br />Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 Driver Version 9.6
  <br />Tue Nov 09 17:42:10 2010 us=481000 TAP-Win32 MTU=1500
  <br />Tue Nov 09 17:42:10 2010 us=497000 Notified TAP-Win32 driver to set a DHCP IP/netmask of 10.80.134.231/255.255.255.0 on interface {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} [DHCP-serv: 10.80.134.0, lease-time: 31536000]
  <br />Tue Nov 09 17:42:10 2010 us=497000 NOTE: FlushIpNetTable failed on interface [101] {E026A80A-7CB5-41F7-8ADA-EA136D0C7957} (status=5) : Access is denied.
  <br />Tue Nov 09 17:42:15 2010 us=317000 TEST ROUTES: 1/1 succeeded len=1 ret=1 a=0 u/d=up
  <br />Tue Nov 09 17:42:15 2010 us=333000 C:\WINDOWS\system32\route.exe ADD 10.80.113.0 MASK 255.255.255.0 10.80.134.1
  <br />Tue Nov 09 17:42:15 2010 us=348000 ROUTE: route addition failed using CreateIpForwardEntry: Access is denied. [status=5 if_index=101]
  <br />Tue Nov 09 17:42:15 2010 us=348000 Route addition via IPAPI failed [adaptive]
  <br />Tue Nov 09 17:42:15 2010 us=348000 Route addition fallback to route.exe
  <br />Tue Nov 09 17:42:15 2010 us=411000 ERROR: Windows route add command failed [adaptive]: returned error code 1
  <br />Tue Nov 09 17:42:15 2010 us=411000 Initialization Sequence Completed</p>