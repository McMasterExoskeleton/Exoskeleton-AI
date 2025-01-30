# a script that can be run to find out all the folders and sub-folders ( CONTENT ) of the s3 bucket, otherwise ppl need to wait for others to response? import boto3
## use this script to find the --version (could be anything) and the file name ( ends with .txt / .csv) to download in a file path (i.e folders) that exsist otherwise error

import boto3  
import os 
from dotenv import load_dotenv 

def list_all_contents():

    load_dotenv() 
    
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID") 
    AWS_SECRET_ACCESS_KEY= os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_BUCKET_NAME= os.getenv("AWS_BUCKET_NAME")
    AWS_BUCKET_REGION= os.getenv("AWS_BUCKET_REGION")

    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name = AWS_BUCKET_REGION
    )
    
    paginator = s3.get_paginator('list_objects_v2')
    result = []

    for page in paginator.paginate(Bucket = AWS_BUCKET_NAME):
        for content in page.get('Contents', []):
            result.append(content['Key'])

    for item in result: 
        print(item) 

if __name__ == "__main__": 

    list_all_contents() 