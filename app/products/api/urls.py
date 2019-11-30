from django.urls import re_path

from .views import DocumentListAPIView , StyleTransferListAPIView # ProductListAPIView, ProductRetrieveAPIView,\



app_name = 'products-api'

urlpatterns = [

    re_path(r'^$', DocumentListAPIView.as_view(), name='list'),
    re_path(r'style', StyleTransferListAPIView.as_view())

]