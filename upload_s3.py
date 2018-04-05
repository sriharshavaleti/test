# test
import boto3 as boto
import mimetypes
import sys
import os

path = sys.argv[1]
s3 = boto.resource('s3')
filename = os.path.basename(path)
with open(path,'rb') as file_content:
    content_type = mimetype.guess_type(path)
    s3.Object(bucket_name, key+filename).put(ContentType = content_type[0],Body = file_content,ACL = 'public-read')
    print("File uploaded succesfully")

