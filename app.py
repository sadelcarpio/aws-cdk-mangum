#!/usr/bin/env python3

import aws_cdk

from aws_cdk_mangum.aws_cdk_mangum_stack import AwsCdkMangumStack

app = aws_cdk.App()
AwsCdkMangumStack(app, "AwsCdkMangumStack")

app.synth()
