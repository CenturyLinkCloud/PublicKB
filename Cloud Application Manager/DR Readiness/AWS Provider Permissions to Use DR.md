{{{
  "title": "Minimal AWS Provider Permissions for Disaster Recovery",
  "date": "02-13-2020",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

In the KB article [Using AWS](../Deploying Anywhere/using-your-aws-account.md#create-an-iam-role-with-the-policy-chosen), a procedure is described to assign a customer prescribed permissions to create an AWS provider in CAM.
This article will list the minimal permissions required in order to perform disaster recovery to the chosen AWS provider.

### Minimal AWS IAM Permissions to Use Disaster Recovery

```json
{ 
   "Version":"2012-10-17",
   "Statement":[ 
      { 
         "Sid":"CamSafehavenPolicy",
         "Effect":"Allow",
         "Action":[ 
            "cloudtrail:DescribeTrails",
            "lightsail:GetInstances",
            "cloudfront:ListDistributions",
            "route53:ListHostedZones",
            "s3:ListAllMyBuckets",
            "s3:GetBucketLocation",
            "apigateway:GET",
            "ec2:RunInstances",
            "iam:DeleteUserPolicy",
            "iam:DeleteUser",
            "iam:DeleteAccessKey",
            "sts:GetFederationToken",
            "cloudformation:CreateStack",
            "cloudformation:DeleteStack",
            "cloudformation:DescribeStackEvents",
            "cloudformation:DescribeStacks",
            "cloudformation:ListStacks",
            "cloudformation:UpdateStack",
            "cloudwatch:DescribeAlarms",
            "cloudwatch:ListDashboards",
            "directconnect:DescribeConnections",
            "ds:DescribeDirectories",
            "dynamodb:ListTables",
            "ec2:AttachVolume",
            "ec2:AuthorizeSecurityGroupIngress",
            "ec2:CreateSecurityGroup",
            "ec2:CreateSnapshot",
            "ec2:CreateTags",
            "ec2:CreateVolume",
            "ec2:DeleteSecurityGroup",
            "ec2:DeleteSnapshot",
            "ec2:DeleteVolume",
            "ec2:DeregisterImage",
            "ec2:DescribeAccountAttributes",
            "ec2:DescribeAvailabilityZones",
            "ec2:DescribeImages",
            "ec2:DescribeInstanceAttribute",
            "ec2:DescribeInstances",
            "ec2:DescribeKeyPairs",
            "ec2:DescribeNetworkInterfaces",
            "ec2:DescribePlacementGroups",
            "ec2:DescribeSecurityGroups",
            "ec2:DescribeSnapshots",
            "ec2:DescribeSubnets",
            "ec2:DescribeTags",
            "ec2:DescribeVolumes",
            "ec2:DescribeVpcs",
            "ec2:DetachVolume",
            "ec2:ModifyInstanceAttribute",
            "ec2:ModifyNetworkInterfaceAttribute",
            "ec2:RegisterImage",
            "ec2:RevokeSecurityGroupIngress",
            "ec2:StartInstances",
            "ec2:StopInstances",
            "ec2:TerminateInstances",
            "ecs:DescribeClusters",
            "ecs:ListClusters",
            "elasticache:DescribeCacheClusters",
            "elasticloadbalancing:DescribeLoadBalancers",
            "elasticloadbalancing:DescribeTargetGroups",
            "iam:CreateAccessKey",
            "iam:CreateUser",
            "iam:ListAccessKeys",
            "iam:ListInstanceProfilesForRole",
            "iam:ListRoles",
            "iam:ListServerCertificates",
            "iam:PutUserPolicy",
            "rds:DescribeDBInstances"
         ],
         "Resource":"*"
      }
   ]
}
```