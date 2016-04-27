{{{
  "title": "FAQs: Runner",
  "date": "04-27-2016",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}


#### Audience

This article is to support customers of Runner, a product that enables teams, developers, and engineers to quickly provision, interact, and modify their environments anywhere - CenturyLink Cloud, third-party cloud providers, and on-premises.  Additionally, the responses in this FAQ document are specific to using the service through the Control Portal.


## FREQUENTLY ASKED QUESTIONS

###### Q: Do I need a CenturyLink Cloud account to use the Runner tools?

A: Yes, you will need a CenturyLink Cloud account. You can start with a free 30 day trial to help kick the tires. However, although you need a CenturyLink Cloud account so you can use the Runner tools against system resources you have on site or with other cloud providers.

###### Q: How can I use Runner services against resources in other cloud providers or my on-premises environment?

A: To run Ansible playbooks against other cloud providers, users would need to leverage the VPN service which would help to provide the necessary VPN connections for accessing third party cloud providers. Runner will establish the VPN connections before the playbook execution if any such connections exist for the account.

###### Q: How can I check the status of my playbook execution?

A: Status of Job execution can be retrieved in either of following ways:
- By registering the job document with a call back url at the time of creating the job
- By making HTTPs calls directly to our status-api

###### Q: Can I run a playbook from a private Github repository?

A: Absolutely! Credentials capable of pulling the repository will need to be provided in the payload sent to the Runner’s Job Service. The code block would look similar to this:

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

###### Q: Will I be able to use Runner to manage my CenturyLink Cloud resources?

A: Yes our services use the underlying Centurylink Cloud APIs to let you manage your resources in Centurylink Cloud. In addition, you can use our services to manage your resources on third-party cloud providers, and on-premises.

###### Q: I previously defined a job, how do I execute it again?

A: You can use the job id of the previously created job to start another execution of that job. Simply POST a request as described in the documentation

Start a Job

Because our Runner’s Job services do not persist any private keys related to the job, you will need to send that information as well if required. For example:

```json
 { "sshPrivateKey":"LS0tLS1CRUdJTiBSU0EgUFJJVkFURS..." }
```

###### Q: How do I provide feedback?

A: If you have questions or feedback, please submit them to our team by emailing [runner-help@ctl.io](mailto:runner-help@ctl.io).
