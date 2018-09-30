import boto3
def lambda_handler(event, context):
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.Table('users')
    print(table.creation_date_time)
    
    table.put_item(
        Item={
            'username': 'janedoe1',
            'last_name': 'Doe1',
            'age': 25,
            'account_type': 'standard_user',
            }
    )
    table.put_item(
        Item={
            'username': 'janedoe1',
            'last_name': 'Doe2',
            'age': 25,
            'account_type': 'standard_user',
            }
    )
    table.put_item(
        Item={
            'username': 'johndoe1',
            'last_name': 'Doe1',
            'age': 26,
            'account_type': 'admin_user',
            }
    )
    return 'Hello from Lambda'
