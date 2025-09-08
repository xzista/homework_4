from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок", help_text="Укажите заголовок")
    content = models.TextField(verbose_name="Содержимое", help_text="Заполните содержимое")
    image = models.ImageField(
        upload_to="blog/blogs_images",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    is_published = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров", help_text="Укажите количество просмотров", default=0
    )

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = [
            "title",
            "created_at",
            "views_count",
            "is_published",
        ]

    def __str__(self):
        return self.title
