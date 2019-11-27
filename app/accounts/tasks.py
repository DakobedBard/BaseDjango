from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def post_signup_welcome_mail(user_pk=None):
    user = User.objects.filter(pk=user_pk)
    if user:
        print("Welcome {}".format(user.username))
    else:
        print("User not found")