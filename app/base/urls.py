from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import accounts.views
import upload.views
import tab_generator.views
from tabs.views import TabsListView, CreateTabView, newTab, TabCreateView, TabDetailView

from pages.views import FrontendRenderView


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

    path('upload', upload.views.Upload.as_view(), name='upload_file'),
    # AWS paths

    # EC2
    path('launch/', upload.views.launch_instance, name='launch'),
    path('terminate/<instanceID>', upload.views.terminate, name='launch'),
    path('list_instances/', upload.views.list_instances, name='list_instances'),

    # S3 Audio Files..
    path('list_files/', upload.views.list, name='list_files'),

    # Style Transfer
    path('style/', upload.views.style, name='style'),

    # # Tab Generator Home
    # path('tabs/', tabs.views.TabsView.as_view()),
    #
    # path('train_model/', upload.views.train_model, name='train_model'),
    # path('tablature/', tabs.views.load_tab, name='load_tabs'),

    # API
    re_path(r'api/products', include("products.api.urls")),

    re_path(r'api/tabs', include("tabs.api.urls")),

    path('tabs_home', TabsListView.as_view(), name = 'tabs_home'),
    path('new_tab', TabCreateView.as_view(), name='tab-create'),
    path('post/<int:pk>/', TabDetailView.as_view(), name='post-detail'),



]
#
# urlpatterns += [
#     re_path(r'(?P<path>.*)', FrontendRenderView.as_view(), name='home')
# ]
#

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
