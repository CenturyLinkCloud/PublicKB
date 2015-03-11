{{{
  "title": "Steps to Install a Headless GNOME GUI Desktop on Ubuntu Server and Then Remote Control Server Desktop with TightVNC",
  "date": "11-22-2013",
  "author": "Dave Burkhardt",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The following instructions provide a detailed step-by-step instructions for CenturyLink Cloud’s customers who wish to provision a GUI desktop on their Ubuntu servers, and then run a remote desktop application (TightVNC) to control the desktop.</p>
<p>Note: Installing any desktop GUI on a Linux server is generally not recommended since these desktop GUI applications can slightly impact the performance of the server. Hence, CenturyLink Cloud does not provision Linux GUI desktops by default. Although, administrators who are new to Linux operating systems may find using a desktop GUI (and the associated tools that is installed with the desktop) easier to use than a Linux command line interface.</p>

<h3>Steps to Install a Headless GNOME GUI Desktop on Ubuntu Server and Then Remote Control Server Desktop with TightVNC</h3>

<ol>
  <li>Create an Ubuntu server in CenturyLink Cloud’s Control Portal</li>
  <li>Establish an OpenVPN tunnel to your CenturyLink Cloud servers (see Quick Start Guide for details), and start an SSH client (The instructions below will utilize PuTTY, see the following URL to download: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
  and enter IP address of server created in Step 1
  </li>
  <li>Type in the ID and password created in Step 1
  <br />
  <br />Note: Linux is case sensitive! Also, for the following steps do not type the [ ] symbols – ONLY the text in-between (unless stated other)
  </li>
  <li>Type: [apt-get install tightvncserver] and select the enter key.
  </li>
  <li>Type: [cd /etc/init.d] and select the enter key.
  </li>
  <li>Type: [nano vncserver] and select the enter key.
  </li>
  <li>Paste the following text (in bold - including the [ ] symbols) into the window – Tip: Here are the steps to paste text in Nano:
  <ol>
    <li>Highlight text below in bold and select copy (including the [ ] symbols):</li>
    <li>Make sure no text exists in the nano vncserver file</li>
    <li>Right click with your mouse in the PuTTY window and text below should now be listed in the vncserver file</li>
    <li>Hold down the ctrl key and the x key, select y to save changes, and then enter
    <pre>
    #!/bin/sh -e
    ### BEGIN INIT INFO
    # Provides: vncserver
    # Required-Start: networking
    # Default-Start: 3 4 5
    # Default-Stop: 0 6
    ### END INIT INFO

    PATH="$PATH:/usr/X11R6/bin/"

    # The Username:Group that will run VNC
    export USER="root"
    #${RUNAS}

    # The display that VNC will use
    DISPLAY="1"

    # Color depth (between 8 and 32)
    DEPTH="16"

    # The Desktop geometry to use.
    #GEOMETRY="<WIDTH>x<HEIGHT>"
    #GEOMETRY="800x600"
    GEOMETRY="1024x768"
    #GEOMETRY="1280x1024"

    # The name that the VNC Desktop will have.
    NAME="my-vnc-server"

    OPTIONS="-name ${NAME} -depth ${DEPTH} -geometry ${GEOMETRY} :${DISPLAY}"

    . /lib/lsb/init-functions

    case "$1" in
    start)
    log_action_begin_msg "Starting vncserver for user '${USER}' on localhost:${DISPLAY}"
    su ${USER} -c "/usr/bin/vncserver ${OPTIONS}"
    ;;

    stop)
    log_action_begin_msg "Stoping vncserver for user '${USER}' on localhost:${DISPLAY}"
    su ${USER} -c "/usr/bin/vncserver -kill :${DISPLAY}"
    ;;

    restart)
    $0 stop
    $0 start
    ;;
    esac

    exit 0
    </pre>
  </li>
  <li>Type: [vncserver] and select the enter key.
  </li>
  <li>You will be prompted to create a TightVNC server password – type in a password (and also make note of it since you will need it every time you logon to remote control your desktop).
  </li>
  <li>Type: [chmod 775  vncserver] and select the enter key.
  </li>
  <li>Type: [update-rc.d vncserver defaults] and select the enter key.
  </li>
  <li>Type: [cd ~/.vnc] and select the enter key.
  </li>
  <li>Type: [nano xstartup] and make sure the xstartup file says exactly the text in bold (including the [ ] symbols):
  <pre>
  #!/bin/sh

  # Uncomment the following two lines for normal desktop:
  # unset SESSION_MANAGER
  # exec /etc/X11/xinit/xinitrc

  #[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
  #[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
  #xsetroot -solid grey
  #vncconfig -iconic &
  #xterm -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &

  unset SESSION_MANAGER
  sh /etc/X11/xinit/xinitrc
  </pre>
  </li>
  <li>Type: [apt-get update] and select the enter key.
  </li>
  <li>Install GNOME desktop by typing: [apt-get install ubuntu-desktop] and select the enter key and yes when prompted. Note: This step takes about 15-20 mins to complete.
  </li>
  <li>Connecting with TightVNC:
  <ol>
    <li>Install TightVNC on your Windows desktop (see http://sourceforge.net/projects/vnc-tight/)</li>
    <li>From PuTTY (ensure you are connected to your Linux server still via the OpenVPN client - see steps 2 &amp; 3 above) type: [vncserver] and select the enter key.</li>
    <li>Take note of the desktop number. In example output below, the desktop number is 2:
    <pre>“New 'X' desktop is WA1BTDIDJB02:2”
Note: The desktop number coordinates with TCP port number you will configure later</pre></li>
    <li>Click on top left corner of your PuTTY window and select Change Settings</li>
    <li>Chose SSH and then Tunnels</li>
    <li>Type 5902 for the source port (note: if you received another number than 2 you will need to replace the 2 in the number 5902 – e.g., desktop number 5 would be 5905. Also, you would use this 5905 in the following steps as well if you received desktop number 5)</li>
    <li>At Destination type: localhost:5902</li>
    <li>Select Add, and then Apply</li>
    <li>Start TightVNC and type: [localhost:5902]</li>
    <li>Select Connect, and type in the password you created in Step 9</li>
    <li>You now should now be able to remote control a GNOME desktop</li>
    <li>Repeat steps b-k every time you need to reconnect to your GNOME desktop.</li>
  </ol>
  </li>
</ol>


  <p>Important Note: It is not recommended as a Linux administration best practice to utilize root, and individual user accounts should be provisioned when accessing/managing a systems. The instructions above were written in the simplest terms in mind, hence why steps instructed to utilize the "root" users account. The steps below provide instructions for creating a user account, and then how to access the aforementioned GNOME GUI via TightVNC.

<ol>
  <li>Follow steps b-k to render a GNOME desktop</li>
  <li>Select System, Administration, and then Users and Groups from the GNOME desktop</li>
  <li>Type in a user name and select Ok</li>
  <li>Create a password and chose Ok</li>
  <li>If you want the user to be an administrator of the system, select "change", click "Administrator", and then Ok</li>
  <li>Close TightVNC and and then within the SSH/PuTTY session type [logout] and enter</li>
  <li>Start a new PuTTY session and connect to your Linux server using the credentials you created in the 3 &amp; 4, and then type: [vncserver] and select the enter key.</li>
  <li>You will be asked to create a vncserver password for your new user</li>
  <li>Follow steps c-k above</li>
</ol>
</p>
