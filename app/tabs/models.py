from django.db import models

class GuitarTab(models.Model):
    title = models.CharField(max_length=30)
    audio_file_path = models.CharField(max_length=30)
    bucket = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    content = models.CharField(max_length=30, default="")

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


class Tablature:
    '''
    This model will represent a tab in the database.. How do I want to store a tab?

    '''
    tab_name = models.CharField(max_length=30)
    audio_file_path = models.CharField(max_length=30)
    bucket = models.CharField(max_length=30)

class MirModel:
    '''
    This model will represent an MIR model.
    The fields for this will be the path in the s3 bucet to the keras model object.

    '''
    model = models.CharField(max_length=40) # This is the path to the model object in S3.  This will be the keras model.

    bucket = models.CharField(max_length=30, default='basedjango')
