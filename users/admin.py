from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "phone",
        "country",
        "avatar",
        "is_active",
    )
    list_filter = (
        "email",
        "country",
        "is_active",
    )
    search_fields = ("email", "country", "phone",)