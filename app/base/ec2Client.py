import boto3
from upload.models import EC2Instance

import time


class ec2Client:
    '''
    I am hardcoding the AMI ... I should look
    '''

    def __init__(self, application, user):
        self.AMI = 'ami-01a4e5be5f289dd12'
        self.REGION = 'us-west-2'
        self.application = application
        self.user = user

    def launch_instance(self, instance_type, PemKey, bootstrap_script=""):
        '''
        :param instance_type:
        :param PemKey:
        :param bootstrap_script:
        :return: instance ID

        Should this return the AWS instance ID or the models PK?? Probably the primary key..
        '''
        ec2 = boto3.resource('ec2', region_name=self.REGION)
        instance = ec2.create_instances(
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

        instance_model = EC2Instance()
        instance_model.instance_ID = instance[0].id
        instance_model.application = self.application
        instance_model.user = self.user
        time.sleep(10)

        instance_model.instance_dns = self.ge

        instance_model.save()

    def get_name(self, instance_id):
        '''

        :param instance_id:
        :return: the dns name of the instance
        '''
        ec2 = boto3.client('ec2')
        response = ec2.describe_instances()

        instancelist = []
        for reservation in (response["Reservations"]):
            for instance in reservation["Instances"]:
                instancelist.append(instance["InstanceId"])
        ec2client = boto3.resource('ec2')
        # response = ec2client.describe_instances()

        instances = ec2client.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        ids = []
        dns = ""
        for instance in instances:
            if instance.id == instance_id:
                ids.append(instance.id)
                resp = ec2.describe_network_interfaces();
                print("printing pub dns name")
                print(resp['NetworkInterfaces'][0]['Association']['PublicDnsName'])
                dns = resp['NetworkInterfaces'][0]['Association']['PublicDnsName']
        return dns
    def terminate_instance(self, instanceID):
        '''
        :param instanceID:  Is this the primary key of the document in the database or the
        :return:
        '''

        ec2 = boto3.resource('ec2', region_name=self.REGION)
        ec2.instances.filter(InstanceIds=[instanceID]).terminate()
        #instance_model = EC2Instance.__class__.objects.get(instance_ID=instanceID)
        instance_model = EC2Instance.objects.filter(instance_ID=instanceID)
        instance_model.delete()

    def stop_instance(self, instanceID):
        ec2 = boto3.resource('ec2', region_name=self.REGION)
        ec2.instances.filter(InstanceIds=[instanceID]).stop()


