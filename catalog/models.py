from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Наименование категории", help_text="Введите название категории"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание категории", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование товара", help_text="Введите название товара")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание товара", blank=True, null=True)
    image = models.ImageField(
        upload_to="catalog/product_images",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, verbose_name="Категория", related_name="Товары", blank=True, null=True
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Укажите цену")
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)
    is_published = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, verbose_name="Владелец", related_name="Товара",)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = [
            "name",
            "category",
            "price",
        ]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product')
        ]

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название компании")
    address = models.CharField(max_length=100, verbose_name="Адрес", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name
