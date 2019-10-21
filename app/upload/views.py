from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
#from base.forms.userCreationForm import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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

def base(request):
    return render(request, "base.html")

def login(request):
    return render(request, "registration/login.html")

def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:
        image_file = request.FILES["image_file"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
        print(image_url)
        return render(request, "upload.html", {
            "image_url": image_url
        })
    return render(request, "upload.html")

@login_required
def upload(request):
    print("The users email is " + request.user.email)
    '''
    Alright I need to pass in the user

    '''


