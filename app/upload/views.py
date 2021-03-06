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

from style_transfer.style_transfer import StyleTransfer


def style(request, *args, **kwargs):
    context = {}
    if request.method == "POST" and request.FILES["image_file"]:
        user = request.user
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        image_url_string = str(image_url)
        s3 = s3Client('basedjango', user )
        image_document = s3.upload_file(image_url, image_url_string.split("/")[-1])

        style_file = request.FILES["style_image"]
        fs = FileSystemStorage()
        filename = fs.save(style_file.name, style_file)
        style_url = fs.url(filename)
        style_url_string = str(style_url)
        s3 = s3Client('basedjango', user )
        style_document = s3.upload_file(style_url, style_url_string.split("/")[-1])
        context =  {"image_url": image_url, "style_url":style_url}

        # output_image = celery_style_transfer.delay()

        return render(request, "style_transfer.html", context)

    #if request.method == "POST" and request.

    return render(request, "style_transfer.html")

from mir.MIR import MIR

def train_model(request, *args, **kwargs):
    '''
    :param request:
    :param args:
    :param kwargs:
    :return:

    This view will return the model.html template.  This page will allow the user to load a model from s3

    '''
    context = {}
    if request.method == "POST":
        mir = MIR(request.user, "heyward-audio-tabs")
        instance_id = mir.train_model()
    return render(request, "model.html", context)

def generate_spectograms(request, *args, **kwargs):
    context = {}
    return render(request, "model.html", context)


from upload.models import Document

@login_required
def upload(request):
    print("The users email is " + request.user.email)
    '''
    Alright I need to pass in the user

    '''


