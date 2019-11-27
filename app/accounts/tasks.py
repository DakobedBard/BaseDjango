from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

@shared_task
def post_signup_welcome_mail(user_pk=None):
    user = User.objects.filter(pk=user_pk)
    send_mail(
        'Subject here',
        'Thanks for using our service..',
        'from@example.com',
        ['mddarr@gmail.com'],
        fail_silently=False,
    )
    if user:
        print("Welcome {}".format(user.username))
    else:
        print("User not found")