from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "phone",
            "country",
            "avatar",
            "password1",
            "password2",
        ]