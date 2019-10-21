from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import upload.views
import tab_generator.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/",upload.views.login , name="login"),
    path("home/", upload.views.home, name ='home'),
   # path('home', views.Home.as_view(), name ='homeClassView'),
    path('signup/',upload.views.signup, name='signup'),
    path('upload/',upload.views.image_upload, name='upload'),
    path('accounts', include('django.contrib.auth.urls')),
    path('secret/', upload.views.secret_page, name='account'),
    path('tabs/', tab_generator.views.youtube_dl, name='youtube_dl')
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
