from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from rest_framework.generics import ListAPIView
from tabs.models import GuitarTab

class GuitarTabListAPIView(ListAPIView):
    queryset = GuitarTab.objects.all()



from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


from upload.tasks import celery_style_transfer
from django import forms

from tabs.models import GuitarTab

from django.views import View

class ListAudioFilesView(View):
    pass



def newTab(request):
    context = {}
    return render(request, "new_tab.html", context )

class TabsListView(View):
    def get(self, request):
        context = {'posts':''}
        return render(request, 'tabs.html' , context)
    def post(self, request):
        context = {}
        return render(request, 'tabs.html', context)

class TabCreateView(LoginRequiredMixin, CreateView):
    model = GuitarTab
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class TabDetailView(DetailView):
    model = GuitarTab


class CreateTabView(View):
    model = GuitarTab
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



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
