from base.ec2Client import ec2Client

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
        instanceID = self.ec2.launch_instance('t2.micro', 'ec2-key-pair')
        return instanceID

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
