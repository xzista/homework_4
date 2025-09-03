from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_main.html'
    context_object_name = 'posts'


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        return self.object
