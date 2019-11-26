from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import accounts.views
import upload.views
import tab_generator.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", accounts.views.login, name="login"),
    path("home/", accounts.views.home, name ='home'),
    path('signup/', accounts.views.signup, name='signup'),
    path('accounts', include('django.contrib.auth.urls')),
    path('secret/', accounts.views.secret_page, name='account'),

    # Audio
    path('tabs/', tab_generator.views.slow_down, name='slow'),
    path('list/',tab_generator.views.list, name='list' ),
    path('tabs/<uuid:pk>/list', tab_generator.views.slow_down, name='listTabs'),

    path('player', tab_generator.views.player, name='player'),
    # Upload
    path('upload_image/', upload.views.image_upload, name='upload'),
    path('upload', upload.views.Upload.as_view(), name='upload_file'),
    # AWS paths

    # EC2
    path('launch/', upload.views.launch_instance, name='launch'),
    path('terminate/<instanceID>', upload.views.terminate, name='launch'),
    path('list_instances/', upload.views.list_instances, name='list_instances'),

    # REST API paths

    path('create_tab/', tab_generator.views.create_guitar_tab_view, name='create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # S3 Audio Files..
    path('list_files/', upload.views.list, name='list_files'),

    # Style Transfer
    path('style/', upload.views.style, name='style')

]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
