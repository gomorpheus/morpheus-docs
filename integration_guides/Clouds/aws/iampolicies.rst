.. _MinimumIAMPolicies:

AWS IAM Permissions
^^^^^^^^^^^^^^^^^^^^^^^^

Below are the AWS IAM Permissions required for |morpheus| services.

autoscaling
```````````

.. code-block::

                  "autoscaling:AttachInstances",
                  "autoscaling:AttachLoadBalancerTargetGroups",
                  "autoscaling:CreateAutoScalingGroup",
                  "autoscaling:DeleteAutoScalingGroup",
                  "autoscaling:DeleteLaunchConfiguration",
                  "autoscaling:DeletePolicy",
                  "autoscaling:DescribeAutoScalingGroups",
                  "autoscaling:DescribeLaunchConfigurations",
                  "autoscaling:DescribeLoadBalancers",
                  "autoscaling:DescribePolicies",
                  "autoscaling:DetachInstances",
                  "autoscaling:PutScalingPolicy",
                  "autoscaling:UpdateAutoScalingGroup",

cloudformation
``````````````
.. code-block::

                  "cloudformation:CreateStack",
                  "cloudformation:DeleteStack",
                  "cloudformation:DescribeStackEvents",
                  "cloudformation:DescribeStackResources",
                  "cloudformation:DescribeStacks",
                  "cloudformation:GetTemplate",
                  "cloudformation:UpdateStack",
                  "cloudformation:ValidateTemplate",

cloudwatch
```````````
.. code-block::

                  "cloudwatch:DeleteAlarms",
                  "cloudwatch:DescribeAlarms",
                  "cloudwatch:GetMetricStatistics",
                  "cloudwatch:PutMetricAlarm",

costexplorer
````````````
.. code-block::

                  "ce:*",

Cost and Usage Reports
``````````````````````
.. code-block::

                  "cur:DescribeReportDefinitions",
                  "cur:PutReportDefinition",

ec2
```````````
.. code-block::

                  "ec2:AllocateAddress",
                  "ec2:AssignPrivateIpAddresses",
                  "ec2:AssociateAddress",
                  "ec2:AttachInternetGateway",
                  "ec2:AttachNetworkInterface",
                  "ec2:AttachVolume",
                  "ec2:AuthorizeSecurityGroupEgress",
                  "ec2:AuthorizeSecurityGroupIngress",
                  "ec2:CancelExportTask",
                  "ec2:CancelImportTask",
                  "ec2:CopyImage",
                  "ec2:CopySnapshot",
                  "ec2:CreateEgressOnlyInternetGateway",
                  "ec2:CreateImage",
                  "ec2:CreateInstanceExportTask",
                  "ec2:CreateInternetGateway",
                  "ec2:CreateKeyPair",
                  "ec2:CreateNatGateway",
                  "ec2:CreateNetworkAcl",
                  "ec2:CreateNetworkAclEntry",
                  "ec2:CreateNetworkInterface",
                  "ec2:CreateRoute",
                  "ec2:CreateSecurityGroup",
                  "ec2:CreateSnapshot",
                  "ec2:CreateSubnet",
                  "ec2:CreateTags",
                  "ec2:CreateVolume",
                  "ec2:CreateVpc",
                  "ec2:DeleteEgressOnlyInternetGateway",
                  "ec2:DeleteInternetGateway",
                  "ec2:DeleteKeyPair",
                  "ec2:DeleteNatGateway",
                  "ec2:DeleteNetworkAcl",
                  "ec2:DeleteNetworkAclEntry",
                  "ec2:DeleteNetworkInterface",
                  "ec2:DeleteRoute",
                  "ec2:DeleteSecurityGroup",
                  "ec2:DeleteSnapshot",
                  "ec2:DeleteSubnet",
                  "ec2:DeleteTags",
                  "ec2:DeleteVolume",
                  "ec2:DeleteVpc",
                  "ec2:DeregisterImage",
                  "ec2:DescribeAccountAttributes",
                  "ec2:DescribeAddresses",
                  "ec2:DescribeAvailabilityZones",
                  "ec2:DescribeClassicLinkInstances",
                  "ec2:DescribeClientVpnConnections",
                  "ec2:DescribeClientVpnEndpoints",
                  "ec2:DescribeConversionTasks",
                  "ec2:DescribeEgressOnlyInternetGateways",
                  "ec2:DescribeExportTasks",
                  "ec2:DescribeImageAttribute",
                  "ec2:DescribeImages",
                  "ec2:DescribeImportImageTasks",
                  "ec2:DescribeImportSnapshotTasks",
                  "ec2:DescribeInstances",
                  "ec2:DescribeInstanceStatus",
                  "ec2:DescribeInstanceTypes",
                  "ec2:DescribeInternetGateways",
                  "ec2:DescribeKeyPairs",
                  "ec2:DescribeNatGateways",
                  "ec2:DescribeNetworkAcls",
                  "ec2:DescribeNetworkInterfaceAttribute",
                  "ec2:DescribeNetworkInterfaces",
                  "ec2:DescribeRegions",
                  "ec2:DescribeRouteTables",
                  "ec2:DescribeSecurityGroupReferences",
                  "ec2:DescribeSecurityGroups",
                  "ec2:DescribeSnapshotAttribute",
                  "ec2:DescribeSnapshots",
                  "ec2:DescribeStaleSecurityGroups",
                  "ec2:DescribeSubnets",
                  "ec2:DescribeTags",
                  "ec2:DescribeTransitGateways",
                  "ec2:DescribeTransitGatewayVpcAttachments",
                  "ec2:DescribeVolumeAttribute",
                  "ec2:DescribeVolumes",
                  "ec2:DescribeVolumeStatus",
                  "ec2:DescribeVpcAttribute",
                  "ec2:DescribeVpcClassicLink",
                  "ec2:DescribeVpcClassicLinkDnsSupport",
                  "ec2:DescribeVpcEndpoints",
                  "ec2:DescribeVpcEndpointServices",
                  "ec2:DescribeVpcPeeringConnections",
                  "ec2:DescribeVpcs",
                  "ec2:DescribeVpnGateways",
                  "ec2:DetachInternetGateway",
                  "ec2:DetachNetworkInterface",
                  "ec2:DetachVolume",
                  "ec2:DisassociateAddress",
                  "ec2:GetPasswordData",
                  "ec2:ImportImage",
                  "ec2:ImportInstance",
                  "ec2:ImportKeyPair",
                  "ec2:ImportSnapshot",
                  "ec2:ImportVolume",
                  "ec2:ModifyImageAttribute",
                  "ec2:ModifyInstanceAttribute",
                  "ec2:ModifyNetworkInterfaceAttribute",
                  "ec2:ModifySnapshotAttribute",
                  "ec2:ModifySubnetAttribute",
                  "ec2:ModifyVolumeAttribute",
                  "ec2:RebootInstances",
                  "ec2:RegisterImage",
                  "ec2:ReleaseAddress",
                  "ec2:ReplaceNetworkAclAssociation",
                  "ec2:ReplaceNetworkAclEntry",
                  "ec2:ResetImageAttribute",
                  "ec2:ResetInstanceAttribute",
                  "ec2:ResetNetworkInterfaceAttribute",
                  "ec2:ResetSnapshotAttribute",
                  "ec2:RevokeSecurityGroupEgress",
                  "ec2:RevokeSecurityGroupIngress",
                  "ec2:RunInstances",
                  "ec2:StartInstances",
                  "ec2:StopInstances",
                  "ec2:TerminateInstances",
                  "ec2:UnassignPrivateIpAddresses",
                  "ec2:UpdateSecurityGroupRuleDescriptionsEgress",

eks
```````````
.. code-block::

                  "eks:*",

elasticloadbalancing
````````````````````
.. code-block::

                  "elasticloadbalancing:AddTags",
                  "elasticloadbalancing:ApplySecurityGroupsToLoadBalancer",
                  "elasticloadbalancing:AttachLoadBalancerToSubnets",
                  "elasticloadbalancing:CreateListener",
                  "elasticloadbalancing:CreateLoadBalancer", 
                  "elasticloadbalancing:CreateRule",
                  "elasticloadbalancing:CreateTargetGroup",
                  "elasticloadbalancing:DeleteListener",
                  "elasticloadbalancing:DeleteLoadBalancer",
                  "elasticloadbalancing:DeleteRule",
                  "elasticloadbalancing:DeleteTargetGroup",
                  "elasticloadbalancing:DescribeLoadBalancers",
                  "elasticloadbalancing:DescribeRules",
                  "elasticloadbalancing:DescribeTargetGroups",
                  "elasticloadbalancing:ModifyListener",
                  "elasticloadbalancing:ModifyTargetGroupAttributes",
                  "elasticloadbalancing:RegisterTargets",
                  "elasticloadbalancing:SetSecurityGroups",
                  "elasticloadbalancing:SetSubnets",

elasticsearch
`````````````
.. code-block::

                  "es:DescribeElasticsearchDomains",
                  "es:ListDomainNames",

iam
```````````
.. code-block::

                  "iam:ListGroups",
                  "iam:ListInstanceProfiles",
                  "iam:ListRoles",

rds
```````````
.. code-block::

                  "rds:AddRoleToDBCluster",
                  "rds:AddTagsToResource",
                  "rds:ApplyPendingMaintenanceAction",
                  "rds:AuthorizeDBSecurityGroupIngress",
                  "rds:CopyDBClusterSnapshot",
                  "rds:CopyDBParameterGroup",
                  "rds:CopyDBSnapshot",
                  "rds:CreateDBCluster",
                  "rds:CreateDBClusterSnapshot",
                  "rds:CreateDBInstance",
                  "rds:CreateDBInstanceReadReplica",
                  "rds:CreateDBSecurityGroup",
                  "rds:CreateDBSnapshot",
                  "rds:DeleteDBCluster",
                  "rds:DeleteDBInstance",
                  "rds:DeleteDBSecurityGroup",
                  "rds:DeleteDBSnapshot",
                  "rds:DescribeAccountAttributes",
                  "rds:DescribeCertificates",
                  "rds:DescribeDBClusterParameterGroups",
                  "rds:DescribeDBClusterParameters",
                  "rds:DescribeDBClusters",
                  "rds:DescribeDBClusterSnapshotAttributes",
                  "rds:DescribeDBClusterSnapshots",
                  "rds:DescribeDBEngineVersions",
                  "rds:DescribeDBInstances",
                  "rds:DescribeDBLogFiles",
                  "rds:DescribeDBParameterGroups",
                  "rds:DescribeDBParameters",
                  "rds:DescribeDBSecurityGroups",
                  "rds:DescribeDBSnapshotAttributes",
                  "rds:DescribeDBSnapshots",
                  "rds:DescribeDBSubnetGroups",
                  "rds:DescribeEngineDefaultClusterParameters",
                  "rds:DescribeEngineDefaultParameters",
                  "rds:DescribeEventCategories",
                  "rds:DescribeEvents",
                  "rds:DescribeOptionGroupOptions",
                  "rds:DescribeOptionGroups",
                  "rds:DescribeOrderableDBInstanceOptions",
                  "rds:ListTagsForResource",
                  "rds:ModifyDBCluster",
                  "rds:ModifyDBClusterParameterGroup",
                  "rds:ModifyDBClusterSnapshotAttribute",
                  "rds:ModifyDBInstance",
                  "rds:ModifyDBParameterGroup",
                  "rds:ModifyDBSnapshotAttribute",
                  "rds:PromoteReadReplica",
                  "rds:RebootDBInstance",
                  "rds:RemoveTagsFromResource",
                  "rds:RestoreDBClusterFromSnapshot",
                  "rds:RestoreDBClusterToPointInTime",
                  "rds:RestoreDBInstanceFromDBSnapshot",
                  "rds:RestoreDBInstanceToPointInTime",
                  "rds:RevokeDBSecurityGroupIngress",
                  "rds:StartDBInstance",
                  "rds:StopDBInstance",

route53
```````````
.. code-block::

                  "route53:ChangeResourceRecordSets",
                  "route53:GetHostedZone",
                  "route53:ListHostedZones",
                  "route53:ListResourceRecordSets",

s3
```````````
.. code-block::

                  "s3:AbortMultipartUpload",
                  "s3:CreateBucket",
                  "s3:DeleteBucket",
                  "s3:DeleteObject",
                  "s3:DeleteObjectVersion",
                  "s3:GetBucketLocation",
                  "s3:GetBucketPolicy",
                  "s3:GetObject",
                  "s3:GetObjectVersion",
                  "s3:ListAllMyBuckets",
                  "s3:ListBucket",
                  "s3:ListBucketMultipartUploads",
                  "s3:ListBucketVersions",
                  "s3:ListMultipartUploadParts",
                  "s3:PutBucketPolicy",
                  "s3:PutObject",

Systems Manager
```````````````
.. code-block::

                  "ssm:GetParameters",


