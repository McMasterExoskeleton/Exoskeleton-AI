import os 
import boto3  ## (requirements.txt)

import argparse ## in built python library 
from dotenv import load_dotenv # pip install -dotenv ( requirements.txt  )

def upload_data(version, function, path): 
    try: 
        s3.upload_file(path, AWS_BUCKET_NAME, f"{version}/{function}/{os.path.basename(path)}")
        #basename = example: home/users/data.txt basename is the data.txt (what the file name will be in the bucket and what it should be when uploading as well)
        print(f"Data uploaded to s3://{AWS_BUCKET_NAME}/{version}/{function}/{os.path.basename(path)}")
    except Exception as e: 
        print(f"Error uploading file: {e}")


def download_data(version, function, path): 
    
    try: 
        s3.download_file(AWS_BUCKET_NAME, f"{version}/{function}/{os.path.basename(path)}", path)
        ## 
        print(f"Data downloaded to {path}")
    
    except Exception as e : 
        print(f"Error downloading data: {e}")


def main(action, version, function, path): 
    if action == "UPLOAD": 
        upload_data(version, function, path)
    elif action == "DOWNLOAD": 
        download_data(version, function, path)



if __name__ == "__main__": 
    
    load_dotenv() ## # reads .env file that will be git ignored so everyone accessing the data from the cloud needs to be 

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


    parser = argparse.ArgumentParser(description="Upload or Download Exoskelton Sensor Data ")
    parser.add_argument("--action", type=str, required= True, choices=["UPLOAD","DOWNLOAD"],help="Upload or Download Exoskeleton Data")
    parser.add_argument("--version", type=str, required= True, help="Dataset Version (e.g 1.0, 2.0, ... )") 
    ## any name that the team puts in? thats why there is no restriction on version naming ( i.e does not have to be numbers) 

    parser.add_argument("--function", type=str, required= True, choices=["WALK","RUN","CLIMB"],help="Action for Exoskeleton")
    parser.add_argument("--path", type=str, required= True, help="Path where data will be uploaded from, or downloaded to")
    ## path must exsist, and file name must exsist under the function otherwise cannot download or upload 

    # verion if action is upload and it is a new version then the new version type needs to exsist or something 
    args = parser.parse_args() 
    main(args.action, args.version, args.function, args.path)

    ## just ask people to drag and drop the csv/text files in the data folder so that it would be easier for them to upload by having a simple predeteremined file path 
    ## it would be ../../data/----- and where they place the rest of the data 