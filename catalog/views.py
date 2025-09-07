from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy, reverse

from catalog.forms import ProductForm
from catalog.models import Product, Contact, Category


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    paginate_by = 8
    ordering = ['updated_at']

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()

        context['categories'] = categories
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_page.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        similar_products = Product.objects.filter(category=product.category).exclude(id=product.id).order_by('?')[:4]

        context['similar_products'] = similar_products
        return context


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_success_url(self):
        return reverse('catalog:product_page', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:home')


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(name='FastDeli')
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        return HttpResponse(f'Спасибо, {name}! Сообщение успешно зарегистрировано.')


    # def home(request):
    #     all_products = Product.objects.all().order_by('-created_at')
    #     latest_products = all_products[:5]
    #     print("ПОСЛЕДНИЕ 5 ПРОДУКТОВ:")
    #     for i, product in enumerate(latest_products, 1):
    #         print(f'{i}. {product.name} категории: {product.category}, с ценой: {product.price} руб.')
    #
    #     context = {
    #         'all_products': all_products,
    #         'latest_products': latest_products
    #     }
    #
    #     return render(request, 'home.html', context)



# def contacts(request):
#     contact = Contact.objects.get(name='FastDeli')
#
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#
#         return HttpResponse(f'Спасибо, {name}! Сообщение успешно зарегистрировано.')
#     context = {
#         'contact': contact
#     }
#     return render(request, 'contacts.html', context)


# def product_page(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     similar_products = Product.objects.filter(category=product.category).exclude(id=product.id).order_by('?')[:4]
#
#     context = {'product': product,
#                'similar_products': similar_products,
#                }
#     return render(request, 'product_page.html', context)
