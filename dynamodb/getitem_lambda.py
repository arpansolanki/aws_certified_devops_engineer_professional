import boto3
def lambda_handler(event, context):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.get_item(
        Key={
            'username': 'mac001',
            'last_name': 'Mack'
            }
    )
    item = response['Item']
    print(item)
    return 'Hello from Lambda'
