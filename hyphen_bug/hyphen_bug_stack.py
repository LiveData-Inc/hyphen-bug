from aws_cdk import CfnOutput, Stack, aws_lambda
from constructs import Construct

ALIAS_NAME = 'HYPHEN-BUG'  # <<< change this to 'HYPHEN_BUG' to make the stack deploy successfully


inline_code = """
def handler(event, context):
    print(f'{event=} {context=}')
"""

class HyphenBugStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        handler = aws_lambda.Function(
            self, 'HyphenBugLambda',
            code=aws_lambda.InlineCode(inline_code),
            handler='index.handler',
            runtime=aws_lambda.Runtime.PYTHON_3_9,
        )

        alias = handler.add_alias(
            alias_name=ALIAS_NAME,
        )

        fn_url = alias.add_function_url(
            auth_type=aws_lambda.FunctionUrlAuthType.NONE
        )

        CfnOutput(self, "FunctionUrl", value=fn_url.url)
