from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование товара', help_text='Введите название товара')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание товара', blank=True, null=True)
    image = models.ImageField(upload_to='static/image', verbose_name='Изображение', help_text='Загрузите изображение', blank=True, null=True)
    category = models.ForeignKey(on_delete=models.SET_NULL, verbose_name='Категория', related_name='Товары', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена', help_text='Укажите цену')
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Время изменения', auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', 'category', 'price', 'create_date', 'modified_date']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование категории', help_text='Введите название категории')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание категории', blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name',]

    def __str__(self):
        return self.name