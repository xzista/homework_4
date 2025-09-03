from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView

from blog.models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_main.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)#.order_by('views_count')


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'image', 'is_published',)
    success_url = reverse_lazy('blog:posts')

    def get_success_url(self):
        return reverse('blog:post_page', args=[self.kwargs.get('pk')])