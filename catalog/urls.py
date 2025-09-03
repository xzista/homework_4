from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactsView

app_name = CatalogConfig.name  # 'catalog'

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_page'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
]
