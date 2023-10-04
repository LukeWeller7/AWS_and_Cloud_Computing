import boto3

s3_client = boto3.client('s3')
response = s3_client.list_buckets() # Collects a list of available buckets


print('Existing buckets:   ')
for bucket in response['Buckets']:
    print(bucket['Name'])
