from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
#from base.forms.userCreationForm import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

def validate_link(link):
    '''
    :param link:     URL of youtube video whose audio I'd like to download and extract..
    :return:         If the link is valid returns the link, if the link is not valid, this function will attempt to return
                    a valid link.  (If the user passes in a list of links, will parse the passed in string to return the first
                    link..
    '''


def tabs(request, *args, **kwargs):
    context = {'method':request.method}
    return render(request, "slowdown.html", context)



def slow_down(request, *args, **kwargs):
    if request.method == "POST":
        print("The request is " + request.method)
        count = User.objects.count()
        context = {'method': request.method,'count':count}
        return render(request, "slowdown.html", context)

    count = User.objects.count()
    context = {'method': request.method, 'count': count}
    return render(request, 'slowdown.html', context)