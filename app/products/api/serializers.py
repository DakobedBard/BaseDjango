from rest_framework import serializers
# from products.models import Product
from upload.models import Document, StyleTransferModel
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
            'extension',
            'user'
        ]


class StyleTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleTransferModel
        fields = [
            'pk',
            'user',
            'title',
            'description',
            'base_image_name',
            'style_image_name',
            'base_image',
            'style_image',
            'output_image'
        ]
