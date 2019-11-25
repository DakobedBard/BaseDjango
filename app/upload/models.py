from django.db import models

class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    s3Path = models.CharField(max_length=500, default='file.txt')
    user = models.CharField(max_length=50,default="Charles")
    bucket=models.CharField(max_length=50, default="basedjango")
    extension = models.CharField(max_length=50, default=".txt")

class EC2Instance(models.Model):
    '''
    There is a default field with name "id" which is auto increment..
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    instance_ID = models.CharField(max_length=30)
    application = models.CharField(max_length=30)
    user = models.CharField(max_length=50, default="BillyStrings@gmail.com")


class StyleTransfer(models.Model):
     style_image = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='style')
     base_image = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='image')

