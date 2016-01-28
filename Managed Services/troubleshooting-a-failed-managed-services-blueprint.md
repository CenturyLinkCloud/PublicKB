{{{
  "title": "Troubleshooting a Failed Managed Services Blueprint",
  "date": "01-13-2016",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Behind the scenes, making a server managed or installing a managed application requires the coordination of diverse components and, while  provisioning has a good success rate, it is possible your server may experience issues with one of the dependencies. The following steps are refined versions of what users have done to assist with the troubleshooting process and expedite the management of your server.

The assumption of this article is that your Blueprint never completed.

### Prerequisites

* An understanding of how to make a server managed, either from [scratch](../Managed Services/created-a-managed-server-now-what.md) or by [converting](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md) an un-managed server to a managed one.

### Steps

If a Managed Services OS Blueprint does not complete as expected, please note the OS and the time the Blueprint was attempted. RHEL Managed Services Blueprints will fail from 9am to 10am UTC as a result of regular maintenance in our managed services infrastructure. Please wait one hour before attempting again. If that is not the issue, follow these steps to expedite troubleshooting.


1. Navigate to the Control Portal Deployment Queue
2. On the Deployment Queue page, click the pull-down list and select the correct data center.
3. Click the radio buttons to find the relevant job and status.
4. If your request is in failed status, click on the request to see additional details.
5. Click Resume to try to run the request from the point of failure.
6. If the issue occurs while running a CLC Blueprint for a Managed Application and the Blueprint fails again after Resuming:
 * If the Blueprint failed at either the step of “Validate Blueprint” or “Reserve Blueprint” call Support at 1-888-638-6771 and notify us about the step the Blueprint failed (such as “Install Managed MS SQL”) and approximate dates and times when you attempted to resume it.
 * If the Blueprint failed after “Reserve Blueprint,” expand the step where the error failed by clicking on it.You may be able to further expand the errant step to see details of the error:
 ![Error Detail](https://t3n.zendesk.com/attachments/token/8L7RLq5vFql23Ai1M2rWlKRdi/?name=Error_Details.png)

  * Call Support at 1-888-638-6771. Please notify us about the step the Blueprint failed (such as “Install Managed MSSQL”) and approximate dates and times when you attempted to resume it.

7. If the issue occurs during Server Creation for a VM you are attempting to “Make Managed” and the job fails at the same point a second time, continue to troubleshoot by seeing if the Blueprint failed at or prior to the "Apply CTS customizations" step.

  * If the Blueprint failed **at** the step called "Apply CTS customizations to ______." (The blank would be specific to the OS.) &nbsp;If this is the case call Support at 1-888-638-6771.Please also note what step the Blueprint failed and approximate
  dates and times when you attempted to Resume it.
  * if Blueprint failed **prior** to a step called "Apply CTS customizations to ______." (The blank would be specific to an Operating System) If so, it is possibly a resource issue. Please check the main dashboard to determine if you have exceeded resource limits.
  ![Dashboard](https://t3n.zendesk.com/attachments/token/8Zk9V4VvIYIhGI2ZcUAbvXRax/?name=Resource_Check.png)
  If it is a resource issue and you require more resources, please adjust accordingly or request limit increases from your account administrator.
  * If it is not a resource issue, please contact Support at 1-888-638-6771. Please also note the step the Blueprint failed and approximate dates and times you attempted to Resume it.
