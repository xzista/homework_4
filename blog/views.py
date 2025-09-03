from django.shortcuts import render
from django.views.generic import ListView

from blog.models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_main.html'
    context_object_name = 'posts'
