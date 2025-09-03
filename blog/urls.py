from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView

app_name = BlogConfig.name  # 'blog'

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='posts'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_page'),
]
