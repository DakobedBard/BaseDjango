from base.ec2Client import ec2Client

train_model_script = '''
git clone https://github.com/HeywardSoftware/BaseDjango.git

'''
from upload.s3Client import s3Client

class MIR:
    def __init__(self, user,  s3_bucket, data_bucket=None, generate_spectogrms=False):
        '''
        If the data bucket is set to None then it will be assumed that the s3_bucket parameter will be pointing to an S3
        bucket that has a test & train folders.  Otherwise the data_bucket will be an S3 bucket with the raw data..

        :param s3_bucket:
        :param data_bucket:
        :param generate_spectogrms:
        '''
        self.s3 = s3_bucket
        self.user = user
        if data_bucket != None:
            self.generate_spectograms()

    def launchEC2(self):
        '''
        Launch the EC2 instance.
        :return:
        '''
        self. ec2 = ec2Client("TabGenerator", self.user)
        instance = self.ec2.launch_instance('g3s.xlarge', 'ec2-key-pair', bootstrap_script=train_model_script)
        print("The instance ID is " + instance[0].id)
        return instance[0].id

    def terminateEC2(self, instanceID):
        try:
            self.ec2.terminate_instance(instanceID)
        except Exception as e:
            print("The error " +e)
        return True

    def generate_spectograms(self):
        pass

    def train_model(self):
        instance_id = self.launchEC2()

