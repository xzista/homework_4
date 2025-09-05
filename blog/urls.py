from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogCreateView

app_name = BlogConfig.name  # 'blog'

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='posts'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_page'),
    path('posts/create/', BlogCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', BlogUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
]
