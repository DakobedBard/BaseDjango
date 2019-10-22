import sys
import boto3
import botocore
import logging
from botocore.exceptions import ClientError
class s3Client:
    def __init__(self, bucketname, username):
        self.bucket = bucketname

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
                s3_client.upload_fileobj(f, self.bucket, "OBJECT_NAME")
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def download(self):
        pass

    def setBucketName(self, bucketname):
        self.bucket = bucketname