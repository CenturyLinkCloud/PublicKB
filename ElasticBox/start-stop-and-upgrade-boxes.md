{{{ "title": "Install, Configure, and Other Events",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

**In this article:**

* Box events
* Event types
* Event execution order
* Event error codes
* Windows return codes

### Box Events

The lifecycle of a service or application is managed virtually by box events like install, configure, start, stop, and dispose. Each event corresponds to its event script type on the box. ElasticBox supports writing event scripts in all languages supported by the base Linux and Windows base images. These include Bash, PowerShell, Salt, Ansible, Chef, and Puppet.

The ElasticBox agent executes and stores the output of the event scripts in a default directory in the virtual machine instance: /var/elasticbox/<instance_id> where instance_id is the ID of the instance. You can refer to this directory as ${folder} in the event scripts to move the output of the executed scripts elsewhere.

### Event Types

There are five types of events on a box. Each event executes depending on the [action](../ElasticBox/instances.md) triggered on a box instance.

**Install**

This installs the box. It’s run when you click deploy on a box and also when you click reinstall on an instance. Use it for install or upgrade tasks like setting up a Java, Ruby, or Python runtime environment.

**Configure**

This handles the initial install and is run after install events. It’s also run when you click Reconfigure on an instance. Use it to reboot the virtual server (using the server command line), start the server from the ElasticBox instance page, and add or remove instance nodes when managed through AWS auto scaling. The event must contain tasks that occur multiple times over the life of a box instance, such as configuring and maintaining connectivity between application tiers.

**Start**

This starts a service. It’s run after configure events and is also triggered when you click Power On on an instance or when the virtual server reboots. The event must contain tasks to start a service.

**Stop**

This cleanly shuts down a service. It’s run when you click Shut Down on an instance. The event must contain tasks to cleanly shutdown a service.

**Dispose**

It’s run when you click Terminate on a successfully deployed instance. The event must contain tasks that clean up the instance before it’s deleted. Examples include de-registering agents and collecting logs and stateful data.

### Event Execution Order

ElasticBox executes events in the order they’re displayed in the box events section. For example, this box nests a git box which in turn nests a git repo box. If we expand the events, we can see the order in which the scripts execute at deploy time.

![installconfigureandotherevents1.png](../images/ElasticBox/installconfigureandotherevents1.png)

See how each event has a pre-event type. The install has pre_install, configure has pre_configure, and so on. Pre-events fulfill certain conditions before performing the next step. For example, you may want use the pre-event to install dependencies or download files or create folders and directories. Pre-events always run before child box events.

### Event Error Codes

It’s good practice to use exit error codes in events to indicate if a task ran successfully or not on an instance. For example, you can return a 1 to indicate an error and write what caused the error to the instance logs.

In both Windows and Linux event shell scripts, ElasticBox understands three types of exit codes that affect the instance state.

|  Use Code  |  To indicate  |   Description   |  Instance State  |
|------------|---------------|-----------------|------------------|
| 0 | Success | Script returns a zero. | Instance is online and available. |
| Non-zero | Failure | Elasticbox fails the event script that returned non-zero. | Instance is unavailable. |
| 100 | Reboot | Indicates that you want to reboot the service or virtual macine. The agent goes into sleep mode waiting for the reboot to complete. To reboot, run the reboot command for the OS type. For example, in Linux it is reboot, in Windows PowerShell it is Restart-computer. | Instance state unaffected. |

**Examples**

This sample shell script checks if a puppet configuration file has executed successfully. If not, the snippet returns the standard error code 1 to indicate an error. The error message from the echo command is recorded in the instance logs. sdsdds

```
puppetfile=`curl -k -s $PUPPET_DEFAULT`
if [ $(echo $puppetfile | wc -c) -gt 1 ]; then
echo "$puppetfile" | elasticbox config | puppet apply -v --detailed-exitcodes --modulepath=$folder/$MODULES_DIRECTORY --templatedir $folder/$TEMPLATES_DIRECTORY
if ! [[ ($? == 0) || ($? == 2) ]]; then
echo "Error: Failed to apply your PuppetDefault configuration file."
exit 1
fi
else
echo "Error: Failed to download PuppetDefault configuration file."
exit 1
fi
```

Here’s another script sample that uses the 0 exit code to indicate that the command completed successfully when connectivity to the Nginx machine is active.

```
# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0
nginx="/usr/local/sbin/nginx"
prog=$(basename $nginx)
NGINX_CONF_FILE="/usr/local/nginx/conf/nginx.conf"
lockfile=/var/lock/subsys/nginx
```

### Windows Return Codes

On Windows machines, we run commands using the PowerShell File parameter.

* When the File parameter encounters fatal errors, it stops running a command but doesn’t return an exit error code.

* When it encounters non-fatal errors, it continues on to the next operation without returning an error code by default.

To work around these limitations and capture errors in the instance, we suggest returning event codes for fatal, non-fatal errors and exceptions:

* Make fatal errors return an error code other than 0.

* Also treat non-fatal errors as fatal to capture them in the ElasticBox instance logs and reflect the true state of the instance. Optionally, apply the same workaround to capture exceptions.

As you can see in this example, the trap lines return an exit code other than 0 to report the error. The first line makes the execution stop at any error. ElasticBox logs show the errors and renders the related VM instance in an unavailable state.

```
$ErrorActionPreference="Stop"
trap {
        Write-Warning $_
        exit 1
}
```

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](../ElasticBox/troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
