#!/usr/bin/env python
import sys
import boto3

s3 = boto3.resource('s3')

bucket_name = sys.argv[1]
file_to_be_deleted = sys.argv[2]

bucket = s3.Bucket(bucket_name)

try:
    client = boto3.client('s3')
    response = client.delete_object(Bucket=bucket_name, Key=file_to_be_deleted)
    print response

#k = Key(bucket)
#try:
#    k.key = file_to_be_deleted
#    bucket.delete_key(k)
#    forDeletion = [{'key': file_to_be_deleted},]
#    response = bucket.delete_objects( Delete={'Objects': forDeletion})
#    print response
except Exception as error:
    print error
