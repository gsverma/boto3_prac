#! /usr/bin/env python

import sys
import boto3

client = boto3.client("s3")

#As request syntax had dozens of attributes, i have skipped all but few essentials
#these attributes could be added on need to implement basis

bucket_name = sys.argv[1]

#if(sys.argv[2] != NULL):

key_name = sys.argv[2]

try:
    response1 = client.get_object(Bucket=bucket_name, Key=key_name,)
    print response1
except Exception as error:
    print error

try:
    response2 = client.get_object_acl(Bucket=bucket_name, Key=key_name,)
    print response2
except Exception as error:
    print error

try:
    response3 = client.get_object_tagging(Bucket=bucket_name, Key=key_name,)
    print response3
except Exception as error:
    print error

#requesting objects metadata
try:
    response4 = client.head_object(Bucket=bucket_name, Key=key_name,)
    print response4
except Exception as error:
    print error


#the output hasnot been refined, a more readable output function ll be created when needed.
#this script was created only for testing available methods.
