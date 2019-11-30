from django.db import models
from django.urls import reverse
from upload.models import Document


def upload_product_image(instance, filename):
    Klass = instance.__class__
    id_ = Klass.objects.count()
    return f"products/{id_}/{filename}" # "products/{id_}/{filename}".format(id_=id_, filename=filename)

from django.conf import settings
from upload.models import Document
#
# class StyleTransferModel(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     description = models.CharField(max_length=200, default='')
#     base_image_name = models.CharField(max_length=50, default="base")
#     style_image_name = models.CharField(max_length=50, default ="stlye")
#     base_image = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='base-image+', default='')
#     style_image = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='style-image+', default='')
#     output_image = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='output-image+',default='')
# class Product(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     #image = models.ImageField(upload_to='products/', blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, default=9.99)
#
#     def __str__(self):
#         return self.title
#
#     def get_api_url(self):
#         return reverse("products-api:detail", kwargs={"id": self.id})