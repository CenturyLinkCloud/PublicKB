{{{
  "title": "How to Ansible with Runner",
  "date": "04-27-2016",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Audience

This article is to support customers of Runner, a product that enables teams, developers, and engineers to quickly provision, interact, and modify their environments anywhere - CenturyLink Cloud, third-party cloud providers, and on-premises.

### Introduction

Here at CenturyLink Cloud, we use a technology called Ansible pretty extensively throughout our platform. Ansible is an IT automation and orchestration engine that enables provisioning, configuration management, deployment, intra-service orchestration, and many other IT needs. Runner wraps all of Ansible’s goodness into a Job Service, along with others services such as SSH, VPN, Status, Queueing, and Scheduling. Throughout this introduction there are a couple of questions we want to try and answer, along with some simple examples; what is Runner, how do you use it and what can it really do?

Let’s start with the basic first question…

### What is Runner?

Runner is a new product from CenturyLink that enables fast and easy automation and orchestration on the CenturyLink Platform, as well as third-party cloud providers such as Amazon’s AWS and Microsoft’s Azure and on-premises infrastructure and devices. Runner provides the ability to quickly provision and modify resources on any environment, and gives users a true hybrid-IT solution.

On a more granular level, Runner is an automation and orchestration engine that we’ve exposed as a service, along with other services, that will enhance the Runner service. Runner, at it’s core, is an Ansible engine. But on top of that engine there exists several other services and APIs, many of which were created in tandem with the Runner Job Service to enhance the job execution capabilities. Here is a little more detail on the services available:

  ![How-to Services](../images/how-to-services.png)

Now that we’ve covered the services available through Runner, lets look at how to use Runner.

### How to use Runner

Using Runner is a fairly straightforward process. To get started, one must first create a job. A job requires a playbook that you have created or one that is publicly available on GitHub, as well as these key ingredients needed:

 - **Playbook and GitHub location –** The playbooks you use must exist on GitHub, either publicly or privately; if privately, your GitHub credentials are required.
 - **Host information –** This information provides the job context for where your job will be run. You can specify a single host or group of hosts you want to use.
 - **Bearer token –** Each job requires authorization in order to run. Runner authorizes your job using your CenturyLink Bearer token (API available here)

Runner takes a JSON payload of user defined options and parameters, including the above required information, and creates a job definition within Runner. For a full list of payload options and parameters, click here. It is worth noting that you can create job and not run it. This will be defined in your API calls, such as:

`[RUNNER API PATH]/jobs/{accountAlias}?immediate=true|false`

Note: Once a job has been created, it can be run or rerun at any point in time.

Below is an example of what the payload might look like:

```
{
  	"description": "Enter your playbook description here",
	"callbacks": [
		{
		  "level": "DEBUG",
		  "url": "http://webhooks.url/ifdesired"
		}
	],
	"hosts":[
		{
		  "id":"localhost",
		  "hostVars":{"ansible_connection":"local"}
		}
	],
	"repository": {
		"defaultPlaybook": "my-playbook.yml",
	    "url": "https://github.com/bmh2git/Hello-World-Playbook"
	},
}
```
The Runner engine grabs your playbook from GitHub and loads it into the Runner. The Runner engine then parses the job to understand which environment it will be working in and establishes the necessary connections to those environments to execute the playbooks.

Once a job has started to execute, Runner will update the status of the job via the Runner Status Service, which can be accessed via the dashboard, API, or your own webhooks endpoints. All updates and changes will be logged and exposed throughout the jobs life.

And that’s it. While fairly simplified, it’s pretty straightforward and easy to create and run jobs using Runner.

### What are Playbooks?

Runner uses Playbooks to execute tasks and commands on the hosts you’ve defined. Playbooks are Ansible’s configuration, deployment, and orchestration language. They can describe a policy you want your remote systems to enforce, or a set of steps in a general IT process. Playbooks are written YAML, and usually contain the extension example.yml.

Within playbooks, users can create or call modules, tasks, hosts, and roles. Hosts are the target systems in which you want to execute on. Modules (also referred to as “task plugins” or “library plugins”) are the ones that do the actual work in Ansible, they are what gets executed in each playbook task. But you can also run a single one using the ‘Ansible’ command. Ansible ships with [over 450 modules](http://docs.ansible.com/ansible/list_of_all_modules.html), and custom ones can be written. Each play contains a list of tasks. Tasks are executed in order, one at a time, against all machines matched by the host pattern, before moving on to the next task. It is important to understand that, within a play, all hosts are going to get the same task directives. It is the purpose of a play to map a selection of hosts to tasks. Roles are ways of automatically loading certain vars_files, tasks, and handlers based on a known file structure. Grouping content by roles also allows easy sharing of roles with other users. Roles are just automation around ‘include’ directives as described above, and really don’t contain much additional magic beyond some improvements to search path handling for referenced files.



```
---
	- name: Hello World
	  hosts: localhost

	  tasks:
	    - name: Display Text
	      shell: echo “Hello World!”
```
