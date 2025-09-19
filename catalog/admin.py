from django.contrib import admin

from catalog.models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "category",
        "owner",
        "is_published",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
        "owner",
        "is_published",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "phone",
        "email",
    )
    search_fields = (
        "name",
        "address",
        "phone",
        "email",
    )
