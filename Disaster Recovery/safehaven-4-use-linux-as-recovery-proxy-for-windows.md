{{{
  "title": "SafeHaven 4: Use Linux as Recovery Proxy for Windows",
  "date": "24-10-2016",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Why do we need this?
Before SafeHaven-4.0.1, the customer is required to deploy a Windows VM as a recovery proxy (aka stub) for any SafeHaven protection group (PG) that is protecting Windows servers. While this method works perfectly in the technical sense, the Windows stub incurs unnecessary Windows OS license cost, even while the stub VM is powered off in CenturyLink CLoud (CLC) for most of the time. In addition, in the ocassional event when a test failover or real failover is perfomred and the stub VMs are powered on, the Windows OS provided by CLC and paid for by the customers are not used since the stub boots into a customer disk image that is replicated by SafeHaven and Microsoft does have provisions in its licensing agreement to allow its customers to temporarily use its production Windows OS license during the short test/real failover scenarios.

An alternative method has been developed to use the open source Ubuntu-14 template which does not have any OS licensing cost in CLC. This should allow the customers to reduce cost for their SafeHaven disaster recovery solution in a significant way. This documents outlines the manual procedure that is necessary as of the SafeHaven-4.0.1 release which hopefully will soon be automated in future releases.





