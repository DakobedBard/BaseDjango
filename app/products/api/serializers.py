from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price'
        ]

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'uploaded_at',
            's3Path',
            'bucket',
            'extension'
        ]
