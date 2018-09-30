import boto3
from boto3.dynamodb.conditions import Key, Attr
def lambda_handler(event, context):
    # TODO 
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.query(
        IndexName='account_type-index',
        KeyConditionExpression=Key('account_type').eq('standard_user')
        )

    items = response['Items']
    print(items)
    return 'Hello from Lambda'
