#!/usr/bin/env python3
import os

import aws_cdk as cdk

from host_app_aws.host_app_aws_stack import HostAppAwsStack
# from host_app_aws.upload_contents_to_s3 import UploadContentsToS3Stack

app = cdk.App()
host_app_aws_stack = HostAppAwsStack(app, "HostAppAwsStack",
    env=cdk.Environment(account="770760105158", region="us-east-2"),
)
# upload_contents_to_s3_stack = UploadContentsToS3Stack(app, "UploadContentsToS3Stack")
app.synth()
