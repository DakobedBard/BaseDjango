from rest_framework import serializers
# from products.models import Product
from upload.models import Document
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = [
#             'id',
#             'title',
#             'description',
#             'price'
#         ]

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id',
            'uploaded_at',
            's3Path',
            'bucket',
            'extension'
        ]
