from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import upload.views as views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/",views.login , name="login"),
    path("home/", views.home, name ='home'),
   # path('home', views.Home.as_view(), name ='homeClassView'),
    path('signup/',views.signup, name='signup'),
    path('upload/',views.image_upload, name='upload'),
    path('accounts', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name='account')

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
