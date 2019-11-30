from django.urls import re_path

from .views import DocumentListAPIView  # ProductListAPIView, ProductRetrieveAPIView,\


app_name = 'products-api'

urlpatterns = [
    re_path(r'^$', DocumentListAPIView.as_view(), name='list'),
    # re_path(r'^(?P<id>\d+)/$', ProductRetrieveAPIView.as_view(), name='detail')

]