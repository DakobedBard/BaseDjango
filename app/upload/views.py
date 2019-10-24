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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {
        'form':form
    })

def login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "registration/login.html", {
        'form':form
    })

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })

@login_required
def secret_page(request):
    return render(request, 'account_details.html')

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'account_details.html'

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
from django import forms

class AudioFilesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        files = kwargs.pop('files')
        super(AudioFilesForm, self).__init__(*args, **kwargs)
        counter = 1
        for q in files:
            #self.fields['files-' + str(counter)] = forms.CharField(label='file')
            self.fields[str(q)] = forms.BooleanField(required=False)

            counter += 1

def list(request, *args, **kwargs):
    docuemnts = Document.objects.filter(user=request.user)
    # context = {'method': request.method, 'count': len(docuemnts), 'documents':docuemnts}
    #

    document_files =  docuemnts.values('s3Path')

    # context['form'] = form
    # # s3 = s3Client('basedjango', request.user )
    # # s3.upload_file(image_url)
    context = {}
    context['documents'] = document_files
    selections = []
    if request.method == 'POST':
        form = AudioFilesForm(request.POST, files=document_files)
        #form = MyForm()
        context['form'] = form
        #context['selections']
        s3 = s3Client('djangobase', request.user)
        if form.is_valid():
            fields = form.fields
            booleans = []
            for field in fields:
                if form.cleaned_data[field]:
                    s3.delete(field)
            context['choices'] = booleans

    else:
        form = AudioFilesForm(files=document_files)

        context['form'] = form
    return render(request, 'list.html',context)







from django import forms



