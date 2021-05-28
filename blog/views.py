from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post

# Create your views here.

# List of Blogs
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

# Blog View
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
