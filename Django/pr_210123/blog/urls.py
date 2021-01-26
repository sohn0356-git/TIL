"""pr_210123 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from blog.views import *

app_name = 'blog'

urlpatterns = [
    url(r'^$', PostLV.as_view(), name='index'),
    url(r'^post/(?P<slug>\w+)/$', PostDV.as_view(), name='post_detail'),
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    url(r'^archive/(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    url(r'^search/$',SearchFormView.as_view(),name='search'),
]
