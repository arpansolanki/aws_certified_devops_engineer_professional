import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr
def lambda_handler(event, context):

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.scan(
        Select= 'ALL_ATTRIBUTES',
        FilterExpression=Attr('account_type').begins_with("s")
    )
    items = response['Items']
    print("hello")
    print(items)
    return 'Hello from Lambda'
