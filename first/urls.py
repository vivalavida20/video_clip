"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from video_clip import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^/(?P<pk>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^/(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^/(?P<pk>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^/(?P<name>[ㄱ-힣]+)/$', views.category, name="category"),
    url(r'^new_category/$', views.new_category, name='new_category'),
]
