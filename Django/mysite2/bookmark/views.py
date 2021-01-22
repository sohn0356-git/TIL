from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

# Create your views here.

class BookmarkLV(ListView):
    template_name = 'bookmark_list.html'
    model = Bookmark

class BookmarkDV(DetailView):
    template_name = 'bookmark_detail.html'
    model = Bookmark