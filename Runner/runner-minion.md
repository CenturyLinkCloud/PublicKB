{{{
  "title": "The Runner Minion",
  "date": "04-29-2016",
  "author": "Benjamin Harristhal",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}


### Audience

This article is to support customers of Runner, a product that enables teams, developers, and engineers to quickly provision, interact, and modify their environments anywhere - CenturyLink Cloud, third-party cloud providers, and on-premises.

### The Runner Minion

Runner supports multi-cloud execution of Runner Jobs.  Runner can execute your Jobs against an AWS cloud environment, an Azure cloud environment, or any other cloud environment. Runner can also execute your Jobs against on-premises systems and resources.

Runner is able to achieve this level of reach by utilizing a component we call the Runner Minion.  The Runner Minion is a small light weight component that you control, which runs in your non CenturyLink Cloud environments. When running, the Runner Minion calls back home to Runner Central via the Runner public API's asking for work for that particular environment.  Because the Runner Minion uses public API's via HTTPS to fetch and respond to work, your remote environments don't require any special configurations other then the ability to call out to the Internet.

You will need to install and run a Runner Minion in all non CenturyLink Cloud environments. At a minimum the Runner Minion needs to be installed in a network location where it can access all parts of your environment. From this location the Runner Minion will utilize ssh/winrm to communicate with systems and resources. Another approach, although a bit excessive, is to install a Runner Minion on each system or resource in your environment.

### How To Install
#### Amazon Environments
The Runner Minion is available as a push-button product installation into the Amazon environment. You can access the AWS Minion product using your CenturyLink Cloud account. The default Runner (Public Products) page will expose a Product Market Place.

- Locate and click on **AWS Minion** in the Public Products of the Runner Jobs page.

  ![AWS Minion](../images/runner-jobs.png)

- Click on **run**, fill in the form data, and click **run** again.

The product installation will create a new server in your AWS account, then install, register, and launch the AWS Minion.

#### Other Environments
The Runner Minion is also available as a docker image.
The docker image is freely available from [DockerHub](https://hub.docker.com/r/centurylink/rnr-minion/).

#### Download the Runner-Minion
Execute a docker pull on the image to download it to your system.

```
docker pull centurylink/rnr-minion
```

#### Register The Runner Minion
Register the Runner Minion to receive an access token.

##### Request
Attribute | Value
--- | --- |
URL | http://api.runner.ctl.io/minions/{account-alias}/tokens
Authorization | "Bearer eye...qaw="
Payload | {}

##### Curl example:
```
curl \
-XPOST \
-H "Content-Type: application/json" \
-H "Authorization: Bearer eyJ0e...fIw" \
https://api.runner.ctl.io/minions/wftc/tokens \
--data '{}'
```

##### Response
Key | Value
--- | ---
"accountAlias"| "{account-alias}",
"location"| "minion.default",
"requestQueue"| "minion.default",
"replyQueue"| "minion.default.reply",
"id"| "ea94a4b...-da2266e761f3",
"token"| "1020...-a023a23b586f"


#### Launch The Runner Minion
Then launch your Runner Minion with the token.

```
docker run -it  centurylink/rnr-minion --token=1020...-a023a23b586f --verbose --minion-api-endpoint=https://api.runner.ctl.io/minions --queue-api-endpoint=https://api.runner.ctl.io/queues
```
