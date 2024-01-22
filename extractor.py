import boto3
from botocore.exceptions import ClientError

def upload_object(bucket_name, keyname, file_to_upload):
    try:
        s3_client = boto3.client('s3')
        response = s3_client.upload_file(
            Filename=file_to_upload,
            Bucket=bucket_name, 
            Key=keyname,
            ExtraArgs={"Tagging": "Project=ZZZ&Area=AAA"}
        )
    except ClientError as e:
        print(e)
# Passamos por parametro o nome do bucket, nome da chave e path do arquivo local
upload_object("bucket-lambda-scripts", "avengers.csv", "./avengers.csv")