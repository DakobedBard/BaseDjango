

class StyleTransfer:
    def __init__(self, image_document_id, style_document_id):
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
        pass

    def returnImage(self):
        '''
        This might have to be an asynchronous call that I have to make ... It will have to wait for the EC2 instance to
        terminate and return the image..

        :return:
        '''
