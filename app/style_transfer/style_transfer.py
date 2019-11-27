from base.ec2Client import ec2Client

test_keras_install = '''#!/bin/bash
cd /home/ubuntu
sudo pip install librosa
sudo pip install tensorflow
sudo pip install keras
sudo pip freeze | grep "keras" > /home/ubuntu/keras.txt
git clone https://github.com/MathiasDarr/KerasStyleTransfer.git 
sudo bash KerasStyleTransfer/test_keras_import.py > keras_import.txt
'''


AmazonUserData = '''#!/bin/bash
cd home/ubuntu

sudo mkdir anaconda
cd anaconda
sudo wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
sudo bash Anaconda3-5.0.1-Linux-x86_64.sh
export python3=/anaconda/anaconda3/bin/python
cd /home/ubuntu

sudo mkdir results

git clone https://github.com/HeywardSoftware/BaseDjango.git
$python3 BaseDjango/app/base/downloadS3.py 'base_image.jpg' base_image.jpg
$python3 BaseDjango/app/base/downloadS3.py 'style_image.jpg' style_image.jpg

$python3 KerasStyleTransfer/styletransfer.py style_image.jpg base_image.jpg results/myimage

'''


script = '''sudo /anaconda/anaconda3/bin/pip install --upgrade pip
python3 KerasStyleTransfer/downloadS3.py 'base_image.jpg' base_image.jpg {}
sudo /anaconda/anaconda3/bin/pip install tensorflow
sudo /anaconda/anaconda3/bin/pip install keras

sudo /anaconda/anaconda3/bin/pip install tensorflow
sudo /anaconda/anaconda3/bin/pip install keras
'''.format('basedjango')


class StyleTransfer:
    def __init__(self, user, image_document_id, style_document_id):
        self.user = user
        self.image_id = image_document_id
        self._style_id = style_document_id

    def validate(self):
        '''
        Validate the images for dimensions etc
        :return: True if the image dimensions are good.
        '''
        return True
    def resize(self, image_url, height, width):
        '''
        :param image_url:  S3 path (or the path in the mediafiles??
        :param height: height to resize the image to
        :param width: width to resize the image to
        :return:
        '''
    def launchEC2(self):
        '''
        Launch the EC2 instance.
        :return:
        '''
        self. ec2 = ec2Client("TabGenerator", self.user)
        instance = self.ec2.launch_instance('g3s.xlarge', 'ec2-key-pair', bootstrap_script=test_keras_install)
        print("The instance ID is " + instance[0].id)
        return instance[0].id

    def terminateEC2(self, instanceID):
        try:
            self.ec2.terminate_instance(instanceID)
        except Exception as e:
            print("The error " +e)
        return True









    def returnImage(self):
        '''
        This might have to be an asynchronous call that I have to make ... It will have to wait for the EC2 instance to
        terminate and return the image..

        :return:
        '''
