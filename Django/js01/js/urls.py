"""js01 URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'js'

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='index'),
    url(r'^js1$',TemplateView.as_view(template_name='js1.html'),name='js1'),
    url(r'^js2$',TemplateView.as_view(template_name='js2.html'),name='js2'),
    url(r'^js3$',TemplateView.as_view(template_name='js3.html'),name='js3'),
    url(r'^js4$',TemplateView.as_view(template_name='js4.html'),name='js4'),
    url(r'^js5$',TemplateView.as_view(template_name='js5.html'),name='js5'),
    url(r'^js6$',TemplateView.as_view(template_name='js6.html'),name='js6'),
    url(r'^js7$',TemplateView.as_view(template_name='js7.html'),name='js7'),
    url(r'^js8$',TemplateView.as_view(template_name='js8.html'),name='js8'),
    url(r'^js9$',TemplateView.as_view(template_name='js9.html'),name='js9'),
]
