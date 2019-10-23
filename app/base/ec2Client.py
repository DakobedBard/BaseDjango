import boto3
from upload.models import EC2Instance


class ec2Client:
    '''
    I am hardcoding the AMI ... I should look
    '''

    def __init__(self, application, user):
        self.AMI = 'ami-01a4e5be5f289dd12'
        self.REGION = 'us-west-2'
        self.application = application
        self.user = user

    def launch_instance(self, instance_type, PemKey, bootstrap_script=None):
        ec2 = boto3.resource('ec2', region_name=self.REGION)
        instance = ec2.create_instances(
            ImageId=self.AMI,
            MinCount=1,
            MaxCount=1,
            KeyName=PemKey,
            InstanceInitiatedShutdownBehavior='terminate',
            IamInstanceProfile={'Name': 'S3fullaccess'},
            InstanceType=instance_type,
            SecurityGroupIds=['sg-03915a624fb5bf7bd']
        )
        instance_model = EC2Instance()
        instance_model.instance_ID = instance[0].id
        instance_model.application = self.application
        instance_model.user = self.user
        instance_model.save()

    def terminate_instance(self, instanceID):
        ec2 = boto3.resource('ec2', region_name=self.REGION)
        ec2.instances.filter(InstanceIds=[instanceID]).terminate()

    def stop_instance(self, instanceID):
        ec2 = boto3.resource('ec2', region_name=self.REGION)
        ec2.instances.filter(InstanceIds=[instanceID]).stop()


