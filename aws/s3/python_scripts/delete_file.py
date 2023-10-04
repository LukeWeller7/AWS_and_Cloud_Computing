import boto3
import sys


s3_client = boto3.client('s3')
s3_client.delete_object(Bucket=sys.argv[1], Key=sys.argv[2])
