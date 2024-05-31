import re

def s3_url_splitter(url):
    split = re.split(r"//|/", url, maxsplit=2)
    bucket = split[1]
    key = split[2]
    return {"bucket": bucket,
            "key": key}