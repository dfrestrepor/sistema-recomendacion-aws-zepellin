#!/usr/bin/env python3

import logging
import os
import boto3
from botocore.exceptions import ClientError

logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)

s3_client = boto3.client('s3')

def main():
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = f'{dir_path}/'
    bucket_name = 'S3-data-emr-motor'
    upload_directory(path, bucket_name)


def upload_s3(path, bucket_name):
    """Upload a bucket s3"""

    for root, dirs, files in os.walk(path):
        for file in files:
            try:
                if file != '_placeholder':  
                    file_directory = os.path.basename(os.path.dirname(os.path.join(root, file)))
		    key = f'{file_directory}/{file}'
                    s3_client.upload_file(os.path.join(root, file), bucket_name, key)
                    print(f"File '{key}' uploaded to bucket '{bucket_name}'")
            except ClientError as e:
                logging.error(e)


if __name__ == '__main__':
    main()
