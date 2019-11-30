from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from products.models import Product
from upload.models import Document, StyleTransferModel
from django.db.models import Q
from .serializers import  DocumentSerializer, StyleTransferSerializer #ProductSerializer, DocumentSerializer

class DocumentListAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = Document.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query))
        return qs
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)



class StyleTransferListAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    serializer_class = StyleTransferSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        qs = StyleTransferModel.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query))
        return qs
    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)






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