from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy
)

import aws_cdk as core
from constructs import Construct
from . import parameters
from . import host_app_aws_stack
from .host_app_aws_stack import HostAppAwsStack

class UploadContentsToS3Stack(Stack):
    
    # def __init__(self, scope: core.Construct, id: str, s3_bucket_name: str, **kwargs) -> None:
    def __init__(self, scope: Construct, construct_id: str, s3_bucket_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        host_app_aws_stack = HostAppAwsStack(self, "HostAppAwsStack",
            env=core.Environment(account="770760105158", region="us-east-2"),
        )

        s3_bucket_src = s3.Bucket.from_bucket_name(self, "ImportedBucket", host_app_aws_stack.s3_bucket_name)

        s3_deploy = s3deploy.BucketDeployment(self, "deployWebsite",
            sources=[s3deploy.Source.asset("./host_app_aws/website/")],
            destination_bucket=s3_bucket_src
        )
    