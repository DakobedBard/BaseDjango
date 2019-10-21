from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {
        'form':form
    })

class Home(TemplateView):
    template_name = 'home.html'

def base(request):
    return render(request, "base.html")

def login(request):
    return render(request, "login.html")

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
