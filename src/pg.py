from pprint import pprint 
import boto3
import re
from s3_url_splitter import s3_url_splitter
from list_buckets import list_buckets
client = boto3.client('s3')

# get file from s3 
response = client.list_buckets()

obj_response = client.list_objects(
    Bucket = 'obfuscator-bucket'
)
# pprint(response)
# remove sensitive info
# upload to s3

file = "s3://obfuscator-bucket/test-file.csv"

# split = re.split(r"//|/", file, maxsplit=2)
# bucket = split[1]
# key = split[2]
# print(split)

# print(bucket, "BUCKET")
# print(key, "KEY")

# test = s3_url_splitter(file)

# print(test)

# print(list_buckets())

pprint(obj_response['Contents'])
