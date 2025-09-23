from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


class ProductService:

    @staticmethod
    def get_products_from_cache():
        """Функция для получения списка продуктов из кэша, или кэширование данный при его отсутствии"""
        if not CACHE_ENABLED:
            return Product.objects.all()
        key = 'product_list'
        products = cache.get(key)
        if products is not None:
            return products
        products = Product.objects.all()
        cache.set(key, products)
        return products

    @staticmethod
    def get_product_list_by_category(category):
        return Product.objects.filter(category=category)
