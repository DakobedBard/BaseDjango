from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.contrib.auth.models import User

def upload_location(instance, filename, **kwargs):
    file_path = 'tabs/{user_id}/{title}/{filename}{}'.format(
    user_id=str(instance.user.id), title=str(instance.title), filename=filename)
    return file_path

class AudioFile(models.Model):
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="up_loaded")
    link = models.CharField(max_length=100)
    slowdown = models.IntegerField(default=100)
    title = models.CharField(max_length=30)
    bucket=models.CharField(max_length=50, default="basedjango")
    path=models.CharField(max_length=50, default="basedjango")

    def __str__(self):
        return self.title


# class GuitarTab(models.Model):
#     date_updated = models.DateTimeField(auto_now_add=True, verbose_name="date update")
#     date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
#     s3AudioPath = models.CharField(max_length=500, default='file.txt')
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     bucket=models.CharField(max_length=50, default="basedjango")
#     title = models.CharField(max_length=50)
#     artist = models.CharField(max_length=50, default="None")
#     youtube_link=models.CharField(max_length=100, default="https://www.youtube.com/watch?v=UTj_wY_6Tas")
#     image = models.ImageField(upload_to=upload_location, null= False, blank = False)
#     slug = models.SlugField(blank=True, unique=True)
#
#     def __str__(self):
#         return self.title

# @receiver(post_delete, sender=GuitarTab)
# def submission_delete(sender, instance, **kwargs):
#     instance.image.delete(False)
#
# def pre_save_tab_post_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(instance.author.username+"-"+instance.title)