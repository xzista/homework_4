import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(subject='Подтверждение почты после регистрации',
                  message=f'Спасибо что присоединились к нашему маркетплейсу FastDeli!\nДля подтверждения почты перейдите по ссылке: {url}\n\n\nЭто письмо отправлено автоматически, отвечать на него не нужно',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email]
                  )
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserRegisterForm
    template_name = "registration.html"
    success_url = reverse_lazy("catalog:home")


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))