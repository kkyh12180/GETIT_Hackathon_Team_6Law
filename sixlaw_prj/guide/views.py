from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView) :
    model = Post
    ordering = '-pk'
    template_name = 'guide/guide_list.html'

    def get_context_data(self, **kwargs) :
        context = super(PostList, self).get_context_data()
        return context

class PostDetail(DetailView) :
    model = Post

    def get_context_data(self, **kwargs) :
        context = super(PostDetail, self).get_context_data()
        return context