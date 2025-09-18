from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import RegisterView, email_verification

app_name = 'users'

urlpatterns = [
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(next_page='catalog:home'), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
]
