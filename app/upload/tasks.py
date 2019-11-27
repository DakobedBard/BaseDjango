from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.contrib.auth import get_user_model

from aws.ec2Client import ec2Client

User = get_user_model()

@shared_task
def launchEC2():
    print("I am in the celery method")
    ec2 = ec2Client()