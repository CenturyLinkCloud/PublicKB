{{{
  "title": "Runner Job Service",
  "date": "04-27-2016",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

#### Audience

This article is to support customers of Runner, a product that enables teams, developers, and engineers to quickly provision, interact, and modify their environments anywhere - CenturyLink Cloud, third-party cloud providers, and on-premises.  Additionally, the responses in this FAQ document are specific to using the service through the Control Portal.

#### Job Service Overview

The Job Service is the primary component of the Runner product. Users can create, modify, and execute jobs at anytime. Many of the other services were created in tandem with the Job Service, and enhance the Job Execution capabilities. The Job Service accepts a payload that references a playbook to be used, whether that is using a public or private GitHub repository. When using a private GitHub repository, GitHub credentials are required.

The Job Service is a simple, text-based job and task definition. The jobs are executed by a highly available ~~job runner~~ service with the ability to execute massively parallel tasks. It also provides the capability to schedule jobs at a defined interval.

The job actions can be performed via REST API calls. The API works with JSON messages over HTTP**S**. It relies on the standard HTTP verbs including GET, POST, PUT, and DELETE.

The URL format of the service is: `https://api.runner.ctl.io/{resource}/{account alias}`.

For example, to retrieve all the Jobs created at the account alias level, you would issue a GET request to https://api.runner.ctl.io/jobs/ABCD. The HTTP request must include headers Content-Type (set to application/json) and Authorization (set to ‘Bearer Token from authentication API’).

In addition to the Job Service, there is also the Job Schedule Service. The Job Schedule Service, allows you to define a set interval at which a job will automatically execute.

#### Job Service API Details

1. Job Service
 - [Create Job](#CreateJob)
 - [Get Job](#GetJob)
 - Update Job
 - Delete Job
 - Get Jobs
 - Start a Job
 - Get Job Executions
 - Re-start a Job Execution
 - Stop a Job Execution
 - Kill a Job Execution
2. Job Schedule Service – The Scheduling service allows you to define a set interval at which a job will automatically execute.
 - Create Job Schedule
 - Update Job Schedule
 - Delete Job Schedule
 - Get Job Schedule(s)

##### CREATE JOB <a id="CreateJob"></a>

Creates a Runner job in a given account. The Runner jobs have to be scripted plays using Ansible. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to create a new job definition to execute the tasks specified in the referenced playbook. You also have the option to run it immediately or execute it later by issuing a start request.

**Structure**

`POST https://api.runner.ctl.io/jobs/{accountAlias}?immediate=true|false`

**Example**

`POST https://api.runner.ctl.io/jobs/AAAA?immediate=false`

**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| immediate	| boolean	| Set to “true” if the job to be executed immediately after creation. Default is “false”. |	No |

**Content Properties**

Playbooks can be executed in couple of different ways:

1. We recommend to have your playbook in a GitHib Repository for complex plays that are referencing multiple dependent playbooks/templates. Please refer to the Repository Entity information listed below.

2. If your playbook is simple and all plays are within a single playbook, then you can base64 encode the playbook and pass it as string to the playbook key below.

Important Note: For creating a job, the playbook has to be referenced either from GitHub or directly, by providing base64 encoded playbook but not both.

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| description	| string |	Description of the job. |	No |
| executionTtl |	integer |	You can mention the time in minutes expected for the job execution to be complete. If the execution doesn’t complete before the specified time, then it will be gracefully stopped. Default value is “180”. |	No |
| callbacks |	array |	Callback entity schema |	No |
| playbook |	string |	If your playbook is simple and all plays are within a single playbook then you can base64 encode the playbook and pass it as string. Please read the above note. |	Yes |
| playbookTags |	array |	If you would like to execute only specific plays/tasks tags, you can list them as comma separated array of string. |	No |
| repository |	complex |	Repository entity schema. Please read the above note. |	Yes |
| hosts |	array |	Hosts entity schema |	Yes |
| properties |	array |	Property entity schema |	No |
| sshPrivateKey |	string |	The default private key (base64 encoded) when connecting to hosts during playbook execution. |	No |
 |useDynamicInventory |	boolean |	Instructs Runner to gather all hosts of your account alias. This makes all hosts available as inventory during the playbook execution. Your playbook can then filter the hosts using the hosts property. |	No |

**Callbacks Entity**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| url   | string | Your callback webhook url. | Yes  |
| level | string | You can choose the level of information you would like to receive from DEBUG, ERROR, RESULT. When not specified the default value will be “DEBUG” | No   |

**Repository Entity**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| credentials |	array |	Required only when executing playbooks from a private GitHub repository. |	No |
| url |	string |	Playbook GitHub repository url. Note: HTTPS url should be provided. |	Yes |
| branch |	string |	Repository branch or tag where the playbook is present. Note: Not required if the playbook is in master branch. |	No |
| defaultPlaybook |	string |	Name of the playbook to be executed with file extension. |	Yes |

**Credentials Entity**

In order to execute the playbook from your private GitHub repository, please provide a username and password or SSH Key associated with your GitHub account.

Note: GitHub credentials are NOT required for a playbook in a public repository.

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- | --- |
| username |	string |	User name of your private GitHub repository. |
| password |	string |	Password of your private GitHub repository. |
| sshPrivateKey	 |string |	The private key (base64 encoded) associated with your private GitHub account. |

**Hosts Entity**

Define list of hosts and their related variable made available to the playbook when a play or task is executed for that host.

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| id |	string |	Host name on which the play is to be executed. |	Yes |
| hostVars |	array |	Host vars are made available to the playbook when a play or task is executed for that host. |	No |
| sshPrivateKey |	string |	Private Key (base64 encoded) required when any task to be performed on the specified host connected via SSH. |	No |

**Properties Entity**

This entity can be used to pass any additional variables to the playbook as extra variables. Similar to the command line –extra-vars argument.

```JSON
{
    "property1": "value1",
    "property2": "value2"
}
```

**Example**

```JSON
{
    "description": "Sample Job",
    "repository": {
        "credentials": {
            "username": "git username",
            "password": "git password"
        },
        "defaultPlaybook": "example.yml",
        "branch": "feature",
        "url": "https://github.com/yourrepository.git"
    },
    "callbacks": [
        {
            "url": "your callback webhook",
            "level": "DEBUG"
        }
    ],
    "hosts": [
        {
            "hostVars": {
                    "ansible_connection": "ssh",
                    "datacenter": "VA1"
                },
            "sshPrivateKey" : "TUlJRW93SUJBQUtDQVF........WE81ZnQ1dg==",
            "id": "localhost"
        }
    ]
}
```

Response

The response will be a list of objects containing entities for each job created in the given account.

Below is the representation of Job Execution Status for various requests:

![Job Execution Status](../images/Runner-Execution-State-diagram.png)








##### GET JOB <a id="GetJob"></a>
