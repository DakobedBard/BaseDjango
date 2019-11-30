from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from products.models import Product
from upload.models import Document

from .serializers import  DocumentSerializer #ProductSerializer, DocumentSerializer

class DocumentListAPIView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#
# class ProductRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     lookup_field = 'id'