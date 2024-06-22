import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.start_instances(
        InstanceIds=['i-1234567890abcdef0'],
    )
    return response
