import boto3
from boto3.dynamodb.conditions import Key, Attr
def lambda_handler(event, context):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.query(
        KeyConditionExpression=Key('username').eq('janedoe1')
    )
    items = response['Items']
    print(items)
    return 'Hello from Lambda'
