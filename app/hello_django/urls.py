from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import upload.views as views

urlpatterns = [
    path("", views.image_upload, name="upload"),
    path("admin/", admin.site.urls),
    path("login/",views.login , name="login"),
    path('', views.Home.as_view(), name ='home'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
