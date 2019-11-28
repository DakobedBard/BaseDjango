from __future__ import absolute_import, unicode_literals
from celery import shared_task

from django.contrib.auth import get_user_model

from aws.ec2Client import ec2Client

from style_transfer.style_transfer import StyleTransfer
User = get_user_model()

from upload.models import StyleTransferModel

@shared_task
def celery_style_transfer(user, image_document, style_document):
    '''
    This will be the async call that will launch the EC2 instance.  What should the task return?
    Probably a model object of a Style Transfer type>?

    :param user:
    :param image_document:
    :param style_document:
    :return:
    '''

    print("I am in the celery method")
    style_transfer = StyleTransfer(user, image_document.pk, style_document.pk)
    style_transfer.launchEC2()

    model = StyleTransferModel()
    model.style_image_document_id =  style_transfer.style_document_id
    model.base_image_document_id = style_transfer.image_document_id





