from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from aws.s3Client import s3Client
from aws.ec2Client import ec2Client
from upload.models import EC2Instance

from upload.forms import AudioFilesForm

from upload.tasks import celery_style_transfer
from django import forms

from django.views import View

class ListAudioFilesView(View):
    pass



class TabsListView(View):
    def get(self, request):
        context = {}
        return render(request, 'list_tabs.html', context)
    def post(self, request):
        context = {}
        return render(request, 'list_tabs.html', context)







class TabsView(View):
    '''

    :param request:
    :param args:
    :param kwargs:
    :return:

    This view will return the model.html template.  This page will allow the user to load a model from s3
    '''
    def get(self, request):
        pass
    def post(self, request):
        pass






def load_tab(request, *args, **kwargs):
    context = {}
    return render(request, "tabs.html", context)
