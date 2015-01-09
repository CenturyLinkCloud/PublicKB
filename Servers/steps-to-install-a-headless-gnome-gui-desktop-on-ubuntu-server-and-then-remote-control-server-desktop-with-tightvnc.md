{{{
  "title": "Steps to Install a Headless GNOME GUI Desktop on Ubuntu Server and Then Remote Control Server Desktop with TightVNC",
  "date": "11-22-2013",
  "author": "Dave Burkhardt",
  "attachments": []
}}}

<p>The following instructions provide a detailed step-by-step instructions for Tier 3’s customers who wish to provision a GUI desktop on their Ubuntu servers, and then run a remote desktop application (TightVNC) to control the desktop.
  <br />&nbsp;
  <br />Note: Installing any desktop GUI on a Linux server is generally not recommended since these desktop GUI applications can slightly impact the performance of the server. Hence, Tier 3 does not provision Linux GUI desktops by default. Although, administrators
  who are new to Linux operating systems may find using a desktop GUI (and the associated tools that is installed with the desktop) easier to use than a Linux command line interface.
  <br />&nbsp;
  <br />Steps to Install a Headless GNOME GUI Desktop on Ubuntu Server and Then Remote Control Server Desktop with TightVNC:
  <br />1. Create an Ubuntu server in Tier 3’s Control Portal (see Quick Start Guide for additional details - <a href="../../../entries/20533612-tier-3-quick-start-guide">http://help.tier3.com/entries/20533612-tier-3-quick-start-guide</a>)
  <br />&nbsp;
  <br />2. Establish an OpenVPN tunnel to your Tier 3 servers (see Quick Start Guide for details), and start an SSH client (The instructions below will utilize PuTTY, see the following URL to download: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)&nbsp;
  and enter IP address of server created in Step 1
  <br />&nbsp;
  <br />3. Type in the ID and password created in Step 1
  <br />&nbsp;
  <br />Note: Linux is case sensitive! Also, for the following steps do not type the [ ] symbols – ONLY the text in-between (unless stated other)
  <br />&nbsp;
  <br />4. Type: [apt-get install tightvncserver] and select the enter key.
  <br />&nbsp;
  <br />5. Type: [cd /etc/init.d] and select the enter key.
  <br />&nbsp;
  <br />6. Type: [nano vncserver] and select the enter key.
  <br />&nbsp;
  <br />7. Paste the following text (in bold - including the [ ] symbols) into the window – Tip: Here are the steps to paste text in Nano:
  <br />a. Highlight text below in bold and select copy (including the [ ] symbols):
  <br />b. Make sure no text exists in the nano vncserver file
  <br />c. Right click with your mouse in the PuTTY window and text below should now be listed in the vncserver file
  <br />d. Hold down the ctrl key and the x key, select y to save changes, and then enter
  <br /><strong>#!/bin/sh -e</strong>
  <br /><strong>### BEGIN INIT INFO</strong>
  <br /><strong># Provides:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; vncserver</strong>
  <br /><strong># Required-Start:&nbsp;&nbsp;&nbsp; networking</strong>
  <br /><strong># Default-Start:&nbsp;&nbsp;&nbsp;&nbsp; 3 4 5</strong>
  <br /><strong># Default-Stop:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0 6</strong>
  <br /><strong>### END INIT INFO</strong>
  <br />&nbsp;
  <br /><strong>PATH="$PATH:/usr/X11R6/bin/"</strong>
  <br />&nbsp;
  <br /><strong># The Username:Group that will run VNC</strong>
  <br /><strong>export USER="root"</strong>
  <br /><strong>#${RUNAS}</strong>
  <br />&nbsp;
  <br /><strong># The display that VNC will use</strong>
  <br /><strong>DISPLAY="1"</strong>
  <br />&nbsp;
  <br /><strong># Color depth (between 8 and 32)</strong>
  <br /><strong>DEPTH="16"</strong>
  <br />&nbsp;
  <br /><strong># The Desktop geometry to use.</strong>
  <br /><strong>#GEOMETRY="&lt;WIDTH&gt;x&lt;HEIGHT&gt;"</strong>
  <br /><strong>#GEOMETRY="800x600"</strong>
  <br /><strong>GEOMETRY="1024x768"</strong>
  <br /><strong>#GEOMETRY="1280x1024"</strong>
  <br />&nbsp;
  <br /><strong># The name that the VNC Desktop will have.</strong>
  <br /><strong>NAME="my-vnc-server"</strong>
  <br />&nbsp;
  <br /><strong>OPTIONS="-name ${NAME} -depth ${DEPTH} -geometry ${GEOMETRY} :${DISPLAY}"</strong>
  <br />&nbsp;
  <br /><strong>. /lib/lsb/init-functions</strong>
  <br />&nbsp;
  <br /><strong>case "$1" in</strong>
  <br /><strong>start)</strong>
  <br /><strong>log_action_begin_msg "Starting vncserver for user '${USER}' on localhost:${DISPLAY}"</strong>
  <br /><strong>su ${USER} -c "/usr/bin/vncserver ${OPTIONS}"</strong>
  <br /><strong>;;</strong>
  <br />&nbsp;
  <br /><strong>stop)</strong>
  <br /><strong>log_action_begin_msg "Stoping vncserver for user '${USER}' on localhost:${DISPLAY}"</strong>
  <br /><strong>su ${USER} -c "/usr/bin/vncserver -kill :${DISPLAY}"</strong>
  <br /><strong>;;</strong>
  <br />&nbsp;
  <br /><strong>restart)</strong>
  <br /><strong>$0 stop</strong>
  <br /><strong>$0 start</strong>
  <br /><strong>;;</strong>
  <br /><strong>esac</strong>
  <br />&nbsp;
  <br /><strong>exit 0</strong>
  <br />&nbsp;
  <br />8. Type: [vncserver] and select the enter key.
  <br />&nbsp;
  <br />9. You will be prompted to create a TightVNC server password – type in a password (and also make note of it since you will need it every time you logon to remote control your desktop).
  <br />&nbsp;
  <br />10. Type: [chmod 775&nbsp; vncserver] and select the enter key.
  <br />&nbsp;
  <br />11. Type: [update-rc.d vncserver defaults] and select the enter key.
  <br />&nbsp;
  <br />12. Type: [cd ~/.vnc] and select the enter key.
  <br />&nbsp;
  <br />13. Type: [nano xstartup] and make sure the xstartup file says exactly the text in bold (including the [ ] symbols):
  <br /><strong>#!/bin/sh</strong>
  <br />&nbsp;
  <br /><strong># Uncomment the following two lines for normal desktop:</strong>
  <br /><strong># unset SESSION_MANAGER</strong>
  <br /><strong># exec /etc/X11/xinit/xinitrc</strong>
  <br />&nbsp;
  <br /><strong>#[ -x /etc/vnc/xstartup ] &amp;&amp; exec /etc/vnc/xstartup</strong>
  <br /><strong>#[ -r $HOME/.Xresources ] &amp;&amp; xrdb $HOME/.Xresources</strong>
  <br /><strong>#xsetroot -solid grey</strong>
  <br /><strong>#vncconfig -iconic &amp;</strong>
  <br /><strong>#xterm -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &amp;</strong>
  <br />&nbsp;
  <br /><strong>unset SESSION_MANAGER</strong>
  <br /><strong>sh /etc/X11/xinit/xinitrc</strong>
  <br />&nbsp;
  <br />14. Type: [apt-get update] and select the enter key.
  <br />&nbsp;
  <br />15. Install GNOME desktop by typing: [apt-get install ubuntu-desktop] and select the enter key and yes when prompted. Note: This step takes about 15-20 mins to complete.
  <br />&nbsp;
  <br />16. Connecting with TightVNC:
  <br />a. Install TightVNC on your Windows desktop (see http://sourceforge.net/projects/vnc-tight/)
  <br />b. From PuTTY (ensure you are connected to your Linux server still via the OpenVPN client - see steps 2 &amp; 3 above) type: [vncserver] and select the enter key.
  <br />c. Take note of the desktop number. In example output below, the desktop number is 2:
  <br />“New 'X' desktop is WA1BTDIDJB02:2”
  <br />Note: The desktop number coordinates with TCP port number you will configure later
  <br />d. Click on top left corner of your PuTTY window and select Change Settings
  <br />e. Chose SSH and then Tunnels
  <br />f. Type 5902 for the source port (note: if you received another number than 2 you will need to replace the 2 in the number 5902 – e.g., desktop number 5 would be 5905. Also, you would use this 5905 in the following steps as well if you received desktop
  number 5)
  <br />g. At Destination type: localhost:5902
  <br />h. Select Add, and then Apply
  <br />i. Start TightVNC and type: [localhost:5902]
  <br />j. Select Connect, and type in the password you created in Step 9
  <br />k. You now should now be able to remote control a GNOME desktop
  <br />&nbsp;
  <br />Repeat steps b-k every time you need to reconnect to your GNOME desktop.
  <br />
  <br />Important Note: It is not recommended as a Linux administration best practice to utilize root, and individual user accounts should be provisioned when accessing/managing a systems. The instructions above were written in the simplest terms in mind, hence
  why steps instructed to utilize the "root" users account.&nbsp; The steps below provide instructions for creating a user account, and then how to access the aforementioned GNOME GUI via TightVNC:
  <br />1. Follow steps b-k to render a GNOME desktop
  <br />2. Select System, Administration, and then Users and Groups from the GNOME desktop
  <br />3. Type in a user name and select Ok
  <br />4. Create a password and chose Ok
  <br />5. If you want the user to be an administrator of the system, select "change", click "Administrator", and then Ok
  <br />6. Close TightVNC and and then within the SSH/PuTTY session type [logout] and enter
  <br />7. Start a new PuTTY session and connect to your Linux server using the credentials you created in the 3 &amp; 4, and then type: [vncserver] and select the enter key.
  <br />8. You will be asked to create a vncserver password for your new user
  <br />9. Follow steps c-k above
  <br />
  <br />
</p>