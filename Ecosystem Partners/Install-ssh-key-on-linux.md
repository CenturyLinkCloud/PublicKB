
{{{
  "title": "Install ssh key on linux",
  "date": "11-1-2015",
  "author": "Andrew Brunette",
  "attachments": [],
  "contentIsHTML": false
}}}

### Technology Profile

Ssh keys can be used to provide secure login and command access without a password.  

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be able to add a task to a Blueprint that will set the server up for passwordless access.

### Prerequisite
- The user needs to generate an ssh key pair
- The user needs to add the private key to his system
- The user needs to have access to the public key

To generate a key pair on a machintosh or -nix system,
1. From a Terminal window,
  1. run ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  2. for the file name, suggest using the default
  3. For the passphrase, suggest blank for secure environments, a non blank phrase for more secure uses.  Note that you will be asked for the passphrase on logins, which defeats the purpose of automation.
  4. Start the ssh agent on your machine: eval "$(ssh-agent -s)"
  5. Add the key to your agent: ssh-add ~/.ssh/id_rsa

### Adding this to your blueprint
This is a script that is added to your blueprint, or run against an existing server.  It will add a prompt to your blueprint that asks for the public key for your key pair.  You will need to provide instructions to the user of your blueprint that direct the user to this article.  The user will need to be directed to find his public key file, copy the text from that file, and insert it into the prompt.


#### Who should I contact for support?
* This is an unsupported script.  
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
