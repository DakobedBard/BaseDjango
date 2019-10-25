from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from upload.s3Client import s3Client
from base.ec2Client import ec2Client
from upload.models import EC2Instance
import os
from django.urls import reverse_lazy

from upload.forms import AudioFilesForm

from django import forms

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))



def list(request, *args, **kwargs):
    docuemnts = Document.objects.filter(user=request.user)
    document_files =  docuemnts.values('s3Path')

    context = {}
    userform = UserForm()
    context['userform'] = userform
    context['documents'] = document_files
    selections = []
    if request.method == 'POST':
        form = AudioFilesForm(request.POST, files=document_files)
        context['form'] = form

        s3 = s3Client('basedjango', request.user)
        if form.is_valid():
            fields = form.fields

            booleans = []
            for index, field in enumerate(fields):
                if form.cleaned_data[field]:
                    document = document_files[index]
                    keys =  document.keys()

                    for key in keys:
                        path = document[key]
                        filepath = path.split("/")[-1]
                        print("The filepath is " + filepath)
                        is_deleted = s3.delete(filepath)
                        print("keys")
                        Document.objects.filter(s3Path = document['s3Path']).delete()

            context['choices'] = booleans

    else:
        form = AudioFilesForm(files=document_files)

        context['form'] = form
    return render(request, 'list.html',context)

class Upload(TemplateView):
    template_name = 'upload.html'



def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        image_url_string = str(image_url)

        print("The type of the image url is " )
        print(type(image_url))
        print("The image file is " + image_url_string.split("/")[-1])
        print("The type of the image url is ")
        print(type(image_url_string))
        s3 = s3Client('basedjango', request.user )
        s3.upload_file(image_url, image_url_string.split("/")[-1])
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")

def file_download(request, *args, **kwargs):
    s3 = s3Client('basedjango', request.user)
    s3.download("youtube.mp3")
    return render(request, "home.html")

def delete_file(request, *args, **kwargs):
    s3 = s3Client('basedjango', request.user)
    s3.delete("youtube.mp3")
    return render(request, "home.html")


def launch_instance(request, *args, **kwargs):
    ec2 = ec2Client("TabGenerator",request.user)
    ec2.launch_instance('t2.micro','ec2-key-pair')
    instances = EC2Instance.objects.all()

    context = {"instances":instances}
    return render(request, "instances.html", context)

def terminate(request,instanceID ):
    instances = EC2Instance.objects.all()
    context = {"instances":instances}
    ec2 = ec2Client("TabGenerator", request.user)
    ec2.terminate_instance(instanceID)
    return render(request, "instances.html", context)


def list_instances(request, *args, **kwargs):
    instances = EC2Instance.objects.all()
    length = len(instances)
    context = {"instances":instances, "length":length}
    return render(request, "instances.html", context)

from upload.models import Document


@login_required
def upload(request):
    print("The users email is " + request.user.email)
    '''
    Alright I need to pass in the user

    '''
