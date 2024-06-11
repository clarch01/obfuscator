import pandas as pd
import boto3
from io import StringIO

from redactor import redactor
from s3_url_splitter import s3_url_splitter


def obfuscator(input):
    client = boto3.client('s3')

# split input 'file_to_obfuscate' into bucket and key values
    bucket_key = s3_url_splitter(input['file_to_obfuscate'])

# get the object from bucket
    response = client.get_object(
        Bucket=bucket_key['bucket'],
        Key=bucket_key['key']
    )
    file_bytestream = response['Body'].read().decode('utf-8')

# remove senesitive data
    df = pd.read_csv(StringIO(file_bytestream))

    df = redactor(df, input['pii_fields'])

    return bytes(pd.DataFrame.to_csv(df), encoding='utf-8')


# test_input = {
#     "file_to_obfuscate": "s3://obfuscator-bucket/test-file",
#     "pii_fields": ["name", "email_address"]
# }

# # list_buckets()
# obfuscator(test_input)
