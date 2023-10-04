import boto3
import sys
import os


file_name = sys.argv[1] # First argument is the file name
bucket = sys.argv[2] # Second argument is the bucket location
object_name = os.path.basename(file_name) # setting the output object_name to file name

s3_client = boto3.client('s3') # Connecting client as s3
s3_client.upload_file(file_name, bucket, object_name) # Upload file to AWS
