{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "NonResourceBasedPermissions",
      "Effect": "Allow",
      "Action": [
        "ec2:CancelSpotInstanceRequests",
        "ec2:DescribeAvailabilityZones",
        "ec2:DescribeIamInstanceProfileAssociations",
        "ec2:DescribeInstanceStatus",
        "ec2:DescribeInstances",
        "ec2:DescribeInternetGateways",
        "ec2:DescribeNatGateways",
        "ec2:DescribeNetworkAcls",
        "ec2:DescribePrefixLists",
        "ec2:DescribeReservedInstancesOfferings",
        "ec2:DescribeRouteTables",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSpotInstanceRequests",
        "ec2:DescribeSpotPriceHistory",
        "ec2:DescribeSubnets",
        "ec2:DescribeVolumes",
        "ec2:DescribeVpcAttribute",
        "ec2:DescribeVpcs",
        "ec2:CreateTags",
        "ec2:DeleteTags",
        "ec2:RequestSpotInstances"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "InstancePoolsSupport",
      "Effect": "Allow",
      "Action": [
        "ec2:AssociateIamInstanceProfile",
        "ec2:DisassociateIamInstanceProfile",
        "ec2:ReplaceIamInstanceProfileAssociation"
      ],
      "Resource": "arn:aws:ec2:us-east-1:140887677285:instance/*",
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/Vendor": "Databricks"
        }
      }
    },
    {
      "Sid": "AllowEc2RunInstancePerTag",
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:us-east-1:140887677285:volume/*",
        "arn:aws:ec2:us-east-1:140887677285:instance/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/Vendor": "Databricks"
        }
      }
    },
    {
      "Sid": "AllowEc2RunInstanceImagePerTag",
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:us-east-1:140887677285:image/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Vendor": "Databricks"
        }
      }
    },
    {
      "Sid": "AllowEc2RunInstancePerVPCid",
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "Resource": [
        "arn:aws:ec2:us-east-1:140887677285:network-interface/*",
        "arn:aws:ec2:us-east-1:140887677285:subnet/*",
        "arn:aws:ec2:us-east-1:140887677285:security-group/*"
      ],
      "Condition": {
        "StringEquals": {
          "ec2:vpc": "arn:aws:ec2:us-east-1:140887677285:vpc/vpc-04d174ecff5d1b3ef"
        }
      }
    },
    {
      "Sid": "AllowEc2RunInstanceOtherResources",
      "Effect": "Allow",
      "Action": "ec2:RunInstances",
      "NotResource": [
        "arn:aws:ec2:us-east-1:140887677285:image/*",
        "arn:aws:ec2:us-east-1:140887677285:network-interface/*",
        "arn:aws:ec2:us-east-1:140887677285:subnet/*",
        "arn:aws:ec2:us-east-1:140887677285:security-group/*",
        "arn:aws:ec2:us-east-1:140887677285:volume/*",
        "arn:aws:ec2:us-east-1:140887677285:instance/*"
      ]
    },
    {
      "Sid": "EC2TerminateInstancesTag",
      "Effect": "Allow",
      "Action": [
        "ec2:TerminateInstances"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:140887677285:instance/*"
      ],
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/Vendor": "Databricks"
        }
      }
    },
    {
      "Sid": "EC2AttachDetachVolumeTag",
      "Effect": "Allow",
      "Action": [
        "ec2:AttachVolume",
        "ec2:DetachVolume"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:140887677285:instance/*",
        "arn:aws:ec2:us-east-1:140887677285:volume/*"
      ],
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/Vendor": "Databricks"
        }
      }
    },
    {
      "Sid": "EC2CreateVolumeByTag",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateVolume"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:140887677285:volume/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/Vendor": "Databricks"
        }
      }
    },
    {
      "Sid": "EC2DeleteVolumeByTag",
      "Effect": "Allow",
      "Action": [
        "ec2:DeleteVolume"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:140887677285:volume/*"
      ],
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/Vendor": "Databricks"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole",
        "iam:PutRolePolicy"
      ],
      "Resource": "arn:aws:iam::*:role/aws-service-role/spot.amazonaws.com/AWSServiceRoleForEC2Spot",
      "Condition": {
        "StringLike": {
          "iam:AWSServiceName": "spot.amazonaws.com"
        }
      }
    },
    {
      "Sid": "VpcNonresourceSpecificActions",
      "Effect": "Allow",
      "Action": [
        "ec2:AuthorizeSecurityGroupEgress",
        "ec2:AuthorizeSecurityGroupIngress",
        "ec2:RevokeSecurityGroupEgress",
        "ec2:RevokeSecurityGroupIngress"
      ],
      "Resource": "arn:aws:ec2:us-east-1:140887677285:security-group/sg-095fabbf68ce5a7e7",
      "Condition": {
        "StringEquals": {
          "ec2:vpc": "arn:aws:ec2:us-east-1:140887677285:vpc/vpc-04d174ecff5d1b3ef"
        }
      }
    }
  ]
}