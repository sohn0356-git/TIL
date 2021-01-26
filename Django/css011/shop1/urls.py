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

app_name = 'shop1'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='shop1/home.html'),name='shop1'),
    url(r'^css01/$', TemplateView.as_view(template_name='shop1/css01.html'),name='css01'),
    url(r'^css02/$', TemplateView.as_view(template_name='shop1/css02.html'),name='css02'),
    url(r'^css03/$', TemplateView.as_view(template_name='shop1/css03.html'),name='css03'),
    url(r'^css04/$', TemplateView.as_view(template_name='shop1/css04.html'),name='css04'),
    url(r'^css05/$', TemplateView.as_view(template_name='shop1/css05.html'),name='css05'),
    url(r'^css06/$', TemplateView.as_view(template_name='shop1/css06.html'),name='css06'),
]
