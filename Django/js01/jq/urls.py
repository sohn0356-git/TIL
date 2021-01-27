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
from django.conf.urls import url
from django.views.generic import TemplateView
from jq.views import *

app_name = 'jq'

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='jq1.html'), name='index'),
    url(r'^2/$',TemplateView.as_view(template_name='jq2.html'), name='jq2'),
    url(r'^3/$',TemplateView.as_view(template_name='jq3.html'), name='jq3'),
    url(r'^4/$',TemplateView.as_view(template_name='jq4.html'), name='jq4'),
    url(r'^5/$',TemplateView.as_view(template_name='jq5.html'), name='jq5'),
    url(r'^6/$',TemplateView.as_view(template_name='jq6.html'), name='jq6'),
    url(r'^login/$',login, name='login'),
]
