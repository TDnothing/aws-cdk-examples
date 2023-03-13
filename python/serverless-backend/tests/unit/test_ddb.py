import aws_cdk as core
import aws_cdk.assertions as assertions
from serverless_backend.ddb_stack import DdbStack


def test_ddb():
    app = core.App()
    stack = DdbStack(app, "ddb-stack")
    template = assertions.Template.from_stack(stack)
    print("==========================")
    print(template)
    template.resource_count_is("AWS::DynamoDB::Table", 2)
