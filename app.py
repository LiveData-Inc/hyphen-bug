#!/usr/bin/env python3
import os

import aws_cdk as cdk

from hyphen_bug.hyphen_bug_stack import HyphenBugStack

app = cdk.App()
HyphenBugStack(
    app, "HyphenBugStack",
    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
)

app.synth()
