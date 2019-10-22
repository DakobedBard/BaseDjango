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
    path('upload', upload.views.Upload.as_view(), name ='upload_file'),
    path('signup/',upload.views.signup, name='signup'),
    path('upload_image/',upload.views.image_upload, name='upload'),
    path('accounts', include('django.contrib.auth.urls')),
    path('secret/', upload.views.secret_page, name='account'),
    path('tabs/', tab_generator.views.slow_down, name='slow'),
    path('list/',tab_generator.views.list, name='list' ),
    path('tabs/<uuid:pk>/list', tab_generator.views.slow_down, name='listTabs'),
    path('player', tab_generator.views.player, name='player'),



]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
