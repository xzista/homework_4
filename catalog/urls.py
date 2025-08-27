from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_page

app_name = CatalogConfig.name  # 'catalog'

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_page, name='product_page'),
]