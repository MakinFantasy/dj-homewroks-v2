from django.shortcuts import render, redirect
from phones.models import Phone
# Create your views here.


def show_catalog(request):

    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    result = str()
    if sort == 'name':
        result = phones.order_by('name')
    elif sort == 'min_price':
        result = phones.order_by('price')
    elif sort == 'max_price':
        result = phones.order_by('price').reverse()

    context = {'phones': result}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)


