from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
#from base.forms.userCreationForm import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from upload.s3Client import s3Client
from tab_generator.audio.youtube_download import download
from django import forms
from upload.models import Document
import os
def validate_link(link):
    '''
    :param link:     URL of youtube video whose audio I'd like to download and extract..
    :return:         If the link is valid returns the link, if the link is not valid, this function will attempt to return
                    a valid link.  (If the user passes in a list of links, will parse the passed in string to return the first
                    link..
    '''


class LinkForm(forms.Form):
    youtube_link = forms.CharField(label="youtubelink", max_length=200)

    def cleanLinkData(self):
        data = self.cleaned_data['youtube_link']
        return data

def player(request, *args, **kwargs):
    context = {}
    return render(request, 'player.html', context)

def latestFileUpdate(directory=None):
    '''
    :return: Returns a file path to the most recenly updated file in the current directory
    '''
    files = os.listdir()
    modified_file = max(files, key=os.path.getctime)
    print("The most recently mod file " + modified_file)
    return modified_file


def list(request, *args, **kwargs):
    docuemnts = Document.objects.filter(user=request.user)
    context = {'method': request.method, 'count': len(docuemnts), 'documents':docuemnts}
    return render(request, 'list.html', context )
def slow_down(request, *args, **kwargs):
    if request.method == "POST":
        print("The request is " + request.method)
        count = User.objects.count()
        form = LinkForm(request.POST)
        print("The request is of type")
        print(str(type(request)))

        if form.is_valid():
            link = form.cleanLinkData()
            download(link)
            uploadFile = latestFileUpdate()
            s3 = s3Client('basedjango',request.user)
            s3.upload_file(uploadFile,"youtubeFile")
        else:
            link = "Invalid Link"
        context = {'method': request.method,'link':link}
        #download()
        #s3 = s3Client('djangobase', request.user)

        return render(request, "slowdown.html", context)
    else:
        form = LinkForm
        count = User.objects.count()
        context = {'method': request.method, 'form': form}
        return render(request, 'slowdown.html', context)