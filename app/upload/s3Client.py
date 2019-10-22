import sys
import boto3
import botocore
import logging
from botocore.exceptions import ClientError
import os
from upload.models import Document
class s3Client:
    def __init__(self, bucketname, username):
        self.bucket = bucketname
        self.username = username


    def upload_file(self,file_name, object_name=None):
        """Upload a file to an S3 bucket
        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            with open("/usr/src/app/" +file_name, "rb") as f:
                print("I open the file " + str(file_name))
                s3_client.upload_fileobj(f, self.bucket, "youtube.mp3")
                document = Document(s3Path=file_name,user=self.username,bucket=self.bucket)
                document.save()
        except ClientError as e:
            logging.error(e)
            print(e)
            return False
        return True

    def download(self):
        pass

    def setBucketName(self, bucketname):
        self.bucket = bucketname