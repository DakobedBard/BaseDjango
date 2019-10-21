from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView

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
