{{{
  "title": "WordPress Technical Specifications",
  "date": "07-17-2015",
  "author": "Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}
### IMPORTANT NOTECenturyLink Cloud WordPress hosting is currently in a Limited Beta program with specific customers by invitation only and is not intended for production usage.During the Limited Beta there is no production Service Level Agreement.
##Overview

CenturyLink Cloud WordPress as a Service runs in the CenturyLink Cloud utilizing the latest stable WordPress release.  System Specifactions and limitations have been chosen to maximize uptime, fulfill business needs, and ensure the security of customer's sites.

##System Specifications

####Microsite Plan Specifications

* Server Specs

  * Disk Space - 1GB
  * RAM - 128MB

* Software Specs
  * Nginx
  * MySQL
  * phpMyAdmin

####Business Plan Specifications

_future product_
  
####Enterprise Plan Specifications

  _future product_
  
##Disallowed Services

**phpmail()** is unauthenticated and not allowed on CenturyLink Cloud WordPress as a service.  [SMTP can be configured using a plugin](wordpress-SMTP-Configuration.md) to send mail from within WordPress.


##Disallowed php functions

Many php Functions have been found to be WordPress security vulnerabilities, and these fucntions have been disabled for CenturyLink Cloud WordPress

* **dl** - Loads a PHP extension at runtime
* **exec** - Execute an external program
* **link** - Create a hard link
* **mail** - Send mail
* **passthru** - Execute an external program and display raw output
* **pclose** - Closes process file pointer
* **pcntl_exec** - Executes specified program in current process space
* **popen** - Opens process file pointer
* **posix_getpwuid** - Return info about a user by user id
* **posix_kill** - Send a signal to a process
* **posix_mkfifo** - Create a fifo special file (a named pipe)
* **posix_setpgid** - Set process group id for job control
* **posix_setsid** - Make the current process a session leader
* **posix_setuid** - Set the UID of the current process
* **posix_uname** - Get system name
* **proc_close** - Close a process opened by proc\_open() and return the exit code of that process
* **proc\_get\_status** - Get information about a process opened by proc_open()
* **proc_nice** - Change the priority of the current process
* **proc_open** - Execute a command and open file pointers for input/output
* **proc\_terminate** - Kills a process opened by proc_open
* **shell_exec** - Execute command via shell and return the complete output as a string
* **show\_source** - Alias of highlight_file()
* **symlink** - Creates a symbolic link
* **system** - Execute an external program and display the output