{{{
  "title": "Introduction to Manual Site",
  "date": "03-14-2018",
  "author": "Mahima Kumar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article provides information on which sites are considered as **Manual** within a SafeHaven cluster.

### What is a Manual Site
A site in which API's are not supported by SafeHaven at the moment is treated as a Manual site. This simply means the production or recovery servers will have to be powered on/off manually instead of the automatic operations. All other operations will remain the same and ansible installation of windows agent will work as well.

### List of Manual Sites under SafeHaven
1. DCC-Foundation
2. Standalone VMware ESXi Host
3. Physical Server
4. Hyper V Generation 1
5. AWS (only when AWS is the production site)
6. KVM
7. Standalone VMware ESXi Host

