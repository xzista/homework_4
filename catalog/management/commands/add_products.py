from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Все данные удалены"))

        try:
            call_command("loaddata", "categories.json")
            self.stdout.write(self.style.SUCCESS("Категории загружены из фикстуры"))

            call_command("loaddata", "products.json")
            self.stdout.write(self.style.SUCCESS("Продукты загружены из фикстуры"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка при загрузке фикстур: {e}"))
