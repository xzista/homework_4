from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}! Сообщение успешно зарегистрировано.')
    return render(request, 'catalog/contacts.html')
