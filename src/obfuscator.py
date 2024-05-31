import csv
import pandas as pd
import boto3
from pprint import pprint
from io import StringIO

from redactor import redactor
from s3_url_splitter import s3_url_splitter

def obfuscator(input):
    client = boto3.client('s3')


    # split input 'file_to_obfuscate' into bucket and key values
    url = s3_url_splitter(input['file_to_obfuscate'])
    bucket = url['bucket']
    key = url['key']

# get the object from bucket 
    response = client.get_object(
        Bucket=url['bucket'],
        Key=url['key']
    )
    file_bytestream = StringIO(response['Body'].read().decode('utf-8'))

    # pprint(file_bytestream.read())
    
    df = pd.DataFrame(file_bytestream)
    df.columns = df.iloc[0]
    df = df[1:]
    # dataframe is split into columns correctly for test case
    pprint(df)
# remove senesitive data
    # data = pd.read_csv(input['file_to_obfuscate'])
    # # column_names = list(data.columns)
    # for field in input['pii_fields']:
    #     new_column = data[field].apply(redactor)
    #     data[field] = new_column

    # print(data)
# put new file back to s3 

test_input = {
    "file_to_obfuscate": "s3://obfuscator-bucket/test-file",
    "pii_fields": ["name", "email_address"]
}

# list_buckets()
obfuscator(test_input)