from django.db import models
from django.conf import settings
class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    s3Path = models.CharField(max_length=500, default='file.txt')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bucket=models.CharField(max_length=50, default="basedjango")
    extension = models.CharField(max_length=50, default=".txt")
    def __str__(self):
        return "Document-Model"

class EC2Instance(models.Model):
    '''
    There is a default field with name "id" which is auto increment..
    '''
    created_at = models.DateTimeField(auto_now_add=True)
    instance_ID = models.CharField(max_length=30)
    instance_dns = models.CharField(max_length=80, default="")
    application = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Style(models.Model):
    style_image_s3Path = models.CharField(max_length=80)
    base_image = models.CharField(max_length=80)
    output_image = models.CharField(max_length=80)


class MirModel(models.Model):
    s3_bucket = models.CharField(max_length=30, default='heyward-audio-tabs')

class Spectogram(models.Model):
    annotation_file_path = models.CharField(max_length=40)
    audio_file_path = models.CharField(max_length=40)


class StyleTransferModel(models.Model):
    description = models.CharField(max_length=30)
    style_image_document_id = models.ForeignKey(Document, on_delete=models.CASCADE,related_name ='tyle_image_document')
    base_image_document_id = models.ForeignKey(Document, on_delete=models.CASCADE,related_name ='base_image_document')
    output_image_document_d = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='output_image_document', )
    style_image_title = models.CharField(max_length=20)
    base_image_title = models.CharField(max_length=20)
    output_image_title = models.CharField(max_length=30)

