{{{
    "title": "CenturyLink Managed Services Anywhere AWS Buy-Your-Own-Cloud Requirements", "date": "05-7-2018",
    "author": "Chris Meyer",
    "attachments": [],
    "contentIsHTML": false
}}}

### Content
* [Overview](#overview)
* [AWS Configuration Requirements](#aws-configuration-requirements)
* [AWS Managed Services Anywhere IAM Policy](#aws-managed-services-anywhere-iam-policy)
* [Supporting AWS Accounts in an Organization](#supporting-aws-accounts-in-an-organization)


### Overview  

This KB details the requirements of Centurylink's Managed Services Anywhere (MSA) offering with customer provided AWS accounts.

### AWS Configuration Requirements
* AWS IAM ARN with policy permissions applied
* Apply ARN to CAM provider that has been enabled for Managed Services Anywhere
* [AWS Cost Explorer ](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-explorer-signup.html) functionality enabled
* Enable AWS IAM profiles to [access billing data](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/grantaccess.html)


### AWS Managed Services Anywhere IAM Policy
The below AWS IAM Policy is required for Managed Services Providers to provide access to review and take action on a customers behalf.

Customers are encouraged to create a separate IAM policy and add it to the existing Cloud Application Manager's Application Life Cycle management role as described [here](https://www.ctl.io/knowledge-base/cloud-application-manager/deploying-anywhere/using-your-aws-account/)

Managed Services Anywhere AWS IAM Policy (as of May 7st, 2018)
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "organizations:*",
                "rds:*",
                "cloudtrail:*",
                "logs:*",
                "autoscaling:*",
                "ds:*",
                "servicediscovery:*",
                "cloudfront:*",
                "route53domains:*",
                "kms:*",
                "events:*",
                "directconnect:*",
                "s3:*",
                "cloudformation:*",
                "elasticloadbalancing:*",
                "autoscaling-plans:*",
                "iam:*",
                "trustedadvisor:*",
                "cloudwatch:*",
                "waf:*",
                "ec2:*",
                "waf-regional:*",
                "ce:*",
                "elasticache:*",
                "acm:*",
                "support:*",
                "sts:AssumeRole"
            ],
            "Resource": "*"
        }
    ]
}
```


### Supporting AWS Accounts in an Organization
* We support managed AWS accounts that are under an AWS Organization assuming the same requirements as independent accounts are meet at the Organizational account level.
