from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

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