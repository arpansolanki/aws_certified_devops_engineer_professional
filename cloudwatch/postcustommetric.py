import boto3
import random
client = boto3.client('cloudwatch', region_name='us-east-1')
#client.put_metric_data(namespace="testns",name="testmetric",unit="Count",value=3.0)
value = float(random.randint(1,101))
print(value)
# Put custom metrics
client.put_metric_data(
    MetricData=[
        {
            'MetricName': 'OpsMetric',
            'Dimensions': [
                {
                    'Name': 'Instance Name',
                    'Value': 'i-12345'
                },
            ],
            'Unit': 'None',
            'Value': value
        },
    ],
    Namespace='OpsNameSpace'
)
 