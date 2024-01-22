import os
import zipfile
import boto3
import shutil

service_name = "minhaPrimeiraFuncao"

cloudformation_bucket = "bucket-lambda-scripts"

s3 = boto3.client("s3")

try:
    shutil.rmtree("package.zip", ignore_errors=True)
    os.remove("package")
except Exception as e:
    pass

os.system("pip install -r ./requirements.txt --upgrade --target package/")

to_move = ["lambda_function.py", "requirements.txt"]

[shutil.copyfile(file, f"package/{file}") for file in to_move]

shutil.make_archive("package", "zip", "package")

shutil.rmtree("package")

s3.upload_file(
    "package.zip",
    cloudformation_bucket,
    f"{service_name}/package.zip",
    {"ContentType": "application/zip"},
)

os.remove("package.zip")