import boto3 # Import the boto3 library
import sys # Import sys

s3_client = boto3.client('s3') # Setting the client as the s3 on AWS
location = {'LocationConstraint': 'eu-west-1'} # Setting a variable for the region location of the bucket
s3_client.create_bucket(Bucket=sys.argv[1], CreateBucketConfiguration=location) # Create the bucket on AWS
