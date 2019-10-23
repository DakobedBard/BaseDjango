import boto3

class ec2Client:
    def __init__(self, ami):
        self.AMI = ami
        self.REGION = 'us-west-2'

    def launch_instance(self, instance_type, PemKey, bootstrap_script=None):
        ec2 = boto3.resource('ec2', region_name=self.REGION)
        instances = ec2.create_instances(
            ImageId=self.AMI,
            MinCount=1,
            MaxCount=1,
            KeyName=PemKey,
            InstanceInitiatedShutdownBehavior='terminate',
            IamInstanceProfile={'Name': 'S3fullaccess'},
            InstanceType=instance_type,
            SecurityGroupIds=['sg-03915a624fb5bf7bd'],
            UserData=bootstrap_script
        )

    def remove_instance(self):
        pass


