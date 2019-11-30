




from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

#
# from products.models import Product

from .serializers import GuitarTabSerializer

class GuitarTabListAPIView(generics.ListAPIView):
    pass
    # queryset = Product.objects.all()
    # serializer_class = GuitarTabSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]


class GuitarTabRetrieveAPIView(generics.RetrieveAPIView):
    pass
    # queryset = Product.objects.all()
    # serializer_class = GuitarTabSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # lookup_field = 'id'


