import boto3
import sys


s3_client = boto3.client('s3')
s3_client.download_file(sys.argv[1], sys.argv[2], sys.argv[3])
