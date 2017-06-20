#!/usr/bin/env python
import sys
import boto3
import botocore

s3 = boto3.resource("s3")

bucket_name = sys.argv[1]
key = sys.argv[2]
local_file_name = sys.argv[3]

try:
    response = s3.Bucket(bucket_name).download_file(key, local_file_name)
    print response
except Exception as error:
    print error
