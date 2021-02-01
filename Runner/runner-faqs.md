{{{
  "title": "FAQs: Runner",
  "date": "06-29-2018",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

#### Audience

This article is to support customers of Runner, a product that enables teams, developers, and engineers to quickly provision, interact, and modify their environments anywhere - Lumen Cloud, third-party cloud providers, and on-premises.  Additionally, the responses in this FAQ document are specific to using the service through the Control Portal.

#### FREQUENTLY ASKED QUESTIONS

**Q: Do I need a Lumen Cloud account to use the Runner tools?**

A: Yes, you will need a Lumen Cloud account. If you don't already have an account with us, you can start with a [free 30 day trial](https://www.ctl.io/free-trial/) to help kick the tires.

**Q: How can I use Runner services against resources present in other cloud providers or on-prem environment?**

**A:** To run Ansible playbooks against other cloud providers, users would need to install and run the Runner Minion. The Runner Minion is available as a product in the Runner Marketplace for AWS users and it's available on DockerHub for other cloud and on-premise environments.  Please refer to the [Runner Minion KB](https://www.ctl.io/knowledge-base/runner/runner-minion) for more information.

**Q: How can I check the status of my playbook execution?**

**A:** Status of Job execution can be retrieved in either of following ways:
- By registering the job document with a call back url at the time of creating the job
- By making HTTPs calls directly to our status-api

**Q: Can I run a playbook from a private Github repository?**

**A:** Absolutely! Credentials capable of pulling the repository will need to be provided in the payload sent to the Runner’s Job Service. The code block would look similar to this:

```json
"repository": {
    "url": "https://github.com/your_playbook.git",
    "ref":"master",
    "credentials": {
        "username": "your.username",
        "password": "password_to_your_username"
    },
    "defaultPlaybook": "site.yml"
}
```

**Q: Will I be able to use Runner to manage my Lumen Cloud resources?**

**A:** Yes our services use the underlying Lumen Cloud APIs to let you manage your resources in Lumen Cloud. In addition, you can use our services to manage your resources on third-party cloud providers, and on-premises.

**Q: I previously defined a job, how do I execute it again?**

**A:** You can use the job id of the previously created job to start another execution of that job. Simply POST a request as described in the documentation "Start a Job"

Because our Runner’s Job services do not persist any private keys related to the job, you will need to send that information as well if required. For example:

```json
 { "sshPrivateKey":"LS0tLS1CRUdJTiBSU0EgUFJJVkFURS..." }
```

**Q: How much will Runner cost me?**

**A:** Runner is a "freemium" service. You are free to use Runner to manage and execute all your Ansible jobs regardless of cloud. Charges apply only for features such as priority jobs.

**Q: Is there a maximum number of concurrent jobs I can have running?**

**A:** Yes, the maximum number of concurrent jobs is four (4).

**Q: How do I handle this error?**

`ERROR: clc_server is not a legal parameter in an Ansible task or handler`

**A:** This error indicates that your environment isn’t fully set up.

Ansible requires explicitly including non-core modules via a library path. (see docs)

Here are two recommended ways for solving this issue:

1. Update the ANSIBLE_LIBRARY environment variable as such ANSIBLE_LIBRARY=/path/to/installed/module
2. Configure the library setting in ansible.cfg. This file is found in /etc but you can also define this file local to your workspace.

**Q: In case of a Job execution failure, where should I look to get more information related to the failure?**

**A:** When you see the execution status as `FAILURE` or `INIT_FAILURE`, then follow the below steps to find out more details on the cause for failure,

Query the status for your execution and then:

* First look for event_type=playbook_result and look for the message in that json block
* Based on the above message you can further narrow down to the actual error message by looking for event_type=runner_on_failed or event_type=runner_on_unreachable or event_type=runner_on_async_failed and get the corresponding message in that json block

**Q: Can I configure my Runner jobs to be executed in a schedule?**

**A:** Yes you could schedule the jobs, please refer the API documentation for more details Job Schedule

**Q: What timezone are Runner jobs executing in?**

**A:** Runner jobs are configured to run relative to the timezone of the browser that's used to create them. If your browser leverages the timezone of the OS, and you're in the Pacific timezone, then the Runner jobs will be in PDT and so you'll want to account for that if you're setting up jobs against servers in other timezones.  

**Q: My Job is still RUNNING, is there a way for me to check the tasks completed and their statuses?**

**A:** Absolutely, there are couple of ways you can check status of an execution at any state:

* Status API – You can also view detailed status of the execution via Status API
* Webhooks – You could check the status via the webhook, if you have specified the details in the call back entity while creating the job

**Q: How do I provide feedback?**

A: If you have questions or feedback, please submit them to our team by emailing [help@ctl.io](mailto:help@ctl.io).
