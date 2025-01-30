# Required Libraries: 

> pip install boto3 

> pip install python-dotenv

# Getting Access to S3: 
After having a local version of the repo, in the Exoskeleton-AI create a .env file and config it like the following: 

>AWS_ACCESS_KEY_ID=  

>AWS_SECRET_ACCESS_KEY= 

>AWS_BUCKET_NAME= mcmaster-exoskeleton-ai-data 

>AWS_BUCKET_REGION= us-east-2

and get the aws_access_key_id and aws_secret_access_key privately ( aws_bucket_name might be subjected to change) 


# Viewing s3 bucket content 
To view the s3 bucket's content(folders, subfolders, files) to find version numbers, files to download, etc.  

Run this command:
>python3 s3_bucketContent.py


# Uploading/Downloading data
To download/upload files from the s3 bucket.

Run this command:
>python3 s3_script.py 
--action <strong>ACTION</strong> 
--version <strong>VERSION</strong> 
--function <strong>FUNCTION</strong> 
--path <strong>PATH</strong><br>

|Parameter|Description|Options| 
|-|-|-|
|<strong>ACTION</strong>| Upload or Download Exoskeleton Data| UPLOAD / DOWNLOAD
|<strong>VERSION</strong>| Dataset Version| 1.0, 2.0, . . .
|<strong>FUNCTION</strong>| Action for Exoskeleton| WALK, RUN, CLIMB
|<strong>PATH</strong>| Path where data will be uploaded from, or downloaded to

## Note: 

It best suggested where you download and upload files from a folder inside the local repo on ur machine as for the paths to be less complicated, in the following example 
the folder is called ***data***, the path must be relative to current directory that is currently being worked out of. 

### Examples: 
***Download***

>python3 s3_script.py --action DOWNLOAD --version 1.0 --function WALK --path ../../data/1.0/walk.csv 


make sure that the walk.csv file does exsist in the s3 bucket, if unsure which files exsist use the viewing s3 bucket script 

***Upload*** 

>python3 s3_script.py --action UPLOAD --version 2.0 --function RUN --path ../../data/2.0/run_v2.csv 

will upload it into s3 as 2.0 / RUN / run_v2.csv 
