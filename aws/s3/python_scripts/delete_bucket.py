import boto3
import sys


s3_client = boto3.client('s3')


def delete_all_objects(bucket_name):
    res = s3_client.list_objects_v2(Bucket=bucket_name) # Collecting all the files inside the bucket
    if 'Contents' in res:
        objects = [{'Key': obj['Key']} for obj in res['Contents']] # Placing the objects into a key format that will suit the delete_objects command
        s3_client.delete_objects(Bucket=bucket_name, Delete={'Objects': objects}) # deletes all the files within the bucket

delete_all_objects(sys.argv[1]) # naming the bucket to delete
s3_client.delete_bucket(Bucket=sys.argv[1])
