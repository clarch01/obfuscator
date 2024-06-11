from pprint import pprint
import boto3
import re
from s3_url_splitter import s3_url_splitter
from list_buckets import list_buckets
from redactor import redactor
import pandas as pd
client = boto3.client('s3')

# get file from s3
# response = client.list_objects(
#     Bucket='obfuscator-bucket'
# # )
# # file = "s3://obfuscator-bucket/test-file-obfuscated"

# obj_response = client.get_object(
#     Bucket = 'obfuscator-bucket',
#     Key='test-file-obfuscated'
# )

# # print(obj_response)
# pprint(obj_response['Body'].read().decode('utf-8'))


# pprint(response)
# remove sensitive info
# upload to s3


# split = re.split(r"//|/", file, maxsplit=2)
# bucket = split[1]
# key = split[2]
# print(split)

# print(bucket, "BUCKET")
# print(key, "KEY")

# test = s3_url_splitter(file)

# print(test)

# print(list_buckets())


d = {"student_id": 1234,
     "name": 'John Smith',
     "course": 'Software',
     "cohort": 'March',
     "graduation_date": '2024-03-31',
     "email_address": 'j.smith@email.com'
     }

test_df = pd.DataFrame(data=d, index=[1])

print(redactor(test_df, ['names']))
