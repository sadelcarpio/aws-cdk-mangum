import os
import subprocess

from aws_cdk import (
    aws_lambda as _lambda,
    Stack,
)
from constructs import Construct


class AwsCdkMangumStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        entrypoint_name = 'fastapi_app'

        _lambda.Function(
            self,
            'FastAPI with Mangum',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("fastapi_app"),
            handler='main.handler',
            layers=[self.create_dependencies_layer(self.stack_name, entrypoint_name)]
        )

    def create_dependencies_layer(self, project_name, function_name: str) -> _lambda.LayerVersion:
        requirements_file = f'{function_name}/requirements.txt'
        output_dir = f'{function_name}/.build'

        if not os.environ.get('SKIP_PIP'):
            subprocess.check_call(
                f'pip install -r {requirements_file} -t {output_dir}/python'.split()
            )

        layer_id = f'{project_name}-{function_name}-dependencies'
        layer_code = _lambda.Code.from_asset(output_dir)

        return _lambda.LayerVersion(self, layer_id, code=layer_code)
