#! /usr/bin/env python

import sys
import boto3

client = boto3.client("s3")
s3 = boto3.resource("s3")
bucket_name = sys.argv[1]
key_name = sys.argv[2]

try:
    response = client.put_object(Bucket=bucket_name, Key=key_name,)
    #with open(key_name) as f:
     #   object_data = f.read()
    print response
except Exception as error:
    print error

#the output hasnot been refined, a more readable output function ll be created when needed.
#this script was created only for testing available methods.
