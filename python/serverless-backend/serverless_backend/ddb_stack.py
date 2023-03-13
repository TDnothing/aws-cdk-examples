from aws_cdk import Stack, aws_dynamodb as _dynamodb
from constructs import Construct
import os


class DdbStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.userTable = _dynamodb.Table(
            self,
            id="userTable",
            table_name="User",
            partition_key=_dynamodb.Attribute(
                name="userid", type=_dynamodb.AttributeType.STRING
            ),
        )

        self.transactionTable = _dynamodb.Table(
            self,
            id="transactionTable",
            table_name="Transaction",
            partition_key=_dynamodb.Attribute(
                name="transactionId", type=_dynamodb.AttributeType.STRING
            ),
        )

    def getAllTable(self):
      return [self.userTable, self.transactionTable]
