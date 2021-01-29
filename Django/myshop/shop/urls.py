"""css011 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from shop.views import *

app_name = 'shop'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='shop2/shop2.html'),name='home'),
    url(r'^login/$',Mainview.login,name='login'),
    url(r'^logout/$',Mainview.logout,name='logout'),
    url(r'^login/impl$',Mainview.loginimpl,name='loginimpl'),
    url(r'^register/$',userlist,name='register'),
    url(r'^aboutus/$',userlist,name='aboutus'),
    url(r'^user/$',userlist,name='userlist'),
    url(r'^user/(?P<id>\w+)/$',userdetail,name='userdetail'),
    url(r'^useradd/$',useradd,name='useradd'),
    url(r'^useraddimpl/$',useraddimpl,name='useraddimpl'),
    url(r'^user/(?P<id>\w+)/delete/$',userdelete,name='userdelete'),
    url(r'^user/(?P<id>\w+)/update/$',userupdate,name='userupdate'),
    url(r'^userupdateimpl/$',userupdateimpl,name='userupdateimpl'),
    url(r'^item/$',itemlist,name='itemlist'),
    url(r'^item/(?P<id>\w+)/$',itemdetail,name='itemdetail'),
    url(r'^itemadd/$',itemadd,name='itemadd'),
    url(r'^itemaddimpl/$',ItemView.upload,name='itemaddimpl'),
    url(r'^item/(?P<id>\w+)/delete/$',itemdelete,name='itemdelete'),
    url(r'^item/(?P<id>\w+)/update/$',itemupdate,name='itemupdate'),
    url(r'^itemupdateimpl/$',ItemView.update,name='itemupdateimpl'),
]
