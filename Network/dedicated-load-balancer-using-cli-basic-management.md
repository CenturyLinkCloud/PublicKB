{{{
  "title": "Dedicated Load Balancer Basic Management Using CLI",
  "date": "9-1-2015",
  "author": "Mark Turpin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Dedicated Load Balancer Basic Management Using CLI

This KB will go over the basics of creating a Load Balancer VIP and Services when using the Command Line Interface (CLI) for dedicated Load Balancers

### Prerequisites

* HA Dedicated Load Balancers have been deployed to your account
* Must have an Admin login to the Netscaler
* Must be able to SSH to the RNAT IP of the HA pair (typically ends with .101)

### Notes

* This example will configure a 2 node web server farm that is load balancing traffic on http (port 80) and using "cookie insert" for persistence type
* Least connection is the default load balancing algorithm
* Ping/TCP checks are the default health monitors

### Steps

1. Log into your dedicated load balancer RNAT IP (typically ends with .101) using SSH and an Admin login
2. Now in the CLI, we will create the server objects.  These will be the web servers being load balanced.

  ```
  add server VA1ACMEWEB01 10.10.10.15
  add server VA1ACMEWEB02 10.10.10.16
  ```

3. Next, we will create a service for both servers (using HTTP)

  ```
  add service VA1ACMEWEB01_http_80 VA1ACMEWEB01 http 80
  add service VA1ACMEWEB02_http_80 VA1ACMEWEB02 http 80
  ```

4. Next, we will create the Virtual Server.  We will use the website name and port in the name for ease of management.  The Virtual Server VIP comes from the pool of private IP's provisioned by the NOC during deployment of the HA pair.

  ```
  add lb vserver www-prod-acme_80 http 10.10.10.104 80
  ```

5. Now that we have the Virtual Server object created, we need to bind both services to it.

  ```
  bind lb vserver www-prod-acme_80 VA1ACMEWEB01_http_80
  bind lb vserver www-prod-acme_80 VA1ACMEWEB02_http_80
  ```

6. Lastly, we will set the persistence type on the Virtual Server to use Cookie Insert

  ```
  set lb vserver www-prod-acme_80 -persistenceType COOKIEINSERT
  ```

### Additional Notes

* This example was performed on Netscaler VPX version 10.5
* For configuration with the GUI, please review [Dedicated LB Basic Management](../Network/dedicated-load-balancer-basic-management.md) for the basics of creating a Load Balancer VIP and Service Group when using Dedicated Load Balancers
* If you begin to add additional networks to load balance in your environment, please review [Load Balance Additional Networks](../Network/loadbalance-additional-networks.md)
* Tracking a Dedicated Load Balancer license expiration date is performed by the customer, please reference our [License Management Article](../Network/dedicated-load-balancer-license-management.md)
