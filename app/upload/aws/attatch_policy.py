import boto3
'''
Demonstrating attatchign policy.. 
'''

iam = boto3.client("iam")

iam.attach_user_policy(UserName='asus-user',PolicyArn='arn:aws:iam::aws:policy/AmazonS3FullAccess')
