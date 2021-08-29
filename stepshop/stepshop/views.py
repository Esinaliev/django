from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    title = 'магазин'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products = Product.objects.all()

    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }

    return render(request, 'stepshop/index.html', context=context)


def contacts(request):
    title = 'магазин'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'stepshop/contact.html', context)

def about(request):
    title = 'магазин'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }

    return render(request, 'stepshop/about.html', context)
