from django.urls import re_path

from .views import GuitarTabListAPIView, GuitarTabRetrieveAPIView

app_name = 'products-api'

urlpatterns = [
    re_path(r'^$', GuitarTabListAPIView.as_view(), name='list'),
    re_path(r'^(?P<id>\d+)/$', GuitarTabRetrieveAPIView.as_view(), name='detail')

]