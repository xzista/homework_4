from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from blog.models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog_main.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True).order_by("-views_count")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = list(context["posts"])

        context["featured_post"] = posts[0] if posts else None
        context["popular_posts"] = posts[1:3] if len(posts) > 1 else []
        context["other_posts"] = posts[3:] if len(posts) > 3 else []

        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "post_page.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = [
        "title",
        "content",
        "image",
        "is_published",
    ]
    template_name = "post_form.html"
    success_url = reverse_lazy("blog:posts")


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BlogPost
    template_name = "post_form.html"
    fields = (
        "title",
        "content",
        "image",
        "is_published",
    )
    success_url = reverse_lazy("blog:posts")
    permission_required = "blog.change_blogpost"

    def get_success_url(self):
        return reverse("blog:post_page", args=[self.kwargs.get("pk")])


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BlogPost
    template_name = "post_delete.html"
    success_url = reverse_lazy("blog:posts")
    permission_required = "blog.delete_blogpost"
