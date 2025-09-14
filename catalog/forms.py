from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "category",
            "description",
            "image",
        ]

    def clean_price(self):
        price = self.cleaned_data["price"]
        if int(price) < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price


    def clean_image(self):
        image = self.cleaned_data.get("image")

        if image.size > 5 * 1024 * 1024:
            raise ValidationError("Размер изображения не должен превышать 5 МБ")

        if not image.name.endswith('.png') or not image.name.endswith('.jpeg'):
            raise ValidationError("Поддерживаются только JPEG и PNG форматы")



    def clean(self):
        cleaned_data = super().clean()
        filter_words = [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]

        product_name = cleaned_data.get("name", "")
        product_description = cleaned_data.get("description", "")

        for word in filter_words:
            if word in product_name.lower():
                self.add_error("name", f'Запрещенное слово в названии: "{word}"')

        for word in filter_words:
            if word in product_description.lower():
                self.add_error("description", f'Запрещенное слово в описании: "{word}"')

        return cleaned_data
