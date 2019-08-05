{{{
  "title": "AWS Statistics",
  "date": "12-28-2017",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article focusses on how to check the AWS statistics of a Protection Group.

### Requirements
1. Access to the SafeHaven Console (GUI).
2. Protection Groups are created.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Periodic checkpoints for the Protection Group are enabled and a Failover with 2 instances are initiated.

### Check AWS Statistics

Select the active **Protection Group** under the Production Datacenter, navigate to the **AWS Statistics** tab and click on it.

There are 4 panels under this tab:
1. EBS Volume(s): attached to the AWS DR-SRN corresponding to the Protection Group
2. AMIs: This panel shows the information of AMIs in AWS SafeHaven created for the Protection Group
3. AWS Snapshots: Shows the information AWS snapshots created for the Protection Group
4. AWS Instances: Shows the information of the AWS instances per the Protected Server inside a Protection Group
