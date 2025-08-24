from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:5]

    print("ПОСЛЕДНИЕ 5 ПРОДУКТОВ:")
    for i, product in enumerate(latest_products, 1):
        print(f'{i}. {product.name} категории: {product.category}, с ценой: {product.price} руб.')

    context = {
        'latest_products': latest_products
    }

    return render(request, 'catalog/home.html', context)


def contacts(request):
    contact = Contact.objects.get(name='FastDeli')

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}! Сообщение успешно зарегистрировано.')
    context = {
        'contact': contact
    }
    return render(request, 'catalog/contacts.html', context)
