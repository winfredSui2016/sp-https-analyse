"""freessl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import django
from django.conf.urls import url
from django.contrib import admin
import app.views as app_views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', app_views.home, name='home'),
    url(r'^docs$', app_views.home, name='docs'),
    url(r'^about$', app_views.home, name='about'),
    # url(r'^login$', app_views.home, name='login'),
    url(r'^login$', login, name='login'),
    url(r'^auth$', login, name='auth'),
    # url(r'^logout$', app_views.home, name='logout'),
    url(r'^logout$', logout, name='logout'),
    url(r'^signup$', app_views.home, name='signup'),
    url(r'^profile$', app_views.home, name='profile'),
    url(r'^user_ssl$', app_views.home, name='user_ssl'),
    url(r'^user_settings$', app_views.home, name='user_settings'),
    url(r'^ssl_create$', app_views.ssl_create, name='ssl_create'),
    url(r'^https_show$', app_views.https_show, name='https_show'),
    url(r'^https_detail', app_views.https_detail, name='https_detail'),
    url(r'^url_access', app_views.url_access, name='url_access'),
    url(r'^url_list', app_views.url_list, name='url_list'),
    url(r'^ssl_create_file$', app_views.ssl_create_file, name='ssl_create_file'),
    url(r'^ssl_create_dns$', app_views.ssl_create_dns, name='ssl_create_dns'),

    url(r'^app/test$', app_views.test),

    url(r'^admin/', admin.site.urls),
]
