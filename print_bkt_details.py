#!/usr/bin/env python

import sys
import boto3

s3 = boto3.resource('s3')
bucket_name = sys.argv[1]
client = boto3.client('s3')

try:
    response1 = client.get_bucket_policy(Bucket=bucket_name)
    print ("\n---------Bucket policy---------\n")
    print response1
    print ("\n ------------------------------------------------- \n")
except Exception as error:
    print ("\n----------Bucket policy-------------\n")
    print error
    print ("\n ------------------------------------------------- \n")

try:
    response2 = client.get_bucket_replication(Bucket=bucket_name)
    print ("\n ---------Replication configuration--------------- \n")
    print response2
    print ("\n ------------------------------------------------- \n")
except Exception as error:
    print ("\n ----------Replication configuration-------------- \n")
    print error
    print ("\n ------------------------------------------------- \n")

try:
    response3 = client.get_bucket_request_payment(Bucket=bucket_name)
    print ("\n ----------------paymnent details----------------- \n")
    print response3
    print ("\n ------------------------------------------------- \n")
except Exception as error:
    print ("\n ---------------payment details------------------- \n")
    print error
    print (" \n ------------------------------------------------- \n")
try:
    response4 = client.get_bucket_tagging(Bucket=bucket_name)
    print ("\n ------------------tag details-------------------- \n")
    print response4
    print ("\n ------------------------------------------------- \n")
except Exception as error:
    print ("\n ------------------tag details-------------------- \n")
    print error
    print ("\n ------------------------------------------------- \n")

try:
    response5 = client.get_bucket_versioning(Bucket=bucket_name)
    print ("\n -------------bucket version details------------- \n")
    print response5
    print ("\n ------------------------------------------------- \n")
except Exception as error:
    print ("\n --------------bucket version details------------ \n")
    print error
    print ("\n ------------------------------------------------ \n")
try:
    response6 = client.get_bucket_website(Bucket=bucket_name)
    print ("\n-------------bucket website configuration-------- \n")
    print response6
except Exception as error:
    print ("\n------------ bucket website configuration--------- \n")
    print error
