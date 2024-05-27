import csv
import pandas as pd
import boto3
from pprint import pprint

def obfuscator(input):
    data = pd.read_csv(input['file_to_obfuscate'])
    # column_names = list(data.columns)
    for field in input['pii_fields']:
        new_column = data[field].apply(redactor)
        data[field] = new_column

    print(data)

def redactor(x):
    return "xxx"

def list_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    pprint(response)

input = {
    "file_to_obfuscate": "test.csv",
    "pii_fields": ["name", "email_address"]
}

# list_buckets()
obfuscator(input)